import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gensim
import jieba
import jieba.posseg as pseg
from sklearn.cluster import DBSCAN as sklearn_DBSCAN


class DBSCAN:
    #计算两个向量的欧氏距离
    def euclidean_dist(self, x1, x2):
        x = np.array(x1)
        y = np.array(x2)
        return np.linalg.norm(x - y)
    
    #密度聚类
    def fit(self,data,neighbor_dist,minpts):
        """
        参数：
        data: 		  数据集
        neighbor_dist: 邻域半径
        minpts:        构成核心对象的邻域最小样本数
        """

        #核心对象集合
        core_obj = set()
        #聚类个数为0
        cluster_num = 0
        #聚类列表clusters
        clusters = []
        #未访问样本集合P
        P = set(data)
        #核心对象集合
        for sample in data:
            #如果样本sample的neighbor_dist邻域中样本数大于等于minpts
            if len([ sample_i for sample_i in data if self.euclidean_dist(sample, sample_i) <= neighbor_dist]) >= minpts:
                core_obj.add(sample)
                        
        #开始聚类
        while len(core_obj): 
            #随机取一核心对象
            obj = list(core_obj)[np.random.randint(0, len(core_obj))]
            #访问该核心对象
            P = P - set(obj)
            
            #未访问集合
            P_OLD = P
            
            #初始化队列Q
            Q = []
            Q.append(obj)
            while len(Q):
                #队首

                q = Q[0]
                #q的邻域
                N_q = [sample for sample in data if self.euclidean_dist(sample, q) <= neighbor_dist]
                #q是核心对象
                if len(N_q) >= minpts:
                    #领域未访问对象入簇
                    delta = set(N_q) & P
                    Q += (list(delta))
                    P = P - delta 
                #出队
                Q.remove(q)
            #类簇+1
            cluster_num = cluster_num + 1
            #簇集合
            C_k = list(P_OLD - P)
            print(C_k)
            #剩余核心对象集合
            core_obj = core_obj - set(C_k)
            #记录簇
            clusters.append(C_k)
            
        return clusters



#分词
def jieba_cut(titel):
    words = []
    segs = pseg.cut(titel)
    for word in segs:
        if word.flag in ['ns', 'n', 'vn', 'v', 'nr']:
            words.append(word.word)
    return words



#绘制聚类结果
def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []    #x坐标列表
        coo_Y = []    #y坐标列表
        for j in range(len(C[i])):
            coo_X.append(C[i][j][0])
            coo_Y.append(C[i][j][1])
        plt.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)
    plt.legend(loc='upper right')
    plt.show()



#简单任务
def task_DBSCAN():
    #数据集：每三个是一组分别是西瓜的编号，密度，含糖量
    data = [(0.697,0.460),(0.774,0.376),(0.634,0.264),(0.608,0.318),(0.556,0.215),
            (0.403,0.237),(0.481,0.149),(0.437,0.211),(0.666,0.091),(0.243,0.267),
            (0.245,0.057),(0.343,0.099),(0.639,0.161),(0.657,0.198),(0.360,0.370),
            (0.593,0.042),(0.719,0.103),(0.359,0.188),(0.339,0.241),(0.282,0.257),
            (0.748,0.232),(0.714,0.346),(0.483,0.312),(0.478,0.437),(0.525,0.369),
            (0.751,0.489),(0.532,0.472),(0.473,0.376),(0.725,0.445),(0.446,0.459)]
    d=DBSCAN()
    clusters=d.fit(data,0.11,5)
    draw(clusters)

'''
task_DBSCAN()
'''



def test_DBSCAN(): 
    #获取数据
    Data = pd.read_excel(r"input_data/新闻.xlsx")
    data = Data.copy()
    #去除
    titel = data['标题'].map(lambda x:[i for i in list(jieba.cut(x)) if len(i) !=1])
    #词向量 CBOW hierarchical softmax模型
    model = gensim.models.Word2Vec(titel,sg=0,vector_size=2,window=5,
                                   min_count=2,negative=5,sample=0.001,hs=1,workers=6)
    model.wv.save_word2vec_format('output_data/wordsX.txt',binary=False)
    model = gensim.models.KeyedVectors.load_word2vec_format('output_data/wordsX.txt',binary=False)
    
    #格式化数据集
    data_mat = [tuple(model[i]) for i in range(len(model))]
    #限制位数
    #data_mat = [tuple(round(xi,3) for xi in model[i]) for i in range(len(model))]      
    
    print(titel)
    
    #DBSCAN
    d = DBSCAN()
    clusters = d.fit(data_mat,0.2,7)
    draw(clusters)

    #sklearn的DBSCAN
    sd = sklearn_DBSCAN(eps=0.2,min_samples=7)
    X = np.array(data_mat)
    Y = sd.fit_predict(X)
    plt.scatter(X[:,0],X[:,1],c=Y)
    plt.show()

'''
test_DBSCAN()
'''





















