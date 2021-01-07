"""
功能：该模块用于将数据文件从.txt文件转化为.json文件
"""

import json


def dealDataFromTxtToJson(fname, savefilename):
    """
    将txt文档转化为json文档
    :param fname: 需要转化的文档
    :param savefilename: 转化后保存的文档
    """
    f = open(fname, 'r')
    str = f.read()   # 读取文件中的所有内容
    str = str.split("---"*30)   # 按某个符号进行分割。从而获得每一本书的数据
    str.pop()  # 去除最后一个元素
    targetArr = []
    for temp in str:
        try:
            bookObj = {}   # 获取每本书的信息
            temp = temp.strip().split('\n')
            bookObj["index"] = temp[0]
            bookObj["name"] = temp[1]
            bookObj["price"] = temp[2]
            bookObj["author"] = temp[3].split(":")[1]
            bookObj["publishTime"] = temp[4].split(":")[1]
            bookObj["publisher"] = temp[5].split(":")[1]
            bookObj["commentNum"] = int(temp[6].split(":")[1].rstrip("条评论"))
            targetArr.append(bookObj)
        except:
            continue

    with open(savefilename, "w+") as jsonFile:  # 将对应的数组转化为json文件
        jsonFile.write(json.dumps(targetArr, indent=4, ensure_ascii=False))   # 注意json默认为使用ascii码来编码，因此中文会出现错误，应该禁止
    f.close()


def main():
    filename = ".\\data\\01dangdangbook.txt"   # 待转化的.txt文件
    savefilename = ".\\data\\02dangdangbook.json"  # 保存json的文件
    dealDataFromTxtToJson(filename, savefilename)


if __name__ == '__main__':
    main()


