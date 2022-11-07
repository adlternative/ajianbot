from nonebot import on_command, CommandSession
import requests
from bs4 import BeautifulSoup
from .. import translate

@on_command('hackernews', aliases=('黑客新闻'))
async def hackernews(session: CommandSession):
    count = 10
    try:
      count = int(session.current_arg_text.strip())

    except ValueError:
      count = 10
      # do nothing
    finally:
      news = await get_hacker_news(count)
      # 向用户发送新闻
      await session.send(news)

async def get_hacker_news(count :int) -> str:
  result = ""
  try:
    response = requests.get("https://rsshub.app/hackernews")
    webpage = response.content
    soup = BeautifulSoup(webpage, "xml")

    # hacker news
    result += soup.title.string.strip() + "\n"

    # news
    for item in soup.find_all('item'):
      # title
      if count == 0:
        break
      if count > 0:
        count -= 1

      title = item.title.string.strip()
      ans = translate.translate_to_zh_cn(title)
      if ans != None:
        title = ans

      result += '[标题] %s' % title + "\n"

      # for urls in item.description.find_
      for tag in item.description.string.split('|'):
        tagSoup = BeautifulSoup(tag, "xml")
        # print(tag)
        taga = tagSoup.find('a', href=True)
        if taga != None and taga.string == "Source":
          result += '[链接] %s\n' % taga['href'] + "\n"

  except Exception as e:
    print(str(e))
    return "请求失败啦！真的不是 ajianbot 的问题！（逃）"
  return result