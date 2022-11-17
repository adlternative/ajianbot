import sys
import subprocess

from nonebot import on_command, CommandSession

@on_command('tldr', aliases=('太长的东西我不读', '太长的东西我不想读'))
async def tldr(session: CommandSession):
    respond = "init"
    try:
      command = session.current_arg_text.strip()
      if not command:
            command = "tldr"
      respond, rc = getTLDR(command, "zh")
      if rc != 0:
        respond, rc = getTLDR(command, "")

      if len(respond) == 0:
        respond = "???"

    except Exception as e:
      respond = "???"
      print(e)
    finally:
      await session.send(respond)

def getTLDR(command:str, lang:str):
    respond = ""
    parts = command.split(' ')

    cmd = ["tldr", "-m"]

    if lang != "" :
      cmd.append("-L=" + lang)

    cmd.extend(parts)

    print(cmd, "begin")
    p = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    rc = p.wait()
    if rc != 0:
        print(cmd, "abort", rc)
        for line in iter(p.stdout.readline, b''):
            respond += line.decode('utf-8')
        for line in iter(p.stderr.readline, b''):
          respond += line.decode('utf-8')

        return respond, rc

    for line in iter(p.stdout.readline, b''):
        respond += line.decode('utf-8')

    print(cmd, "end", rc)
    return respond, 0
