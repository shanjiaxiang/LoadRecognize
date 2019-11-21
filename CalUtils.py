import numpy as np
import os
import re
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd


class CalUtils:
    def __init__(self):
        pass

    @staticmethod
    def getLowPass(sourceList):
        sourceMatrix = np.mat(sourceList)
        [m, n] = sourceMatrix.shape

        result = np.zeros((m, n))
        for i in range(m):
            # b, a = signal.butter(8, 0.15, 'lowpass')
            # b, a = signal.butter(8, 0.5, 'lowpass') #76
            # b, a = signal.butter(8, 0.4, 'lowpass') #63
            b, a = signal.butter(8, 0.6, 'lowpass')  # 76

            temp = signal.filtfilt(b, a, sourceMatrix[i])  # 矩阵
            temp = np.round(temp, decimals=2)
            result[i, :] = temp
        return result

    # 标准差
    @staticmethod
    def getSTD(source):
        return round(np.std(source), 2)

    # 偏度
    @staticmethod
    def getSKEW(source):
        return round(pd.Series(source).skew(), 2)

    # 四分位距
    @staticmethod
    def getIQR(source):
        lower = np.quantile(source, 0.25, interpolation='lower')  # 下四分位数
        higher = np.quantile(source, 0.75, interpolation='higher')  # 上四分位数
        return round(higher - lower, 2)  # 四分位距

    # 均值
    @staticmethod
    def getAverage(source):
        return round(np.sum(source) / len(source), 2)

    # 峰度
    @staticmethod
    def getKurtorsis(source):
        return round(pd.Series(source).kurtosis(), 2)

    # 关系系数YZ
    @staticmethod
    def getRelYZ(source):
        g_s_m = pd.Series(source[1])  # 利用Series将列表转换成新的、pandas可处理的数据
        g_a_d = pd.Series(source[2])
        return round(g_s_m.corr(g_a_d), 2)  # 计算标准差，round(a, 4)是保留a的前四位小数

    # 关系系数XY
    @staticmethod
    def getRelXY(source):
        g_s_m = pd.Series(source[0])  # 利用Series将列表转换成新的、pandas可处理的数据
        g_a_d = pd.Series(source[1])
        return round(g_s_m.corr(g_a_d), 2)  # 计算标准差，round(a, 4)是保留a的前四位小数

    # 关系系数XZ
    @staticmethod
    def getRelXZ(source):
        g_s_m = pd.Series(source[0])  # 利用Series将列表转换成新的、pandas可处理的数据
        g_a_d = pd.Series(source[2])
        return round(g_s_m.corr(g_a_d), 2)  # 计算标准差，round(a, 4)是保留a的前四位小数
