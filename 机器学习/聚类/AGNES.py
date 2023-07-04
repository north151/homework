import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gensim
import jieba
import jieba.posseg as pseg
from sklearn.cluster import AgglomerativeClustering as sklearn_AGNES





class AGNES:

    #欧氏距离
    def euclidean_dist(self, x1, x2):
        x = np.array(x1)
        y = np.array(x2)
        return np.linalg.norm(x - y)

    #两集合最小距离   
    def dist_min(self,C_i,C_j):
        min_dist = np.inf
        for x in C_i: 
            for z in C_j: 
                dist = self.euclidean_dist(x,z) 
                if dist < min_dist: 
                    min_dist = dist        

        return min_dist

    #两集合最大距离
    def dist_max(self,C_i,C_j):
        max_dist = -np.inf
        for x in C_i: 
            for z in C_j: 
                dist = self.euclidean_dist(x,z) 
                if dist > max_dist: 
                    max_dist = dist  

        return max_dist

    #两集合平均距离
    def dist_avg(self,C_i,C_j):
        avg_dist = 0.0
        for x in C_i: 
            for z in C_j: 
                avg_dist += self.euclidean_dist(x,z) 
        avg_dist = avg_dist / (len(C_i)*len(C_j)) 
        
        return avg_dist




    #最小距离及其下标
    def find_min_dist_pos(self,dist_matrix):
        min_dist =  np.inf
        x = 0
        y = 0
        for i in range(len(dist_matrix)):
            for j in range(len(dist_matrix[i])):
                if i!=j and dist_matrix[i][j] < min_dist:
                    min_dist = dist_matrix[i][j]
                    x = i
                    y = j
        return (x,y,min_dist)


    def cal_dist(self, dist_type,x,y):
        dist = 0.0
        if dist_type == 'min':
            dist = self.dist_min(x,y)
        elif dist_type == 'max':
            dist = self.dist_max(x,y)
        else:
            dist = self.dist_avg(x,y)
        return dist




    #层次聚类
    def fit(self,data,dist_type, k):
        """        
        参数：
        data: 数据集
        dist_type: 'min','max','avg'之一
        k: 聚类个数
        """
        #聚类划分
        clusters = []
        #初始簇
        for sample in data:
            C_i = []
            C_i.append(sample)
            clusters.append(C_i)
        #距离矩阵
        dist_matrix = []
        for x in clusters:
            m_i = []
            for y in clusters:
                dist = self.cal_dist(dist_type, x, y)
                m_i.append(dist)
            dist_matrix.append(m_i)
        
        #簇个数
        q = len(data)

        #合并,更新
        while q > k:
            x,y,min_dist = self.find_min_dist_pos(dist_matrix)
            #合并两个集合C_x,C_y
            clusters[x].extend(clusters[y])
            #删除集合C_y,因为它已经合并
            clusters.remove(clusters[y])
            #更新距离矩阵
            dist_matrix = []
            for x in clusters:
                m_i = []
                for y in clusters:
                    dist = self.cal_dist(dist_type, x, y)
                    m_i.append(dist)
                dist_matrix.append(m_i)
            q = q - 1
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
def task_AGNES():
    #数据集：每三个是一组分别是西瓜的编号，密度，含糖量
    data = [(0.697,0.460),(0.774,0.376),(0.634,0.264),(0.608,0.318),(0.556,0.215),
            (0.403,0.237),(0.481,0.149),(0.437,0.211),(0.666,0.091),(0.243,0.267),
            (0.245,0.057),(0.343,0.099),(0.639,0.161),(0.657,0.198),(0.360,0.370),
            (0.593,0.042),(0.719,0.103),(0.359,0.188),(0.339,0.241),(0.282,0.257),
            (0.748,0.232),(0.714,0.346),(0.483,0.312),(0.478,0.437),(0.525,0.369),
            (0.751,0.489),(0.532,0.472),(0.473,0.376),(0.725,0.445),(0.446,0.459)]

    d=AGNES()
    clusters=d.fit(data,'avg',4)
    draw(clusters)


'''
task_AGNES()
'''




def test_AGNES(): 
    #获取数据
    Data = pd.read_excel(r"input_data/新闻.xlsx")
    data = Data.copy()
    #去除
    titel = data['标题'].map(lambda x:[i for i in list(jieba.cut(x)) if len(i) !=1])
    #词向量 CBOW hierarchical softmax模型
    model = gensim.models.Word2Vec(titel,sg=0,vector_size=2,window=5,
                                   min_count=2,negative=5,sample=0.001,hs=1,workers=6)
    model.wv.save_word2vec_format('wordsX.txt',binary=False)
    model = gensim.models.KeyedVectors.load_word2vec_format('wordsX.txt',binary=False)
    
    #格式化数据集
    data_mat = [tuple(model[i]) for i in range(len(model))]   
    #限制位数
    #data_mat = [tuple(round(xi,3) for xi in model[i]) for i in range(len(model))]      

    #AGNES 算法
    a = AGNES()
    clusters = a.fit(data_mat, 'avg', 5)
    draw(clusters)

    #sklearn库的 AGNES 算法
    sa = sklearn_AGNES(n_clusters = 5)
    X = np.array(data_mat)
    Y = sa.fit_predict(X)
    plt.scatter(X[:,0], X[:,1],c=Y)
    plt.show()


test_AGNES()






