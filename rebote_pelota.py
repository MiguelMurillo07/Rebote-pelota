# Una pelota se deja caer desde una altura h, y en cada rebote sube el 10% menos del anterior. Hacer el diagrama de flujo y programa en python, que lea h, y que calcule e imprima en cual rebote la pelota no alcanza a subir la quinta parte de la altura inicial.


print("--------------------------------------")
print("-----------Rebote Pelota--------------")
print("--------------------------------------")

# input

h = int(input("Digite el valor de la altura del que quiera caer la pelota: "))
r = 0
k = h/5

while h>k:
     h = h-(h*0.10)
     r = r+1
     
     
print("La pelota no alcanza a subir la quinta parte en el rebote número " +str(r))

