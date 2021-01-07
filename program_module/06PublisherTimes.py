"""
软设2班
created by Tang Xin
copyright USTC
2021.1.4
功能：根据出版社出现的次数的统计信息分别绘制所有书籍和热门书籍对应的条形图
"""


import matplotlib.pyplot as plt
import json
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置全局字体为微软雅黑
matplotlib.rcParams['font.size'] = 15  # 设置全局字体大小为15


def plotPublisherTimes(datafilename, savefile):
    """
    根据所有书籍出版社出现次数的统计信息绘制条形图
    :param datafilename: 保存出版社出现次数的统计信息的文件，用于读取
    :param savefile: 保存条形图的文件
    """
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        publishers = []  # 保存出版社的名字
        times = []  # 保存出版社的次数
        for key in data:  # 遍历所有数据
            publishers.append(key)
            times.append(data[key])

    plt.figure(figsize=(15, 15))  # 设置绘制的图片的大小
    plt.barh(range(len(publishers)), times, height=0.8, color='orange', alpha=0.8)  # 绘制横向的条形图
    plt.yticks(range(len(publishers)), publishers, fontsize=10)
    plt.xlim(0, 310)  # 设置x轴的范围
    plt.xlabel("出现次数", fontsize=10)
    plt.title("书籍出版商出现次数", color="red")
    for x, y in enumerate(times):  # 在每个条形块上绘制对应的数值
        plt.text(y + 0.1, x - 0.2, '%s' % y, fontsize=10)
    plt.savefig(savefile)
    plt.show()

def plotPublisherTimes1(datafilename, savefile):
    """
    根据热门书籍出版社出现次数的统计信息绘制条形图
    :param datafilename: 保存出版社出现次数的统计信息的文件，用于读取
    :param savefile: 保存条形图的文件
    """
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        publishers = []
        times = []
        for key in data:
            publishers.append(key)
            times.append(data[key])
    plt.figure(figsize=(15, 10))
    plt.barh(range(len(publishers)), times, height=0.5, color='orange', alpha=0.8)
    plt.yticks(range(len(publishers)), publishers, fontsize=10)
    plt.xlim(0, 60)
    plt.xlabel("出现次数", fontsize=10)
    plt.title("书籍出版商出现次数", color="red")
    for x, y in enumerate(times):
        plt.text(y + 0.1, x - 0.2, '%s' % y, fontsize=10)
    plt.savefig(savefile)
    plt.show()


def main():
    filename = ".\\data\\07dangdang_allbooks_publisher_statistics.json"  # 所有书籍的出版商出现次数的统计信息
    hotfilename = ".\\data\\08dangdang_hotbooks_publisher_statistics.json"  # 热门书籍的出版商出现次数的统计信息
    allsavefilename = ".\\image\\04bookspublisher"  # 保存所有书籍的条形图的文件
    hotsavefilename =".\\image\\05hotbookspublisher"  # 保存热门书籍的条形图的文件
    plotPublisherTimes(filename, allsavefilename)
    plotPublisherTimes1(hotfilename, hotsavefilename)


if __name__ == '__main__':
    main()