from flask import Flask, jsonify
import re
import requests
from bs4 import BeautifulSoup as bs
import lxml


app = Flask(__name__)

@app.route("/getCaptcha", methods=["GET","POST"])
def getCaptcha():
    url = "https://wss.mahadiscom.in/wss/wss?uiActionName=getViewPayBill"
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    skinhash = soup.find_all('script',type="text/javascript", text=True)
    captcha=skinhash[-2].text.split("'")
    return jsonify({"captcha": str(captcha[1])})
		
