from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import test_internet
g_Tk = Tk()
#g_Tk.geometry("900x600+100+100") # width height x y
# 400 400 100   // 300
#               // 300
DataList = []

myFont = 'KoPub돋움체 Medium'

keyword = ''
inputGenre = 0
inputCountry = ''

# 타이틀
def InitTopText():
    TempFont = font.Font(g_Tk, size=18, family=myFont)
    MainText = Label(g_Tk, font=TempFont, text="영화 검색 APP",
                     relief='flat')
    MainText.grid(row=0,column=0,columnspan=4)

# 검색 입력창
def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, family=myFont)
    InputLabel = Entry(g_Tk, font=TempFont, relief='flat', width=37, borderwidth=8)
    InputLabel.grid(row=1,column=0,columnspan=3)

# 검색 버튼
def InitSearchButton():
    TempFont = font.Font(g_Tk, size=15, family=myFont)
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction,
                          background='#00C73C',relief='flat', fg='white', width=5)
    SearchButton.grid(row=1,column=3)

#검색 버튼 누른 후 동작
def SearchButtonAction():
    global GenreComboBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    RederListBox.delete(0, END)

    SearchKeyword()

#    print(GenreStr.get())

    RenderText.configure(state='disabled')

# 검색
def SearchKeyword():
    global keyword, GenreStr, GenreDic
    global CountryStr, CountryDic
    itemCnt = 1

    keyword = str(InputLabel.get())
    itemElements = test_internet.FindKeyword(keyword, GenreDic[GenreStr.get()], CountryDic[CountryStr.get()])
    for item in itemElements:
        if item.find("title") != None:
            title = item.find("title").text
            #RenderText.insert(INSERT, title)
            #RenderText.insert(INSERT, "\n")
            RederListBox.insert(itemCnt, title)
            itemCnt += 1
            print(title)

# 장르 ↕
def InitGenreComboBox():
    global GenreComboBox
    global GenreStr
    global GenreDic

    TempFont = font.Font(g_Tk, size=15, family=myFont)
    GenreStr = StringVar()
    GenreComboBox = ttk.Combobox(g_Tk, font=TempFont, textvariable=GenreStr, state='readonly')
    GenreComboBox['values']=('장르','드라마', '판타지', '서부', '공포', '로맨스',
                             '모험', '스릴러', '느와르', '컬트', '다큐멘터리',
                             '코미디', '가족', '미스터리', '전쟁',
                             '애니메이션', '범죄', '뮤지털', 'SF',
                             '액션', '무협', '에로', '서스펜스', '서사',
                             '블랙코미디', '실험', '영화카툰', '영화음악',
                             '영화패러디포스터')

    GenreDic = {}
    for i, value in enumerate(GenreComboBox['values']):
        GenreDic[value] = i

    GenreComboBox.grid(row=2,column=0,columnspan=2)
    GenreComboBox.current(0)


# 국가코드 ↕
def InitCountryComboBox():
    global CountryComboBox
    global CountryStr
    global CountryDic

    TempFont = font.Font(g_Tk, size=15, family=myFont)
    CountryStr = StringVar()
    CountryComboBox = ttk.Combobox(g_Tk, font=TempFont, textvariable=CountryStr, state='readonly')
    CountryComboBox['values']=('국가','한국', '일본', '미국', '홍콩', '영국',
                             '프랑스', '기타')

    CountryDic = {'국가':'','한국':'KR', '일본':'JP', '미국':'US',
                  '홍콩':'HK', '영국':'GB','프랑스':'FR', '기타':'ETC'}

    CountryComboBox.grid(row=2,column=2,columnspan=2)
    CountryComboBox.current(0)

# 리스트 창
def InitRenderText():
    global RenderText

    RenderTextScrollbar=Scrollbar(g_Tk)
    RenderTextScrollbar.grid(row=3,column=3)

    TempFont = font.Font(g_Tk, size=10, family=myFont)
    RenderText = Text(g_Tk,font=TempFont, width=70, #height=27 borderwidth=12,
                      relief='flat',
                      yscrollcommand=RenderTextScrollbar.set)
    RenderText.grid(row=3,column=4,rowspan=6, columnspan=4)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderText.configure(state='disabled')

def InitRenderListBox():
    global RederListBox

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.grid(row=3, column=3)

    TempFont = font.Font(g_Tk, size=10, family=myFont)
    RederListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                           width=70, height=22, #borderwidth=12,
                      relief='flat',
                      yscrollcommand=RenderTextScrollbar.set)
    RederListBox.grid(row=3, column=0, rowspan=6, columnspan=4)
    RenderTextScrollbar.config(command=RederListBox.yview)
    #RederListBox.configure(state='disabled')

#…
InitTopText()
InitInputLabel()
InitSearchButton()
InitGenreComboBox()
InitCountryComboBox()
InitRenderText()
InitRenderListBox()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
g_Tk.mainloop()
