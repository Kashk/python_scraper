# -*- coding: utf-8 -*- 
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity

def clean(item):
    if isinstance(item, basestring):
        item = item.encode('utf-8')
        return item.strip(" \"\n\r\t-!@#$%^&*<>,.")
    return item

class Loader(ItemLoader):
    default_input_processor = MapCompose(clean)
    default_output_processor = TakeFirst()
