import matplotlib.pyplot as plt
import json
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['font.size'] = 15


def plotPublisherTimes(datafilename, savefile):
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        publishers = []
        times = []
        for key in data:
            publishers.append(key)
            times.append(data[key])

    plt.figure(figsize=(15, 15))
    plt.barh(range(len(publishers)), times, height=0.8, color='orange', alpha=0.8)  # 从下往上画
    plt.yticks(range(len(publishers)), publishers, fontsize=10)
    plt.xlim(0, 310)
    plt.xlabel("出现次数", fontsize=10)
    plt.title("书籍出版商出现次数", color="red")
    for x, y in enumerate(times):
        plt.text(y + 0.1, x - 0.2, '%s' % y, fontsize=10)
    plt.savefig(savefile)
    plt.show()

def plotPublisherTimes1(datafilename, savefile):
    with open(datafilename, 'r+') as f:
        data = json.loads(f.read())
        publishers = []
        times = []
        for key in data:
            publishers.append(key)
            times.append(data[key])
    plt.figure(figsize=(15, 10))
    plt.barh(range(len(publishers)), times, height=0.5, color='orange', alpha=0.8)  # 从下往上画
    plt.yticks(range(len(publishers)), publishers, fontsize=10)
    plt.xlim(0, 60)
    plt.xlabel("出现次数", fontsize=10)
    plt.title("书籍出版商出现次数", color="red")
    for x, y in enumerate(times):
        plt.text(y + 0.1, x - 0.2, '%s' % y, fontsize=10)
    plt.savefig(savefile)
    plt.show()


def main():
    filename = ".\\data\\07dangdang_allbooks_publisher_statistics.json"
    hotfilename = ".\\data\\08dangdang_hotbooks_publisher_statistics.json"
    allsavefilename = ".\\image\\04bookspublisher"
    hotsavefilename =".\\image\\05hotbookspublisher"
    plotPublisherTimes(filename, allsavefilename)
    plotPublisherTimes1(hotfilename, hotsavefilename)


if __name__ == '__main__':
    main()