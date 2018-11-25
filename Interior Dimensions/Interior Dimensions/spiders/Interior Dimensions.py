import scrapy

from car.items import CarItem

i = 0


class category_spider(scrapy.Spider):
    name = "price"
    start_urls = ['https://www.thecarconnection.com/']

    def parse(self, response):
        node_list = response.xpath("//div[@id='list-by-category-container']/a")
        for node in node_list:
            t_url = node.xpath("./@href").extract()
            if len(t_url):
                t_url_next = "https://www.thecarconnection.com" + t_url[0]
                yield scrapy.Request(url=t_url_next, callback=self.parse_next, dont_filter=False)

    def parse_next(self, response):
        node_list1 = response.xpath("//div[@class='name']")
        for node1 in node_list1:
            c_url = node1.xpath("./a/@href").extract()
            if len(c_url):
                c_url_next = "https://www.thecarconnection.com" + c_url[0]

                yield scrapy.Request(url=c_url_next, callback=self.parse_third, dont_filter=False)

        if len(response.xpath("//li[@class='next']")):
            url_c = response.xpath("//li[@class='next']/a/@href").extract()
            if len(url_c):
                url_c_n = "https://www.thecarconnection.com" + url_c[0]

                yield scrapy.Request(url_c_n, callback=self.parse_next, dont_filter=False)

        if len(response.xpath("//li[@class='next']")) == 0:
            node_list2 = response.xpath("//div[@class='name']")
            for node1 in node_list2:
                h_url = node1.xpath("./a/@href").extract()
                if len(h_url):
                    h_url_next = "https://www.thecarconnection.com" + h_url[0]

                    yield scrapy.Request(url=h_url_next, callback=self.parse_third, dont_filter=False)

    def parse_third(self, response):
        spec = response.xpath("//div[@id='ymm-nav']/a[@id='ymm-nav-specs-btn']/@href").extract()
        if len(spec):
            spec_next = "https://www.thecarconnection.com" + spec[0]

            yield scrapy.Request(url=spec_next, callback=self.parse_four, dont_filter=False)

    def parse_four(self, response):
        item = CarItem()

        type = response.xpath("//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[1]").extract()

        if len(type):
            if type == ['<div class="specs-set-title">Interior Dimensions</div>']:
                name = response.xpath("//div[@id='tcc3-global-container']/h1/text()").extract()
                if len(name):
                    item['name'] = name[0]

                else:
                    item['name'] = 'NAA'

                name0 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[2]/span[1]/text()").extract()
                if len(name0):
                    item['name0'] = name0[0]
                    item['number0'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[2]/span[2]/text()").extract()[0]
                else:
                    item['name0'] = 'NAA'
                    item['number0'] = 'NAA'

                name1 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[3]/span[1]/text()").extract()
                if len(name1):
                    item['name1'] = name1[0]
                    item['number1'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[3]/span[2]/text()").extract()[0]

                name2 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[4]/span[1]/text()").extract()
                if len(name2):
                    item['name2'] = name2[0]
                    item['number2'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[4]/span[2]/text()").extract()[0]

                name3 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[5]/span[1]/text()").extract()
                if len(name3):
                    item['name3'] = name3[0]
                    item['number3'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[5]/span[2]/text()").extract()[0]

                name4 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[6]/span[1]/text()").extract()
                if len(name4):
                    item['name4'] = name4[0]
                    item['number4'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[6]/span[2]/text()").extract()[0]

                name5 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[7]/span[1]/text()").extract()
                if len(name5):
                    item['name5'] = name5[0]
                    item['number5'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[7]/span[2]/text()").extract()[0]

                name6 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[8]/span[1]/text()").extract()
                if len(name6):
                    item['name6'] = name6[0]
                    item['number6'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[2]/div[8]/span[2]/text()").extract()[0]

                yield item


        type1 = response.xpath("//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[1]").extract()

        if len(type1):
            if type1 == ['<div class="specs-set-title">Interior Dimensions</div>']:
                name = response.xpath("//div[@id='tcc3-global-container']/h1/text()").extract()
                if len(name):
                    item['name'] = name[0]

                else:
                    item['name'] = 'NAA'

                name0 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[2]/span[1]/text()").extract()
                if len(name0):
                    item['name0'] = name0[0]
                    item['number0'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[2]/span[2]/text()").extract()[0]
                else:
                    item['name0'] = 'NAA'
                    item['number0'] = 'NAA'

                name1 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[3]/span[1]/text()").extract()
                if len(name1):
                    item['name1'] = name1[0]
                    item['number1'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[3]/span[2]/text()").extract()[0]

                name2 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[4]/span[1]/text()").extract()
                if len(name2):
                    item['name2'] = name2[0]
                    item['number2'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[4]/span[2]/text()").extract()[0]

                name3 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[5]/span[1]/text()").extract()
                if len(name3):
                    item['name3'] = name3[0]
                    item['number3'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[5]/span[2]/text()").extract()[0]

                name4 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[6]/span[1]/text()").extract()
                if len(name4):
                    item['name4'] = name4[0]
                    item['number4'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[6]/span[2]/text()").extract()[0]

                name5 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[7]/span[1]/text()").extract()
                if len(name5):
                    item['name5'] = name5[0]
                    item['number5'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[7]/span[2]/text()").extract()[0]

                name6 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[8]/span[1]/text()").extract()
                if len(name6):
                    item['name6'] = name6[0]
                    item['number6'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[3]/div[8]/span[2]/text()").extract()[0]

                yield item


        type2 = response.xpath("//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[1]").extract()

        if len(type2):
            if type2 == ['<div class="specs-set-title">Interior Dimensions</div>']:
                name = response.xpath("//div[@id='tcc3-global-container']/h1/text()").extract()
                if len(name):
                    item['name'] = name[0]

                else:
                    item['name'] = 'NAA'

                name0 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[2]/span[1]/text()").extract()
                if len(name0):
                    item['name0'] = name0[0]
                    item['number0'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[2]/span[2]/text()").extract()[0]
                else:
                    item['name0'] = 'NAA'
                    item['number0'] = 'NAA'

                name1 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[3]/span[1]/text()").extract()
                if len(name1):
                    item['name1'] = name1[0]
                    item['number1'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[3]/span[2]/text()").extract()[0]

                name2 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[4]/span[1]/text()").extract()
                if len(name2):
                    item['name2'] = name2[0]
                    item['number2'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[4]/span[2]/text()").extract()[0]

                name3 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[5]/span[1]/text()").extract()
                if len(name3):
                    item['name3'] = name3[0]
                    item['number3'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[5]/span[2]/text()").extract()[0]

                name4 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[6]/span[1]/text()").extract()
                if len(name4):
                    item['name4'] = name4[0]
                    item['number4'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[6]/span[2]/text()").extract()[0]

                name5 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[7]/span[1]/text()").extract()
                if len(name5):
                    item['name5'] = name5[0]
                    item['number5'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[7]/span[2]/text()").extract()[0]

                name6 = response.xpath(
                    "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[8]/span[1]/text()").extract()
                if len(name6):
                    item['name6'] = name6[0]
                    item['number6'] = response.xpath(
                        "//div[@id='specs-categories']/div[2]/div[1]/div[1]/div[8]/span[2]/text()").extract()[0]

                yield item
















