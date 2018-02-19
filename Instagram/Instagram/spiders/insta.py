from scrapy.http import  Request, FormRequest
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from Instagram.items import *
import json
import MySQLdb

class Instagram(BaseSpider):
    name = 'Instagram'
    #start_urls = ['https://www.instagram.com/rajasekhar/?__a=1','https://www.instagram.com/karthik/?__a=1', 'https://www.instagram.com/aravind/?__a=1', 'https://www.instagram.com/kiranmayi/?__a=1',]
    start_urls = ['https://www.instagram.com/kiranmayi/?__a=1']
    #handle_httpstatus_list = [401, 404, 302, 303, 403, 500, 100]
    def __init__(self):
        """Connecting to Database"""
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd='',db="", charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()
    def parse(self, response):
        data = json.loads(response.body)
        user_data = data.get('user', {})
        full_name = user_data.get('full_name', '')
        if full_name is None:
            full_name = ''
        id_ = user_data.get('id', '')
        username = user_data.get('username', '')
        url = user_data.get('profile_pic_url', '')
        logging_page_id = user_data.get('logging_page_id', '')
        mutual_followers = user_data.get('mutual_followers','')
        biography = user_data.get('biography', '')
        insta = InstagramItem()
        insta['fullname'] = full_name
        insta['username'] = username
        insta['title'] = str(id_)
        insta['propicurl'] = str(url)
        insta['logging_page_id'] = str(logging_page_id)
        insta['mutual_followers'] = str( mutual_followers)
        insta['biography'] = str(biography)
        yield insta



