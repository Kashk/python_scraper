# -*- coding: utf-8 -*- 
class Format(object):

    def process_item(self, item, spider):
        if item['description'] is not None:
            item['description'] = ('\n\n').join(item['description'])

        return item
