"""
功能：根据出版日期的统计信息绘制对应的条形图和饼图
"""


import matplotlib.pyplot as plt
import json
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置全局字体为微软雅黑
matplotlib.rcParams['font.size'] = 15  # 设置全局字体大小为15


def plotPublishTime_Bar(datafilename, savefile):
    """
    根据出版日期的统计信息绘制相应的条形图
    :param datafilename: 保存出版日期统计信息的文件，用于读取
    :param savefile: 保存绘制的条形图的文件
    """
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        # 保存各个年份区间的书籍数目
        times = []
        times.append(data["Books_lessthan_2016"]["Bookslessthan2016Num"])  # <2016
        times.append(data["Books_2016"]["Books2016Num"])  # 2016
        times.append(data["Books_2017"]["Books2017Num"])  # 2017
        times.append(data["Books_2018"]["Books2018Num"])  # 2018
        times.append(data["Books_2019"]["Books2019Num"])  # 2019
        times.append(data["Books_2020"]["Books2020Num"])  # 2020
        plt.figure(figsize=(15, 10))
        bar1 = plt.bar(range(len(times)), times, width=0.3, color="orange")  # 绘制纵向条形图
        plt.xticks(range(len(times)), ['<2016', '2016', '2017', '2018', '2019', '2020'])
        plt.xlabel("年份")
        plt.ylabel("次数")
        plt.title("书籍年份分布情况", color='red')
        for bar in bar1:  # 在每个条形块上绘制对应的数值
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
        plt.savefig(savefile)
        plt.show()

def plotPublishTime_Pie(datafilename, savefile):
    """
    根据出版日期的统计信息绘制相应的饼图
    :param datafilename: 保存出版日期统计信息的文件，用于读取
    :param savefile: 保存绘制的饼图的文件
    """
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        # 计算各个年份区间的书籍数目，同时统计所占比例
        size1 = data["Books_lessthan_2016"]["Bookslessthan2016Num"]
        size2 = data["Books_2016"]["Books2016Num"]
        size3 = data["Books_2017"]["Books2017Num"]
        size4 = data["Books_2018"]["Books2018Num"]
        size5 = data["Books_2019"]["Books2019Num"]
        size6 = data["Books_2020"]["Books2020Num"]
        size = size1 + size5 + size4 + size3 + size2 + size6
        labels = ['<2016', '2016', '2017', '2018', '2019', '2020']  # 对应年份区间的标签
        percents = [size1 / size, size2 / size, size3 / size, size4 / size, size5 / size, size6 / size]  # 所有年份区间所占比例
        explode = (0, 0, 0, 0, 0, 0)
        plt.pie(percents, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, normalize=True)  # 绘制饼图
        plt.title("书籍年份分布情况", color='red')
        plt.savefig(savefile)
        plt.show()


def main():
    filename = '.\\data\\09dangdang_allbooks_publishTime_statistics.json'  # 所有书籍出版时间的数据文件
    hotfilename = '.\\data\\10dangdang_hotbooks_publishTime_statistics.json'  # 热门书籍出版时间的数据文件
    savefile1 = ".\\image\\06all_Publish_Time"  # 保存所有书籍出版时间的条形图
    savefile2 = ".\\image\\07hot_Publish_Time"  # 保存热门书籍出版时间的条形图
    savefile3 = ".\\image\\08all_Publish_Time_Pie"  # 保存所有书籍出版时间的饼图
    savefile4 = ".\\image\\09hot_Publish_Time_Pie"  # 保存热门书籍出版时间的饼图
    plotPublishTime_Bar(filename, savefile1)
    plotPublishTime_Bar(hotfilename, savefile2)
    plotPublishTime_Pie(filename, savefile3)
    plotPublishTime_Pie(hotfilename, savefile4)

if __name__ == '__main__':
    main()
