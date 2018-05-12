from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = int(0.02126 * r + 0.7152 *g + 0.0722*b)

    unit = (256.0+1)/length
    return (ascii_char[int(gray/unit)])


im = Image.open("test.jpg")
w,h = im.size
print(w,h)
im = im.resize((w,h),Image.NEAREST)
txt = ""

for i in range(int(w/100)):
    for j in range(int(h/100)):
        txt += get_char(*im.getpixel((j,i)))
    txt += "\n"
print(txt)
with open("OUTPUT.jpg","w") as f:
    f.write(txt)
