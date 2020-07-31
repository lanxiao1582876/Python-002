# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
import pymysql





class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        movie_name =  item['movie_name']
        movie_class = item['movie_class']
        movie_time = item['movie_time']
       
        output = f'|{movie_name}|\t|{movie_class}|\t|{movie_time}|\n\n'
        print(type(output))
        print(output)

        import csv

        with open('manyan_scrap.csv', mode='a+', encoding='utf-8') as csv_file:
            fieldnames = ['movie_name', 'movie_class', 'movie_time']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
            #writer.writeheader()
            writer.writerow(item)
        return item

class ScrapymysqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='192.168.43.128',
            port=3306,
            db='python',
            user='root',
            password='Jiwei123@',
            charset='utf8',
            use_unicode=True
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            # 
            """insert into manyan(movie_name, movie_class, movie_time) value (%s, %s, %s)""", (item['movie_name'], item['movie_class'], item['movie_time'],))
        # 提交事务
        self.connect.commit()
        # 必须实现返回
        return item


#  class WebcrawlerScrapyPipeline(object):
#     '''保存到数据库中对应的class
#        1、在settings.py文件中配置
#        2、在自己实现的爬虫类中yield item,会自动执行'''

#     def __init__(self, dbpool):
#         self.dbpool = dbpool

#     @classmethod
#     def from_settings(cls, settings):
#         '''1、@classmethod声明一个类方法，而对于平常我们见到的叫做实例方法。
#            2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
#            3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
#         #读取settings中配置的数据库参数
#         dbparams = dict(
#             host=settings['MYSQL_HOST'],  
#             db=settings['MYSQL_DBNAME'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
#             cursorclass=MySQLdb.cursors.DictCursor,
#             use_unicode=False,
#         )
#         dbpool = adbapi.ConnectionPool('MySQLdb', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
#         return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

#     # pipeline默认调用
#     def process_item(self, item, spider):
#         query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
#         query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
#         return item

#     # 写入数据库中
#     # SQL语句在这里
#     def _conditional_insert(self, tx, item):
#         sql = "insert into manyan(movie_name,movie_class,url,movie_time) values(%s,%s,%s)"
#         params = (item['movie_name'], item['movie_class'], item['movie_time'])
#         tx.execute(sql, params)
#         return item

#     # 错误处理方法
#     def _handle_error(self, failue, item, spider):
#         print(failue)


