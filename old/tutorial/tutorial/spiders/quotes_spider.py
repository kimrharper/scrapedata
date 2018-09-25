# import scrapy
# from scrapy_splash import SplashRequest
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/js/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield SplashRequest(url=url, callback=self.parse)
#
#     def parse(self, response):
#         input('type something here')
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)