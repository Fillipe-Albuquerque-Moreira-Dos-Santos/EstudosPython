cpf = input('Insira seu CPF')

cpf = cpf.strip()

cpf = cpf.replace('-','')

cpf = cpf.replace('-','')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')