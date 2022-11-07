from os import path

import nonebot
import config

from nonebot.log import logger
import logging

if __name__ == '__main__':
    nonebot.init(config)
    logger.setLevel(logging.WARNING)

    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    nonebot.run()