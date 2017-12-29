# baseballdb-datasette

Configuration for publishing the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/statistics/) with [Datasette](https://github.com/simonw/datasette).

### overview
See the following blog posts for an overview of the project and data.
* ["Publishing the Lahman Baseball Database with Datasette"](http://lawlesst.github.io/notebook/baseball-datasette.html)
* ["Now Publishing Complete Lahman Baseball Database with Datasette"](http://lawlesst.github.io/notebook/baseball-datasette-full.html)

### configuration notes
* server OS, Ubuntu 16.04.3
* Datasette is run as a daemon using [systemd](https://en.wikipedia.org/wiki/Systemd). See [service config](baseballdb.service) for systemd config.
* [`run.py`](run.py) handles starting Datasette with systemd. The command line script, `datasette`, bundled with the library didn't play well with systemd.
* Apache is used to proxy the Python application and serve requests on port 80 and via SSL. The configuration in `/etc/apache2/sites-available` looks like this:
 ```
 <VirtualHost *:80>
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8001/
    ProxyPassReverse / http://127.0.0.1:8001/
RewriteEngine on
RewriteCond %{SERVER_NAME} =yourdomain.com
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
 ```
* Python 3 and pip were installed using apt-get:
 * `sudo apt-get install python3 python-pip`
* Pythons [virtualenv](https://docs.python.org/3/library/venv.html) is used to manage the Python libraries and referenced from the systemd configuration. The environment is expected to be at `venv` in the same directory as the datasette configuration.
