'''
 Source code from Medium's article "Build Your Own Python App to Track
 Amazon Prices" (https://bit.ly/2QwJAmD), written by c0d3x27
 (https://medium.com/@c0d3x27).
 Important note: Amazon actually blocks this source code, nonetheless, there
 are interesting parts.
'''
import requests
from bs4 import BeautifulSoup
import smtplib
import time


def analyze_price():

    app = requests.get(URL, headers=headers)
    scrapper = BeautifulSoup(app.content, 'html.parser')

    print(scrapper.prettify())

    title = scrapper.find(id="productTitle").get_text()
    price = scrapper.find(id="priceblock_ourprice").get_text()
    StrToFloat_price = float(price[1:6].replace(',', '.'))

    if(StrToFloat_price < 20000):

        send_notification()
        print(StrToFloat_price)
        print(title.strip())


def send_notification():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(frommail, passwd)

    subject = 'Low price found!'
    body = 'Here is the Amazon item link: \n\n' + URL

    msg = 'Subject: {}\n\n{}'.format(subject, body)

    server.sendmail(frommail, tomail, msg)
    print('Notification has been sent successfully')

    server.quit()


frommail = 'javier.piedragil@gmail.com'
passwd = 'dtqozgkzymutkxsq'
tomail = 'jpiedragil@koresmas.tech'

URL = 'https://www.amazon.com.mx/' + 'dp/B07X3YSKDP/?coliid=I1D4B0BJO5BNAF' + \
      '&colid=2AU1NBU9OMFK1&psc=1&ref_=lv_ov_lig_dp_it'

headers = {"User-Agent": 'Mozilla/5.0 \
           (Macintosh; Intel Mac OS X 9.10; rv:69.0) \
           Gecko/20100101 Firefox/68.0'}

while True:

    analyze_price()
    time.sleep(60*60*24)
