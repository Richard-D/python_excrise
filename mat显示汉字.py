import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams["font.family"] = "SimHei"
plt.plot([3,1,4,5,2])
plt.ylabel("纵轴")
plt.savefig("test",dpi = 600)
plt.show()

a = np.arange(0.0,5.0,0.02)
plt.xlabel("横轴 时间", fontproperties="SimHei",fontsize=20)
plt.ylabel("纵轴 值", fontproperties="SimHei",fontsize = 20)
plt.title(r"正弦波 $y=cos(2\pi x)$",)
plt.plot(a,np.cos(2*np.pi*a),"r--")
plt.annotate(r"$\mu=100$",xy = (2,1), xytext=(3,1.5),
             arrowprops = dict(facecolor="black",shrink=0.1,width = 2))

plt.axis([-1,6,-2,2])
plt.grid(True)
plt.show()

