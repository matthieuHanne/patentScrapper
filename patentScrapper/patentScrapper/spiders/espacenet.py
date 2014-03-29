from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from patentScrapper.items import PatentscrapperItem
from scrapy.http import Request

class EspacenetSpider(CrawlSpider):
    name = 'espacenet'

    def __init__(self, keywords=None, *args, **kwargs):
        super(EspacenetSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://worldwide.espacenet.com/searchResults?compact=false&ST=singleline&query=%s&locale=en_EP&DB=worldwide.espacenet.com' % keywords]
        allowed_domains = ['worldwide.espacenet.com']
        rules = (
            Rule(SgmlLinkExtractor(), callback='parse_links', follow=True)
        )

    def parse_links(self, response):
        print "linnnk"
        filename = response.url.split("/")[-2] + "parle_links"
        open(filename, 'wb').write(response.body)

    def parse(self, response):
        sel = Selector(response)
        i = PatentscrapperItem()
        links = sel.xpath('//a[@class="publicationLinkClass"]/@href').extract()
        for link in links:
            yield Request("http://worldwide.com"+link, callback=self.parse)
            print 'test'
            open('brvt', 'wb').write(response.body)
            i['bookmark'] = sel.xpath("//div[@id='pagebody']/h3/text()").extract()
            i['inventors'] = 0
            i['applicants'] = 0
            i['classification'] = 0
            i['applicationNumber'] = 0
            i['priorityNumbers'] = 0
            i['published'] = 0
            i['core'] = 0

        #return i
