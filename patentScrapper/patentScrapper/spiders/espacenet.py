from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from patentScrapper.items import PatentscrapperItem
from scrapy.http import Request
from types import *

class EspacenetSpider(CrawlSpider):
    name = 'espacenet'
    items = []
    def __init__(self, keywords=None, *args, **kwargs):
        super(EspacenetSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://worldwide.espacenet.com/searchResults?compact=false&ST=singleline&query=%s&locale=en_EP&DB=worldwide.espacenet.com' % keywords]
        allowed_domains = ['worldwide.espacenet.com']
        rules = (
           # Rule(SgmlLinkExtractor(), callback='parse_links', follow=True) TODO
        )


    def parse_patent(self, response):
        sel = Selector(response)
        i = PatentscrapperItem()

        i['bookmark'] = sel.select('normalize-space(//div[@id="pagebody"]/h1/text())').extract()
        i['inventors'] =sel.select('normalize-space(//table[@class="tableType3"]/tbody/tr[3]/td/span/text())').extract()
        i['applicants'] =sel.select('normalize-space(//table[@class="tableType3"]/tbody/tr[4]/td/span/text())').extract()
        i['applicationNumber'] =sel.select('normalize-space(//table[@class="tableType3"]/tbody/tr[6]/td/text())').extract()
        i['priorityNumbers'] = sel.select('normalize-space(//table[@class="tableType3"]/tbody/tr[7]/td/span/a/text())').extract()
        i['core'] = sel.select('normalize-space(//div[@class="application article clearfix"]/p[@class="printAbstract"]/text())').extract()
        #i['published'] = 0 TODO
        #i['classification'] = 0 TODO
        #self.items.append(i)
        yield i

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//a[@class="publicationLinkClass"]/@href').extract()
        for link in links:
           yield Request("http://worldwide.espacenet.com"+link, callback=self.parse_patent)

        nextPage = sel.xpath('//a[@class="paginationNext"]/@href').extract()
        yield Request("http://worldwide.espacenet.com/"+nextPage, callback=self.parse)
        return

