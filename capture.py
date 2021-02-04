from selenium import webdriver
import time
import webbrowser
import pyautogui

wd = webdriver.Chrome('/Users/sangminpark/downloads/chromedriver')
url = 'http://ncov.mohw.go.kr/'
time.sleep(3)
wd.get(url)

# while True:
#     print(pyautogui.position())
#     time.sleep(1)

pyautogui.screenshot(
    '/Users/sangminpark/downloads/screenshot.png', region=(60, 1630, 940, 480))
# wd.save_screenshot(screenshot_name)

wd.quit()
