'''
 !/usr/bin/env python
 Function： TextEncodingConversion
 Compiler：PyCharm 
 Developer：Zong Zhaopeng
 Date:  2018/10/29 10:49
 Encoding: utf-8
 Contact: 1003160664@qq.com
 Version: 1.0
 References:
'''
import os

in_path = "Z:/test/"
out_path = "Z:/test/"
# 文件后缀：".txt" ".bat"
format = ".txt"
# 初始编码：ANSI、Unicode、Unicode big endian
initialEncode = 'GB18030' #'GB18030'
# 目标编码
destEncode = 'UTF-8'

fileList = [fileName for fileName in os.listdir(in_path) if fileName[-4:] == format]

print("start conversion...")
for fileName in fileList:
    print(fileName)
    with open(in_path + fileName, encoding=initialEncode) as f:
        data = f.read()
    with open(out_path + fileName, 'w', encoding=destEncode) as f:
        f.write(data)

print("conversion finish!")