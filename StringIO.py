from io import StringIO,BytesIO

f = StringIO()
f.write("Hello")
print(f.getvalue())

m = StringIO("Hello\nHI")
while True:
    s =m.readline()
    if s == "":
        break
    print(s.strip())

# 操作二进制数据
b = BytesIO()
b.write("中文".encode("utf-8"))



d= StringIO("WORLD")
print(d.tell())
b.readlines()
print(d.tell())


# 被覆盖
ff = BytesIO("中文".encode("utf-8"))
ff.write(b'123')
ss = ff.getvalue().decode("utf-8")
print(ss)