#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

numero= 2
print(numero)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:


type(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(numero)



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre= "Hernan"


# 5) Crear una variable que contenga un número complejo

# In[3]:


a= 4j + 5


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

type(a)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:


a= 'True'
b= True
a==b


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print('La variable 1 es de tipo ', type(a))
print('La variable 2 es de tipo ', type(b))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


a= 5+2.45
print(a)


# 11) Realizar una operación de suma de números complejos

# In[2]:

a= 4j+5
b= 3+2j
print(a+b)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

c= a+5
print(c)



# 13) Realizar una operación de multiplicación

# In[5]:


a=5*8
print(a)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:


a= 2**8
print(a)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

a= 27/4
print(a)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

b= 27//4
print(b)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


c= 27%4
print(c)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


4*6+3


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


a= "apto"
b= " 30"
c=a+b
print(c)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


a="2"
b=2
a==b
# La operacion arroja que es falsa porque la variable a es de tipo str y la variable b es de tipo int


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

a = "2"
a = int(a)
a==b



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float('3.8')
# Porque python reconoce la "," como un separador de datos, y no para definir un decimal, para eso se usa el "." 


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

a = -3
a -= 1
print(a)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


1 << 2
#Es una operacion binaria, donde el 1 se representa como 0001, y el numero 2, corresponde a la cantidad de 0 que se desplaza hacia la izquierda en este caso,
#quedando de esta forma 0100, que es el valor "4" en binario


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

# 2+'2' no se permite porque es la suma de un valor int y el otro es str
print(float(2) + float('2'))
print(int(2) + int('2'))
print(str(2) + str('2'))




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

a = "hola " * 3
print (a)

