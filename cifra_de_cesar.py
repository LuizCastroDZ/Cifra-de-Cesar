# -*- coding: utf-8 -*-
"""Cifra de cesar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZASe76lSwMbdC1A1dVO--ogpijGNVZq7
"""

#Função para criptografar

def cripto(frase):
  tradutor = ""
  for letra in frase:
    if letra in "aA":
      tradutor = tradutor + "d"
    elif letra in "bB":
      tradutor = tradutor + "e"
    elif letra in "cC":
      tradutor = tradutor + "f"
    elif letra in "dD":
      tradutor = tradutor + "g"
    elif letra in "eE":
      tradutor = tradutor + "h"
    elif letra in "fF":
      tradutor = tradutor + "i"
    elif letra in "gG":
      tradutor = tradutor + "j"
    elif letra in "hH":
      tradutor = tradutor + "k"
    elif letra in "iI":
      tradutor = tradutor + "l"
    elif letra in "jJ":
      tradutor = tradutor + "m"
    elif letra in "kK":
      tradutor = tradutor + "n"
    elif letra in "lL":
      tradutor = tradutor + "o"
    elif letra in "mM":
      tradutor = tradutor + "p"
    elif letra in "nN":
      tradutor = tradutor + "q"
    elif letra in "oO":
      tradutor = tradutor + "r"
    elif letra in "pP":
      tradutor = tradutor + "s"
    elif letra in "qQ":
      tradutor = tradutor + "t"
    elif letra in "rR":
      tradutor = tradutor + "u"
    elif letra in "sS":
      tradutor = tradutor + "v"
    elif letra in "tT":
      tradutor = tradutor + "w"
    elif letra in "uU":
      tradutor = tradutor + "x"
    elif letra in "vV":
      tradutor = tradutor + "y"
    elif letra in "wW":
      tradutor = tradutor + "z"
    elif letra in "xX":
      tradutor = tradutor + "a"
    elif letra in "yY":
      tradutor = tradutor + "b"
    elif letra in "zZ":
      tradutor = tradutor + "c"
    else:
    
      tradutor = tradutor + letra
  return tradutor

#print(cripto(input("Digite um texto: ")))

#Função para descriptografar
def decripto(frase):
  tradutor = ""
  for letra in frase:
    if letra in "d":
      tradutor = tradutor + "a"
    elif letra in "e":
      tradutor = tradutor + "b"
    elif letra in "f":
      tradutor = tradutor + "c"
    elif letra in "g":
      tradutor = tradutor + "d"
    elif letra in "h":
      tradutor = tradutor + "e"
    elif letra in "i":
      tradutor = tradutor + "f"
    elif letra in "j":
      tradutor = tradutor + "g"
    elif letra in "k":
      tradutor = tradutor + "h"
    elif letra in "l":
      tradutor = tradutor + "i"
    elif letra in "m":
      tradutor = tradutor + "j"
    elif letra in "n":
      tradutor = tradutor + "k"
    elif letra in "o":
      tradutor = tradutor + "l"
    elif letra in "p":
      tradutor = tradutor + "m"
    elif letra in "q":
      tradutor = tradutor + "n"
    elif letra in "r":
      tradutor = tradutor + "o"
    elif letra in "s":
      tradutor = tradutor + "p"
    elif letra in "t":
      tradutor = tradutor + "q"
    elif letra in "u":
      tradutor = tradutor + "r"
    elif letra in "v":
      tradutor = tradutor + "s"
    elif letra in "w":
      tradutor = tradutor + "t"
    elif letra in "x":
      tradutor = tradutor + "u"
    elif letra in "y":
      tradutor = tradutor + "v"
    elif letra in "z":
      tradutor = tradutor + "w"
    elif letra in "a":
      tradutor = tradutor + "x"
    elif letra in "b":
      tradutor = tradutor + "y"
    elif letra in "c":
      tradutor = tradutor + "z"
    else:
    
      tradutor = tradutor + letra
  return tradutor

#print(cripto(input("Digite um texto: ")))

#Main
i = 1
while i < 2:
  escolha = input("\nCriptografar[1] / Descriptografar:[2] / Sair:[3] ----  ")      #Escolha da ação do codigo

  if escolha == "1":                                                                #Criptografar a mensagem
    mensagem = cripto(input("\nDigite a mensagem: "))
    print("\nSua mensagem encriptada é: "+ mensagem)
    continuar = input("\nDeseja continuar? Sim[1] Não[2] ----  ")
    if continuar == "1":
      i += 0
    elif continuar == "2":
      i += 1
      print("Ate mais!")

  elif escolha == "2":                                                              #Criptografar a mensagem
    mensagem = decripto(input("\nDigite a mensagem: "))
    print("\nSua mensagem desncriptografada é: "+ mensagem)
    continuar = input("\nDeseja continuar? Sim[1] Não[2] ----  ")
    if continuar == "1":
      i += 0
    elif continuar == "2":
      i += 1
      print("\nAte mais!")

  else:
    i += 1
    print("\nAte mais!")
  
  #CONSEGUI DIAAAAXO