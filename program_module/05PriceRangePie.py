"""
软设2班
created by Tang Xin
copyright USTC
2021.1.4
功能：根据价格区间统计信息分别绘制所有书籍和热门书籍对应的饼图
"""

import matplotlib.pyplot as plt
import json


def plotPieWithPrice(datafilename, savefilename, flag=0):
    """
    根据价格区间的统计信息绘制相应的饼图
    :param datafilename: 保存价格统计信息的文件，用于读取
    :param savefilename: 用于保存饼图的文件
    :param flag: 判断输入文件是全部书籍的数据（flag=0），还是热门书籍的数据(flag=1)
    """
    with open(datafilename, 'r+') as f:
        total_data = json.loads(f.read())
        size1 = total_data['price_lessthan50']  # 价格<50的书籍的数目
        size2 = total_data['price_lessthan100']  # 价格[50,100)的书籍的数目
        size3 = total_data['price_lessthan150']  # 价格[100,150)的书籍的数目
        size4 = total_data['price_morethan150']  # 价格>150的书籍的数目
        total = size1 + size2 + size3 +size4   # 总的书籍数目
        sizes = [size1 / total, size2 / total, size3 / total, size4 / total]  # 各个区间书籍所占比例
        labels = ["[0,50)", "[50,100)", "[100,150)", ">150"]
        explode = (0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=200)  # 绘制饼图
        if flag == 0:  # flag=0表示数据为全部书籍的统计数据，flag=1表示为热门书籍的统计数据
            plt.title("书籍价格区间比例图", fontproperties='SimHei', fontsize=20, color='red')
            plt.savefig(savefilename)
        else:
            plt.title("热门书籍价格区间比例图", fontproperties='SimHei', fontsize=20, color='red')
            plt.savefig(savefilename)
        plt.show()


def main():
    allbooks = '.\\data\\05dangdang_totalbooks_pricerange.json'  # 所有书籍的价格区间的统计信息
    hotbooks = '.\\data\\06dangdang_hotbooks_pricerange.json'   # 热门书籍的价格区间的统计信息
    savefile1 = ".\\image\\02Price_allbook"  # 保存全部书籍的饼图的文件
    savefile2 = ".\\image\\03Price_hotbook"  # 保存热门书籍的饼图的文件
    flag = 1  # 区别全部书籍和热门书籍数据,0表示全部,1表示热门
    plotPieWithPrice(allbooks, savefile1)
    plotPieWithPrice(hotbooks, savefile2, flag)


if __name__ == '__main__':
    main()