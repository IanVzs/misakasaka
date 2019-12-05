"""微信机器人 @猪头进行唤醒"""
import os
import json
import itchat

from logger.logger import LOGGER
from web_crawler.spiders import crawl_image
from weather_api import weather
from dbgo import db_read
from chinese_xinhua import chinese_xinhua_dict

ACTIVE_SIGN = {}
MEID = ''

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    """回复他人消息"""
    global ACTIVE_SIGN
    global MEID
    LOGGER.write_dict2json(msg)
    user_name = msg["FromUserName"]
    rsp_msg = ''
    if "猪头是我我是猪头" in msg.text:
        MEID = msg["FromUserName"]
    if "猪头" in msg.text and not actived(msg["FromUserName"]):
        ACTIVE_SIGN[msg["FromUserName"]] = 1
        rsp_msg = "hHi~ o(*￣▽￣*)ブ  我是猪头."
    if ("再见" in msg.text or "拜" in msg.text or
            "bye" in msg.text or "退" in msg.text or
            "下" in msg.text) and actived(msg["FromUserName"]):
        ACTIVE_SIGN[msg["FromUserName"]] = 0
        rsp_msg = "ヾ(￣▽￣)Bye~Bye~, 猪头会乖乖的."

    if "图" in msg.text and actived(msg["FromUserName"]) == 1:
        if "的" in msg.text:
            image_key = msg.text.split("的")[0]
        else:
            image_key = msg.text.split("图")[0]
        sign = crawl_image(image_key, 1)
        file_path = f'/home/ubuntu/misaka_back/donwload/crawl_image/{image_key}/'
        if sign:
            for i in range(1):
                file_name = os.listdir(file_path)[i]
                file_path = f'{file_path}{file_name}'
                itchat.send_image(file_path, msg["FromUserName"])
    if "天气" in msg.text and actived(user_name):
        if "的" in msg.text:
            city_name = msg.text.split("的")[0]
        else:
            city_name = msg.text.split("天气")[0]
        if not city_name or not weather.get_city_id(city_name):
            city_name = msg["User"]["City"]
        rsp_msg = weather.get_weather(city_name)
    if "在哪儿" in msg.text and actived(user_name):
        all_nickname = db_read.get_all_nickname()
        for nickname in all_nickname.keys():
            if nickname in msg.text:
                break
            else:
                nickname = ''
        if not nickname:
            wx_user_id = msg["ToUserName"]
            base_info = db_read.get_base_info(wx_user_id=wx_user_id)
            nickname = base_info.get("nickname") or ''
        city = all_nickname[nickname].get("city")
        rsp_msg = f'{nickname}在{city}呢.'
    if (msg.text[0] == '"' and msg.text[-1] == '"') or (msg.text[0] == '“' and msg.text[-1] == '”') and actived(user_name):
        words = msg.text[1:-1]
        rsp_msg = ''
        if len(words) == 1:
            info_ = chinese_xinhua_dict.get_word(words)
        elif len(words) > 1:
            info_ = chinese_xinhua_dict.get_words(words)
        else:
            info_ = chinese_xinhua_dict.get_words("沉默")
        if info_:
            rsp_msg = json.dumps(info_, ensure_ascii=False, sort_keys=True, indent=4)
        rsp_msg = rsp_msg or ''


    if (user_name == MEID and "^(*￣(oo)￣)^" not in rsp_msg and actived(user_name)):
        itchat.send_raw_msg(msg['MsgType'], rsp_msg + "^(*￣(oo)￣)^", msg['ToUserName'])
        rsp_msg = ''

    return rsp_msg


def actived(user_name):
    """是否被激活"""
    global ACTIVE_SIGN
    return ACTIVE_SIGN.get(user_name)

itchat.auto_login(enableCmdQR=True, hotReload=True)
#print(itchat.get_friends()[1])
itchat.run()
