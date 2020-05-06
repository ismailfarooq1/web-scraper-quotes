# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesScrapeSpider(scrapy.Spider):
    name = 'quotes_scrape'
    allowed_domains = ['quotes.toscrape.com']
    

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            return splash:html()
        end
    '''  

    def start_requests(self):
        print("\nHELLOOO\n")
        yield SplashRequest(url="http://quotes.toscrape.com/js/", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        print("\nPSSSSSTTTT\n")
        print(response)
