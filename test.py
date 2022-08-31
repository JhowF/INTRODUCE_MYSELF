import numbers
from unicodedata import numeric


nome = input("Digite seu nome completo: ").upper().strip()

if nome == "JONATHAN":
    print("Usúario valido".upper())
    
else:
    print("Usuario invalido!")

idade = input("digite sua idade: ").strip()

if idade >="0" and idade<="9":
    pass
    idade = int(idade)
    if idade < 18:
        print("Sinto muito, más so aceitamos maiores de idade")
    else:
        print("Tudo certo!")
    
else:
    print("Digite somente número!")
    
    

    

    

