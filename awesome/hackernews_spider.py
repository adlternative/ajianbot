from bs4 import BeautifulSoup
import requests

response = requests.get("https://rsshub.app/hackernews")
webpage = response.content

soup = BeautifulSoup(webpage, "xml")

# 获取第一个 title 标签
print(soup.title.string.strip())

for item in soup.find_all('item'):
  print('===%s===' % item.title.string.strip())
  # for urls in item.description.find_
  for tag in item.description.string.split('|'):
    tagSoup = BeautifulSoup(tag, "xml")
    # print(tag)
    taga = tagSoup.find('a', href=True)
    if taga != None and taga.string == "Source":
      print('%s\n' % taga['href'])

exit(0)