from tutorial.items import MyItem
import scrapy
import time

# char = ['大','小','一','二','三','十','百','千','多','不']

# id = ['43','49']

char = ['大','小']
id = ['43','49']
big5 = ['A46A','A470']
era = ['甲骨文','金文','楚系文字']
era_english = ['oracle','jinwen','chuxi']



class ImageSpider(scrapy.Spider):
    name = "chinese"

    def start_requests(self):

        for i in range(len(char)):
            for u,e in enumerate(era):
                url = ("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(id[i],
                                                                                                            char[i],
                                                                                                            era[u]))
                filename = big5[i]+era_english[u]
                yield scrapy.Request(url=url, callback=self.parse,meta={'index':i,
                                                                        'id':id[i],
                                                                        'big5':big5[i],
                                                                        'char':char[i],
                                                                        'era':era[u],
                                                                        'era_english':era_english[u],
                                                                        'filename':'big5'
                                                                        })

    def parse(self, response):
        print(response.meta['char'])
        i =0
        item = MyItem()
        for elem in response.xpath("//img"):
            time.sleep(5)
            img_url = elem.xpath("@src").extract_first()
            img_url = 'http://char.iis.sinica.edu.tw'+img_url
            mname = 'acs/'+ response.meta['id']+'/'+response.meta['id']+response.meta['era_english']+str(i)+'.gif'
            i+=1
            item['image_urls'] = img_url
            item['image_name'] = mname
            yield item