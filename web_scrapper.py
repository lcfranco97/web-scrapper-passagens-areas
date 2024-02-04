from bs4 import BeautifulSoup
import requests
from email.message import EmailMessage 
import smtplib


URL = "https://www.google.com/travel/flights/search?tfs=CBwQAhosEgoyMDI0LTEyLTEyahAIAhIML2cvMXB4eXl6eDNycgwIAxIIL20vMDZnbXIaLBIKMjAyNC0xMi0yN2oMCAMSCC9tLzA2Z21ychAIAhIML2cvMXB4eXl6eDNyQAFIAXABggELCP___________wGYAQE&tfu=EgYIAhAAGAA&hl=pt-PT"



headers = {'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h3', class_ = 'zBTtmb ZSxxwc').get_text()
price = soup.find('div', class_ = 'YMlIz FpEdX jLMuyc').get_text().strip()

num_price = price[0:5]
num_price = num_price.replace(' ', '').replace('\xa0', '')
num_price = float(num_price)


def send_email():
    email_content = """
    https://www.google.com/travel/flights/search?tfs=CBwQAhosEgoyMDI0LTEyLTEyahAIAhIML2cvMXB4eXl6eDNycgwIAxIIL20vMDZnbXIaLBIKMjAyNC0xMi0yN2oMCAMSCC9tLzA2Z21ychAIAhIML2cvMXB4eXl6eDNyQAFIAXABggELCP___________wGYAQE&tfu=EgYIAhAAGAA&hl=pt-PT
    """
    msg = EmailMessage()
    msg['Subject'] = 'Preço passagem para Rio de Janeiro BAIXOU!!!'
    
    msg['From'] = 'lcautomacao97@gmail.com'
    msg['To'] = 'lcautomacao97@gmail.com'
    password = 'izsz wucl eyyl cjsc'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    
    s = smtplib.SMTP('smtp.gmail.com', '587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    
    print('Sucesso ao enviar o email')

if ( num_price < 1100):
    send_email()






