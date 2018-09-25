import scrapy
from scrapy.http import FormRequest


class GolfscraperSpider(scrapy.Spider):
    name = "golfscraper"
    allowed_domains = ["golf.org.au","www.golf.org.au"]
    ids = ['3012801330', '3012801331', '3012801332', '3012801333']
    start_urls = []
    for id in ids:
        start_urls.append('http://www.golf.org.au/handicap/%s' %id)

    def parse(self, response):
        scrapy.FormRequest('http://www.golf.org.au/default.aspx?s=handicap',
                           formdata={
                               '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                               'ctl11$ddlHistoryInMonths':'48',
                               '__EVENTTARGET': 'ctl11$ddlHistoryInMonths',
                               '__EVENTVALIDATION' : response.css('input#__EVENTVALIDATION::attr(value)').extract_first(),
                               'gaHandicap' : '6.5',
                               'golflink_No' : '2012003003',
                               '__VIEWSTATEGENERATOR' : 'CA0B0334',
                           },
                           callback=self.parse_details)

    def parse_details(self,response):
        for name in response.css('div.rnd-course::text').extract():
            yield {'name' : name}