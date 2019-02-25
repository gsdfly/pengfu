# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,json

class PengfuPipeline(object):
    # @classmethod
    # def from_crawler(cls, crawler):
    #     # print('11111111111111111')
    #     # print(cls) #当前管道对象
    #     # print(crawler) #整个项目爬虫对象
    #     # print('22222222222222')
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    def __init__(self):
        self.db = pymysql.connect("47.75.84.250", "root", "158269", "lty", charset='utf8')
        self.cursor = self.db.cursor()
    # def open_spider(self,spider):
    #     print(spider)
    #     print('open_spider')

    def process_item(self, item, spider):
        # print(item)
        # return item
        # sql = '''
        #     insert into pengfu (name,title,content,img) values (%s,%s,%s,%s)
        # '''
        # try:
        #     self.cursor.execute(sql, (item['name'],item['title'],item['content'],item['img']))
        #     self.db.commit()
        # except Exception as e:
        #     self.db.rollback()
        # str = json.dumps(dict(item), ensure_ascii=False) + " "
        # str = str.encode('utf-8').decode('utf-8')
        # print(str)
        return item

    def close_spider(self,spider):
        print('close_spider')
        self.db.close()