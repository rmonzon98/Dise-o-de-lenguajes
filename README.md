# Proyecto de diseño de lenguajes
## Diseño de la aplicación
###  \_\_main__
Este script es el encargado de la interfaz del usuario. Es el que solicita las expresiones, envía los datos a las clases que manipulan los datos e imprime en consola los resultados.

### infixtopostfix
Este script tiene dos tareas principales:
* Verificar que la expresión no tenga errores
* Convertir la expresión a un estado que le convenga al programa

#### Funciones
```sh
def validChar(char):
```
Esta función recibe un carácter y regresa un valor booleano. En caso de que el carácter no sea un operador devolverá un True, sino devolverá un False.

```sh
def getAlphabet(expresion):
```
Recibe una expresión y devuelve un alfabeto (todas las etiquetas) de la expresión.

```sh
def computableExpresion(expresion):
```
Recibe una expresión y la convierte en una expresión que la computadora pueda entenderla.

```sh
def isEmpty(arrayContent):
```
Verifica si una lista está vacía.

```sh
def lastElement(arrayContent):def lessThan(arrayContent,character):
```
Devuelve el ultimo elemento de una lista
```sh
def lessThan(arrayContent,character):
```
Compara la precedencía entre dos caracteres y devuelve True si el segundo carácter tiene un valor menor o igual al primero, sino devuelve un False.
```sh
def infixaPostfix(exp):
```
Recibe una expresión infix y devuelve una expresión postfix
```sh
def convertOperators(expresion):
```
Convierte los operadores “especiales” en sus operaciones equivalentes. ej: a+ = aa*.
```sh
def expresionParaArbol(expresion):
```
Recibe una expresión infix y la convierte a postfix, con la diferencia que le agrega al final la concatenación de #

### builder (dentro de la carpeta de AFN)
Este script es el encargado de recibir una expresión regular en postfix y crear el AFN.
#### Funciones
```sh
def ThompsonAlgorithm(postfixexp):
```
Se implementa el algoritmo de Thompson a partir de una expresión postfix.
#### Clase
clase NFA
Tiene los atributos
* initial: que representa el estado inicial del NFA
* final: que representa el estado de aceptación del NFA
* label: que representa la etiqueta de transición
* dict: tiene la información del NFA en un dict. ejemplo NFA de a:  {initial:{label:final}}

Tiene las funciones
* getX: hay un get por cada atributo de la clase para devolver el valor de cada atributo
* unionOperator: realiza la operación unión entre dos NFA
* concat: realiza la operación concatenación entre dos NFA
* closure: realiza la operación cerradura a un NFA
* createCopy: crea una copia de un diccionario que recibe como parametro
* createDict: crea el diccionario inicial de un NFA

### subsets
Script encargado de crear los subconjuntos a partir de un AFN.

#### Funciones
```sh
def eCerradura(dictionary, finalNode, node):
```
Recibe un diccionario, el nodo de aceptación del NFA, nodo desde donde se empezará a mover a través de epsilon. Devuelve una lista los nodos que visito.
```sh
def move(dictionary,finalNode,states,label):
```
Recibe un diccionario del NFA, nodo de aceptación del NFA , estados a evaluar y etiqueta donde se permitirá moverse además de epsilon.
```sh
def subsetsBuilder(alphabet,states,dictionary,initial,final):
```
Recibe el alfabeto del NFA, lista de todos los estados, diccionario del NFA, nodo inicial y nodo de aceptación. Regresa una lista con las transiciones entre los estados, nombres de los estados, lista de estados y lista que indica si un estado es de aceptación dependiendo.

### simulaciones
script encargado de realizar las simulaciones del AFN y AFD

#### Funciones
```sh
def eCerradura(dictionary, finalNode, node):
```
Recibe un diccionario, el nodo de aceptación del NFA, nodo desde donde se empezará a mover a través de epsilon. Devuelve una lista los nodos que visito.
```sh
def move(dictionary,finalNode,states,label):
```
Recibe un diccionario del NFA, nodo de aceptación del NFA , estados a evaluar y etiqueta donde se permitirá moverse además de epsilon.
```sh
def simulationNFA(dictionary, initial, final, expresion, subsets,alphabet):
```
Recibe el diccionario del NFA, nodo de aceptación, la expresión regular a evaluar, conjunto de los subconjuntos, el alfabeto. Regresa True si llego a un nodo de aceptación de lo contrario regresa un valor False.

```sh
def simulationFDA(dictionary, initial, final, expresion, subsets,alphabet):
```
Recibe la lista de subconjuntos de FDA, lista de estados, la expresión regular a evaluar y el alfabeto. Regresa True si llego a un nodo de aceptación de lo contrario regresa un valor False.
### graph
script encargado de graficar el AFN y AFD.
### graphDirect
script encargado de graficar el AFD creado de manera directa.
### AFD
script que tiene la clase leaf, esta clase se utiliza para representar las hojas de un árbol con la expresión ingresada. Y tiene la función de validar que un carácter sea un carácter válido.
#### Funciones
```sh
def validChar(char):
```
Esta función recibe un carácter y regresa un valor booleano. En caso de que el carácter no sea un operador devolverá un True, sino devolverá un False.
#### clase
class leaf
Representa cada hoja de un árbol sintactico
Tiene los atributos:
* typeLeaf: identifica si la hoja es un operador, carácter o epsilon
* label: guarda su etiqueta en caso de ser tipo carácter o epsilon
* primerapos: primera pos de la hoja
* ultimapos: ultima pos de la hoja
* pos: pos de la hoja:

Tiene las funciones:
* setX: establece el valor de un atributo según el valor que se le paso
* getX: regresa el valor de cada atributo.
* toString: regresa un string con la información de la hoja

### builder
Script encargado de crear el árbol sintáctico y el AFD.
#### Funciones
```sh
def buildAFD(expresion):
```
Recibe una expresión para devolver el AFD.

## Pruebas
En la carpeta de "Imagenes de pruebas" se encuentran todas las imagenes

## Anexos
* Link a vídeo de Youtube de pruebas: https://youtu.be/uWOR17EG8Ww
 