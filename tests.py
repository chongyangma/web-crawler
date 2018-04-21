import sys
sys.path.insert(0, './scripts')

import scrape_callback
from scrape_callback import ScrapeCallback

if __name__ == '__main__':
    scrape_callback.link_crawler('http://example.webscraping.com/', '/(places/default/index|places/default/view)', scrape_callback=ScrapeCallback())
