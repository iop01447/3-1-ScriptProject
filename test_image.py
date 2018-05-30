from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk

g_Tk = Tk()
g_Tk.geometry("900x600+100+100") # width height x y

url="http://imgmovie.naver.com/mdi/mit110/1531/153129_P01_105507.jpg"
with urllib.request.urlopen(url) as u:
    raw_data=u.read()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = Label(g_Tk,image=photo)     #height=y,width=x
label.pack()

g_Tk.mainloop()
