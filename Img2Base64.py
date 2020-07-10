import base64
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def Img2Base64(filename):
    # 二进制方式打开图文
    f=open(filename, 'rb')
    # 读取文件内容，转换为base64编码
    res = base64.b64encode(f.read())
    f.close()
    s = res.decode()
    print('![](data:image/jpeg;base64,%s)' %s)
    return res
    # print('![](data:image/jpeg;base64,%s)'%res.decode())

def Base642Img(filename, decode):
    imgdata = base64.b64decode(decode)
    file = open(filename, 'wb')
    file.write(imgdata)
    file.close()
    imgdata = mpimg.imread(filename)
    plt.figure("Image")  # 图像窗口名称
    plt.imshow(imgdata)
    plt.axis('on')  # 关掉坐标轴为 off
    plt.title('image')  # 图像题目
    plt.show()
# test
print(Img2Base64("Y:\\f.jpg"))
t = Img2Base64("Y:\\f.jpg")
Base642Img("Y:\\1.jpg", t)