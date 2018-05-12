# 读取二进制文件，比如图片、视频等等，使用'rb'
# with open('E:\python\\untitled1/1.jpg',"rb") as f:
#     print(f.read())

# 读取非UTF-8编码的，要传入encoding参数
with open("E:\python\\基础练习（待整理）\gbk.txt","r",encoding="utf-8") as m:
    print(m.read())
