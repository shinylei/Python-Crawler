# -*- coding: UTF-8 -*- 
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
        	try:
        		stock = re.findall(r's[hz]\d{6}', href)[0]
        		url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
        		yield scrapy.Request(url, callback=self.parse_stock)
        	except:
        		continue

    def parse_stock(self, response):
    	infoDic = {}
    	stockInfo = response.css('.stock-bets')
    	name = stockInfo.css('.bets-name').extract()[0] 
    	keys = stockInfo.css('dt').extract()
    	vals = stockInfo.css('dd').extract()
    	for i in range(len(keys)):
    		key = re.findall(r'>.*?</dt>', keys[i])[0][1:-5]
    		try:
    			val = re.findall(r'\d\.?\d*</dd>', vals[i])[0][0: -5]
    		except:
    			val = '--'
    		infoDic[key] = val

    	yield infoDic