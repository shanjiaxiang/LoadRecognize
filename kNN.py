import numpy as np
import math
import operator


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    normDataSet = np.round(normDataSet, decimals=2)
    return normDataSet, ranges, minVals

def singleAutoNorm(dataSet, minVals, ranges):
    normDataSet = dataSet - np.tile(minVals, (1, 1))
    normDataSet = normDataSet / np.tile(ranges, (1, 1))
    normDataSet = np.round(normDataSet, decimals=2)
    return normDataSet

def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    print("sortedDist:", sortedDistIndicies[:29])
    # print("labels:",labels)
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
