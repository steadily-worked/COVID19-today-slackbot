# COVID19-today-slackbot

Slackbot that informs COVID-19 confirmed cases today<br>
Production process in [here](https://steadily-worked.tistory.com/category/Slackbot)

## Change log

#### 2021.01.05
- Slackbot was born
- It helps users to know how many COVID-19 confirmed cases have ocurred today

#### 2021.01.25
- Add image showing the trend of COVID-19 confirmation and cure using PyAutoGUI and Selenium

## Getting Started

- Add your Slackbot in [here](https://api.slack.com/apps)
- Copy your API token
- Paste it in `slackbot.py`
<img width="468" alt="token" src="https://user-images.githubusercontent.com/61453718/106829691-fe8f4e00-66cf-11eb-9dfc-d3c2b6f6830d.png">

## Install

```python
pip install slacker
pip install bs4
pip install selenium
pip install pyautogui
```

## Running the tests

#### download chromedriver
- in [here](https://chromedriver.chromium.org/downloads) (before downloading, check your Google Chrome version)

#### setting driver & image path
- Enter the path where chromedriver is saved in Line 37.
- Then, enter the path to save screenshots taken by PyAutoGUI in Line 44.

#### write down
- the bot token in Line 8
- the Slack channel that the bot will send messages to in Line 14 instead of #bots-playground

#### install virtualenv
```Python
python -m venv "your virtualenv name"
```

#### run virtualenv
```Python
source "your virtualenv name"/bin/activate
```

#### run slackbot.py
```Python
python3 slackbot.py
```

## Result

<img width="427" alt="스크린샷 2021-02-03 오후 2 49 25" src="https://user-images.githubusercontent.com/61453718/106831094-a3ab2600-66d2-11eb-9b4e-32975cff0ba9.png">
