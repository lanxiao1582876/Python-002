import scrapy
from spiders.items import maoyanItem
from scrapy.selector import Selector
from lxml import etree
from time import sleep 

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):      
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
    # 解析函数
    def parse(self, response):
        # 打印网页的url
        # print(response.url)
        # 打印网页的内容
        # print(response.text)
        try:
            movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:11]
            for movie in movies:
                item = maoyanItem()
                movie_name = movie.xpath('./div[1]/span[1]/text()')
                movie_class = movie.xpath('./div[2]/text()')[-1]
                movie_time = movie.xpath('./div[4]/text()')[-1]
                
                print(movie_name.extract_first().strip())
                print(movie_class.extract().strip())
                print(movie_time.extract().strip())
    
                item['movie_name'] = movie_name.extract_first().strip()
                item['movie_class'] = movie_class.extract().strip()
                item['movie_time'] = movie_time.extract().strip()
                yield item
        except expression as e:
            print(e)
        
            