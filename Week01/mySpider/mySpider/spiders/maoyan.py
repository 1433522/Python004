# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        items = []

        movies = response.xpath("//div[@class='movie-hover-info']")[:10]
        for movie in movies:
            print(movie)
            item = MovieItem()

            title = movie.xpath("./div[1]/span[1]/text()").get()
            mv_type = movie.xpath("./div[2]/text()")[1].get().strip()
            mv_date = movie.xpath('./div[4]/text()')[1].get().strip()

            item['title'] = title
            item['mv_type'] = mv_type
            item['mv_date'] = mv_date

            items.append(item)

        return items


