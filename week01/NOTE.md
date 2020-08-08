学习笔记
# 一 Xpath
## 1 复制路径
1  F12 --找到相关代码 --右键copy --copy path 

2  插件Xpath hlper --ctrl+shift+x 打开插件 --  ctrl+shift 到相关页面 自动显示路径 --f12 ctrl+f 复制即可找到代码行
## 2  自己写路径
```
<div class="movie-hover-info">
            <div class="movie-hover-title" title="釜山行2：半岛">
              <span class="name">釜山行2：半岛</span>
                <span class="score channel-detail-orange"><i class="integer">6.</i><i class="fraction">6</i></span>
            </div>
            <div class="movie-hover-title xh-highlight" title="釜山行2：半岛">
              <span class="hover-tag">类型:</span>
              动作／惊悚
            </div>
            <div class="movie-hover-title" title="釜山行2：半岛">
              <span class="hover-tag">主演:</span>
              姜栋元／李贞贤／权海孝
            </div>
            <div class="movie-hover-title movie-hover-brief" title="釜山行2：半岛">
              <span class="hover-tag">上映时间:</span>
              2020-08-12
            </div>
          </div>
``` 
movie = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:11]  
movie.xpath('./div[1]/span[1]/text()')  匹配到电影名字  
movie.xpath('./div[2]/text()')[-1]      匹配到类型  
# 2 爬虫思路
1 请求下载，即request  
2 找到相应的路径，例如用xpath,后看规律，是否是用循环  
3 利用方法去除不用的元素，例如换行符(\n)等  
4 取出的数放到字典或列表等，然后存到相应的文件里(panda)

# 3 scrapy
## 1 结构
1. 引擎(Engine)  
“大脑”， 指挥其他组件 协同工作。
2. 调度器(Scheduler)  
调度器接收引擎发过来的请求，按照先后顺序，压入队列中，同时去除重复的请求
3. 下载器(Downloader)  
下载器用于下载网页内容， 并返回给爬虫。
4. 爬虫(Spiders)  
用于从特定的网页中提取需要的信息，即所谓的实体(ltem)
用户也可以从中提取出链接，让Scrapy继续抓取下一个页面。
5. 项目管道(ltem Pipelines)  
项目管道负责处理爬虫从网页中抽取的实体。
主要的功能是持久化实体、验证实体的有效性、清除不需要的信息等。

## 2 路径  
引擎--spider中间件--spider--引擎--调度器--引擎--(下载中间件)--下载器，请求网络返回--引擎--spider--pipeline(或者继续调度)





