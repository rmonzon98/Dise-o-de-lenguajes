from  PostfixGen.infixtopostfix import *
from AFN.builder import ThompsonAlgorithm
from Graph.graph import graph
from Graph.graphDirect import graphDirect
from Subconjuntos.subsets import eCerradura, subsetsBuilder
from Simulaciones.simulaciones import simulationNFA, simulationFDA
from DirectAFD.builder import buildAFD

if __name__ == "__main__":
    option = input("Desea:   \n1.Crear AFN y luego AFD   2.AFD directo\n>>")
    if option == "1":
        expresion = input ("\nIngrese la expresión, por favor: ")
        if firstExpresion(expresion):
            nuevaexpresion = computableExpresion(expresion)
            print("Expresion ingresada: ",expresion)
            print("Expresion entendible para computadora: ",nuevaexpresion)
            postfixexp = infixaPostfix(nuevaexpresion)
            print("Expresion en Postfix:",postfixexp)
            result = ThompsonAlgorithm(postfixexp)
            nfaDict = result.getDict()
            #print("Dict con el NFA resultante:\n",nfaDict)
            prueba = graph(postfixexp,result)
            transitions = prueba.createTransitions()
            prueba.graphic(transitions,"Thompson")
            s0 = result.getInitial()
            sf = result.getFinal()
            states = prueba.getStates()
            #print("Nodo inicial: ",s0,"\nNodo de aceptación/final: ",sf)
            alphabet = getAlphabet(expresion)
            dictTrans = result.getDict()
            subsets, numberSubsets, subsetsInfo, finalNodeInside = subsetsBuilder(alphabet, states, dictTrans, s0, sf)
            prueba.graphSubsets(subsets,numberSubsets,"Subconjuntos",finalNodeInside) 
            simulation = True
            while simulation:
                segundaExpresion = input ("\n-------------Nueva Simulación-------------\nIngrese la expresión a evaluar, por favor:\n>> ")
                resultSimNFA = simulationNFA(dictTrans, s0, sf, segundaExpresion, subsetsInfo, alphabet)
                print("Resultado de la simulación AFN: ", resultSimNFA)
                resultSimFDA = simulationFDA(subsets, numberSubsets, segundaExpresion, alphabet)
                print("Resultado de la simulación AFD: ", resultSimNFA)
                option = input ("¿Desea realizar otra simulacion?\n1.Sí   2.No\n>> ")
                if option == "2":
                    simulation = False
        else: 
            print("La expresion tiene errores")
    elif option == "2":
        expresion = input ("\nIngrese la expresión, por favor: ")
        if firstExpresion(expresion):
            print("----------CREACIÓN AFD DIRECTO----------")
            expresion = convertOperators(expresion)+"#"
            nuevaExpresionComputable = computableExpresion(expresion)
            postfixexpNueva = infixaPostfix(nuevaExpresionComputable)
            labelsDstates, acceptance = buildAFD(postfixexpNueva)
            prueba = graphDirect(acceptance, labelsDstates, "AFD directo")
        else:
            print("Expresion equivocada")
            nuevaexpresion = computableExpresion(expresion)
            postfixexp = infixaPostfix(nuevaexpresion)
    else:
        print("Opcion equivocada")