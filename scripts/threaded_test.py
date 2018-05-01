# -*- coding: utf-8 -*-

import argparse
from threaded_crawler import threaded_crawler
#from mongo_cache import MongoCache
from disk_cache import DiskCache
from alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = DiskCache()
    cache.clear()
    threaded_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test of multi-thread crawler')
    parser.add_argument('thread_num', type=int, help='Number of threads')
    args = parser.parse_args()
    main(args.thread_num)
