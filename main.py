from logging import root
import tkinter

def updata_pp():
    print("正在下载")

top = tkinter.Tk()
top.geometry('500x300')
top.title("片片更新器 BY-Flower")
down = tkinter.Button(top, text = "点我更新", command = updata_pp)

down.pack()
top.mainloop()
