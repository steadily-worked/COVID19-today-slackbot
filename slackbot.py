#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

from slacker import Slacker
from datetime import datetime
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import webbrowser
import pyautogui

token = 'xoxb-'


def send_slack_message(msg):
    full_msg = msg
    slack = Slacker(token)
    slack.files.upload(
        '/Users/sangminpark/downloads/screenshot.png', channels='#random')
    slack.chat.post_message('#random', full_msg, as_user=True)


def run():
    target = request.urlopen("http://ncov.mohw.go.kr/")
    soup = BeautifulSoup(target, "html.parser")
    nums = []

    for item in soup.select("div.datalist"):
        for data in item.select("span.data"):
            data.string = data.string.replace(',', '')
            nums.append(int(data.string))

    send_slack_message(f"어제의 코로나 확진자수는: {sum(nums)}명입니다.")


def runImage():
    wd = webdriver.Chrome('/Users/sangminpark/downloads/chromedriver')
    url = 'http://ncov.mohw.go.kr/'
    time.sleep(3)
    wd.get(url)

    time.sleep(2)
    pyautogui.screenshot(
        '/Users/sangminpark/downloads/screenshot.png', region=(60, 1630, 940, 480))

    wd.quit()


if __name__ == "__main__":
    try:
        runImage()
        run()
    except Exception as e:
        send_slack_message(e)
