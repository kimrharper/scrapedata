# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request



class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.meta.get('filename', '')

    def get_media_requests(self, item, info):
        try:
            img_url = item['image_urls']
            meta = {'filename': item['image_name']}
            yield Request(url=img_url, meta=meta)
        except Exception as e: print(e)


    # #Name download version
    # def file_path(self, request, response=None, info=None):
    #     item=request.meta['image_name'] # Like this you can use all from item, not just url.
    #     # image_guid = request.url.split('/')[-1]
    #     return 'full/%s' % (item)
    #
    # # #Name thumbnail version
    # # def thumb_path(self, request, thumb_id, response=None, info=None):
    # #     image_guid = thumb_id + response.url.split('/')[-1]
    # #     return 'thumbs/%s/%s.jpg' % (thumb_id, image_guid)
    #
    # def get_media_requests(self, item, info):
    #     # yield Request(item['image']) # Adding meta. Dunno how to put it in one line :-)
    #     for image in item:
    #         yield Request(image)