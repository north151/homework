from math import log 
import operator
import numpy as np

class DecisionTree:
    

    #出现次数最多标签值Y[i]
    def majorityCount(self,classList):
        """
        输入参数 classlist: 标签Y列表
        输出结果：          出现次数最多Y[i]
        """
        #出现次数最多标签值Y[i]
        classcount = {}
        for vote in classList:
            if vote not in classcount.keys():
                classcount[vote] = 0
            classcount[vote] += 1
        #标签值排序
        sortedclasscount = sorted(classcount.items(),operator.itemgetter(1),reverse=True)
        return sortedclasscount[0][0]



    #计算信息熵
    def cal_entropy(self,data):
        """
        输入参数 data: 数据集
        输出结果：     数据集的信息熵
        """
        #样本量
        inst_num = len(data)
        #不同标签值Y[i]出现的次数
        labelcounts = {}
        for featVect in data:
            #当前样本点标签值
            current_label = featVect[-1]
            if current_label not in labelcounts.keys():
                labelcounts[current_label]=0
            labelcounts[current_label] += 1 
        
        #信息熵
        entropy = 0.0
        for key in labelcounts:
            #各标签值的占比
            prob = float(labelcounts[key])/inst_num 
            #计算信息熵
            entropy -= prob* log(prob,2)

        return entropy
    
    
    
    
    #划分出子树数据集
    def split_data(self,data,feature_index,feature_value,feature_type):
        """
        输入参数 data：         父节点数据集
        输入参数 feature_index: 划分属性
        输入参数 feature_value: 划分属性取值
        输入参数 feature_type:  划分属性取值类型
        输出结果 splitedData:   子树数据集
        """
        #子树数据集
        splitedData = []
        
        #离散属性
        if feature_type == "D":
            for featVect in data:
                if featVect[feature_index] == feature_value:
                    #去除子树数据集中已选属性值
                    reducedFev = featVect[:feature_index]
                    reducedFev.extend(featVect[feature_index+1:])
                    #添加数据点
                    splitedData.append(reducedFev)

        #连续属性左子树"<="y
        if feature_type == "L":
            for featVect in data:
                if featVect[feature_index] <= feature_value:
                    splitedData.append(featVect)

        #连续属性右子树">"
        if feature_type == "R":
            for featVect in data:
                if featVect[feature_index] > feature_value:
                    splitedData.append(featVect)            
        return splitedData    
   
   
   
   
   
   
    #选择最优划分属性
    def choose_best_feature_to_split(self,data):
        """ 
        输入参数 data：           数据集
        输出结果 best_feature:    最优划分属性
        输出结果 best_div_value : 最优划分属性的划分点取值
        """
        #可用特征数
        feature_num = len(data[0])-1
        #当前信息熵
        baseEnt = self.cal_entropy(data)
        
        #最大信息增益,最优划分属性,划分点
        bestInforGain = 0.0
        best_feature = -1
        best_div_value = 0

        #信息增益最大作为最优划分属性
        for i in range(feature_num):
            #特征取值列表
            featureList = [example[i] for example in data]
            #特征取值种数
            uniqueValues = set(featureList)
            
            #离散属性
            if isinstance(data[0][i],str):
                #划分后信息熵
                newEnt = 0.0
                for value in uniqueValues:
                    #划分分支
                    subdata = self.split_data(data, i, value,"D")
                    #添加分支信息熵
                    prob = float(len(subdata))/len(data)
                    newEnt += prob*self.cal_entropy(subdata)
                #信息增益
                inforGain = baseEnt - newEnt

            #连续属性
            else:
                #特征值种数排序列表
                sort_uniqueValues = sorted(uniqueValues)
                #划分后信息熵
                minEnt = np.inf                
                for j in range(len(sort_uniqueValues)-1):
                    #划分点(中间点,二分法)
                    div_value = (sort_uniqueValues[j]+sort_uniqueValues[j+1])/2
                    #小于等于划分点
                    subdata_left = self.split_data(data, i, div_value, "L")
                    #大于划分点
                    subdata_right = self.split_data(data, i, div_value, "R")
                    #添加分支信息熵
                    prob_left = float(len(subdata_left))/len(data)
                    prob_right = float(len(subdata_right))/len(data)
                    ent = prob_left*self.cal_entropy(subdata_left)+prob_right*self.cal_entropy(subdata_right)
                    #选中划分点
                    if ent < minEnt:
                        minEnt = ent
                        best_div_value = div_value
                        
                #信息增益
                inforGain = baseEnt - minEnt
            
            #选中最优划分属性
            if inforGain > bestInforGain:
                bestInforGain = inforGain
                best_feature = i                    
        
        return best_feature,best_div_value


    


    
    #创建决策树
    def create_decision_tree(self,data,labels):
        """
        输入参数 data:   数据集
        输入参数 labels: 特征名列表
        输出结果 model_Tree: 字典形式决策树模型
        """
        #标签Y列表
        classList = [example[-1] for example in data]
        #标签Y全相同,返回标签值
        if classList.count(classList[0]) == len(classList):
            return classList[0]
        #数据集只有标签一列,返回出现次数最多Y[i]
        if len(data[0]) == 1: 
            return self.majorityCount(classList)

        #最优划分属性,划分点
        bestFeat,best_div_value= self.choose_best_feature_to_split(data) 
        
        #离散属性
        if isinstance(data[0][bestFeat],str):
            #最优属性
            bestFeatLabel = labels[bestFeat] 
            #根结点
            model_Tree = {bestFeatLabel:{}}
            #删除已选属性 
            del(labels[bestFeat])
    
            #特征取值列表
            featValues = [example[bestFeat] for example in data]
            #特征取值分支
            uniqueVals = set(featValues)
            #子树
            for value in uniqueVals:
                #可用属性列表
                subLabels = labels[:]          
                model_Tree[bestFeatLabel][value] = \
                    self.create_decision_tree(self.split_data(data, bestFeat,value,"D"),subLabels)
                    
        #连续属性
        else:
            #最优属性
            bestFeatLabel = labels[bestFeat]+"<"+str(best_div_value)
            #根结点
            model_Tree ={bestFeatLabel:{}}
            #可用属性列表
            subLabels = labels
            #左子树
            model_Tree[bestFeatLabel]["Y"]= \
                self.create_decision_tree(self.split_data(data,bestFeat,best_div_value,"L"),subLabels)
            #右子树
            model_Tree[bestFeatLabel]["N"]=\
                self.create_decision_tree(self.split_data(data,bestFeat,best_div_value, "R"),subLabels)

        return model_Tree







    #决策树预测函数
    def predict(self,tree_model,feature_names,test_vect):    
        """
        输入参数 tree_model:    决策树模型
        输入参数 feature_names: 属性名列表
        输入参数 test_vect:     待预测样本点
        输出结果 classlabel:    预测标签
        """
        #当前节点名
        firstStr = list(tree_model.keys())[0]
        #查找"<"
        lessIndex = str(firstStr).find('<')

        #连续属性
        if lessIndex > -1:
            #子节点
            secondDict = tree_model[firstStr]
            #当前节点属性名
            feat_name = str(firstStr)[:lessIndex]
            #
            featIndex = feature_names.index(feat_name)
            div_value = float(str(firstStr)[lessIndex+1:])

            #左子树
            if test_vect[featIndex] <= div_value:
                #非叶节点,递归预测
                if isinstance(secondDict["Y"], dict):
                    classLabel = self.predict(secondDict["Y"],feature_names, test_vect)
                #叶节点,返回结点标记
                else:
                    classLabel = secondDict["Y"]
            #右子树
            else:
                #非叶节点,递归预测
                if isinstance(secondDict["N"], dict):
                    classLabel = self.predict(secondDict["N"],feature_names, test_vect)
                #叶节点,返回结点标记
                else:
                    classLabel = secondDict["N"]
            return classLabel

        #离散属性
        else:
            #当前节点
            secondDict = tree_model[firstStr]
            #下一划分属性
            featIndex = feature_names.index(firstStr)
            #下一分支
            key = test_vect[featIndex]
            #进入分支(当前节点->子节点)
            valueOfFeat = secondDict[key]

            #非叶节点,递归分类
            if isinstance(valueOfFeat, dict):
                classLabel = self.predict(valueOfFeat, feature_names, test_vect)
            #叶结点,返回标记
            else:
                classLabel = valueOfFeat
            return classLabel
