#library of the simple information able to be explained

def explainVar(input):
    analyte = input.split()
    return "This creates a variable, {}, which holds data.".format(analyte[0])
def explainFor(input):
    return "A for loop will repeat the block of code under it a fixed number of times, established by the iterator"
def explainWhile(input):
    return "A while loop will repeat the block of code under it while the statement is True"
def explainDef(input):
    return "A def will create a function, a block of code that will only run when called"
def explainPrint(input):
    return 'A print statement will output what is in the parentheses.'



explainLibrary = {
    '=': explainVar,
    'for': explainFor,
    'while': explainWhile,
    'def': explainDef,
    'print': explainPrint
}

