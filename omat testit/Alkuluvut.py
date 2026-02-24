luku = int(input("Anna luku johon asti etsitään alkulukuja: "))

lista = []  #talletetaan alkuluvut

for i in range(1, luku+1):
    if i+1 % i == 0: #and luku // 1 == luku and luku // i ==1:
        lista.append(i)
print(lista)