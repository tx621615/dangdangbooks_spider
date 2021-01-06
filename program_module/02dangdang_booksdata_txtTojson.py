import json


def dealDataFromTxtToJson(fname, savefilename):
    f = open(fname, 'r')
    str = f.read()   # 读取文件中的所有内容
    str = str.split("---"*30)   # 按某个符号进行分割。从而获得每一本书的数据
    str.pop()  # 去除最后一个元素
    targetArr = []
    for temp in str:
        try:
            bookObj = {}
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

    with open(savefilename, "w+") as jsonFile:
        jsonFile.write(json.dumps(targetArr, indent=4, ensure_ascii=False))   # 注意json默认为使用ascii码来编码，因此中文会出现错误，应该禁止
    f.close()


def main():
    filename = ".\\data\\01dangdangbook.txt"
    savefilename = ".\\data\\02dangdangbook.json"
    dealDataFromTxtToJson(filename, savefilename)


if __name__ == '__main__':
    main()


