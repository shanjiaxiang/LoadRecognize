import numpy as np
import random
class FileUtils:
    def __init__(self):
        pass

    @staticmethod
    def WriteToFile(filePath, content):
        if not os.path.exists(filePath):
            with open(filePath, "w") as f:
                print(f)

        with open(filePath, "a") as f:
            f.write(content)

    @staticmethod
    def readOneRecord(path):
        filePath = "D:\\16.研究\\应急疏散模型\\数据\\行走数据\\滤波" + '\\' + path + ".txt"
        sourceList = []
        temp1 = []
        temp2 = []
        temp3 = []

        sourceList.append(temp1)
        sourceList.append(temp2)
        sourceList.append(temp3)

        with open(filePath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            randomStart = random.randint(1, len(lines) - 70)  # 窗口起始位置
            for i in range(randomStart, randomStart+70):
                lineSplit = lines[i].split('\t')
                for j in range(3):
                    sourceList[j].append(float(lineSplit[j]))

        return sourceList, path

    @staticmethod
    def ReadSourceDatas(path):
        sourceList = []
        tempX = []
        tempY = []
        tempZ = []
        tempA = []

        sourceList.append(tempX)
        sourceList.append(tempY)
        sourceList.append(tempZ)
        sourceList.append(tempA)

        filePath = "D:\\16.研究\\应急疏散模型\\负重识别\\datas\\clean" + '\\' + path + ".txt"
        with open(filePath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                # if i < 200:
                #     continue
                # if i > 500:
                #     break
                lineSplit = lines[i].split('\t')
                for j in range(4):
                    sourceList[j].append(float(lineSplit[j]))
        return sourceList
