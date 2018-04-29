import sys
sys.path.insert(0, './scripts')

import link_crawler
import scrape_callback
from scrape_callback import ScrapeCallback
import alexa_fn

if __name__ == '__main__':
    link_crawler.link_crawler('http://example.webscraping.com',
                              '/(places/default/index)',
                              delay=1, num_retries=1, max_depth=1, user_agent='GoodCrawler')
    scrape_callback.link_crawler('http://example.webscraping.com/',
                                 '/(places/default/index)',
                                 scrape_callback=ScrapeCallback())

    urls = alexa_fn.alexa()
    print(len(urls))
