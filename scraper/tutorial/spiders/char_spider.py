from tutorial.items import MyItem
import scrapy
import time

char_line1 = ['大','小','一','二','三','十','百','千','多','不']
char_line2 = ['人','夫','子','男','女','王','主','我','你','他']
char_line3 = ['口','說','目','見','耳','聞','手','工','腳','行']
era,era_english = ['甲骨文','金文','楚系文字','小篆'],['oracle','jinwen','chuxi','smallseal']

class CharSpider(scrapy.Spider):
    name = "chars"

    def start_requests(self):
        for c in char_line3:
            time.sleep(1)
            big5= c.encode('hkscs').hex()
            url = 'http://char.iis.sinica.edu.tw/Search/char_SQL.aspx?char={}&type=0'.format(big5)
            yield scrapy.Request(url=url,meta={'char':c,'big5':big5})

    def parse(self, response):
        meta = response.meta
        # img = response.xpath("//img[@name='charImg']/@src").extract_first()[2:]

        meta['id'] = idnum = response.xpath("//input[@type='hidden' and @name='char']/@value").extract()[0]
        for chinese_era, english_era in zip(era, era_english):
            time.sleep(2)
            url = ("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(idnum,
                                                                                                         meta['char'],
                                                                                                         chinese_era))
            print(url)
            meta['era'] = chinese_era
            meta['era_english'] = english_era
            yield scrapy.Request(url=url,callback=self.parse_images,meta=meta)

    def parse_images(self, response):
        i = 0
        item = MyItem()

        # code for original image [doesntwork]
        # item['image_urls'] = 'http://char.iis.sinica.edu.tw/'+ response.meta['orig_pic']
        # item['image_name'] = 'acs/' + response.meta['big5'] + '/' + response.meta['big5']+'.gif'
        # yield item
        char_meta = []

        for elem in response.xpath("//img"):
            m = response.meta
            img_url = 'http://char.iis.sinica.edu.tw' + elem.xpath("@src").extract_first()
            img_name = 'acs/' + m['big5'] + '/' + m['big5'] + '-' + m['era_english'] +'_'+ '{:03}'.format(i) + '.gif'
            item['image_urls'],item['image_name'] = img_url,img_name
            char_meta.append([m['char'],m['big5'],m['id'],m['era_english'],m['era'],img_name])
            i += 1
            time.sleep(2)
            yield item

        with open('chars_data.csv', 'a') as c_data:
            for row in char_meta:
                for column in row:
                    c_data.write(column + ',')
                c_data.write('\n')
        c_data.close()

