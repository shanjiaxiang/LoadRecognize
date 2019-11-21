import numpy as np
import os
import re
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import CalUtils
import FileUtils

name = 'after背包兜里.txt'
destFile = "D:\\16.研究\\应急疏散模型\\数据\\行走数据\\滤波"+'\\' + "after背包兜里.txt"
paths = ["背包兜里.txt","行走兜里.txt","拎包兜里.txt"]

for path in paths:

    sourceList = FileUtils.FileUtils.ReadSourceDatas(path)
    print("sourceList:", sourceList)
    filtedData = CalUtils.CalUtils.getLowPass(sourceList)
    print("filtedData:",filtedData)
    stdData = CalUtils.CalUtils.getSTD(filtedData[1])
    skew = CalUtils.CalUtils.getSKEW(filtedData[1])
    irq = CalUtils.CalUtils.getIQR(filtedData[1])
    rel = CalUtils.CalUtils.getRelYZ(filtedData)

    print("stdData:",stdData)
    print("skew:",skew)
    print("irq:",irq)
    print("rel:",rel)

plt.subplot(221)
plt.plot(filtedData[0])
plt.subplot(222)
plt.plot(filtedData[1])
plt.subplot(223)
plt.plot(filtedData[2])
# plt.subplot(224)
# plt.plot(irq)
plt.show()
