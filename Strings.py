#!/usr/bin/env python
# coding: utf-8

# # Strings
# 
# <span style="color: red;"><b>Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.</b></span>

# #### 1. Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# <pre>
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
# </pre>

# In[11]:


st1 = input("Digite uma frase: ")
st2 = input("Digite outra frase para comparar: ")

if st1 > st2:
    print("{} contém: "+ str(len({})).format(st1,st1))
    print("{} contém: "+ str(len({})).format(st2,st2))
    print('{} é maior que {}'.format(st1,st2))
else:
    print("{} contém: "+ str(len({})).format(st1,st1))
    print("{} contém: "+ str(len({})).format(st2,st2))
    print('{} é maior que {}'.format(st2,st1))


# #### 2. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
# <pre>
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133
# </pre>

# In[ ]:




