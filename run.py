"""启动"""
import time
import itchat

from it_chat import wx_robot
from weather_api import weather
from dbgo import db_read

def weather_time():
    """定时任务，一天拉取一次天气m信息，检测是否有报警天气"""
    time.sleep(6*60*60)
    rlt_cur = db_read.get_all_baseinfo()
    for info in rlt_cur:
        city = info[2]
        wx_user_id = info[1]
        msg = weather.get_weather(city, only_today=False)
        itchat.send_raw_msg(1, rsp_msg + "^(*￣(oo)￣)^", wx_user_id)
