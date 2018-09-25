# from tutorial.items import MyItem
# import scrapy
# import time
#
# # char = ['大','小','一','二','三','十','百','千','多','不']
#
# # id = ['43','49']
#
# char = ['大','小']
# id = ['43','49']
# big5 = ['A46A','A470']
# era = ['甲骨文','金文','楚系文字']
# era_english = ['oracle','jinwen','chuxi']
#
#
#
# class CharSpider(scrapy.Spider):
#     name = "chars"
#
#     def start_requests(self):
#         url = 'http://char.iis.sinica.edu.tw/Search/char_SQL.aspx?char=A464&type=0'
#         yield scrapy.Request(url=url)
#
#     def parse(self, response):
#         html = response.xpath
#         img = response.xpath("//img[@name='charImg']").extract()
#         print(img)
#         idnum = response.xpath("//input[@type='hidden' and @name='char']/@value").extract()
#         print(idnum)
#         input('')