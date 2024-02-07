N = int(input());

while (N > 0):
    n = str(input());
    v = n.split();
    
    if v[0].endswith(v[1]):
        print("encaixa", end="\n");
    else:
        print("nao encaixa", end="\n");
    
    N -= 1;