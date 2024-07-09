import os, sys
os.system("git pull")
try:
    import("UAGEN")
except Exception as e:
    exit(str(e)) 
