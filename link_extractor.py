from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class LinkExtractor:
    def __init__(self, response):
        link_extractor = LxmlLinkExtractor(allow=(), deny=(),
                                           allow_domains=(),
                                           deny_domains=(),
                                           deny_extensions=None,
                                           restrict_xpaths=(),
                                           restrict_css=(),
                                           tags=('a', 'area'),
                                           attrs=('href'),
                                           canonicalize=False,
                                           unique=True,
                                           process_value=None,
                                           strip=True)
        self.links = link_extractor.extract_links(response)

    def get_links(self):
        return self.links
