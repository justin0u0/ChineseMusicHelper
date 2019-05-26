
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
url = "https://lms.nthu.edu.tw"
login_url = url + "/sys/lib/ajax/login_submit.php"
login = r.get(login_url, params=user)
login.encoding = 'utf-8'
""" Debug
print (login.url)
print (login.json())
"""

course = None
if login.json()["ret"]["status"] != "true":
    pass
else:
    print ("login successfully")
    payloads = {
        "courseID": "38413",
        "f": "doc",
        "cid": "1823070"
    }
    course = r.get(url + "/course.php", params=payloads)
    course.encoding = "utf-8"
    # print (course.text)

soup = BeautifulSoup(course.text, "lxml")
block = soup.find("div", class_="block")

for div in block.find_all("div"):
    print ("downloading ... " + div.a["title"])
    d_url = url + div.a["href"]
    d_file = "./assets/" + div.a["title"]

    with requests.get(d_url, stream=True, cookies=r.cookies) as res:
        res.raise_for_status()
        with open(d_file, "wb") as f:
            for chunk in res.iter_content(chunk_size=8192):
                if (chunk):
                    f.write(chunk)

    print ("done")

print ("Finished, all mp3 files are stored in assets folder.")



