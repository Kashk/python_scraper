# -*- coding: utf-8 -*- 
import scrapy 
from scrapers.item_loader import Loader
from pyvirtualdisplay import Display 
from selenium import webdriver
from scrapers.items import * 

class HomeawaySpider(scrapy.Spider):
    name = "discover_new_properties"
    allowed_domains = ["homeaway.com"]
    url1 = 'https://www.homeaway.com/vacation-rental/p%svb'
    url2 = 'https://www.homeaway.com/vacation-rental/p%s'

    property_fields_with_reviews = {
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
    property_fields_without_reviews = {
            'title': 'h1::text',
            'description': '.preview p::text',
            'sleeps': '.amenity-table tbody tr:nth-child(1) td:nth-child(2)::text',
            'bedrooms':'.amenity-table tbody tr:nth-child(2) td:nth-child(2)::text',
            'bathrooms': '.amenity-table tbody tr:nth-child(3) td:nth-child(2)::text',
            'property_type':'.amenity-table tbody tr:nth-child(4) td:nth-child(2)::text',
            'min_stay': '.amenity-table tbody tr:nth-child(5) td:nth-child(2)::text',
            'suitability': '.summary-amenities ul li::text',
            'location': '.js-breadcrumbLink::text',
            'location': '.js-breadcrumbLink span::text',
            'owner_name': '.owner-name::text'
            #'amenities':}
            }


    amenity_fields = [
            {
                'name': '#propertyType::text',
                'description': '#propertyType ~ div ul li::text',
                'description': '#propertyType ~ div ul li span::text'
            },
            {
                'name': '#theme::text',
                'description': '#theme ~ div ul li::text',
                'description': '#theme ~ div ul li span::text'
            },
            {
                'name': '#general::text',
                'description': '#general ~ div ul li::text',
                'description': '#general ~ div ul li span::text'
            },
            {
                'name': '#kitchen::text',
                'description': '#kitchen ~ div ul li::text',
                'description': '#kitchen ~ div ul li span::text'
            },
            {
                'name': '#dining::text',
                'description': '#dining ~ div ul li::text',
                'description': '#dining ~ div ul li span::text'
            },
            {
                'name': '#entertainment::text',
                'description': '#entertainment ~ div ul li::text',
                'description': '#entertainment ~ div ul li span::text'
            },
            {
                'name': '#outside::text',
                'description': '#outside ~ div ul li::text',
                'description': '#outside ~ div ul li span::text'
            },
            {
                'name': '#suitability::text',
                'description': '#suitability ~ div ul li::text',
                'description': '#suitability ~ div ul li span::text'
            },
            {
                'name': '#poolSpa::text',
                'description': '#poolSpa ~ div ul li::text',
                'description': '#poolSpa ~ div ul li span::text'
            },
            {
                'name': '#attractions::text',
                'description': '#attractions ~ div ul li::text',
                'description': '#attractions ~ div ul li span::text'
            },
            {
                'name': '#leisureActivities::text',
                'description': '#leisureActivities ~ div ul li::text',
                'description': '#leisureActivities ~ div ul li span::text'
            },
            {
                'name': '#localservicesandbusinesses::text',
                'description': '#localservicesandbusinesses ~ div ul li::text',
                'description': '#localservicesandbusinesses ~ div ul li span::text'
            },
            {
                'name': '#sportsandadventureactivities::text',
                'description': '#sportsandadventureactivities ~ div ul li::text',
                'description': '#sportsandadventureactivities ~ div ul li span::text'
            }
        ]
    driver_fields = {
            'images': '.photo-div img' 
            }

    def __init__(self):
        pass
        # self.display = Display(visible=1, size=(1440, 863))
        # self.display.start()
        # self.driver = webdriver.Chrome()
        # self.driver.set_window_size(1440, 863)

    def start_requests(self):
        for num in range(1, 800000):
            yield scrapy.Request(self.url1 % num, meta = {'dont_redirect': True})
            yield scrapy.Request(self.url2 % num, meta = {'dont_redirect': True})

    def parse(self, response):
        # self.driver.get(response.url)

        p = Loader(house(), response=response)
        if(len(response.css('.reviews-summary'))):
            for field, css_path in self.property_fields_with_reviews.iteritems():
                p.add_css(field, css_path)
        else:
            for field, css_path in self.property_fields_without_reviews.iteritems():
                p.add_css(field, css_path)

        p.add_value('link', response.url)

        # for item in self.amenity_fields:
        #     a = Loader(amenity(), response=response)
        #     for field, css_path in item.iteritems():
        #         try:
        #             a.add_css(field, css_path)
        #         except Exception as e:
        #             print e
        #     yield a.load_item()
        # imgs = self.driver.find_elements_by_css_selector('.prop-photo-item-image')

        # for img in imgs:
            # p.add_value('images', img.get_attribute('data-src'))

        # self.display.stop()
        yield p.load_item()
