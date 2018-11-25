# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()#车名
    price = scrapy.Field()#车价
    #pass
#class CartypeItem(scrapy.Item):
    cartype=scrapy.Field()
    t_url=scrapy.Field()

#class CategoryItem(scrapy.Item):
    c_url = scrapy.Field()#分类的链接

