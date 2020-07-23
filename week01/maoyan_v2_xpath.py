import requests
import lxml.etree

# 爬取页面详细信息

# 猫眼页面
url = 'https://maoyan.com/films?showType=3'

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# 模仿浏览器的报头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
connection = 'keep-alive'
# 使用一个字典之前一定要先声明
header =  {}
header['user-agent'] = user_agent
header['accept'] = accept
header['connection'] = connection

response = requests.get(url, headers=header)
# print(response.text)

# xml化处理 dd
selector = lxml.etree.HTML(response.text.replace("<dd>","</dd><dd>"))

from time import sleep
mylist = []
for i in range(1,11):
    # 电影名称
    film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd['+str(i)+']/div[1]/div[2]/a/div/div[1]/span[1]/text()')                       
    print(f'电影名称: {film_name}')

    # 类型
    #film_class = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[i]/div[1]/div[2]/a/div/div[2]/text()')[1].strip()
    film_class = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd['+str(i)+']/div[1]/div[2]/a/div/div[2]/text()')[1].strip()

    print(f'类型：{film_class}')

    # 上映日期
    plan_date = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd['+str(i)+']/div[1]/div[2]/a/div/div[4]/text()')[1].strip()
    print(f'上映日期: {plan_date}')

    mylist.append([film_name,film_class,plan_date])
    print(mylist)

    sleep(2)


import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)

