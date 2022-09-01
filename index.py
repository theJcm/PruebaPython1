# PROBLEMA 1
#strTexto = "La nota la es una de las notas de la canción"
strTexto = "En este texto, voy a repetir la letra a"
lstPalabras = strTexto.upper().split(" ")
lstPalabraRepetida = ["", 0]
for palabra in lstPalabras:
    contador = len([itm for itm in lstPalabras if palabra == itm])
    if contador > lstPalabraRepetida[1]:
        lstPalabraRepetida[0] = palabra
        lstPalabraRepetida[1] = contador

print(f"Mayor palabra repetida: {lstPalabraRepetida[0]}")
print(f"Cantidad de repeticiones: {lstPalabraRepetida[1]}")


# PROBLEMA 2
def multiplicacion(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
 
    if num2 == 1:
        return num1 
 
    if num1 == 1:
        return num2
 
    return num1 + multiplicacion(num1, num2 - 1)

 
def multiplicar(num1, num2):
    res = multiplicacion(num1, abs(num2))
    return -res if (num2 < 0) else res

strNumero = "-3,5"
lstNumeros = strNumero.split(",")
intPrimerNumero = int(lstNumeros[0])
intSegundoNumero = int(lstNumeros[1])
res = multiplicacion(intPrimerNumero, intSegundoNumero)
print(res)

# PROBLEMA 3
#lstVelas = [4,5,4,1,3,5]
lstVelas = [1,2,2,2,1]
intMaxAlturaVela = max(lstVelas)
intCantidadVelasAltas = len([itm for itm in lstVelas if itm is intMaxAlturaVela])
print(f"Maxima altura de velas: {intMaxAlturaVela}")
print(f"Cantidad de velas con maxima altura: {intCantidadVelasAltas}")
