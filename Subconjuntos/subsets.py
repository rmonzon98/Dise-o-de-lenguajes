def eCerradura(dictionary, finalNode, node):
    #print("\nEntra ",states," con ",secondElement)
    #Si la ecerradura se hace al primer nodo se ejecuta esta parte
    if not finalNode == node:
        falseStates = []
        if type(node) == list:
            for i in node:
                falseStates.append(i)
        else:
            falseStates.append(node)
        for i in falseStates:
            if not i == finalNode:
                subDict = dictionary[i]
                key = list(subDict.keys())
                if key[0] == "ε":
                    values = list(subDict.values())[0]
                    if type(values) == list:
                        for k in values:
                            if k not in falseStates:
                                falseStates.append(k)
                    else:
                        if values not in falseStates:
                            falseStates.append(values)
        return falseStates

def move(dictionary,finalNode,states,label):
    result=[]
    for i in states:
        if not i == finalNode:
            subDict = dictionary[i]
            key = list(subDict.keys())[0]
            if key == label:
                values = list(subDict.values())[0]
                if type(values) == list:
                    for k in values:
                        result.append(k)
                else:
                    result.append(values)
    temp = []
    for i in result:
        temp.append(eCerradura(dictionary,finalNode,i))
    for i in temp:
        if type(i) == list:
            for j in i:
                result.append(j)
        elif i == None:
            pass
        else:
            result.append(i)
    return list(set(result))
  
def subsetsBuilder(alphabet,states,dictionary,initial,final):

    Dstates = []
    falseStates = states
    Dstates.append(sorted(eCerradura(dictionary,final,[initial])))
    for i in Dstates[0]:
        temp = falseStates.index(i)
        falseStates.pop(temp)

    for i in Dstates:
        if len(falseStates)>0:
            for j in alphabet:
                newList = (sorted(move(dictionary,final,i,j)))
                if newList not in Dstates and not newList == []:
                    Dstates.append(newList)
                    if type(newList) == list:                    
                        for k in newList:
                            if k in falseStates:
                                temp = falseStates.index(k)
                                falseStates.pop(temp)
                    else:
                        if newList in falseStates:
                            temp = falseStates.index(newList)
                            falseStates.pop(temp)
    transitions = []
    nameStates = []
    for i in range(0,len(Dstates)):
        nameStates.append(i)
    for i in Dstates:
        for j in alphabet:
            temp = sorted(move(dictionary,final,i,j))
            if not temp == []:
                transitions.append((Dstates.index(i),Dstates.index(temp),j))
    return transitions, nameStates