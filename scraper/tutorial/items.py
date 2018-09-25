# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MyItem(scrapy.Item):

    # ... other item fields ...
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
    images = scrapy.Field()


class ImageItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()

