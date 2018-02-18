import os
import re

files = [file for file in os.listdir(".") if (file.lower().endswith('.eml'))]
files.sort(key=os.path.getmtime)

for file in sorted(files, key=os.path.getmtime):
    with open(file) as myfile:
        data = myfile.readlines()
        print(data)
