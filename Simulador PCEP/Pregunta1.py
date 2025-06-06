#Pregunta 1
#What is the expected output of the following code?
w = [7,3,23,42]
x = w[1:]
y = w[1:]
z = w

y[0] = 10
z[1] = 20

print("Pregunta 1 Respuesta:")
print(w)

#A. [7, 3, 23, 42]
#B. [7, 20, 23, 42] -> OK
#C. [10, 20, 42]
#D. [10, 20, 23, 42]

#----------------------------------------------------------
#Revisar el snippet y escoger uno de las siguientes respuestas
#la cual es verdadera
nums = []
vals =  nums
vals.append(1)

print("Pregunta 2 Respuesta:")
print("Len: " + str(len(nums)) + " Vals: " + str(len(vals)))

#A. vals is longer than nums
#B. nums and vals are of the same length --> OK
#C. nums is longer than vals

#----------------------------------------------------------
#Cual es la salida esperada del siguiente codigo

data = {'a':1, 'b':2,'c':3}
print("Pregunta 3 Respuesta:")
#print(data['a','b'])

#A. (1, 2)
#B. The code is erroneous. --> OK
#C. {'a':1, 'b':2}
#D. [1,2]

#----------------------------------------------------------
#Cuantos elementos contiene la lista L?

L = [i for i in range(-1,-2)]

print("Pregunta 4 Respuesta:")
print("Tamaño L: " + str(len(L)))

#A. one
#B. two
#C. three
#D. zero --> OK

#----------------------------------------------------------
#Cual es la salida del siguiente snippet?

my_list = [0,1,2,3]
x=1
for elem in my_list:
    x *= elem

print("Pregunta 5 Respuesta:")
print(x)

#A. 1
#B. 0 --> OK
#C. 6

#----------------------------------------------------------
#Cual es la salida esperada para el siguiente codigo?

nums = [1,2,3]
data = ('Peter',) * (len(nums) - nums[::-1][0])

print("Pregunta 6 Respuesta:")
print("len(nums): " + str(len(nums)))
print("nums[::-1][0] : " + str(nums[::-1][0]))
print(data)

#A. ('Peter', 'Peter',)
#B. PeterPeter
#C. The code is erroneous.
#D. ('Peter')
#E. () --> OK

#----------------------------------------------------------
#Cual es la salida del siguiente codigo?

x= [0,1,2]
x.insert(0,1)
del x[1]
print("Pregunta 7 Respuesta:")
print(sum(x))

#A. 2
#B. 4
#C. 5
#D. 3