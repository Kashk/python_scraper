# -*- coding: utf-8 -*- 
from scrapy.exceptions import DropItem
from validators.number import is_not_number
from validators.url import is_not_valid_url

required = ['title', 'owner_name', 'link', 'sleeps', 'bedrooms', 'bathrooms', 'property_type', 'location']
optional = ['description', 'min_stay', 'suitability', 'images', 'amenities']
numerical = ['sleeps', 'bedrooms', 'bathrooms']
url = ['link', 'images']

class Validator(object):
    def process_item(self, item, spider):
        if item is not None:
            self.required_fields(item)
            item = self.optional_fields(item)
            item = self.numerical_fields(item)
            item = self.url_fields(item)

            return item

    def required_fields(self, item):
        for field in required:
            if not field in item:
                raise DropItem("Missing field: %s" % field)

    def optional_fields(self, item):
        for field in optional:
            if not field in item:
                item[field] = None
        return item

    def numerical_fields(self, item):
        for field in numerical:
            if is_not_number(item[field]) and field in required:
                raise DropItem("%s is not a number" % field)
        return item

    def url_fields(self, item):
        for field in url:
            if is_not_valid_url(item[field]) and field in required:
                raise DropItem("%s is not a valid url" % field)
        return item




                
