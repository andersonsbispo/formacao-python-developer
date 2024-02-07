saldo = 1000;
saque = float(input("Digite o valor que deseja sacar: "));

status = "Sucesso" if saldo >= saque else "Falha";

print(f"{status} ao realizar o saque!");