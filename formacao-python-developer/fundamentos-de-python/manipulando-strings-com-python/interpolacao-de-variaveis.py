nome = str(input("Digite o seu nome: "));
idade = int(input("Digite a sua idade: "));
profissao = str(input("Digite a sua profissão: "));
linguagem = str(input("Digite a linguagem de programação que você está matriculado: "));

dados = {"nome": "Anderson", "idade": 26}

print("Nome: %s Idade %d" % (nome, idade));

print("Nome: {} Idade {}".format(nome, idade));

print("Nome: {1} Idade: {0}".format(idade, nome));
print("Nome: {1} Idade {0} Nome: {1} {1}".format(idade, nome));

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade));
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome));
print("Nome: {nome} Idade {idade}".format(**dados));

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.");

PI = 3.14159;

print(f"Valor de PI: {PI:.2F}");
print(f"Valor de PI: {PI:10.2F}");