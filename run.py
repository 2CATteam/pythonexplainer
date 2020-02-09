import subprocess

def testRun(code, input):
    f = open('/var/www/peter/output.py', 'w')
    traceList = code.split('\n')
    for i in range(len(traceList)):
        f.write(traceList[i])
        f.write('\n')
    f.close()
    res = runProg('/var/www/peter/output.py', input).decode('utf-8')
    print(res)
    return { "out": res }

def runProg(code, input):
    try:
        proc = subprocess.run(["python3", code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=input.encode('utf-8'))
        return proc.stdout
    except:
        return b''
