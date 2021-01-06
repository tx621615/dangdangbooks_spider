import requests  # urllib urllib3
from bs4 import BeautifulSoup  # re  lxml(xpath)
import json
import time
import random
import re


def getHTMLText(url):
    h = {"User-Agent": "Mozilla/5.0"}  # 模拟人类访问行为
    try:
        r = requests.get(url, headers=h)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return ""


def parsePage(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        soup_allli = soup.find_all('li', class_=re.compile("line[\d]"))  # 获得所有li标签
        for soup_li in soup_allli:
            global count
            if count > 1000:
                break

            count = count + 1
            print(count, file=desf)

            soup_name = soup_li.a.attrs['title'].strip() # 获取书名
            print(soup_name, file=desf)

            soup_price = soup_li.find('p', class_="price")
            price = soup_price.span.get_text()
            price = price.strip('¥')
            print(price, file=desf)

            soup_author = soup_li.find('p', class_="search_book_author")
            detail = soup_author.get_text()
            detail = detail.split('加')
            detail = detail[0].split('/')
            try:
                name = detail[0].strip()
                print("作者名:" + name, file=desf)
            except:
                print("作者名:未知", file=desf)
            try:
                date = detail[1].strip()
                print("出版日期:" + date, file=desf)
            except:
                print("出版日期:未知", file=desf)
            try:
                shop = detail[2].strip()
                print("出版社:" + shop, file=desf)
            except:
                print("出版社:未知", file=desf)
            soup_comment = soup_li.find('p', class_="search_star_line")
            commentnum = soup_comment.get_text()
            print("评论数:" + commentnum, file=desf)
            print("---"*30, file=desf)
    except:
        print("")


def main():
    start_url = 'http://search.dangdang.com/?key=python&act=input&page_index={}'
    for i in range(1, 26):
        url = start_url.format(i)
        html = getHTMLText(url)
        parsePage(html)


if __name__ == '__main__':
    datafilename = ".\\data\\01dangdangbook.txt"  # 实际使用了dangdangbooks.txt保存data,这里只是为了避免覆盖而进行的测试
    count = 0  # 用于统计书籍序号
    with open(datafilename, 'w+') as desf:  # 保存数据到文件
        main()
