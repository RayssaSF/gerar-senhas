from random import choice
import string

Site=input("Digite o Site: ")
print("Vamos Gerar uma senha para o Site: " ,Site)
quant=int(input("Digite Quantos Caracteres deve ter a Senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''
for i in range(quant):
    senha_segura += choice(caracteres)
    
print(f'A Senha Gerada para o Site : {Site} é a Senha: {senha_segura}')



