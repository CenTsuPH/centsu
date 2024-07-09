import os, sys
os.system("git pull")
try:
    __import__("UAGEN.cpython-311.so")
except Exception as e:
    exit(str(e)) 
