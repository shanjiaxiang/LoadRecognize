def getAverage(source):
    s = 0
    for item in source:
      s += item
    return s/len(source)