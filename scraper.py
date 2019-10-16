import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/JBL-JBLCHARGE3BLKAM-Waterproof-Portable-Bluetooth/dp/B01F24RHF4/ref=sr_1_3?crid=ESSM2UUIVQ4I&keywords=jbl+charge+3&qid=1568812510&s=gateway&sprefix=jbl+%2Caps%2C180&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < .075):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('*email*', '*pword*')

    subject = 'Price went down'
    body = 'Check the link https://www.amazon.com/JBL-JBLCHARGE3BLKAM-Waterproof-Portable-Bluetooth/dp/B01F24RHF4/ref=sr_1_3?crid=ESSM2UUIVQ4I&keywords=jbl+charge+3&qid=1568812510&s=gateway&sprefix=jbl+%2Caps%2C180&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "fromEmail",
        "ToEmail",
        msg
    )
    print('CHECK YO EMAIL')
    server.quit()