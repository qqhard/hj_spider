from scrapy.spiders import Spider
import scrapy
from scrapy_splash import SplashRequest

class HJSpider(Spider):
    name = 'hj_spider'
    start_urls = ['http://fund.eastmoney.com/HBJJ_dwsy.html']

    def parse(self, response):

        if response.url in self.start_urls:
            urls = response.xpath('//*/td[5][@class="jc"]/nobr/a[1]/@href').extract()
            # urls = response.xpath('//*/td[5][@class="jc"]/nobr/a[1]/@href').extract()[0:4]
            for url in urls:
                yield SplashRequest(url=url, callback=self.parse,
                    args={
                        'wait': 5.0,
                        'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
                    })
        else:
            self.parse_detail(response)


    def parse_detail(self, response):
        name = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[1]/div[1]/div/text()').extract()
        nh_shouyi = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[2]/dl[3]/dd[1]/span[2]/text()').extract()

        start_date = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[1]/text()').extract()
        scale = response.xpath('//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/text()').extract()
        ttt = response.xpath('//*[@id="highcharts-24"]/svg/g[5]/g[3]/rect/@height').extract()
        # print (response.url, name, nh_shouyi, start_date, scale, ttt)
        print ('{};;{};;{};;{};;{};;{}'.format(name, response.url, nh_shouyi, start_date, scale, ttt))
        pass


