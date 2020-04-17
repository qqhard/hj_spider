from scrapy.spiders import Spider
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy_splash import SplashRequest


class HJSpider(Spider):
    name = 'hj2_spider'
    start_urls = ['http://fund.eastmoney.com/HBJJ_dwsy.html']

    def parse(self, response):

        if response.url == 'http://fund.eastmoney.com/HBJJ_dwsy.html':
            urls = response.xpath('//*/td[5][@class="jc"]/nobr/a[1]/@href').extract()[0:4]
            for url in urls:
                yield SplashRequest(url=url, callback=self.parse, args={'wait': 0.5})
                # yield scrapy.Request(url, callback=self.parse)
        else:
            self.parse_detail(response)


    def parse_detail(self, response):
        name = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[1]/div[1]/div/text()').extract()
        nh_shouyi = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[1]/dl[4]/dd/span/text()').extract()
        start_date = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/text()').extract()
        scale = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/text()').extract()
        ttt = response.xpath('//*[@id="highcharts-24"]/svg/g[5]/g[3]/rect[4]/@height').extract()
        # print (response.url, name, nh_shouyi, start_date, scale, ttt)
        print ('{};;{};;{};;{};;{};;{}'.format(name[0], response.url, nh_shouyi[0], start_date[0], scale[0], ttt[0]))
        pass


