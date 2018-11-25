import scrapy
#from car.items import CategoryItem

from car.items import CarItem
#from car.items import CartypeItem

class cate(scrapy.Spider):
    print(3)
class category_spider(scrapy.Spider):
    name = "price"
    start_urls = ['https://www.thecarconnection.com/']

    # start_urls=["https://www.thecarconnection.com"]
    #allowed_domains=['https://www.thecarconnection.com']
    
    def parse(self,response):
        node_list=response.xpath("//div[@id='list-by-category-container']/a")
        for node in node_list:
            item=CarItem()
            #item['cartype']=node.xpath('.').extract()[0]
            item['cartype']=node.extract()[0]
            item['t_url']=node.xpath("@href").extract()[0]
            t_url_next="https://www.thecarconnection.com" + item['t_url']
            #print('1111')
            #print(t_url_next)
            yield scrapy.Request(url=t_url_next,meta={'item':item},callback=self.parse_next,dont_filter=True)
            #yield item
            

    def parse_next(self, response):
        node_list1 = response.xpath("//div[@class='name']")
        for node1 in node_list1:
            item=CarItem()
            item=response.meta['item']
            item['c_url']=node1.xpath("./a/@href").extract()[0]
            #url=node1.xpath("./a/@href").extract()[0]

            c_url_next="https://www.thecarconnection.com" + item['c_url']
            #print('9999')
            #print(c_url_next)

            yield scrapy.Request(url=c_url_next,meta={'item':item},callback=self.parse_third,dont_filter=True)
        
        if len(response.xpath("//li[@class='next']")) :
            url_c=response.xpath("//li[@class='next']/a/@href").extract()[0]
            url_c_n="https://www.thecarconnection.com" + url_c
            #yield item
            #print('lzii1')
        
            yield scrapy.Request(url_c_n,meta={'item':item},callback=self.parse_next,dont_filter=True)
            
        if len(response.xpath("//li[@class='next']"))==0:
            for node1 in node_list1:
                item=CarItem()
                item=response.meta['item']
                item['c_url']=node1.xpath("./a/@href").extract()[0]
            #url=node1.xpath("./a/@href").extract()[0]

                c_url_next="https://www.thecarconnection.com" + item['c_url']
                yield scrapy.Request(url=c_url_next,meta={'item':item},callback=self.parse_third,dont_filter=True)
                
                
            

    def parse_third(self, response):
        #node_list2=response.xpath("//div[@class='trim-msrp']")
        #for node2 in node_list2:
            item=CarItem()
            item=response.meta['item']
            item['price']=response.xpath("//div[@class='trim-msrp']/span/text()").extract()[0]
            item['name']=response.xpath("//h1[@id='title']/text()[1]").extract()[0]

            #print(item['price'])
            #print('00lizi')
            
            yield item
    


        # items=[]
        # node_list=response.xpath("//div[@class='clear']/a")
        # for node in node_list:
        # name=node.xpatn("./span/text()").extract()

        # print(name[0])
