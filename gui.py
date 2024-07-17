#From https://qiita.com/MatsuM2_1007/items/77d72b96067688f8dafc

import tkinter
import sys
from time import sleep
import webbrowser

root = tkinter.Tk()
root.title("Quick Bookmark")
root.geometry("400x550")
root.resizable(0, 0)

def info_po(button1):
    sleep(0.5)
    webbrowser.open("https://www.google.co.jp/")

def info_po2(button2):
    sleep(0.5)
    webbrowser.open("https://www.youtube.com/")

def info_po3(button3):
    sleep(0.5)
    webbrowser.open("https://qiita.com/")

def info_po4(button4):
    sleep(0.5)
    webbrowser.open("https://twitter.com/")

def info_po5(button5):
    sleep(0.5)
    webbrowser.open("https://www.yahoo.co.jp/")

def exit(button6):
    sys.exit()
    root.destroy()

label = tkinter.Label(text="                                          ブックマーク                                          ", background='#7fffd4', font=("MSゴシック", "45", "bold"), foreground='#000000')
label.pack()

button1 = tkinter.Button(text='Googleを開く', width=1000)
button1.pack()
button1.bind("<Button-1>",info_po)

button2 = tkinter.Button(text='YouTubeを開く', width=1000)
button2.pack()
button2.bind("<Button-1>",info_po2)

button3 = tkinter.Button(text='Quiitaを開く', width=1000, foreground="#00ff00")
button3.pack()
button3.bind("<Button-1>",info_po3)

button4 = tkinter.Button(text='Twitterを開く', width=1000, foreground="#00ffff")
button4.pack()
button4.bind("<Button-1>",info_po4)

button5 = tkinter.Button(text='YahooJapanを開く', width=1000)
button5.pack()
button5.bind("<Button-1>",info_po5)

button6 = tkinter.Button(text='終了', width=1000)
button6.pack()
button6.bind("<Button-1>",exit)

root.mainloop()
