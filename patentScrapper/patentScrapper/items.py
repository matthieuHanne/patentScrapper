from scrapy.item import Item, Field

class PatentscrapperItem(Item):
    bookmark = Field()
    inventors = Field()
    applicants = Field()
    classification = Field()
    applicationNumber = Field()
    priorityNumbers = Field()
    published = Field()
    core = Field()
    pass
