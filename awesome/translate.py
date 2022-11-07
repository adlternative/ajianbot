from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.com'])

def translate_to_zh_cn(message) -> str:
  result = translator.translate(message, dest='zh-cn')
  if result != None:
    return result.text
  return None