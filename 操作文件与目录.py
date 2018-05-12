import json
import pickle

d = dict(name="Bob",age = 20,score = 88)
print(json.dumps(d))

with open("dumm.txt","wb") as z:
    pickle.dump(d,file=z)

zz=open("dumm.txt","rb")
d = pickle.load(zz)
zz.close()
print(d)

try:
    zz = open("dumm.txt", "rb")
    d = pickle.load(zz)
    print(d)
finally:
    zz.close()

with open("json.js","w") as o:
    json.dump(d,o)

# loads直接反序列化json
json_str =  '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

#读json
with open("dump2.txt","r") as m:
    json.load(m)


