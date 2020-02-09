import library

def readCode( text ):
    listOfCode = text.split('\n')
    output = {}
    for i in range(len(listOfCode)):
            for key in library.explainLibrary:
                    if key in listOfCode[i]:
                            #print('{} contains the key: {}'. format(listOfCode[i], key))
                            explainOut = callExplainFunc(library.explainLibrary[key], listOfCode[i])
                            output[i] = explainOut
    return output

def callExplainFunc(name, input):
    return name(input)

