"""
软设2班
created by Tang Xin
copyright USTC
2021.1.4
功能：该模块用于爬取当当网前1001本书的信息（书名，价格，作者，出版社，出版日期，评论数）
"""


import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url):
    """
    根据url获取相应的HTML文档
    :param url: 需要查询的网站
    :return: 返回url对应的HTML文档
    """

    h = {"User-Agent": "Mozilla/5.0"}  # 模拟人类访问行为
    try:
        r = requests.get(url, headers=h)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return ""


def parsePage(html):
    """
    通过BeautifulSoup库解析对应的HTML文档，获取书籍对应的书名，价格，作者，出版社，出版日期，评论数
    :param html: 需要解析的HTML文档
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        soup_allli = soup.find_all('li', class_=re.compile("line[\d]"))  # 获得所有li标签
        for soup_li in soup_allli:
            global count
            if count > 1000:   # 爬取1001本书籍信息
                break

            count = count + 1  # 计算书籍的序号
            print(count, file=desf)

            soup_name = soup_li.a.attrs['title'].strip()  # 获取书名
            print(soup_name, file=desf)

            soup_price = soup_li.find('p', class_="price")  # 获取价格
            price = soup_price.span.get_text()
            price = price.strip('¥')
            print(price, file=desf)

            soup_author = soup_li.find('p', class_="search_book_author")  # 获取作者等相关信息
            detail = soup_author.get_text()
            detail = detail.split('加')
            detail = detail[0].split('/')
            try:
                name = detail[0].strip()  # 获取作者
                print("作者名:" + name, file=desf)
            except:
                print("作者名:未知", file=desf)
            try:
                date = detail[1].strip()  # 获取出版日期
                print("出版日期:" + date, file=desf)
            except:
                print("出版日期:未知", file=desf)
            try:
                shop = detail[2].strip()  # 获取出版社
                print("出版社:" + shop, file=desf)
            except:
                print("出版社:未知", file=desf)
            soup_comment = soup_li.find('p', class_="search_star_line")  # 获取评论数
            commentnum = soup_comment.get_text()
            print("评论数:" + commentnum, file=desf)
            print("---"*30, file=desf)
    except:
        print("")


def main():
    start_url = 'http://search.dangdang.com/?key=python&act=input&page_index={}'  # 当当网url基本格式，page_index是一个变化的参数，以便用于不断翻页
    for i in range(1, 26):
        url = start_url.format(i)  # 形成对应的页的url
        html = getHTMLText(url)   # 获取对应的HTML文档
        parsePage(html)          # 解析文档


if __name__ == '__main__':
    datafilename = ".\\data\\01dangdangbook.txt"  # 实际使用了dangdangbooks.txt保存data,这里只是为了避免覆盖而进行的测试
    count = 0  # 用于统计书籍序号
    with open(datafilename, 'w+') as desf:  # 保存数据到文件
        main()
