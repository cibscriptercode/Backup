# Bucle for: -------------------------------
lista_frutas = ['banano', 'Manzana']
for fruta in lista_frutas:
    print(fruta)

palabra = 'palabra'
for letra in palabra:
    print(letra, end=' ')

for i in range(5):
    print(f"el valor de i es: {i}")

for i in range(5, 10):
    print(f"el valor de i es: {i}")

for i in range(1, 100, 3):
    print(f"el valor de i es: {i}")

email = 'juan@gmail.com'
for i in range(len(email)):
    print(f"el valor de i es: {i}")


# Bucle while: -------------------------------
cont = 0
while cont<5:
    print(f"cont: {cont}")
    cont+=1

cont = 0
while True:
    print(f"cont: {cont}")
    cont+=1 
    if cont==5:
        break; 

# Instrucciones continue, pass, y else: ------
  