import json

j1 = {"name":"홍길동", "birth":"0525", "age": 30}
d1 = json.dumps(j1)
print(json.loads(d1))
j1 = {"name":"홍길동", "birth":"0525", "age": 20}
d1 = json.dumps(j1)
print(json.loads(d1))

