# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Identity


class house(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field(output_processor = Identity())
    sleeps = scrapy.Field()
    bedrooms = scrapy.Field()
    bathrooms = scrapy.Field()
    property_type = scrapy.Field()
    min_stay = scrapy.Field()
    suitability = scrapy.Field(output_processor = Identity())
    images = scrapy.Field(output_processor = Identity())
    amenities = scrapy.Field(output_processor = Identity())
    pass


