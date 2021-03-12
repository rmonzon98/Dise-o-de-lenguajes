from  PostfixGen.infixtopostfix import computableExpresion, infixaPostfix, getAlphabet, expresionParaArbol
from Thompson.builder import ThompsonAlgorithm
from Graph.graph import graph
from Subconjuntos.subsets import eCerradura, subsetsBuilder
from Simulaciones.simulaciones import simulationNFA, simulationFDA

if __name__ == "__main__":
 
    expresion = input ("Ingrese la expresión, por favor: ")
    nuevaexpresion = computableExpresion(expresion)
    print("Expresion ingresada\n",expresion)
    print("Expresion entendible para computadora\n",nuevaexpresion)
    postfixexp = infixaPostfix(nuevaexpresion)
    directExp = expresionParaArbol(nuevaexpresion)
    print("Expresion en Postfix\n",postfixexp)
    result = ThompsonAlgorithm(postfixexp)
    nfaDict = result.getDict()
    print("Dict con el NFA resultante\n",nfaDict)
    prueba = graph(postfixexp,result)
    transitions = prueba.createTransitions()
    prueba.graphic(transitions,"Thompson")
    s0 = result.getInitial()
    sf = result.getFinal()
    states = prueba.getStates()
    print("Nodo inicial: ",s0,"\nNodo final: ",sf)
    alphabet = getAlphabet(expresion)
    dictTrans = result.getDict()
    subsets, numberSubsets, subsetsInfo = subsetsBuilder(alphabet, states, dictTrans, s0, sf)
    prueba.graphSubsets(subsets,numberSubsets,"Subconjuntos") 
    segundaExpresion = input ("Ingrese la expresión a evaluar, por favor: ")
    resultSimNFA = simulationNFA(dictTrans, s0, sf, segundaExpresion, subsetsInfo)
    print("Resultado de la simulación AFN: ", resultSimNFA)
    resultSimFDA = simulationFDA(subsets, numberSubsets, segundaExpresion)
    print("Resultado de la simulación AFD: ", resultSimNFA)