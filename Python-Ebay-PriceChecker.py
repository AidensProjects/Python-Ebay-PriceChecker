import smtplib
import requests
from bs4 import BeautifulSoup
from usernamepassword import * # Includes variables - SendersEmail / TwoFactorPassword / RecieverEmail

# Tests if page is working
# print(soup.prettify())

# EXAMPLES - EXAMPLES - EXAMPLES - EXAMPLES - EXAMPLES - 
# SendersEmail = 'exampleSender@gmail.com'
# TwoFactorPassword = 'ageagaegawdadag'
# RecieverEmail = 'exampleReciever@gmail.com'

def get_product_amount(soup):
    return int([int(x) for x in print_h1(soup).split() if x.isdigit()][0]) 

def send_mail(url, SendersEmail, RecieverEmail, TwoFactorPassword):
    print("Sending Email")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(RecieverEmail, TwoFactorPassword)
    # THE EMAIL YOU ARE SENDING THE MAIL FROM, 2-Factor Authentication Password

    subject = 'New Product!'
    body = 'Check this out - {}'.format(url),
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        RecieverEmail, # THE ADDRESS SENDING THE EMAIL
        RecieverEmail, # PUT THE EMAIL YOU WANT IT TO BE SENT TOO
        msg
    )
    print("Email Has Been Sent")
    server.quit()

def print_h1(soup):
    mystr = ""
    for x in soup.h1:
        try:
            mystr += x.decode_contents()
            mystr += ' '
        except:
            mystr += x
        mystr = mystr.strip('\n')
        mystr = mystr.replace('<b>','')
        mystr = mystr.replace('</b>','')
    return mystr

def __main__():
    URL = 'https://www.ebay.co.uk/sch/i.html?_dmd=1&_stpos=N90AB&_fosrp=1&_ftrt=901&_sop=2&_ftrv=1&_ipg=60&_sadis=15&_from=R40&_sacat=0&_nkw=jnco&_blrs=recall_filtering'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    print("\nProduct We Are Monitoring:")
    print(print_h1(soup))

    if get_product_amount(soup) > 354:
        send_mail(URL, SendersEmail, RecieverEmail, TwoFactorPassword)

__main__()