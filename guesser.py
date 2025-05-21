#         "adivinhador" de números 1
#programação desenvolvida 100% por Ian Souza Molina 

#essa é uma das primeiras programações feitas por mim em python e
#não possuo interesses comerciais com esta programação, estou fazendo 
#apenas por diversão.

#----------------------------------------------------------------
#obs.:esta programação não descobre realmente o número.
#quando o número é digitado no início ,é salvo para usá-lo
#no fim da programação.
#----------------------------------------------------------------

import getpass
import time
s = True
n = False 


# Solicita que o usuário insira uma número e o inicio
print("por favor, digite o número escolhido")
x = getpass.getpass("vou adivinhar o seu número !: ")
print(".")
print("responda apenas com s de sim ou n de não")
print(".")
time.sleep(3)
#1pergunta
a = input("seu número é terminado em 1,3,5,7 ou 9 ?    ")
#2 pergunta
b  = input("seu número  é par..... ?")
print(b)
time.sleep(3)
#3 pergunta 
c= input("seu número é positivo ou diferente de zero ?")
print(".")
#4pergunta 
d = input("eu número é múltiplo de 3 e/ou 5 ?")
print (".")
#5 pergunta
print("analisando as possibilidades")
print(".")
time.sleep(3)
#resultado 
print("acho que o número escolhido  foi...")
if getpass == 22:
    print("vinte e dois é BOZONAROOOOO ")
if getpass == 56 :
   print("Meu nome é enENNNNNNEEEEEEEIAAAAAASSSSSSS ")
if getpass == 13 :
   print("Vai dar PT,vai dá,validar PT...")
else :
 print (x)