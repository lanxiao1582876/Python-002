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
        # output = f'|{m_title}|\t|{m_type}|\t|{m_time}|\n\n'
        # with open('./maoyanmovie2.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        import csv
        f = open('./maoyanmovie2.csv','a+',encoding='utf-8', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow([movie_name, movie_class, movie_time])
        f.close()
        return item

