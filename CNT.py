import os, sys
try:
    __import__("solo").logo()
except Exception as e:
    exit(str(e))
