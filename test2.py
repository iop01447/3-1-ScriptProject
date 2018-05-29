import os
import sys
import urllib.request
client_id = "mmi_2tPnCtDa9tKRyXnq"
client_secret = "qu3J2HEtRr"
encText = urllib.parse.quote("사랑")
url = "https://openapi.naver.com/v1/search/movie.xml?dispaly=10&start=1&query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
#
# cLen = req.getheader("Content-Length")
# req.read(int(cLen))
