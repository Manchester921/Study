# -*- coding: utf-8 -*-
import scrapy

# from items import DoubanmovieItem
from doubanMovie.items import DoubanmovieItem


class MovieinfoSpider(scrapy.Spider):
    name = 'movieInfo'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    # start_urls =  ['https://movie.douban.com/top250?start=%s&filter='%i for i in range(250) if i%25==0]
    

    def parse(self, response):
        movie_items = response.xpath('//div[@class="item"]')
        for item in movie_items:
            movie = DoubanmovieItem()
            movie['rank'] = item.xpath('div[@class="pic"]/em/text()').extract()
            movie['title'] = item.xpath('div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            movie['link'] = item.xpath('div[@class="info"]/div[@class="hd"]/a/@href').extract()
            movie['rating'] = item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            movie['participants'] = item.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            movie['quote'] = item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            
            movie['picSrc'] = item.xpath('div[@class="pic"]/a/img/@src').extract()
            
            yield movie
            pass

        nextPage = response.xpath('//span[@class="next"]/a/@href')
        if nextPage:
            url = response.urljoin(nextPage[0].extract())
            yield scrapy.Request(url, self.parse)

        pass
