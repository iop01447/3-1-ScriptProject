# -*- coding: utf-8 -*-

import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def SendEmail(text):
    #global value
    host = "smtp.gmail.com" # Gmail STMP 서버 주소.
    port = "587"
    #htmlFileName = "logo.html"

    senderAddr = "iop0144772@gmail.com"     # 보내는 사람 email 주소.
    recipientAddr = "iop01447@naver.com"   # 받는 사람 email 주소.

    msg = MIMEText(text)
    #msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "영화 검색 상세 정보"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    #htmlFD = open(htmlFileName, 'rb')
    #HtmlPart = MIMEText(htmlFD.read(),'html', _charset='UTF-8')
    #htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    #msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host,port)
    #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("iop0144772@gmail.com","dbsuddl5")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()








































