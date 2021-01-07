"""
软设2班
created by Tang Xin
copyright USTC
2021.1.4
功能: 该模块用于统计分析书籍信息（根据评论数，价格区间，出版社，出版日期）
"""


import json


def countCommentNum(filename, hotfilename, totalStatistic_filename):
    """
    统计不同评论数（0，100，1000，10000， >10000）的书籍信息
    :param filename: 保存所有书籍信息的文件，用于读取
    :param hotfilename: 用于保存评论数大于1000的所有书籍信息，这些书籍称为hotbooks
    :param totalStatistic_filename: 用于保存根据评论划分后的书籍信息
    """
    with open(filename, 'r+') as fjson:
        books = json.loads(fjson.read())
        hotbooks = []  # 统计评论大于1000的书，这些书籍形成hotbooks
        for bookobj in books:
            try:
                temp = {}
                if bookobj['commentNum'] >= 1000:
                    temp['index'] = bookobj['index']
                    temp['name'] = bookobj['name']
                    temp['commentNum'] = bookobj['commentNum']
                    temp['price'] = bookobj['price']
                    temp['publisher'] = bookobj['publisher']
                    temp['publishTime'] = bookobj['publishTime']
                    hotbooks.append(temp)
            except:
                continue
        with open(hotfilename, "w+") as jsonFile:
            jsonFile.write(json.dumps(hotbooks, indent=4, ensure_ascii=False))

        # 统计各个评论区间的书，0，100，1000，10000
        commentnum_lessthan100 = []
        commentnum_lessthan1000 = []
        commentnum_lessthan10000 = []
        commentnum_morethan10000 = []
        for bookobj in books:
            try:
                temp = {}
                temp['index'] = bookobj['index']
                temp['name'] = bookobj['name']
                temp['commentNum'] = bookobj['commentNum']
                if bookobj['commentNum'] < 100:
                    commentnum_lessthan100.append(temp)
                elif bookobj['commentNum'] < 1000:
                    commentnum_lessthan1000.append(temp)
                elif bookobj['commentNum'] < 10000:
                    commentnum_lessthan10000.append(temp)
                else:
                    commentnum_morethan10000.append(temp)
            except:
                continue

        # 形成对应的json文件
        commentnum_lessthan100_Json = {}
        commentnum_lessthan1000_Json = {}
        commentnum_lessthan10000_Json = {}
        commentnum_morethan10000_Json = {}
        totalStatistic_Json = {}
        commentnum_lessthan100_Json['commentnum_lessthan100_booksNum'] = len(commentnum_lessthan100)
        commentnum_lessthan100_Json['commentnum_lessthan100_books'] = commentnum_lessthan100
        commentnum_lessthan1000_Json['commentnum_lessthan1000_booksNum'] = len(commentnum_lessthan1000)
        commentnum_lessthan1000_Json['commentnum_lessthan1000_books'] = commentnum_lessthan1000
        commentnum_lessthan10000_Json['commentnum_lessthan10000_booksNum'] = len(commentnum_lessthan10000)
        commentnum_lessthan10000_Json['commentnum_lessthan10000_books'] = commentnum_lessthan10000
        commentnum_morethan10000_Json['commentnum_morethan10000_booksNum'] = len(commentnum_morethan10000)
        commentnum_morethan10000_Json['commentnum_morethan10000_books'] = commentnum_morethan10000
        totalStatistic_Json['commentnum_lessthan100_books'] = commentnum_lessthan100_Json
        totalStatistic_Json['commentnum_lessthan1000_books'] = commentnum_lessthan1000_Json
        totalStatistic_Json['commentnum_lessthan10000_books'] = commentnum_lessthan10000_Json
        totalStatistic_Json['commentnum_morethan10000_books'] = commentnum_morethan10000_Json
        with open(totalStatistic_filename, 'w+') as jsonFile:
            jsonFile.write(json.dumps(totalStatistic_Json, indent=4, ensure_ascii=False))


# 对所有书籍的统计，对热度书籍的统计,注意hotbooks和dangdangbooks中json格式要完全一致
def countPriceRange(filename, savefilename):
    """
    统计处于不同价格区间（0，50，100，150，>150）的书籍信息
    :param filename: 保存所有书籍信息的文件，用于读取
    :param savefilename: 保存统计后数据的文件
    """
    with open(filename, 'r+') as fjson:
        pricerange1 = []   # 0-50
        pricerange2 = []   # 50-100
        pricerange3 = []   # 100-150
        pricerange4 = []   # >150
        books = json.loads(fjson.read())

        for bookobj in books:  # 获取各个区间的书籍信息
            try:
                temp = {}
                if float(bookobj['price']) < 50:
                    temp['index'] = bookobj['index']
                    temp['name'] = bookobj['name']
                    temp['price'] = float(bookobj['price'])
                    pricerange1.append(temp)
                elif float(bookobj['price']) < 100:
                    temp['index'] = bookobj['index']
                    temp['name'] = bookobj['name']
                    temp['price'] = float(bookobj['price'])
                    pricerange2.append(temp)
                elif float(bookobj['price']) < 150:
                    temp['index'] = bookobj['index']
                    temp['name'] = bookobj['name']
                    temp['price'] = float(bookobj['price'])
                    pricerange3.append(temp)
                else:
                    temp['index'] = bookobj['index']
                    temp['name'] = bookobj['name']
                    temp['price'] = float(bookobj['price'])
                    pricerange4.append(temp)
            except:
                continue
        # 形成对应的json文件
        books_price_range = {}
        books_price_range['price_lessthan50'] = len(pricerange1)
        books_price_range['price_lessthan100'] = len(pricerange2)
        books_price_range['price_lessthan150'] = len(pricerange3)
        books_price_range['price_morethan150'] = len(pricerange4)
        with open(savefilename, 'w+') as f:
            f.write(json.dumps(books_price_range, indent=4, ensure_ascii=False))


# 统计书籍中各个出版商的数目
def countPublisherNum(filename, savefilename):
    """
    统计书籍中各个出版社出现次数
    :param filename: 保存所有书籍信息的文件，用于读取
    :param savefilename: 保存统计后数据的文件
    :return:
    """
    with open(filename, 'r+') as fjson:
        books = json.loads(fjson.read())
        publishers = {}
        for bookobj in books:  # 统计各个出版社数目
            try:
                if bookobj['publisher'] != "未知":
                    if bookobj['publisher'] in publishers:
                        publishers[bookobj['publisher']] = publishers[bookobj['publisher']] + 1
                    else:
                        publishers[bookobj['publisher']] = 1
            except:
                continue
        with open(savefilename, "w+") as jsonFile:  # 保存为json文件
            jsonFile.write(json.dumps(publishers, indent=4, ensure_ascii=False))


def coutPublishTimeRangeNum(filename, savefilename):
    """
    统计处于不同出版日期（<2016,2016,2017,2018,2019,2020）的书籍信息
    :param filename: 保存所有书籍信息的文件，用于读取
    :param savefilename: 保存统计后数据的文件
    :return:
    """
    with open(filename, 'r+') as fjson:
        books = json.loads(fjson.read())
        # 统计处于不同出版日期（<2016,2016,2017,2018,2019,2020）的书籍信息
        Bookslessthan2016 = []
        Books2016 = []
        Books2017 = []
        Books2018 = []
        Books2019 = []
        Books2020 = []
        for bookobj in books:
            try:
                year = int(bookobj['publishTime'].split('-')[0])
                temp = {}
                temp['index'] = bookobj['index']
                temp['name'] = bookobj['name']
                temp['publishTime'] = bookobj['publishTime']
                if year < 2016:
                    Bookslessthan2016.append(temp)
                elif year == 2016:
                    Books2016.append(temp)
                elif year == 2017:
                    Books2017.append(temp)
                elif year == 2018:
                    Books2018.append(temp)
                elif year == 2019:
                    Books2019.append(temp)
                elif year == 2020:
                    Books2020.append(temp)
                else:
                    continue
            except:
                continue
        # 用字典保存所有信息，以便形成json文件
        Bookslessthan2016_json = {}
        Books2016_json = {}
        Books2017_json = {}
        Books2018_json = {}
        Books2019_json = {}
        Books2020_json = {}
        Bookslessthan2016_json['Bookslessthan2016Num'] = len(Bookslessthan2016)
        Bookslessthan2016_json['Bookslessthan2016'] = Bookslessthan2016
        Books2016_json['Books2016Num'] = len(Books2016)
        Books2016_json['Books2016'] = Books2016
        Books2017_json['Books2017Num'] = len(Books2017)
        Books2017_json['Books2017'] = Books2017
        Books2018_json['Books2018Num'] = len(Books2018)
        Books2018_json['Books2018'] = Books2018
        Books2019_json['Books2019Num'] = len(Books2019)
        Books2019_json['Books2019'] = Books2019
        Books2020_json['Books2020Num'] = len(Books2020)
        Books2020_json['Books2020'] = Books2020
        statistic_json = {}
        statistic_json['Books_lessthan_2016'] = Bookslessthan2016_json
        statistic_json['Books_2016'] = Books2016_json
        statistic_json['Books_2017'] = Books2017_json
        statistic_json['Books_2018'] = Books2018_json
        statistic_json['Books_2019'] = Books2019_json
        statistic_json['Books_2020'] = Books2020_json

        with open(savefilename, "w+") as jsonFile:  # 保存为json文件
            jsonFile.write(json.dumps(statistic_json, indent=4, ensure_ascii=False))


def main():
    filename = ".\\data\\02dangdangbook.json"  # 所有书籍的数据文件
    hotfilename = ".\\data\\03dangdanghotbook.json"  # 用于保存热门书籍的文件
    totalStatistic_filename = ".\\data\\04dangdang_commentnum_statistics.json"   # 保存评论数统计信息的文件
    countCommentNum(filename, hotfilename, totalStatistic_filename)

    all_books_price_range = ".\\data\\05dangdang_totalbooks_pricerange.json"   # 保存所有书籍价格区间统计信息的文件
    hotbooks_price_range = ".\\data\\06dangdang_hotbooks_pricerange.json"    # 保存热门书籍价格区间统计信息的文件
    countPriceRange(filename, all_books_price_range)
    countPriceRange(hotfilename, hotbooks_price_range)

    all_books_publisher = ".\\data\\07dangdang_allbooks_publisher_statistics.json"    # 保存所有书籍出版社出现次数统计信息的文件
    hotbooks_publisher = ".\\data\\08dangdang_hotbooks_publisher_statistics.json"    # 保存热门书籍出版社出现次数统计信息的文件
    countPublisherNum(filename, all_books_publisher)  # 48
    countPublisherNum(hotfilename, hotbooks_publisher)

    all_books_publishTime = ".\\data\\09dangdang_allbooks_publishTime_statistics.json"   # 保存所有书籍出版时间统计信息的文件
    hotbooks_publishTime = ".\\data\\10dangdang_hotbooks_publishTime_statistics.json"   # 保存热门书籍出版时间统计信息的文件
    coutPublishTimeRangeNum(filename, all_books_publishTime)
    coutPublishTimeRangeNum(hotfilename, hotbooks_publishTime)


if __name__ == '__main__':
    main()