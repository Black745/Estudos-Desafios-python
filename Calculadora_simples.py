from random import randint
computador=randint(0,10)
opcoes=0
print("Digite o valor para ver as opções:")
num=int(input("digite o primeiro valor: "))
num2=int(input("digite o segundo valor: "))
while opcoes !=5:
    print("""
    [0]subtrair
    [1]somar
    [2]multiplicar
    [3]dividir
    [4]novos numeros
    [5]sair do menu)""")
    opc=int(input("digite sua opcao: "))
    if opc==1:
        soma=num+num2        
        print(f"a soma de {num} + {num2}={soma}")
    elif opc == 2:
        multiplica=num*num2
        print(f"o resultado de {num} x {num2}={multiplica}")
    elif opc ==3:
         divisao=num/num2
         print(f"o resultado de {num} / {num2}= {divisao}")
    elif opc == 4:
          num=int(input("digite o primeiro valor: "))
          num2=int(input("digite o segundo valor: "))
    elif opc == 5:
          opcoes+=5
    elif opc==0:
        Subtrai=num-num2
        print(f"o resultado de {num} - {num2}={Subtrai}") 
    Choice=str(input("deseja continuar? [S] ou [N] "))
    if Choice not in 'Ss':
        break
