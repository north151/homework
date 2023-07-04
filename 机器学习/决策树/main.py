from DecisionTree import *
from TreeVisualization import *
from CART import *
from SplitData import *

#属性名称
feature_names = ['Color','Root','Sound','texture','qibu','cugan','size']
data = [    ['A','A','A','A','A','A',0,'yes'],
            ['B','A','B','A','A','A',0,'yes'],
            ['B','A','A','A','A','A',0,'yes'],
            ['A','A','B','A','A','A',0,'yes'],
            ['C','A','B','A','A','A',0,'yes'],
            ['A','B','A','A','B','B',0,'yes'],
            ['B','B','A','B','B','B',0,'yes'],
            ['B','B','A','A','B','A',0,'yes'],
            ['B','B','B','B','B','A',1,'no'],
            ['A','C','C','A','C','B',1,'no'],
            ['C','C','C','C','C','A',1,'no'],
            ['C','A','A','C','C','B',2,'no'],
            ['A','B','A','B','A','A',2,'no'],
            ['C','B','B','B','A','A',2,'no'],
            ['B','B','A','A','B','B',2,'no'],
            ['C','A','A','B','C','A',0,'no'],
            ['A','A','B','C','B','A',1,'no']
        ]
#属性类型，0: 离散属性，1: 连续属性
featLabelProperties=[0,0,0,0,0,0,1]
#标签
labels = ['yes','no']

#划分训练集,测试集
train_data,test_data = split_Output_Data(data,0.3)


# 信息增益
model = DecisionTree()
tree = model.create_decision_tree(train_data, feature_names)
feature_names = ['Color','Root','Sound','texture','qibu','cugan','size']
y_pred = []
y_true = []     
for x in test_data:
   label= model.predict(tree, feature_names, x)
   y_pred.append(label)
   y_true.append(x[-1])

import pandas as pd
result = pd.DataFrame()
result['true']=y_true
result['pred']=y_pred
print("\nC4.5预测结果对比:\n",result)
print("\n决策树:\n    ",tree,"\n\n")
createPlot(tree)


# 基尼指数
model = CART()
tree = model.create_decision_tree(train_data, feature_names)
feature_names = ['Color','Root','Sound','texture','qibu','cugan','size']
y_pred = []
y_true = []     
for x in test_data:
   label= model.predict(tree, feature_names, x)
   y_pred.append(label)
   y_true.append(x[-1])
import pandas as pd
result = pd.DataFrame()
result['true']=y_true
result['pred']=y_pred
print("\nCART预测结果对比:\n",result)
print("\n决策树:\n    ",tree,"\n\n")
createPlot(tree)




