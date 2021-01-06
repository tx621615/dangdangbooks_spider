import matplotlib.pyplot as plt
import json
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['font.size'] = 15


def plotPublishTime_Bar(datafilename, savefile):
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        times = []
        times.append(data["Books_lessthan_2016"]["Bookslessthan2016Num"])
        times.append(data["Books_2016"]["Books2016Num"])
        times.append(data["Books_2017"]["Books2017Num"])
        times.append(data["Books_2018"]["Books2018Num"])
        times.append(data["Books_2019"]["Books2019Num"])
        times.append(data["Books_2020"]["Books2020Num"])
        plt.figure(figsize=(15, 10))
        bar1 = plt.bar(range(len(times)), times, width=0.3, color="orange")
        plt.xticks(range(len(times)), ['<2016', '2016', '2017', '2018', '2019', '2020'])
        plt.xlabel("年份")
        plt.ylabel("次数")
        plt.title("书籍年份分布情况", color='red')
        for bar in bar1:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
        plt.savefig(savefile)
        plt.show()

def plotPublishTime_Pie(datafilename, savefile):
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        size1 = data["Books_lessthan_2016"]["Bookslessthan2016Num"]
        size2 = data["Books_2016"]["Books2016Num"]
        size3 = data["Books_2017"]["Books2017Num"]
        size4 = data["Books_2018"]["Books2018Num"]
        size5 = data["Books_2019"]["Books2019Num"]
        size6 = data["Books_2020"]["Books2020Num"]
        size = size1 + size5 + size4 + size3 + size2 + size6
        labels = ['<2016', '2016', '2017', '2018', '2019', '2020']
        percents = [size1 / size, size2 / size, size3 / size, size4 / size, size5 / size, size6 / size]
        explode = (0, 0, 0, 0, 0, 0)
        plt.pie(percents, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, normalize=True)
        plt.title("书籍年份分布情况", color='red')
        plt.savefig(savefile)
        plt.show()


def main():
    filename = '.\\data\\09dangdang_allbooks_publishTime_statistics.json'
    hotfilename = '.\\data\\10dangdang_hotbooks_publishTime_statistics.json'
    savefile1 = ".\\image\\06all_Publish_Time"
    savefile2 = ".\\image\\07hot_Publish_Time"
    savefile3 = ".\\image\\08all_Publish_Time_Pie"
    savefile4 = ".\\image\\09hot_Publish_Time_Pie"
    plotPublishTime_Bar(filename, savefile1)
    plotPublishTime_Bar(hotfilename, savefile2)
    plotPublishTime_Pie(filename, savefile3)
    plotPublishTime_Pie(hotfilename, savefile4)

if __name__ == '__main__':
    main()