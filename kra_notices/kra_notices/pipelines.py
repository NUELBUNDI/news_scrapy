# useful for handling different item types with a single interface

# 1.Convert Html to text

import html2text
import mysql.connector

h = html2text.HTML2Text()
h.ignore_links= False

from itemadapter import ItemAdapter


class KranewsPipeline:
    def process_item(self, item, spider):
        
        item['article']= h.handle(item['article'])
        
        return item
    
class SavingToMysqlPipeline(object):
    
    def __init__(self) -> None:
        self.create_connection()
        
    def create_connection(self):
        self.connection = mysql.connector.connect(
            
            host     = 'localhost',
            user     =  'root',
            password =  '1234',
            database =  'scrapy_db',
            port     =  '3306'
        )
        
        self.curr = self.connection.cursor()
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute(""" insert into kra_notices (notice_title,notice_date,notice_text,notice_url) VALUES(%s, %s,%s,%s)""",(
            
            item['title'],
            item['date'],
            item['article'],
            item['url']
        ))
        
        self.connection.commit()

