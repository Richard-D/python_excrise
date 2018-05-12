from PIL import Image
import numpy as np
a = np.array(Image.open("1.jpg"))
print(a.shape,a.dtype)

b = [255,255,255] - a
im = Image.fromarray(b.astype("uint8")) # 还原回图片
im.save("2.jpg")
