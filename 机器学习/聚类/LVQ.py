from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
import numpy as np
import math


class LVQ:
    #两个样本点欧氏距离
    def euclidean_dist(self, x1, x2):
        x2=x2[0]
        dist = math.sqrt(math.pow(x1[0]-x2[0], 2)+math.pow(x1[1]-x2[1], 2))
        return dist

    #与样本最近的点
    def get_min_dist_proto_vect(self, proto_vects,x):
        min_dist = np.inf
        min_index = -1
        for i in range(len(proto_vects)):
            dist=self.euclidean_dist(proto_vects[i],x)
            if dist < min_dist:
                min_dist=dist
                min_index=i
        return min_index  

    #LVQ训练
    def fit(self,data_x,data_y,proto_vects,proto_labels,learnrate,max_iters):
        """
        参数：
        data_x:       训练集
        data_y:       标记
        proto_vects:  初始化的原型向量
        proto_labels: 原型向量对应的类别标记
        learnrate:    学习率
        max_iters:    最大迭代次数
        """
        
        iters = 0
        while iters < max_iters:
            #随机选一个样本点
            sample_index = np.random.choice(len(data_x), 1, replace=False)
            #与其最近样本点
            min_dist_index = self.get_min_dist_proto_vect(proto_vects,data_x[sample_index])
            #根据样本的类别来更新原型向量
            if proto_labels[min_dist_index] == data_y[sample_index]:
                proto_vects[min_dist_index] = proto_vects[min_dist_index] + learnrate*(proto_vects[min_dist_index]-data_x[sample_index])
            else:
                proto_vects[min_dist_index] = proto_vects[min_dist_index] - learnrate*(proto_vects[min_dist_index]-data_x[sample_index])
            iters += 1
        return proto_vects,proto_labels



#简单任务
def task_LVQ():   
    #三个类簇的中心
    center = [[1, 1], [-1, -1], [1, -1]] 
    cluster_std = 0.35
    #三类簇数据集
    X1, Y1 = make_blobs(n_samples=1000, centers=center,n_features=2, 
                        cluster_std=cluster_std, random_state=1)
    #查看数据集
    print(X1)
    print(Y1[0:100])
    lvq = LVQ()
    #此处原型向量为随意设置
    proto_vects,proto_labels=lvq.fit(X1,Y1,X1[0:100],Y1[0:100],0.01,60)
    #数据集可视化
    #plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
    plt.scatter(proto_vects[:, 0],proto_vects[:, 1], marker='o', c=proto_labels)


'''
task_LVQ()

'''












