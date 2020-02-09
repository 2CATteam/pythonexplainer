import subprocess

def testRun(code, input):
    f = open('output.py', 'w')
    traceList = code.split('\n')
    for i in range(len(traceList)):
        f.write(traceList[i])
        f.write('\n')
    f.close()
    res = runProg('output.py', input).decode('utf-8')
    if (res==None):
        print("Haha")
    print(res)
    return

def runProg(code, input):
    try:
        proc = subprocess.run(["python", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=input.encode('utf-8'), check=True)
        return proc.stdout
    except:
        return None


test = '''a = 1
b = 2
c = a + b
print(c)
print(input())'''

testRun(test, 'hi')