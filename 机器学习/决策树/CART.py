from math import log 
import operator
import numpy as np

class CART:
    #计算信息熵
    def cal_entropy(self,data):
        """
        输入参数 data: 数据集
        输出结果： 数据集的信息熵
        """
        inst_num = len(data)#数据集样本数量
        labelcounts = {}#统计类别出现的次数
        for featVect in data:
            #特征向量的最后一列为类别标签
            current_label = featVect[-1]
            if current_label not in labelcounts.keys():
                #初始化标签计数为0
                labelcounts[current_label]=0
            #统计各个类别的出现次数
            labelcounts[current_label] += 1 

        #更改:
            
            
        entropy = 1
        for key in labelcounts:
            #各标签值占比
            prob = float(labelcounts[key])/inst_num 
            #基尼指数
            entropy -= prob**2


        return entropy



    #划分数据集，根据划分属性和属性的取值，对原数据集进行划分
    def split_data(self,data,feature_index,
                   feature_value,feature_type):
        """
        输入参数 data：划分前的数据集
        输入参数 feature_index: 划分属性
        输入参数 feature_value: 划分属性的取值
        输入参数 feature_type: 划分属性类型
        输出结果 splitedData:划分后的数据集
        """
        splitedData = []#保存划分后的数据子集
        if feature_type == "D":#对于离散属性
            for featVect in data:
                if featVect[feature_index] == feature_value:
                    reducedFev = featVect[:feature_index]
                    reducedFev.extend(featVect[feature_index+1:])
                    splitedData.append(reducedFev)
        if feature_type == "L":#对于连续属性"<="
            for featVect in data:
                if featVect[feature_index] <= feature_value:
                    splitedData.append(featVect)
        if feature_type == "R":#对于连续属性">"
            for featVect in data:
                if featVect[feature_index] > feature_value:
                    splitedData.append(featVect)            
        return splitedData    


    #选择最优划分属性!!!
    def choose_best_feature_to_split(self,data):
        """ 
        输入参数 data： 当前数据集
        输出结果 best_feature: 返回选择的最优划分属性
        输出结果 best_div_value : 返回最优划分属性的划分点取值
        """
        #当前可用特征个数
        feature_num = len(data[0])-1
        
        #初始化最大信息增益,最优划分属性,划分点
        bestInforGain = np.inf
        best_feature = -1
        best_div_value = 0
        
        
        #对每个可用属性，计算信息增益，选择信息增益最大的
        #特征作为划分属性
        for i in range(feature_num):
            if isinstance(data[0][i],str):#离散属性
                #统计离散属性的所有可能取值
                featureList = [example[i] for example in data]
                uniqueValues = set(featureList)
                newEnt = 0.0
                #根据每个取值进行数据划分，并计算信息增益
                for value in uniqueValues:
                    #每个离散取值划分一个对应的数据子集
                    subdata = self.split_data(data, i, value,"D")
                    prob = float(len(subdata))/len(data)
                    #计算数据子集上的信息熵
                    newEnt += prob*self.cal_entropy(subdata)

                
                inforGain = newEnt

                #选取信息增益最大的属性作为划分属性
                if inforGain < bestInforGain:
                    bestInforGain = inforGain
                    best_feature = i
                    
                    
            else:#连续属性
                #对连续属性的取值去重复并进行升序排序
                featureList = [example[i] for example in data]
                uniqueValues = set(featureList)
                sort_uniqueValues = sorted(uniqueValues)
                minEnt = np.inf
                #采用二分法处理连续属性                
                for j in range(len(sort_uniqueValues)-1):
                    #取两个连续取值的中间值作为划分点
                    div_value = (sort_uniqueValues[j]+sort_uniqueValues[j+1])/2
                    #属性取值小于等于划分点的子集
                    subdata_left = self.split_data(data, i, div_value, "L")
                    #属性取值大于划分点的子集
                    subdata_right = self.split_data(data, i, div_value, "R")
                    prob_left = float(len(subdata_left))/len(data)
                    prob_right = float(len(subdata_right))/len(data)
                    #如式(2.5)的右半部分
                    ent = prob_left*self.cal_entropy(subdata_left)+\
                        prob_right*self.cal_entropy(subdata_right)
                    if ent < minEnt:
                        minEnt = ent
                        best_div_value = div_value
                        
                #计算信息增益
                # inforGain = baseEnt - minEnt
                
                inforGain = minEnt
                
                #选中最优划分属性
                if inforGain < bestInforGain:
                    bestInforGain = inforGain
                    best_feature = i
                    
                    
                    
                    
        return best_feature,best_div_value
    #统计出现次数最对的类别
    def majorityCount(self,classList):
        """
        输入参数 classlist: 数据集样本类别组成的列表
        输出结果： 出现次数最多的类别
        """
        classcount = {}
        for vote in classList:
            if vote not in classcount.keys():
                classcount[vote] = 0
            classcount[vote] += 1
        sortedclasscount = sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)
        return sortedclasscount[0][0]
    
    
    
    
    #创建决策树
    def create_decision_tree(self,data,labels):
        """
        输入参数 data: 训练数据集
        输入参数 labels: 属性名的列表
        输出结果 model_Tree: 以字典的形式返回决策树模型
        """
        #获取数据集的样本类别标签列表
        classList = [example[-1] for example in data]
        #当类别完全相同时则停止继续划分，直接返回该类的标签
        if classList.count(classList[0]) == len(classList):
            return classList[0]
        #遍历完所有的特征时，返回出现次数最多的类别作为返回值
        if len(data[0]) == 1: 
            return self.majorityCount(classList)
        #获取最好的分类特征索引beatFeat以及划分点best_div_value
        bestFeat,best_div_value= self.choose_best_feature_to_split(data)
        if isinstance(data[0][bestFeat],str):#离散属性
            bestFeatLabel = labels[bestFeat] #获取该特征的名字
            #生成一个树结点
            model_Tree = {bestFeatLabel:{}} 
            del(labels[bestFeat])#删除属性
            #获取离散属性的所有可能取值
            featValues = [example[bestFeat] for example in data]
            uniqueVals = set(featValues)
            #为每个取值生成一个孩子结点，递归构造决策树
            for value in uniqueVals:
                subLabels = labels[:]          
                model_Tree[bestFeatLabel][value] = \
                    self.create_decision_tree(self.split_data(data, 
                                                              bestFeat, 
                                                              value,"D"),
                                              subLabels)
        else:#连续属性
            bestFeatLabel = labels[bestFeat]+"<"+str(best_div_value)
            model_Tree ={bestFeatLabel:{}}#生成一个树结点
            subLabels = labels
            #递归生成左子树
            model_Tree[bestFeatLabel]["Y"]= \
                self.create_decision_tree(self.split_data(data, 
                                                          bestFeat, 
                                                          best_div_value, "L"),
                                          subLabels)
            #递归生成右子树
            model_Tree[bestFeatLabel]["N"]=\
                self.create_decision_tree(self.split_data(data, 
                                                          bestFeat, 
                                                          best_div_value, "R"),
                                          subLabels)
        return model_Tree
    #决策树预测函数
    def predict(self,tree_model,feature_names,test_vect,unknown='unknown'):
        """
        输入参数 tree_model: 以字典形式保存的决策树模型
        输入参数 feature_names: 特征的命名
        输入参数 test_vect: 测试样本的特征向量
        输出结果 classlabel: 预测类别标签
        """
        firstStr = list(tree_model.keys())[0]#查找根节点
        lessIndex = str(firstStr).find('<') #在根节点中查找"<"符号
        #节点对应的划分属性是连续属性，firstStr的格式为"feat_name<div_value"
        if lessIndex > -1:
            secondDict = tree_model[firstStr]#根节点的子节点
            feat_name = str(firstStr)[:lessIndex] # 连续属性名
            featIndex = feature_names.index(feat_name)
            div_value = float(str(firstStr)[lessIndex+1:])
            #进入左子树,递归分类
            if test_vect[featIndex] <= div_value:
                if isinstance(secondDict["Y"], dict):#非叶子节点，递归分类
                    classLabel = self.predict(secondDict["Y"], 
                                                    feature_names, test_vect)
                else:#叶子节点，直接返回结点的类别标记
                    classLabel = secondDict["Y"]
            else:#进入右子树，递归分类
                if isinstance(secondDict["N"], dict):#非叶子节点，递归分类
                    classLabel = self.predict(secondDict["N"], 
                                                    feature_names, test_vect)
                else:#叶子节点，直接返回结点的类别标记
                    classLabel = secondDict["N"]
            return classLabel
        else:#对于离散属性
            secondDict = tree_model[firstStr]#根节点的子节点
            featIndex = feature_names.index(firstStr)
            key = test_vect[featIndex]
            # 如果不存在该分支
            if key not in secondDict.keys():
                return unknown
            valueOfFeat = secondDict[key]
            if isinstance(valueOfFeat, dict):#非叶子节点，递归分类
                classLabel = self.predict(valueOfFeat, feature_names, test_vect)
            else:#叶子节点，直接返回结点的类别标记
                classLabel = valueOfFeat
            return classLabel
