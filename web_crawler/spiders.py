"""爬虫z控制中枢"""
from web_crawler.image_spider.zhazhadu import CRAWLER__ZHAZHADU

def crawl_image(image_key, image_num=1):
    if image_num < 600:
        page_num = 1
        start_page_num = 1
    else:
        page_num = 2
        start_page_num = 1
    sign = CRAWLER__ZHAZHADU.start(image_key, page_num, start_page_num, image_num)
    return sign

