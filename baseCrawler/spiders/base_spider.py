import scrapy
# from link_extractor import LinkExtractor
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import time

class BaseSpider(scrapy.Spider):
    name = "base"
    link_extractor = LxmlLinkExtractor(allow=(), deny=(), allow_domains=(["example.com"]), deny_domains=(),
                                       deny_extensions=None, restrict_xpaths=(), restrict_css=(), tags=('a', 'area'),
                                       attrs=('href',), canonicalize=False, unique=True, process_value=None, strip=True)

    def start_requests(self):
        base_url = 'http://example.com/'

        yield scrapy.Request(url=base_url, callback=self.parse)

    def parse(self, response):

        links = self.link_extractor.extract_links(response)
        links_processing_start = time.time()
        for link in links:
            yield {
                'source_url': response.url,
                'destination_url':link.url
            }
            yield scrapy.Request(url=link.url, callback=self.parse)
        print("TOTAL TIME TOOK | " + str(time.time() - links_processing_start) + " | TOTAL LINKS COUNT | " + str(len(links)))
        yield {
            'url': response.url,
            'download_time': response.meta['__end_time'] - response.meta['__start_time'],
            'download_latency': response.meta['download_latency']
        }

    def parseError(self, response):
        print('Error')
