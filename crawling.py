from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(target, "html.parser")

nums = []

for item in soup.select("div.datalist"):
    for data in item.select("span.data"):
        data.string = data.string.replace(',', '')
        nums.append(int(data.string))

print("오늘 발표된 어제 코로나 확진자수는:",sum(nums),"명입니다")
