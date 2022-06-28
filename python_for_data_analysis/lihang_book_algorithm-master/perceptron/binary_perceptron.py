# encoding=utf-8
# @Author: WenDesi
# @Date:   09-08-16
# @Email:  wendesi@foxmail.com
# @Last modified by:   WenDesi
# @Last modified time: 08-11-16

import pandas as pd
import numpy as np
import cv2
import random
import time

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class Perceptron(object):

    def __init__(self):
        #步长
        self.learning_step = 0.000001

        #训练最大时间阈值
        self.max_iteration = 5000

    def predict_(self, x):
        wx = sum([self.w[j] * x[j] for j in range(len(self.w))])
        return int(wx > 0)

    def train(self, features, labels):
        #拿到维数+1（b）初始化参数
        self.w = [0.0] * (len(features[0]) + 1)

        #正确数
        correct_count = 0
        time = 0

        #只要不超时
        while time < self.max_iteration:
            #index随机抽取一个样本
            index = random.randint(0, len(labels) - 1)
            x = list(features[index])
            # print(x)
            x.append(1.0)#为了后面跟b相乘的时候保持b系数为1，也为了和b维度相通
            # print(x)
            y = 2 * labels[index] - 1

            #构建函数，使w和x相乘
            wx = sum([self.w[j] * x[j] for j in range(len(self.w))])

            #如果训练结果符合训练集标签，则count++
            if wx * y > 0:
                correct_count += 1
                #当训练的正确数大于这个阈值——训练强度——避免过拟合
                if correct_count > self.max_iteration:
                    break
                #如果是正确的话直接进入下一次循环
                continue

            for i in range(len(self.w)):
                #更新，参数b已经包含在w里面了，步长*（y*【x】）
                self.w[i] += self.learning_step * (y * x[i])

    def predict(self,features):
        labels = []
        for feature in features:
            x = list(feature)
            x.append(1)
            labels.append(self.predict_(x))
        return labels


if __name__ == '__main__':

    print('Start read data')

#返回当前的时间戳
    time_1 = time.time()

    raw_data = pd.read_csv('../data/train_binary.csv', header=0)
    data = raw_data.values

    imgs = data[0::, 1::]
    labels = data[::, 0]

    # 选取 2/3 数据作为训练集， 1/3 数据作为测试集
    train_features, test_features, train_labels, test_labels = train_test_split(
        imgs, labels, test_size=0.33, random_state=23323)
    print (train_features.shape)
    print (test_features.shape)

    time_2 = time.time()
    print( 'read data cost ', time_2 - time_1, ' second', '\n')

    print ('Start training')
    p = Perceptron()
    p.train(train_features, train_labels)

    time_3 = time.time()
    print( 'training cost ', time_3 - time_2, ' second', '\n')

    print( 'Start predicting')
    test_predict = p.predict(test_features)
    time_4 = time.time()
    print( 'predicting cost ', time_4 - time_3, ' second', '\n')

    score = accuracy_score(test_labels, test_predict)
    print( "The accruacy socre is ", score)

    print("The w ",p.w[:-1])
    print("The b ",p.w[-1])

