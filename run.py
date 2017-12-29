"""
Script for running datasette on Ubuntu server using systemd.
"""

from datasette.app import Datasette
import json
import sys

metadata_data = {
    "title": "Lahman’s Baseball Database",
    "license": "Creative Commons Attribution-ShareAlike 3.0 Unported License",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/",
    "source": "Sean Lahman",
    "source_url": "http://www.seanlahman.com/baseball-archive/statistics/"
}

if __name__ == "__main__":

    ds = Datasette(
        ["baseball.db"],
        cache_headers=True,
        cors=True,
        page_size=100,
        max_returned_rows=250,
        sql_time_limit_ms=1000,
        inspect_data=None,
        metadata=metadata_data,
        template_dir="templates"
    )
    # Force initial hashing/table counting
    ds.inspect()
    ds.app().run(host="0.0.0.0", port=8001)
