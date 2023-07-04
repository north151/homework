import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import random
import math


class KMEANS:
    # 原始数据
    data = pd.DataFrame()
    # 算法分类标签
    tag="tag"
    # 中心点坐标列表
    centers_list=[]
    centers=np.zeros(shape=(1,1),dtype=float)
    # 距离函数
    dis=None
    
    #构造函数
    def __init__(self,data,label=None):
        #数据
        if label!=None:
            self.data=data.drop([label],axis=1)
        else:
            self.data=data
        self.data=PCA(n_components=2).fit_transform(self.data.values)
        #类别
        self.tag=pd.Series([0]*self.data.shape[0])
        #中心点
        self.centers=self.data[0].reshape(1,self.data[0].shape[0])
        self.centers_list=[]
        
         
    #距离计算
    def getDis(self,x,x0):
        qdis=(x-x0)**2
        if len(qdis.shape)!=1:
            qdis=np.sum(qdis,axis=1)
        else:
            qdis=np.sum(qdis)
        return qdis**0.5


    # 更新最佳中心点
    def update_center(self):
        data=self.data
        # 到中心的距离
        for i in range(data.shape[0]):
            dist = self.dis(self.centers,data[i])
            self.tag[i]=dist.argmin()
        # 更新簇中心坐标
        for i in range(self.centers.shape[0]):
            tmp = self.data[self.tag==i]
            num = tmp.shape[0]
            tmp = np.sum(tmp,axis=0)
            self.centers[i]=tmp/num

    #绘制
    def draw(self,tag):
        for i in set(tag):
            tmp=self.data[tag==i]
            plt.scatter(tmp[:,0],tmp[:,1])
        plt.show()
        
    
    # 运行算法
    def kmeans(self,num=1):
        #计算距离
        self.dis=self.getDis
        X=pd.DataFrame(self.data).drop_duplicates().reindex().values
        x=random.sample(range(X.shape[0]),num)
        self.centers = X[x]   
        pre=0.0
        for i in range(self.centers.shape[0]):
            tmp = self.data[self.tag==i]
            tmp=(tmp-self.centers[i])**2
            tmp=np.sum(tmp,axis=1)
            pre+=np.sum(tmp)

        while True:
            self.update_center()
            now=0.0
            for i in range(self.centers.shape[0]):
                tmp = self.data[self.tag==i]
                tmp=(tmp-self.centers[i])**2
                tmp=np.sum(tmp,axis=1)
                now+=np.sum(tmp)  
            if math.fabs(pre-now)<=0.1:
                break
            pre=now


def task_KMEANS(num=3):
    #获取数据
    Data=pd.read_csv('input_data/iris.csv',names=range(5))
    data=Data.copy()
    #创建对象
    k=KMEANS(data,4)
    k.kmeans(num)
    k.draw(k.tag)


task_KMEANS(5)



