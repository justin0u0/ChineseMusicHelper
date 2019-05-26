
import os
import requests
import lxml
from bs4 import BeautifulSoup

# read config file
import json

user = None
with open("./config.json") as json_file:
    user = json.load(json_file)

r = requests.Session()
login_url = "https://lms.nthu.edu.tw/sys/lib/ajax/login_submit.php"
login = r.get(login_url, params=user)
login.encoding = 'utf-8'
# print (login.url)
# print (login.json())

course = None
url = "https://lms.nthu.edu.tw/course.php"
if login.json()["ret"]["status"] != "true":
    pass
else:
    print ("login successfully")
    payloads = {
        "courseID": "38413",
        "f": "doc",
        "cid": "1823070"
    }
    course = r.get(url, params=payloads)
    course.encoding = "utf-8"
    # print (course.text)

soup = BeautifulSoup(course.text, "lxml")
block = soup.find("div", class_="block")
for div in block.find_all("div"):
    print (div.a["href"])
    print (div.a["title"])

