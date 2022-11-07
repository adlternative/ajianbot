from .. import translate
from nonebot import on_command, CommandSession
from nonebot.log import logger

@on_command('translate', aliases=('翻译'))
async def trans(session: CommandSession):
  message = session.current_arg_text.strip()
  if not message:
    await session.send('你咋填的空字符串')
    return
  try:
    ans = translate.translate_to_zh_cn(message)
    if ans != None:
      message = ans
    await session.send(message)
  except Exception as e:
    logger.error(str(e))
    message = '翻译失败，真的不是 ajianbot 的错'
    await session.send(message)
