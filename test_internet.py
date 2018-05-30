import http.client
import urllib.request
server = "openapi.naver.com"
client_id = "Y1ISEIMTWXqCgWUOuLsD"
client_secret = "rTt8fYC9LA"

#inputGenre = 0      # 1~28
#inputContry = ""    # 한국 (KR), 일본 (JP), 미국 (US), 홍콩 (HK), 영국 (GB), 프랑스 (FR), 기타 (ETC)

def FindKeyword(Keyword, inputGenre, inputCountry):
    global client_id, client_secret

    conn = http.client.HTTPSConnection(server)
    encText = urllib.parse.quote(Keyword)
    conn.request("GET", "/v1/search/movie.xml?dispaly=10&start=1&query=" + encText
                 + "&genre=" + str(inputGenre) + "&country=" + str(inputCountry),
                 None, {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    req = conn.getresponse()
    response_body = req.read()
    data = str(response_body.decode('utf-8'))

    from xml.etree import ElementTree
    tree = ElementTree.fromstring(data)

    itemElements = tree.getiterator("item")  # return list type

    return itemElements


#itemElements = FindKeyword(inputGenre, inputContry)
#for item in itemElements:
#    title = item.find("title").text
#    link = item.find("link").text
#    image= item.find("image").text
#    subtitle= item.find("subtitle").text
#    pubDate= item.find("pubDate").text
#    director= item.find("director").text
#    actor= item.find("actor").text
#    userRating= item.find("userRating").text
#
#    print("=========================================")
#    print("title: ", title)
#    print("link: ", link)
#    print("image url: ", image)
#    print("sub title: ", subtitle)
#    print("제작년도: ", pubDate)
#    print("영화 감독: ", director)
#    print("출연 배우: ", actor)
#    print("유저 평점: ", userRating)
#    print("=========================================")

