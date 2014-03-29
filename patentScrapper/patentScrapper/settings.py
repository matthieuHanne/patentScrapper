# Scrapy settings for patentScrapper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'patentScrapper'

SPIDER_MODULES = ['patentScrapper.spiders']
NEWSPIDER_MODULE = 'patentScrapper.spiders'
ITEM_PIPELINES = {'patentScrapper.pipelines.PatentscrapperPipeline': 100 }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'patentScrapper (+http://www.yourdomain.com)'
