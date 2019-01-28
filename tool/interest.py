'''
计算收益
'''
# def calculate(money,year,intrate):
#     #
#     total = money * (1+intrate) ** year
#     if (year==0):
#         total = 0
#     return round(total,2)
# intList = []
# for i in range(10):
#     money = calculate(10000,i+1,0.07)
#     # allmoney = sum(money + calculate(10000,i,0.03))
#     intList.append(money)
# print(round(sum(intList),2))

import pandas as pd
s = pd.Series([1,2,3,4])
print(s.describe([0.1]))


