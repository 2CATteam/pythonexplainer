import Levenshtein

def Lowes(code):
    KeywordsPython = ["False", "class", "finally", "is", "return", "None", "continue", "for", "lambda", "try", "True", "def", "from", "nonlocal", "while", "and", "del", "global", "not", "with", "as", "elif", "if", "or", "yield", "assert", "else", "import", "pass", "break", "except", "in", "raise"]
    KeywordsJava = ["abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while"]
    KeywordsJS = ["abstract", "arguments", "await", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue", "debugger", "default", "delete", "do", "double", "else", "enum", "eval", "export", "extends", "false", "final", "finally", "float", "for", "function", "goto", "if", "implements", "import", "in", "instanceof", "int", "interface", "let", "long", "native", "new", "null", "package", "private", "protected", "public", "return", "short", "static", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "true", "try", "typeof", "var", "void", "volatile", "while", "with", "yield"]
    KeywordsC = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

    InJava = [KeywordsJava[i] for i in range(len(KeywordsJava)) if KeywordsJava[i] not in KeywordsPython]
    InJS = [KeywordsJS[i] for i in range(len(KeywordsJS)) if KeywordsJS[i] not in KeywordsPython]
    InC = [KeywordsC[i] for i in range(len(KeywordsC)) if KeywordsC[i] not in KeywordsPython]
    NotInPython = list(set(InJava) | set(InJS) | set(InC))

    FinalDict = {}

    #code = '''a = [x for x in range(8)]
#b = []
#for i in range(len(a)):
    #for j in a[~i]:
        #if (a[i] % j != 0):
            #b.append(a[i])'''

    code.replace("=", " = ")
    code.replace("(", " ( ")
    code.replace(")", " ) ")

    lines = code.splitlines()

    for i in range(len(code.splitlines())):
        split = lines[i].split()
        for x in range(len(split)):
            if split[x] in NotInPython:
                errorStr = ("The word " + \
                            split[x] + " on line " + \
                            str(i) + " isn't a keyword in Python. Maybe try something else.")
                FinalDict[i] = errorStr

    Variables = {}
    varLoc = {}
    varLine = 0
    for i in code.splitlines():
        split = i.split()
        for j in range(len(split)):
            if i[j] == "=":
                try:
                    Variables[split[j-1]] += 1
                except KeyError:
                    Variables[split[j-1]] = 1
                    varLoc[split[j-1]] = i
                    varLine = i

    for i in Variables.keys():
        if Variables[i] == 1:
            for j in Variables.values():
                if Levenshtein.distance(i,j) <= 1 and Levenshtein.distance(i,j) > 0:
                    finalStrError = ("\n" + i + " is incredibly similar to another variable in your code and you've only set it once. Perhaps it's a typo?")
                    FinalDict[varLine] = finalStrError



    return FinalDict
