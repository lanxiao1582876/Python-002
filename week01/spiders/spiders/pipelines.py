# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


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

        # with open('./maoyan_v2.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        # return item

        # import pandas as pd
        # movie1 = pd.DataFrame(data = item)
        # # windows需要使用gbk字符集
        # movie1.to_csv('./maoyan2.csv', encoding='utf8', index=False, header=False)
        # return item


