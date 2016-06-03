from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity

def clean(item):
    if isinstance(item, basestring):
        return item.strip(" \"-!@#$%^&*<>,.")
    return item

class Loader(ItemLoader):
    default_input_processor = MapCompose(clean)
    default_output_processor = TakeFirst()
