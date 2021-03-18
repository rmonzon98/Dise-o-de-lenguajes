from DirectAFD.AFD import *

def buildAFD(expresion): 
    alphabet = [] 
    for i in expresion:
        if validChar(i):
            if not i in ["#","ε"]:
                if not i in alphabet:
                    alphabet.append(i) 
    tree = []
    auxiliarTree = []
    cont = 1
    for i in expresion:
        if validChar(i):
            temp = leaf(i,cont)
            tree.append(temp)
            auxiliarTree.append(temp)
            cont = cont + 1 
        else:
            if i == "_":
                temp = leaf(i)
                second = tree.pop()
                first = tree.pop()
                temp.setAnulable(True if (first.getAnulable() and second.getAnulable()) else False)
                #getPrimeraPos
                primera = sorted(first.getPrimeraPos())
                if first.getAnulable():
                    primera = sorted(primera + second.getPrimeraPos())
                temp.setPrimeraPos(primera)
                #getUltimaPos
                ultima = sorted(second.getUltimaPos())
                if second.getAnulable():
                    ultima = sorted(ultima + first.getUltimaPos())
                #Se guardan en los arrays
                temp.setUltimaPos(ultima)
                tree.append(temp)
                auxiliarTree.append(temp)
            if i == "|":
                temp = leaf(i)
                second = tree.pop()
                first = tree.pop()
                temp.setAnulable(True if (first.getAnulable() or second.getAnulable()) else False)
                primera = first.getPrimeraPos()
                for i in second.getPrimeraPos():
                        primera.append(i)
                temp.setPrimeraPos(primera)
                primera = first.getUltimaPos()
                for i in second.getUltimaPos():
                    primera.append(i)
                temp.setUltimaPos(primera)
                tree.append(temp)
                auxiliarTree.append(temp)
            if i == "*":
                temp = leaf(i)
                first = tree.pop()
                temp.setAnulable(True)
                temp.setPrimeraPos(first.getPrimeraPos())
                temp.setUltimaPos(first.getUltimaPos())
                tree.append(temp)
                auxiliarTree.append(temp)

    cont = cont
    siguientepos = {}
    for i in range(1,cont):
        siguientepos.update({i:[]})
    for i in auxiliarTree:
        if i.getLabel() == "*":
            for j in i.getUltimaPos():
                values = siguientepos[j]
                values = values+i.getPrimeraPos()
                values = sorted(values)
                siguientepos.update({j:values})
        if i.getLabel() == "_":
            index = auxiliarTree.index(i)
            c1 = auxiliarTree[index-2]
            c2 = auxiliarTree[index-1]
            for j in c1.getUltimaPos():
                values = siguientepos[j]
                values = values + c2.getPrimeraPos()
                values = sorted(values)
                siguientepos.update({j:values})

    Dstates = []
    labelsDstates = []
    Dstates.append(auxiliarTree[len(auxiliarTree)-1].getPrimeraPos())  
    for i in Dstates:
        for l in alphabet:
            correctLabel = []
            for j in i:
                for k in auxiliarTree:                
                    if k.getType() == "c":
                        if k.getPos() == j and k.getLabel() == l:
                            correctLabel.append(j)
            if len(correctLabel) > 0:
                values = []
                for j in correctLabel:
                    values = values + siguientepos[j]
                    values = sorted(list(dict.fromkeys(values)))
                if not values in Dstates:
                    Dstates.append(sorted(values))
                    labelsDstates.append((Dstates.index(i),l,Dstates.index(values)))
                else:
                    labelsDstates.append((Dstates.index(i),l,Dstates.index(values)))
    acceptance = []
    for i in Dstates:
        if cont-1 in i:
            acceptance.append(True)
        else:
            acceptance.append(False)
    return labelsDstates, acceptance