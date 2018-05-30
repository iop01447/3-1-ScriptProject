# python 3.4

from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox

class Password(simpledialog.Dialog):
    def body(self, master):
        self.title("비밀번호 변경")
        Label(master, text='비밀번호 변경\n로그인된 사용자의 비밀번호를 변경합니다.').grid(row=0, columnspan=2)

        Label(master, text='이전 비밀번호').grid(row=1, sticky=W)
        Label(master, text='새 비밀번호').grid(row=2, sticky=W)
        Label(master, text='새 비밀번호 확인').grid(row=3, sticky=W)

        self.oldpw = Entry(master, width=16, show='●')
        self.newpw1 = Entry(master, width=16, show='●')
        self.newpw2 = Entry(master, width=16, show='●')
        self.oldpw.grid(row=1, column=1, sticky=W)
        self.newpw1.grid(row=2, column=1, sticky=W)
        self.newpw2.grid(row=3, column=1, sticky=W)
        return self.oldpw

    def apply(self):
        if not self.newpw1.get() == self.newpw2.get():
            tkinter.messagebox.showerror('오류', '입력한 비밀번호가 일치하지 않습니다')


root = Tk()
dialog = Password(root)
