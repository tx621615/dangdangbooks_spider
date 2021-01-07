"""
功能: 根据评论数统计信息绘制相应饼图
"""


import matplotlib.pyplot as plt
import json


def plotPieWithCommentNum(datafilename, savefile):
    """
    根据评论数的统计信息绘制相应的饼图
    :param datafilename:  保存评论数统计信息的文件，用于读取
    :param savefile: 保存饼图的文件
    :return:
    """
    with open(datafilename, 'r+') as f:
        total_data = json.loads(f.read())
        size1 = total_data['commentnum_lessthan100_books']['commentnum_lessthan100_booksNum']  # 评论数小于100的书籍数目
        size2 = total_data['commentnum_lessthan1000_books']['commentnum_lessthan1000_booksNum']  # 评论数[100，1000)的书籍数目
        size3 = total_data['commentnum_lessthan10000_books']['commentnum_lessthan10000_booksNum']  # 评论数[1000，10000)的书籍数目
        size4 = total_data['commentnum_morethan10000_books']['commentnum_morethan10000_booksNum']   # 评论数大于1000的书籍数目
        # 各个区间书籍所占比例
        size1 = size1 / 1001
        size2 = size2 / 1001
        size3 = size3 / 1001
        size4 = size4 / 1001
        sizes = [size1, size2, size3, size4]
        labels = ['0-100', '100-1000', '1000-10000', '>10000']  # 各个区间的标签
        explode = (0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)  # 绘制饼图
        plt.title("不同评论数的书籍所占比例", fontproperties='SimHei', fontsize=20, color='red')
        plt.savefig(savefile)  # 保存图片
        plt.show()


def main():
    filename = '.\\data\\04dangdang_commentnum_statistics.json'  # 评论数统计信息的数据文件
    savefile1 = '.\\image\\01all_comment_figure'  # 保存图片的文件
    plotPieWithCommentNum(filename, savefile1)

if __name__ == '__main__':
    main()
