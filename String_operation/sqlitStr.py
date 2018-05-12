val = "a,b,  guido"
print(type(val))

a = val.split(",")
print(a)
pieces = [x.strip() for x in val.split(",")]
print(pieces)
_ = "::".join(pieces)
print(_)