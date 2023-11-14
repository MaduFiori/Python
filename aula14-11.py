#!/usr/bin/env python
# coding: utf-8

# In[28]:


cadastrar = input ('Cadastrar um novo cliente?')
nomes = []
cpf = []
cep = []

while cadastrar == 'sim':
    cadastrar = input ('Digite o nome do cliente:')
    nomes.append(cadastrar)
    cadastrar = input ('Digite o cpf:')
    cpf.append(cadastrar)
    cadastrar = input ('Digite o cep do cliente:')
    cep.append(cadastrar)
    
    cadastrar = input ('Digite o nome do cliente:')
    nomes.append(cadastrar)
    cadastrar = input ('Digite o cpf:')
    cpf.append(cadastrar)
    cadastrar = input ('Digite o cep do cliente:')
    cep.append(cadastrar)
    
    
    dicio = dict(zip(nomes,zip(cpf,cep)))
    print (dicio)


# In[33]:


numeros = [3,5,12,6,35,40,2]
a = (max(numeros))
print (a)


# In[ ]:




