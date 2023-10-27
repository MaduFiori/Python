#!/usr/bin/env python
# coding: utf-8

# In[1]:


letra = input ('Digite 3 letras: ')
if letra == "ABC":
    print("Parabéns!!")
else:
    print("Que pena!")


# In[26]:


venda = int(input('Digite o valor das vendas : '))
meta = int(input('Digite a meta esperada: '))
calc = meta*2

if venda > calc:
    print('Você ganhou bônus de 20%, valor total da venda + bônus R${}'.format(venda*0.2 + venda))
    
elif venda < meta:
    print('Você ganhou bônus de 0%, valor total R${}'.format(venda))
else:
    print('Você ganhou bônus de 10%, valor total da venda + bônus R${}'.format(venda*0.1 + venda))

