from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import test_internet
g_Tk = Tk()
g_Tk.geometry("900x600+100+100") # width height x y
# 400 400 100   // 300
#               // 300
DataList = []

myFont = 'KoPub돋움체 Medium'
#
# # 이런 식으로 쓰면 되지 않을까 .. #
# inputGenre = 5
# inputCountry = 'KR'
# itemElements = test_internet.FindKeyword(inputGenre, inputCountry)
# for item in itemElements:
#     title = item.find("title").text
#     link = item.find("link").text
#     print("=========================================")
#     print("title: ", title)
#     print("link: ", link)
#     print("=========================================")
# # 이런 식으로 쓰면 되지 않을까 .. #

# 영화 검색 앱
def InitTopText():
    TempFont = font.Font(g_Tk, size=20, family=myFont)
    MainText = Label(g_Tk, font=TempFont, text="영화 검색 APP", relief='flat', borderwidth=4)
    MainText.grid(row=0,column=0,columnspan=4)

# 검색 창
def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, family=myFont)
    InputLabel = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='flat')
    InputLabel.grid(row=1,column=0,columnspan=3)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, family=myFont)
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction,
                          background='#00C73C', relief='flat')
    SearchButton.grid(row=1, column=3)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')

def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()
    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[3].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():  #
                        pass
                    else:
                        continue

                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass  #
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "시설명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "주소: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "전화번호: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")

def InitSearchListBox():
    global SearchListBox

    TempFont = font.Font(g_Tk, size=15, family=myFont)
    SearchListBox = ttk.Combobox(g_Tk)

    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화시설")
    SearchListBox.grid(row=2,column=0,columnspan=2)

def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.grid(row=3,column=3)

    TempFont = font.Font(g_Tk, size=10, family=myFont)
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='groove',
                      yscrollcommand=RenderTextScrollbar.set)
    RenderText.grid(row=3,column=0,rowspan=6,columnspan=4)
    RenderTextScrollbar.config(command=RenderText.yview)

    RenderText.configure(state='disabled')

#…
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
g_Tk.mainloop()
