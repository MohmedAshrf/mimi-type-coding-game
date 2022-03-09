import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
dic={}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dic[ext.lower()] = mt
    print("Debug messages...",ext,mt, file=sys.stderr, flush=True)

for i in range(q):
    fname = input()  # One file name per line.
    print("file name",fname, file=sys.stderr, flush=True)
    lst=fname.split('.')
    if lst[-1]!='' and len(lst)>1 :
        extention=fname.split('.')[-1]
        print("extention",extention, file=sys.stderr, flush=True)
        if extention.lower() in dic.keys():
            print(dic[extention.lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
