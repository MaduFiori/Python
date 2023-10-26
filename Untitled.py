#!/usr/bin/env python
# coding: utf-8

# In[15]:


salario = input ('Qual é o seu salário?')
custo = input ('Qual é o seu custo de vida básico?')
cartao = input ('Qual o valor do seu cartão?')

print ('O seu salário é de '+ salario+ ', seu custo básico é de '+custo+ ' e o seu crtão é no valor de '+cartao)


# In[ ]:


salario = input ('Qual é o seu salário?')
custo = input ('Qual é o seu custo de vida básico?')
cartao = input ('Qual o cvalor do seu cartão?')

liquido = salario - custo



# In[11]:


print ('ola')


# In[21]:


salario = input ('Qual é o seu salário?')
custo = input ('Qual é o seu custo de vida básico?')
cartao = input ('Qual o valor do seu cartão?')

liquido = int(salario) - int(custo) - int(cartao)

print('seu saldo líquido ficará '+ str(liquido))


# In[45]:


email = input ('Qual é o seu email? ')
print(email)

if '@gmail.com' in email:
    print('Seu email contém @gmail')
elif '@hotmail.com' in email:
    print('Seu email contém @hotmail')
else:
    print('Seu email está inválido')

