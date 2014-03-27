from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from patentScrapper.items import PatentscrapperItem

class EspacenetSpider(CrawlSpider):
    name = 'espacenet'
    allowed_domains = ['worldwide.espacenet.com']
    start_urls = ['http://worldwide.espacenet.com/publicationDetails/biblio?locale=en_EP&II=0&FT=D&CC=BR&DB=worldwide.espacenet.com&NR=PI1103049A2&date=20140304&ND=3&KC=A2&adjacent=true']

    #rules = (
    #    Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)

    def parse(self, response):
        sel = Selector(response)
        i = PatentscrapperItem()
        i['bookmark'] = sel.xpath("//div[@id='pagebody']/h3/text()").extract()
        i['inventors'] = 0
        i['applicants'] = 0
        i['classification'] = 0
        i['applicationNumber'] = 0
        i['priorityNumbers'] = 0
        i['published'] = 0
        i['core'] = 0
        print i['bookmark']
        print 'test'
       #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        return i
