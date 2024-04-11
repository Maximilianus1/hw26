import requests
import json
import os
os.chdir(os.getcwd())
x = requests.get('https://jsonplaceholder.org/posts')
y = json.loads(x.text)
for i in range(len(y)):
    os.mkdir(f"file{i+1}")
    with open(f"file{i+1}/file{i+1}.txt","w") as file:
        file.write(str(y[i]))
