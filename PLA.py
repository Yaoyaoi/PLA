import numpy as np
import matplotlib.pyplot as plt


def inputLine():
    line = input()
    fileName = line.split()[1]
    return fileName


def loadData(fileName):
    fid = open(fileName)
    lines = fid.readlines()
    data_load = []
    for line in lines:
        line = line.strip('\n')  # Omit escape sequence of a newline, important
        line_split = line.split('\t')
        if line_split[2] == '+':  # 将yn值存入data_load的第三项
            line_split[2] = 1
        else:
            line_split[2] = -1
        data_load.append([float(line_split[0]), float(line_split[1]), float(line_split[2])])
    data_load = np.concatenate([data_load], axis=0)
    # print(data_load)
    return data_load


def checkAndPickANode(w, done, data):  # return (x, y, done)
    for item in data:
        x = np.hstack([np.array([1]), item[:2]])
        label = item[2]
        labelPre = float(np.sign(w.dot(x)))
        if labelPre != label:
            return (x, label, done)
    done = True
    x = np.array((0, 0, 0))
    return (x, 0, done)


def PLA(data):
    done = False
    y = 0
    x = np.ones((1, 3))[0]  # d reduction
    w = np.random.rand(1, 3)[0]  # random line
    while not done:  
        w += y * x
        (x, y, done) = checkAndPickANode(w, done, data)
    return w


def Plot(data, w0, w1, w2):  # 画出图像
    if w0*w1 > 0:
        x1 = np.arange(-w0/w1, 0, 0.01)
    else:
        x1 = np.arange(0, -w0/w1, 0.01)
    x2 = -(w1*x1+w0)/w2
    plt.title('PLA result')
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
    fileName = inputLine()
    data = loadData(fileName)
    w = PLA(data)
    print("<%s,%s,%s>" % (w[0], w[1], w[2]))
    Plot(data, w[0], w[1], w[2])