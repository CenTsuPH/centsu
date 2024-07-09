import os, sys
os.system("git pull")
try:
    __import__("SILENTX").menu()
except Exception as e:
    exit(str(e)) 
