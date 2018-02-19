# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb
from Instagram.items import *

class InstagramPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(db = 'SAMPLE_INSTAGRAM', host = 'localhost' , user = 'root' , passwd='')
        self.conn.set_character_set('utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')
        self.cursor.execute('SET autocommit=1')

    def process_item(self, item, spider):
        if isinstance(item, InstagramItem):
            query = "insert into Insta(fullname, username, title, propicurl,logging_page_id,mutual_followers,biography ) values( %s, %s, %s, %s,%s, %s, %s)"

            values = (item.get('fullname', ''), item.get('username', ''), item.get('title', ''), item.get('propicurl', ''), item.get('logging_page_id',''), item.get('mutual_followers',''), item.get('biography',''))
            self.cursor.execute(query, values)
            self.conn.commit()
        #return item

