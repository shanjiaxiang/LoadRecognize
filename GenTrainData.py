import numpy as np
import os
import re
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
from CalUtils import *

from FileUtils import *
import random


class GenTrainData:

    @staticmethod
    def genRandomTrainData(paths, num, windowWidth):
        size = len(paths)
        filterData = []
        for i in range(size):
            # 数据滤波
            sourceList = FileUtils.ReadSourceDatas(paths[i - 1])
            filtedMatrix = CalUtils.getLowPass(sourceList)
            print(np.shape(filtedMatrix))
            filterData.append(filtedMatrix.tolist())
        print("filterData:", filterData)
        vectors = []
        labels = []
        for i in range(num):
            index = random.randint(1, size) - 1
            sourceData = filterData[index]
            sourceMatrix = np.mat(sourceData)
            [m, n] = sourceMatrix.shape
            randomStart = random.randint(1, n - windowWidth)  # 窗口起始位置
            recordMatrix = np.zeros((m, windowWidth))
            recordMatrix[:, :] = sourceMatrix[:, randomStart: randomStart + windowWidth]
            vector = GenTrainData.getVector2(recordMatrix)
            label = paths[index]
            vectors.append(vector)
            labels.append(label)
        return vectors, labels

    @staticmethod
    def genTrainData(paths):
        vectors = []
        labels = []
        i = 0
        for path in paths:
            i = i + 1
            trainDataFile = "D:\\16.研究\\应急疏散模型\\数据\\行走数据\\滤波" + '\\' + path + ".txt" + "train"  # 训练数据文件
            if not os.path.exists(trainDataFile):  # 训练数据不存在
                # 数据滤波
                sourceList = FileUtils.ReadSourceDatas(path)
                filtedMatrix = CalUtils.getLowPass(sourceList)
                vectors, labels = GenTrainData.getVectorsList(filtedMatrix, 200, 70, path, vectors, labels)
                # labels.append(labelList)

                # with open(trainDataFile, "w") as f:
                #     print(f)
            else:  # 训练数据存在
                continue
        return vectors, labels

    @staticmethod
    def getVectorsList(filterMatrix, num, windowWidth, label, vectorList, labelList):
        [m, size] = filterMatrix.shape
        for i in range(num):
            randomStart = random.randint(1, size - windowWidth)  # 窗口起始位置
            recordMatrix = np.zeros((m, windowWidth))
            recordMatrix[:, :] = filterMatrix[:, randomStart: randomStart + windowWidth]
            vector = GenTrainData.getVector(recordMatrix)
            vectorList.append(vector)
            labelList.append(label)
        return vectorList, labelList

    @staticmethod
    def getVector(record):
        stdData = CalUtils.getSTD(record[1])
        skew = CalUtils.getSKEW(record[1])
        irq = CalUtils.getIQR(record[1])
        rel = CalUtils.getRelYZ(record)
        vector = []
        vector.append(stdData)
        vector.append(skew)
        vector.append(irq)
        vector.append(rel)
        return vector

    @staticmethod
    def getVector2(record):
        # 计算合加速度时域特征
        stdData = CalUtils.getSTD(record[3])  # 标准差
        skew = CalUtils.getSKEW(record[3])  # 偏度
        irq = CalUtils.getIQR(record[3])  # 四分位距
        average = CalUtils.getAverage(record[3])  # 均值
        kurtorsis = CalUtils.getKurtorsis(record[3])  # 峰度

        relXY = CalUtils.getRelXY(record)  # XY相关系数
        relYZ = CalUtils.getRelYZ(record)  # YZ相关系数
        relXZ = CalUtils.getRelXZ(record)  # XZ相关系数
        vector = []
        vector.append(stdData)
        vector.append(skew)
        vector.append(irq)
        vector.append(average)
        vector.append(kurtorsis)
        vector.append(relXY)
        vector.append(relYZ)
        vector.append(relXZ)
        return vector

# paths = ["背包兜里", "行走兜里", "拎包兜里"]
# vectors, labels = GenTrainData.genRandomTrainData(paths, 10, 70)
# print(vectors)
# print(len(vectors))
# print(labels)
# print(len(labels))
