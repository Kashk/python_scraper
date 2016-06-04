# -*- coding: utf-8 -*- 
import scrapy 
from troco_scrapers.item_loader import Loader
from pyvirtualdisplay import Display 
from selenium import webdriver
from troco_scrapers.items import * 

class HomeawaySpider(scrapy.Spider):
    name = "homeaway"
    allowed_domains = ["homeaway.com"]
    start_urls = (
        'https://www.homeaway.com/vacation-rental/p565133vb',
    )

    property_fields = {
            'title': 'h1::text',
            'description': '.preview p::text',
            'sleeps': '.amenity-table tbody tr:nth-child(2) td:nth-child(2)::text',
            'bedrooms':'.amenity-table tbody tr:nth-child(3) td:nth-child(2)::text',
            'bathrooms': '.amenity-table tbody tr:nth-child(4) td:nth-child(2)::text',
            'property_type':'.amenity-table tbody tr:nth-child(5) td:nth-child(2)::text',
            'min_stay': '.amenity-table tbody tr:nth-child(6) td:nth-child(2)::text',
            'suitability': '.summary-amenities ul li::text',
            'location': '.js-breadcrumbLink::text',
            'location': '.js-breadcrumbLink span::text',
            'owner_name': '.owner-name::text'
            #'amenities':}
            }

    driver_fields = {
            'images': '.photo-div img' 
            }

    def __init__(self):
        pass
        # self.display = Display(visible=1, size=(1440, 863))
        # self.display.start()
        # self.driver = webdriver.Chrome()
        # self.driver.set_window_size(1440, 863)

    def parse(self, response):
        # self.driver.get(response.url)

        p = Loader(house(), response=response)
        for field, css_path in self.property_fields.iteritems():
            p.add_css(field, css_path)

        p.add_value('link', response.url)
        # imgs = self.driver.find_elements_by_css_selector('.prop-photo-item-image')

        # for img in imgs:
            # p.add_value('images', img.get_attribute('data-src'))

        # self.display.stop()
        yield p.load_item()
