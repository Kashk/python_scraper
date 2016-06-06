# -*- coding: utf-8 -*- 
import scrapy 
from troco_scrapers.item_loader import Loader
from pyvirtualdisplay import Display 
from selenium import webdriver
from troco_scrapers.items import * 
from homeaway import HomeawaySpider
from troco_scrapers.database.tables import *

class ImagesSpider(HomeawaySpider):
    name = "images"
    allowed_domains = ["homeaway.com"]
    url = 'https://www.homeaway.com/vacation-rental/p%svb'
    def start_requests(self):
        s = session()

        homes = s.query(Home).all()

        for home in homes:
            yield scrapy.Request(home.link, meta = {'dont_redirect': True})

