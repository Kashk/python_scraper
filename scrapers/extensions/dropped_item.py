from scrapy import signals
from scrapy.exceptions import NotConfigured
import json
from troco_scrapers.database.tables import *

class StoreDroppedItems(object):
    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.item_dropped, signal=signals.item_dropped)

        return ext

    def item_dropped(self, item, response, exception, spider):
        s = session()
        d = DroppedItems(reason = exception, data = json.dumps(dict(item)), link = response.url)
        s.add(d)
        s.commit()
        

