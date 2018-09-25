from tutorial.items import MyItem
import scrapy
import time

# char = ['大','小','一','二','三','十','百','千','多','不']
# big5char = ['A46A','A470']
# id = ['43','49']

char = ['大','小']
id = ['43','49']
era = ['甲骨文','金文','楚系文字']
l=[]

for i in range(len(char)):
    for e in era:
        l.append("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(id[i],char[i],e))
input(l)

class ImageSpider(scrapy.Spider):
    name = "chinese"

    def start_requests(self):
        urls = l
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for elem in response.xpath("//img"):
            img_url = elem.xpath("@src").extract_first()
            img_url = 'http://char.iis.sinica.edu.tw'+img_url
            yield MyItem(image_urls=[img_url])