s=0
a=0
print("Digite seu salário e o total de anos que você trabalhou para conseguir essa quantia: ")
print("SALARIO: ")
s=float(input())
print("ANOS: ")
a=int(input())
print("ANOS TRABALHADOS")

if a<5:
    aumento=(s*5)/100
    print("Como você trabalhou menos de 5 anos na empresa, recebeu um aumento de 5%: com isso receu:",s+aumento)
elif a<=5 and a>=10:
    aumento2=(s*10)/100
    print("Como você trabalhou entre 5 e 10 anos na empresa, recebeu um aumento de 10% em seu salário geral,m com isso recebeu: ",s+aumento2)  
elif a>10 and a<=15:
    aumento3=(s*15)/100
    print("Como você trabalhou de 11 á 15 anos na empresa, você recebeu um aumento de 15% em seu salário geral, com isso, recebeu: ",s+aumento3)
else: 
    aumento4=(s*20)/100
    print("Como você trabalhou um período maior ou igual á 16 anos na empresa, você recebeu um aumento de 20% em seu salário geral, com isso recebeu: ",aumento4+s)