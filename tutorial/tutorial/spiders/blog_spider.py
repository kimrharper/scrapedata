import scrapy

pagination = '//div[@id="main"]/div/div/ul'


class BlogSpider(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "blog"

    # URL(s) to start with.
    start_urls = [
        'http://lang-8.com/3076/journals',
    ]

    # Use XPath to parse the response we get.
    def parse(self, response):
        hxs = response
        item = TutorialItem()
        link = hxs.select('//div//img/@src').extract()
        item['image_urls'] = ["http://www.roxie.com" + link]
        print(item)
        return item
        # page = response
        # filename = 'bloogg.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

