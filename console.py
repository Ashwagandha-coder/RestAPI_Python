import requests

res = requests.get("127.0.0.1:3000/api/main")
print(res.json())