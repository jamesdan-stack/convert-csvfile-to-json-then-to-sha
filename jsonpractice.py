import json


info = {
    'name':'james',
    'position':'python developer',
    'age':23,
    'salary': 20
}


data = json.dumps(info)

print(data)