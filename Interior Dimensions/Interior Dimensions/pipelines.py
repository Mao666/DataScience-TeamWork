# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CarPipeline(object):
    #def _init_(self):
        #self.f=open("info.json","w")
    def process_item(self, item, spider):

        
    
        #content=json.dumps(dict(item)) + ",\n"
        #self.f.write(content)
        return item
    
    #def close_spider(self,spider):
        #self.f.close()