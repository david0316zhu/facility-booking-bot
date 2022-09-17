import requests


res = requests.get(url="https://fbs.intranet.smu.edu.sg/")
print(res.content)