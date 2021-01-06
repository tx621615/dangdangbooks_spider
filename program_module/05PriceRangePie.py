import matplotlib.pyplot as plt
import json


def plotPieWithPrice(datafilename, savefilename, flag=0):
    with open(datafilename, 'r+') as f:
        total_data = json.loads(f.read())
        size1 = total_data['price_lessthan50']
        size2 = total_data['price_lessthan100']
        size3 = total_data['price_lessthan150']
        size4 = total_data['price_morethan150']
        total = size1 + size2 + size3 +size4
        sizes = [size1 / total, size2 / total, size3 / total, size4 / total]
        labels = ["[0,50)", "[50,100)", "[100,150)", ">150"]
        explode = (0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=200)
        if flag == 0:
            plt.title("书籍价格区间比例图", fontproperties='SimHei', fontsize=20, color='red')
            plt.savefig(savefilename)
        else:
            plt.title("热门书籍价格区间比例图", fontproperties='SimHei', fontsize=20, color='red')
            plt.savefig(savefilename)
        plt.show()


def main():
    allbooks = '.\\data\\05dangdang_totalbooks_pricerange.json'
    hotbooks = '.\\data\\06dangdang_hotbooks_pricerange.json'
    savefile1 = ".\\image\\02Price_allbook"
    savefile2 = ".\\image\\03Price_hotbook"
    flag = 1  # 区别全部书籍和热门书籍数据,0表示全部,1表示热门
    plotPieWithPrice(allbooks, savefile1)
    plotPieWithPrice(hotbooks, savefile2, flag)


if __name__ == '__main__':
    main()