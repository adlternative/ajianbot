from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('cron', hour='18',)
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=809854994,
                                 message=f'现在{now.hour}点{now.minute}分{now.second}秒啦！准时下班吃饭！')
    except CQHttpError:
        pass

@nonebot.scheduler.scheduled_job('cron', hour='00', minute='21')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=809854994,
                                 message=f'现在{now.hour}点{now.minute}分{now.second}秒啦！准时上床睡觉！')
    except CQHttpError:
        pass

@nonebot.scheduler.scheduled_job('cron', hour='06',)
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=809854994,
                                 message=f'现在{now.hour}点{now.minute}分{now.second}秒啦！准时上班开卷！')
    except CQHttpError:
        pass