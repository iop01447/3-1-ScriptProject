# import telepot
# from urllib.request import urlopen
#
# # movie_telegram_bot
# bot = telepot.Bot('618132164:AAGRSPO6NjwzNQvRTcK-aWysp8WurNsBTgw')
# print(bot.getMe())
# # 595832994
# print(bot.sendMessage('549346292', '안녕하세요. 영화 텔레그램 봇입니다.'))
# bot.sendMessage('549346292', '열심이시군요. 혜리씨.')
#
# url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&LAWD_CD=11110&DEAL_YMD=201712'
# response = urlopen(url).read()
# print(response)

r = int(input())
a = int(input())

r = r/100/12
money = a

for i in range(1,13):
    money *= (1+r)
    print("{0}달 후 잔고: {1:.2f}".format(i, money))
    money+=a

# 하 슈벌 에
