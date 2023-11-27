#!/usr/bin/env python
# coding: utf-8

# In[76]:


bebidas=[]
suprimentos=[]

produtos = [' beb46275','TFA23962','TFA64715','TFA69555','TFA56743',
'BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623',
'BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792',
'TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146',
'BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251',
'BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

precos = [
1258.69, 917.65, 1050.26, 414.36, 904.9, 1077.77,
 640.14, 379.92, 1201.62, 1206.15, 1256.34, 729.27,
 1252.72, 432.89, 457.95, 1191.3, 421.77, 1165.32, 1040.62,
 781.12, 1059.19, 1232.68, 1112.44, 1265.35, 575.2, 1150.78,
 544.38, 949.14, 1043.73, 758.28, 398.22, 662.56, 723.15, 468.72,
 366.52, 513.45, 703.74, 421.34, 961.38]

dict = {}

for item in produtos:
    item = item.strip().upper()
    if 'BEB' in item:
        bebidas.append(item)
    elif 'TFA' in item:
        suprimentos.append(item)
for i in range(len(produtos)):
    produtos[i] = produtos[i].strip().upper()
if 'BEB' in produtos[i]:
    bebidas.append(produtos[i])
    precos.append(precos[i])

dict = {}
for i,j in zip(bebidas, precos):
    dict[i] = j
print(dict)   


# In[ ]:




