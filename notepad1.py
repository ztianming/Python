'''
 !/usr/bin/env python
 Function： notepad
 Compiler：PyCharm 
 Developer：Zong Zhaopeng
 Date:  2018/10/26 21:03
 Encoding: utf-8
 Contact: 1003160664@qq.com
 Version: 1.0
 References:https://www.cnblogs.com/Kobe10/p/5712233.html
'''
from tkinter import *
# 弹出窗口
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
# form email.policy import default
from setuptools.sandbox import save_argv

# 文件名
fileName = ''


###### 7.about
# 将函数与about进行了绑定
def author():
    showinfo('作者信息', '本软件由Alex完成！')


def about():
    showinfo('版权信息.copyright', '本软件归属于Alex')


# 打开文件函数
def openFile():
    #
    global fileName;
    # 提供一个打开的方式   默认的扩展名.txt
    fileName = askopenfilename(defaultextension='.txt')
    # 如果打开的文件是空的，设置为空
    if fileName == '':
        fileName = None
    # 如果不为空，就加载到title上
    else:
        # 找到实际路径
        root.title(os.path.basename(fileName) + ' - notepad')
        # 如果打开的手编辑器里面有正在编写的内容，就要清空原来的内容
        # 删除从头到尾   第一行的第0列
        textPad.delete(1.0, END)
        # 打开文件
        f = open(fileName, 'r')
        # 插入内容，从1.0处插入
        textPad.insert(1.0, f.read())
        # 关闭文件
        f.close()


# 新建文件
def newFile():
    global fileName
    root.title('未命名文件 - notepad')
    fileName = None
    textPad.delete(1.0, END)
    print("ctril + n")


######保存和另存为
# 保存时保存在到一个默认的地址
# 另存是需要弹出一个对话框去存储你要存取的地址
######
# 封装保存
def save():
    global fileName
    # 如果文件存在的话就是直接保存在默认的路径
    # 如果不存在的话就是另存为一个新的文件
    try:
        f = open(fileName, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()


# 文件的另存为保存
def saveas():
    # 初始化文件名和后缀名
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global fileName
    fileName = f
    # 打开文件写文件
    fh = open(f, 'w')
    # 写入的内容得到
    msg = textPad.get(1.0, END)
    # 写入内容到文件
    fh.write(msg)
    fh.close()
    # 存储文件
    root.title(os.path.basename(f) + ' - notepad')


# 复制粘贴撤销重做
def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


# 查找和全选
# 全选
def selectAll():
    textPad.tag_add('sel', '1.0', END)


# 查找
# 这里要用到自定义窗体，弹出窗体toplevel,查看前面代码
def search():
    # 创建弹出窗口进行查找
    topsearch = Toplevel(root)
    topsearch.geometry('250x50+200+250')
    label1 = Label(topsearch, text='Find')
    label1.grid(row=0, column=0, padx=5)  # 显示
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找')
    button1.grid(row=0, column=2)

    # 匹配输入的值并且在里面查询

root = Tk()
root.title('notepad')
# 构建一个矩形窗体    初始化的显示位置  100  100
root.geometry('800x500+100+100')

######  2.create Menu
menuBar = Menu(root)
root.config(menu_=menuBar)

fileMenu = Menu(menuBar)
# accelerator 快捷键，  new  点击事件函数
fileMenu.add_command(label='新建', accelerator='Ctrl + N', command=newFile)
fileMenu.add_command(label='打开', accelerator='Ctrl + O', command=openFile)
fileMenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
fileMenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
menuBar.add_cascade(label='文件', menu=fileMenu)

# 按键绑定事件
root.bind_all("<Control-n>", lambda event: newFile())
root.bind_all("<Control-o>", lambda event: openFile())
root.bind_all("<Control-s>", lambda event: save())
root.bind_all("<Control-Shift-KeyPress-S>", lambda event: saveas())
root.bind_all("<Control-f>", lambda event: search())

###### 3.编辑菜单
editMenu = Menu(menuBar)
editMenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editMenu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
# 分隔符
editMenu.add_separator()
editMenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editMenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editMenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
# 分隔符
editMenu.add_separator()
editMenu.add_command(label='查找', accelerator='Ctrl + F', command=search)
editMenu.add_command(label='全选', accelerator='Ctrl + A', command=selectAll)
menuBar.add_cascade(label='编辑', menu=editMenu)

aboutMenu = Menu(menuBar)
aboutMenu.add_command(label='作者', command=author)
aboutMenu.add_command(label='版权', command=about)
menuBar.add_cascade(label='关于', menu=aboutMenu)

###### 4. 实现toolBar
toolBar = Frame(root, height=25, bg='light sea green')
shortButton = Button(toolBar, text='打开', command=openFile)
# 流式布局：靠左
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolBar, text='保存', command=save)
shortButton.pack(side=LEFT)
# 全部填充海蓝色
toolBar.pack(expand=NO, fill=X)

###### 5. status bar
# 对齐方式  W  左对齐
status = Label(root, text='Ln20', relief=SUNKEN, anchor=W)
# 显示status状态栏 x轴填充
status.pack(side=BOTTOM, fill=X)

###### 6. linenumber&text
lnlabel = Label(root, width=2, bg='antique white')
# 将Y轴填充满
lnlabel.pack(side=LEFT, fill=Y)

# 重做
textPad = Text(root, undo=True)
# 允许进行扩展 ,填充X，Y轴
textPad.pack(expand=YES, fill=BOTH)

# 右侧的移动下滑栏
scroll = Scrollbar(textPad)
# 在Y轴显示   yscrollcommand
textPad.config(yscrollcommand=scroll.set)
# 这是为了让编辑内容和下拉栏同时移动
scroll.config(command=textPad.yview)
# 显示
scroll.pack(side=RIGHT, fill=Y)

# 进入死循环  让窗口一直显示
root.mainloop()

