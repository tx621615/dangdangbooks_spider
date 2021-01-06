import matplotlib.pyplot as plt
import json


def plotPieWithCommentNum(datafilename, savefile):
    with open(datafilename, 'r+') as f:
        total_data = json.loads(f.read())
        size1 = total_data['commentnum_lessthan100_books']['commentnum_lessthan100_booksNum']
        size2 = total_data['commentnum_lessthan1000_books']['commentnum_lessthan1000_booksNum']
        size3 = total_data['commentnum_lessthan10000_books']['commentnum_lessthan10000_booksNum']
        size4 = total_data['commentnum_morethan10000_books']['commentnum_morethan10000_booksNum']
        size1 = size1 / 1001
        size2 = size2 / 1001
        size3 = size3 / 1001
        size4 = size4 / 1001
        sizes = [size1, size2, size3, size4]
        labels = ['0-100', '100-1000', '1000-10000', '>10000']
        explode = (0, 0, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
        plt.title("不同评论数的书籍所占比例", fontproperties='SimHei', fontsize=20, color='red')
        plt.savefig(savefile)
        plt.show()


def main():
    filename = '.\\data\\04dangdang_commentnum_statistics.json'
    savefile1 = '.\\image\\01all_comment_figure'
    plotPieWithCommentNum(filename, savefile1)

if __name__ == '__main__':
    main()
