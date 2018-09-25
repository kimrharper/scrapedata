import scrapy
import pandas as pd

class ChineseSpider(scrapy.Spider):
    name = "chinese"

    def start_requests(self):
        urls = [
            'http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char=592&word=我&font=甲骨文',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        newfile = pd.DataFrame(columns=['id', 'char', 'link'])
        newfile.loc[1] = ([1, 'chinese', 'www.google.com'])

        page = response.url.split("/")[-2]
        filename = 'chinese-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)