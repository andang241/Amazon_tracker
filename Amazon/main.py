import requests
import bs4
import smtplib
import os
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "vi-VN,vi;q=0.8"
}
response = requests.get(url=url, headers=headers)
soup = bs4.BeautifulSoup(response.text, "html.parser")
result = soup.select_one(selector=".a-section .a-price .a-offscreen")
current_price = float(result.getText().split("$")[1])

username = "ninjaversusbear241@gmail.com"
password = os.environ.get("PASSWORD")
to_address = "andbhe140655@gmail.com"
if current_price < 100.0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username,
                            to_addrs=to_address,
                            msg="Subject:CHANCE \nPrice is lower than 100$. Go to Amazon and buy now!!!")
