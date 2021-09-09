alph = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alph_list = list(alph)
number_alphabet = []
for i in range(0, len(alph)):
    number_alphabet.append(i)

message_received_by_alicia = "26 2 15 16 6 0 13"
alicia_message_list = message_received_by_alicia.split()
n_alicia = 33
e_alicia = 7
aux1 = 0
aux2 = 0
message = ""
alicia_result = ""
for j in range(0, len(alicia_message_list)):
    for i in range(0, len(number_alphabet)):
        aux1 = number_alphabet[i] ** e_alicia
        aux2 = aux1 % n_alicia
        if str(aux2) == alicia_message_list[j]:
            message = message + " " + str(aux2)
            alicia_result = alicia_result + alphabet_list[number_alphabet[i]] + " "

message_received_by_benito = "22 8 10 9 18 0"
benito_message_list = message_received_by_benito.split()
n_benito = 39
e_benito = 5
aux1 = 0
aux2 = 0
message = ""
benito_result = ""
for j in range(0, len(benito_message_list)):
    for i in range(0, len(number_alphabet)):
        aux1 = number_alphabet[i] ** e_benito
        aux2 = aux1 % n_benito
        if str(aux2) == benito_message_list[j]:
            message = message + " " + str(aux2)
            benito_result = benito_result + alphabet_list[number_alphabet[i]] + " "
list_message_benito = benito_result.split()
list_message_alicia = alicia_result.split()
first_three_letters_benito = ""
first_three_letters_alicia = ""
for i in range(0, 3):
    first_three_letters_benito = first_three_letters_benito + list_message_benito[i] + " "
    first_three_letters_alicia = first_three_letters_alicia + list_message_alicia[i] + " "

print("Mensaje original de  Alicia: ", alicia_result)
print("Tres primeras letras que recibeAlicia: ", first_three_letters_alicia)
print("Mensaje orginila de benito Benito: ", benito_result)
print("Tres primeras letras que recibe Benito: ", first_three_letters_benito)