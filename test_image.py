from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk

# g_Tk = Tk()
# g_Tk.geometry("900x600+100+100") # width height x y

def imageRead():
    imageUrl="http://imgmovie.naver.com/mdi/mit110/1531/153129_P01_105507.jpg"
    with urllib.request.urlopen(imageUrl) as u:
        raw_data = u.read()

    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)

    return photo

# imageLabel = Label(g_Tk,image=photo)     # image size: 110x154
# imageLabel.place(x=750, y=20)
# imageLabel = Label(g_Tk,image=photo)     # image size: 110x154
# imageLabel.place(x=750, y=224)
# imageLabel = Label(g_Tk,image=photo)     # image size: 110x154
# imageLabel.place(x=750, y=428)

# g_Tk.mainloop()
