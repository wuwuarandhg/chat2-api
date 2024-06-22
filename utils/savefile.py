import time

import chatgpt.globals as globals
from chatgpt.refreshToken import save_refresh_map
from chatgpt.wssClient import save_wss_map

from utils.Logger import logger


async def write_token_file(token_file,token_list):
    try:           
        content = "\n".join(token_list).encode() + '\n'.encode()
        globals.dbx.files_upload(content, token_file, mode=globals.WriteMode('overwrite'))
    except Exception as e:
        logger.error(f"write file error.{str(e)}")


async def save_files():
    '''把REFRESH_MAP_FILE和token.txt里失效的refresh_token删除'''
    await save_refresh_map(globals.refresh_map)
    await save_wss_map(globals.wss_map)
    await write_token_file(globals.TOKENS_FILE, globals.token_list)
    await write_token_file(globals.ERROR_TOKENS_FILE, globals.error_token_list)
