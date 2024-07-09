import os, sys
os.system("git pull")
try:
    __import__("UAGEN")
except Exception as e:
    exit(str(e)) 
