import numpy as np
import matplotlib.pyplot as plt
import random

savepath = "train.txt"


def inputLine():
    plot = False
    line = input()
    lineSplit = line.split()
    m = int(lineSplit[2])
    n = int(lineSplit[3])
    if len(lineSplit) == 5:
        plotstring = lineSplit[4]
        if plotstring == 'plot':
            plot = True
    wstring = lineSplit[1].split('[')
    wstring = wstring[1].split(']')[0]
    wstring = wstring.split(',')
    w = np.array((float(wstring[0]), float(wstring[1]), float(wstring[2])))
    return (w, m, n, plot)


def sign(wx):
    labelnum = 0
    label = 0
    if wx > 0:
        labelnum = 1
        label = '+'
    if wx < 0:
        labelnum = -1
        label = '-'
    return (labelnum, label)


def DataEmit(w, m, n):
    x1array = -w[0]/w[1]*np.random.rand(n+m, 1)
    data = np.hstack([x1array, np.zeros((n+m, 2))])
    countm = m
    countn = n
    labelneed = 0
    with open(savepath, 'w') as f:
        for i in range(m+n):
            # w2x2 = random.random()-(w1*x1array[i][0]+w0)
            x2 = -w[0]/w[2] * random.random()
            x = np.array((1, data[i][0], x2))
            labelnum, label = sign(w.dot(x))
            while not labelnum:  # no node on the line
                x2 = -w[0]/w[2] * random.random()
                x = np.array((1, data[i][0], x2))
                labelnum, label = sign(w.dot(x))
            if labelnum == 1:
                countm -= 1
                if countm == 0:
                    labelneed = -1
            else:
                countn -= 1
                if countn == 0:
                    labelneed = 1
            if labelneed != 0:
                while labelnum != labelneed:
                    x2 = -w[0]/w[2] * random.random()
                    x = np.array((1, data[i][0], x2))
                    labelnum, label = sign(w.dot(x))
            data[i] = np.hstack([data[i][0], x2, labelnum])
            f.write("%s\t%s\t%s\n" % (data[i][0], x2, label))
    return data
#  print(data)


def Plot(w, data):
    if w[0]*w[1] > 0:
        x1 = np.arange(-w[0]/w[1], 0, 0.01)
    else:
        x1 = np.arange(0, -w[0]/w[1], 0.01) 
    x2 = -(w[1]*x1+w[0])/w[2]
    plt.title('dataemit')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot(x1, x2)
    for item in data:
        if item[2] == 1:
            plt.scatter(item[0], item[1], marker='o', color='blue')
        else:
            plt.scatter(item[0], item[1], marker='x', color='red') 
    plt.show()


if __name__ == "__main__":
    (w, m, n, plot) = inputLine()
    data = DataEmit(w, m, n)
    if plot:
        Plot(w, data)
