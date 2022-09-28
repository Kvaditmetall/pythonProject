n = ['hi', "привет", "шумбрат", "приветос"]
i = input("Privet")
# print(n)
for n in n:
    if n in i:
        print('Шумбрат Ялгай')
        break
else:
    print('Пошел на хер безкультурная скотина')
