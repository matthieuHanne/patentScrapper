from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from patentScrapper.items import PatentscrapperItem
from scrapy.http import Request
from types import *

class EspacenetSpider(CrawlSpider):
    name = 'espacenet'
    x = 0
    def __init__(self, keywords=None, *args, **kwargs):
        super(EspacenetSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://worldwide.espacenet.com/searchResults?compact=false&ST=singleline&query=%s&locale=en_EP&DB=worldwide.espacenet.com' % keywords]
        allowed_domains = ['worldwide.espacenet.com']
        rules = (
           # Rule(SgmlLinkExtractor(), callback='parse_links', follow=True)
        )


    def parse_patent(self, response):
        sel = Selector(response)
        i = PatentscrapperItem()
        self.x+= 1
        filename = 'patent'+`self.x`
        open(filename, 'wb').write(response.body)
        i['bookmark'] = sel.xpath("//div[@id='pagebody']/h3/text()").extract()
        i['inventors'] = 0
        i['applicants'] = 0
        i['classification'] = 0
        i['applicationNumber'] = 0
        i['priorityNumbers'] = 0
        i['published'] = 0
        i['core'] = 0

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//a[@class="publicationLinkClass"]/@href').extract()
        #for link in links:
           #yield Request("http://worldwide.com"+link, callback=self.parse_patent)

        nextPage = sel.xpath('//a[@class="paginationNext"]/@href').extract()
        print "URL ->    SIZE   " +`len(nextPage)`
        if type(nextPage) is list:
            yield Request("http://worldwide.com/"+nextPage[0], callback=self.parse)
        else:
            yield Request("http://worldwide.com/"+nextPage, callback=self.parse)

        #return i

