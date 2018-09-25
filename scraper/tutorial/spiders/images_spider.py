from tutorial.items import MyItem
import scrapy
import time

# char = ['大','小','一','二','三','十','百','千','多','不']
# big5char = ['A46A','A470']
# id = ['43','49']

char = ['大','小']
id = ['43','49']
era = ['甲骨文','標楷體']
l=[]



class ImageSpider(scrapy.Spider):
    name = "chinese"

    def start_requests(self):

        for i in range(len(char)):
            for e in era:
                url = ("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(id[i],
                                                                                                               char[i],
                                                                                                               e))
                yield scrapy.Request(url=url, callback=self.parse,meta={'index':1,'id':id[i],'char':char[i],'era':e})

    def parse(self, response):
        print(response.meta['char'])
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            img_url = 'http://char.iis.sinica.edu.tw'+img_url
            yield MyItem(image_urls=[img_url])