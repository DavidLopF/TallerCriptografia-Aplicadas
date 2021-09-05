alph = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

password = "LZAHL ZBTHW YBLIH XBLKL ILYOH ZLYCH ROKH"
print("Clave para desifrar: " , password)

answer = []
password = password.replace(" ", "")
temp = []
aux = []

for i in range(len(alph)):
    aux.append(alph[i])

for i in range(len(alph)):
    temp.append(0)

for i in range(len(password)):  # Analisis criptografico
    for j in range(len(alph)):
        if password[i] == alph[j]:
            temp[j] += 1


def buscarMax():
    for i in range(len(temp)):
        if temp[i] == max(temp):
            return i


def buscarPos(letra):
    for i in range(len(aux)):
        if aux[i] == letra:
            return int(i)

for i in range(len(password)):
    x = buscarPos(password[i])
    answer.append(alph[x-7])

res = "".join(answer)

print("Analisis criptografico: ", temp)
print("letra que mas se repite:", alph[buscarMax()])
print("Intento de decifrar con desplazamiento de 7 (hasta la letra E): ", res)
