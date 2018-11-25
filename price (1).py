import scrapy

from car.items import CarItem


class category_spider(scrapy.Spider):
    name = "price"
    start_urls = ['https://www.thecarconnection.com/']

    
    def parse(self,response):
        node_list=response.xpath("//div[@id='list-by-category-container']/a")
        for node in node_list:
            t_url=node.xpath("./@href").extract()[0]
            t_url_next="https://www.thecarconnection.com" + t_url
            yield scrapy.Request(url=t_url_next,callback=self.parse_next,dont_filter=False)
                       
    def parse_next(self, response):
        node_list1 = response.xpath("//div[@class='name']")
        for node1 in node_list1:         
            c_url=node1.xpath("./a/@href").extract()[0]

            c_url_next="https://www.thecarconnection.com" + c_url
  

            yield scrapy.Request(url=c_url_next,callback=self.parse_third,dont_filter=False)
        
        if len(response.xpath("//li[@class='next']")) :
            url_c=response.xpath("//li[@class='next']/a/@href").extract()[0]
            url_c_n="https://www.thecarconnection.com" + url_c
        
            yield scrapy.Request(url_c_n,callback=self.parse_next,dont_filter=False)
            
        if len(response.xpath("//li[@class='next']"))==0:
            node_list2= response.xpath("//div[@class='name']")
            for node1 in node_list2:            
                h_url=node1.xpath("./a/@href").extract()[0]

                h_url_next="https://www.thecarconnection.com" + h_url
                yield scrapy.Request(url=h_url_next,callback=self.parse_third,dont_filter=False)
                                         
    def parse_third(self, response):
        spec=response.xpath("//div[@id='ymm-nav']/a[@id='ymm-nav-specs-btn']/@href").extract()[0]
        spec_next="https://www.thecarconnection.com" + spec          
        yield scrapy.Request(url=spec_next,callback=self.parse_four,dont_filter=False)
    
    def parse_four(self,response):
        item=CarItem()
        
        '''name=response.xpath("//div[@id='tcc3-global-container']/h1/text()").extract()
        if len(name):
            item['name']=name[0]
        else:
            item['name']='NAA'  '''
        print('a')
            
        '''name0=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[2]/span[1]/text()").extract()
        if len(name0):
            item['name0']=name0[0]
            item['number0']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name0']='NAA'
            item['number0']='NAA'
        
        
        name1=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[3]/span[1]/text()").extract()
        if len(name1):
            item['name1']=name1[0]
            item['number1']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[3]/span[2]/text()").extract()[0]
        else:
            item['name1']='NAA'
            item['number1']='NAA'
            
        name2=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[4]/span[1]/text()").extract()
        if len(name2):
            item['name2']=name2[0]
            item['number2']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[4]/span[2]/text()").extract()[0]
        else:
            item['name2']='NAA'
            item['number2']='NAA'
            
            
        name3=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[5]/span[1]/text()").extract()
        if len(name3):
            item['name3']=name3[0]
            item['number3']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[5]/span[2]/text()").extract()[0]
        else:
            item['name3']='NAA'
            item['number3']='NAA'
            
        name4=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[6]/span[1]/text()").extract()
        if len(name4):
            item['name4']=name4[0]
            item['number4']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[6]/span[2]/text()").extract()[0]
        else:
            item['name4']='NAA'
            item['number4']='NAA'
            
            
            
        name5=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[7]/span[1]/text()").extract()
        if len(name5):
            item['name5']=name5[0]
            item['number5']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[7]/span[2]/text()").extract()[0]
        else:
            item['name5']='NAA'
            item['number5']='NAA'
            
            
        name6=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[8]/span[1]/text()").extract()
        if len(name6):
            item['name6']=name6[0]
            item['number6']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[8]/span[2]/text()").extract()[0]
        else:
            item['name6']='NAA'
            item['number6']='NAA'
            
            
        name7=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[9]/span[1]/text()").extract()
        if len(name7):
            item['name7']=name7[0]
            item['number7']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[9]/span[2]/text()").extract()[0]
        else:
            item['name7']='NAA'
            item['number7']='NAA'
            
        name8=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[1]/div[2]/span[1]/text()").extract()
        if len(name8):
            item['name8']=name8[0]
            item['number8']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[1]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name8']='NAA'
            item['number8']='NAA'
            
        name9=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[2]/div[2]/span[1]/text()").extract()
        if len(name9):
            item['name9']=name9[0]
            item['number9']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[2]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name9']='NAA'
            item['number9']='NAA'
            
            
        name10=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[3]/div[2]/span[1]/text()").extract()
        if len(name10):
            item['name10']=name10[0]
            item['number10']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[3]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name10']='NAA'
            item['number10']='NAA'
            
            
        name11=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[2]/span[1]/text()").extract()
        if len(name11):
            item['name11']=name11[0]
            item['number11']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name11']='NAA'
            item['number11']='NAA'
            
            
        name12=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[5]/div[2]/span[1]/text()").extract()
        if len(name11):
            item['name12']=name12[0]
            item['number12']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[5]/div[2]/span[2]/text()").extract()[0]
        else:
            item['name12']='NAA'
            item['number12']='NAA'
        #name0=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[8]/span[1]/text()").extract()
        #if len(name0):
            #if name0[0]=='Passenger Doors':
                #item['door']=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[8]/span[2]/text()").extract()[0]
            #else:
                #item['door']=NNA
        #else:
            #item['door']=NNA
            
        #door=response.xpath("//div[@id='specs-categories']/div[1]/div[@class='category-details']/div[1]/div[8]/span[2]/text()").extract()
        #if len(door):
            #item['door']=door[0]
        #else:
            #item['door']=NNA
        #name1=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[2]/div[2]/span[1]/text()").extract()
        #if len(name1):
            #if name1[0]=='Base Curb Weight (lbs)':
                #item['weight']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[2]/div[2]/span[2]/text()").extract()[0]
            #else:
                #item['weight']=NNA
        #else:
            #item['weight']=NNA
        
        #weight=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[2]/div[2]/span[2]/text()").extract()
        #if len(weight):
            #item['weight']=weight[0]
        #else:
            #item['weight']=NNA
        ##name2=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[2]/span[1]/text()").extract()
        ##if len(name2):
            ##if name2[0]=='Width, Max w/o mirrors (in)':
                ##item['width']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[2]/span[2]/text()").extract()[0]
            ##else:
                ##item['width']=NNA
        ##else:
            ##item['width']=NNA
       
                
        #width=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[2]/span[2]/text()").extract() 
        #if len(width):
            
            #item['width']=width[0]
        #else:
            #item['width']=NNA
        ##name3=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[4]/span[1]/text()").extract()
        ##if len(name3):
            ##if name3[0]=='Wheelbase (in)':
                ##item['wheelbase']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[4]/span[2]/text()").extract()[0]
            ##else:
                ##item['wheelbase']=NNA
        ##else:
            ##item['wheelbase']=NNA
        #wheelbase=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[4]/span[2]/text()").extract() 
        #if len(wheelbase):
            
            #item['wheelbase']=wheelbase[0]
        #else:
            #item['wheelbase']=NNA     
        #item['wheelbase']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[4]/span[2]/text()").extract()[0]
        
        #item['track_rear']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[5]/span[2]/text()").extract()[0]
        ##name4=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[6]/span[2]/text()")..extract()
        ##if len(name4):
            ##if name4[0]=='Wheelbase (in)':
                ##item['wheelbase']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[4]/span[2]/text()").extract()[0]
            ##else:
                ##item['wheelbase']=NNA
        ##else:
            ##item['wheelbase']=NNA
        #height=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[6]/span[2]/text()").extract()
        #if len(height):
            
            #item['height']=height[0]
        #else:
            #item['height']=NNA 
        #item['height']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[6]/span[2]/text()").extract()[0]
        #length=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[8]/span[2]/text()").extract()
        #if len(length):
            
            #item['length']=length[0]
        #else:
            #item['length']=NNA 
        #item['length']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[8]/span[2]/text()").extract()[0]
        
        #item['track_front']=response.xpath("//div[@id='specs-categories']/div[2]/div[@class='category-details']/div[4]/div[10]/span[2]/text()").extract()[0]
        
        #item['SAE']=response.xpath("//div[@id='specs-categories']/div[4]/div[@class='category-details']/div[1]/div[4]/span[2]/text()").extract()[0]'''
        
        
        
        yield item
           
    
  


        # items=[]
        # node_list=response.xpath("//div[@class='clear']/a")
        # for node in node_list:
        # name=node.xpatn("./span/text()").extract()

        # print(name[0])
