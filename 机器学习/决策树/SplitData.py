
import pandas as pd
from sklearn.model_selection import train_test_split
from TreeVisualization import *

# 划分训练集,测试集
def split_Output_Data(Data,size):
    '''
    输入: 样本数据集Data
    输出: 训练集train_data,测试集test_data
    功能: 将样本划分为 训练集 和 测试集
    '''
    #测试集占样本百分比
    train_data,test_data = train_test_split(Data, test_size=size) 
    #打印训练集
    print("train data:")
    for d in train_data:
        print("          ",d)
    #打印测试集
    print("test data:")
    for d in test_data:
        print("          ",d)
    
    return train_data,test_data




def creat_Output_Tree(model,model_type,train_data,test_data,feature_names):
   #构造决策树
   feature_names = ['Color','Root','Sound','texture','qibu','cugan','size']
   tree = model.create_decision_tree(train_data, feature_names)
   createPlot(tree)
   #测试集预测标签列表
   y_pred = []
   #测试集实际标签列表
   y_true = []     
   for x in test_data:
      #测试集标签值
      label= model.predict(tree, feature_names, x)
      #测试集预测标签值
      y_pred.append(label)
      #测试集实际标签值
      y_true.append(x[-1])
      #结果
      result = pd.DataFrame()
      result['true']=y_true
      result['pred']=y_pred
   print("\n",model_type,"预测结果对比:\n",result)
   print("\n决策树:\n    ",tree,"\n\n")






































