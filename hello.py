#多元线性回归模型
import pandas as pd  
import numpy as np  
from sklearn.linear_model import LinearRegression  
  
# 读取数据  
data = pd.read_excel('data1.xlsx')  
  
# 提取自变量和因变量  
X = data[['Count', 'frequency']]  
y = data[['1 try', '2 tries', '3 tries', '4 tries', '5 tries', '6 tries', '7 or more tries (X)']]  
  
# 拟合线性回归模型  
model = LinearRegression()  
model.fit(X, y)  
  
# 对于特定的单词和日期，预测尝试次数的分布  
word = 'EERIE'  
date = '2023-03-01'  
  
# 计算该单词的count和frequency  
letters = list(word)  
count = len(letters) - len(set(letters))  
frequency = 23.66480   # 这里假设EERIE的常见程度为23.66480 
  
# 进行预测  
X_test = np.array([[count, frequency]])  
y_pred = model.predict(X_test)  
  
# 输出结果  
print(f'Predicted distribution of tries for {word} on {date}:')  
print(f'1 try: {y_pred[0, 0]:.2f}%')  
print(f'2 tries: {y_pred[0, 1]:.2f}%')  
print(f'3 tries: {y_pred[0, 2]:.2f}%')  
print(f'4 tries: {y_pred[0, 3]:.2f}%')  
print(f'5 tries: {y_pred[0, 4]:.2f}%')  
print(f'6 tries: {y_pred[0, 5]:.2f}%')  
print(f'7 or more tries: {y_pred[0, 6]:.2f}%')  
  
# 对于模型预测的不确定性，可以使用交叉验证等方法进行评估，这里不再展开。