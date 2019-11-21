from CalUtils import *
from FileUtils import *
from GenTrainData import *
from kNN import *
from CommonUtils import *


def walkClassTest(paths, k):
    hoRatio = 0.10
    # vectorList, labelList = GenTrainData.genTrainData(paths)
    vectorList, labelList = GenTrainData.genRandomTrainData(paths, 1000, 70)
    print("len:", len(vectorList), "vectorList:", vectorList)
    print("len:", len(labelList), "labelList:", labelList)
    normMat, ranges, minVals = autoNorm(np.array(vectorList))
    print("normMat:", normMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    print("numTestVecs:", numTestVecs)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i, :], normMat[numTestVecs:m, :], np.array(labelList)[numTestVecs:m], k)
        print("识别结果:", classifierResult, "真实结果:", labelList[i])
        if (classifierResult != labelList[i]):
            errorCount += 1.0
    print("测试用例数：", numTestVecs)
    recRatio = (100 - round(errorCount*100 / numTestVecs, 2))
    print("正确率:", recRatio, "%")
    return recRatio


def randomWalkClassTest(paths):
    size = len(paths)
    recCount = 0.0
    vectorList, labelList = GenTrainData.genTrainData(paths)
    normMat, ranges, minVals = autoNorm(np.array(vectorList))
    print(normMat)
    num = 10
    for i in range(1000):
        index = random.randint(1, size)  # 随机类别
        oneRecord, label = FileUtils.readOneRecord(paths[index - 1])
        print("record:", oneRecord, " label:", label)
        filtedRecord = CalUtils.getLowPass(oneRecord)
        # print("filtedRecord:",filtedRecord)
        vector = GenTrainData.getVector(filtedRecord)
        # print("vector:",vector)
        normR = singleAutoNorm(np.array(vector), minVals, ranges)
        # normR, rangeR, minValR = autoNorm(np.array(vector))
        print("normR", normR)
        result = classify(normR[0], normMat, np.array(labelList), 3)
        print("识别结果:", result, "真实结果:", label)
        if result == label:
            recCount += 1.0
    recRatio = (recCount / 1000.0) * 100
    print("正确率:", round(recRatio, 4), "%")


# randomWalkClassTest(paths)

def testCal():
    for path in paths:
        sourceList = FileUtils.ReadSourceDatas(path)
        lowPass = CalUtils.getLowPass(sourceList)
        stdData = CalUtils.getSTD(lowPass[1])
        skew = CalUtils.getSKEW(lowPass[1])
        irq = CalUtils.getIQR(lowPass[1])
        rel = CalUtils.getRelYZ(lowPass)

        print("stdData:", stdData)
        print("skew:", skew)
        print("irq:", irq)
        print("rel:", rel)
        # break
    plt.subplot(221)
    plt.plot(lowPass[0])
    plt.subplot(222)
    plt.plot(lowPass[1])
    plt.subplot(223)
    plt.plot(lowPass[2])
    plt.show()


paths = ["背包", "背包拉箱", "兜里", "兜里拉箱", "拎包", "拎包拉箱", "手持", "手持拉箱"]
recList = []
for i in range(20):
    recList.append(walkClassTest(paths, 3))
print(recList)
print("平均正确率:", getAverage(recList), "%")
