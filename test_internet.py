import http.client
import urllib.request
server = "openapi.naver.com"
client_id = "Y1ISEIMTWXqCgWUOuLsD"
client_secret = "rTt8fYC9LA"

def FindKeyword():
    global client_id, client_secret

    conn = http.client.HTTPSConnection(server)
    Keyword = str(input("Keyword : "))
    encText = urllib.parse.quote(Keyword)
    conn.request("GET", "/v1/search/movie.xml?dispaly=10&start=1&query=" + encText,
                 None, {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    req = conn.getresponse()
    response_body = req.read()
    data = str(response_body.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(data)

    itemElements = tree.getiterator("item")  # return list type

    for item in itemElements:
        title = item.find("title").text

        print("=========================================")
        print("title : ", title)
        print("=========================================")

FindKeyword()