conta_normal = False;
conta_universitaria = False;

saldo = 2000;
saque = float(input("Digite o valor que deseja sacar: "));
cheque_especial = 450;

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!");
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!");
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!");
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!");
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!");
else:
    print("Sistema não reconhece o seu tipo de conta, entre em contato com o seu gerente.");