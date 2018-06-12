# -*- coding:utf-8 -*-

import tkinter
import time
import datetime

def gettime():
          s = str(datetime.datetime.now())+'\n'
          txt.insert(tkinter.END,s)

          root.after(1000,gettime)

root = tkinter.Tk()
root.geometry('320x240')
txt = tkinter.Text(root)
txt.pack()
gettime()
root.mainloop()
#第二次修改，将上一次注释删除
#第三次修改
