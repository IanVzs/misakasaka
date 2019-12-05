"""查看天气"""

import json
import requests

ALL_CITY_INFO = {}

def fill_city_info():
    """载入城市JSON信息，存储到内存ALL_CITY_INFO"""
    city_info_dict = {}
    with open("/home/ubuntu/misaka_back/weather_api/city.json") as city_file:
        city_info = json.load(city_file)
        for city_signal in city_info:
            if city_signal["cityZh"] in city_info_dict.keys():
                city_signal["cityZh"] = f'{city_signal["leaderZh"]}{city_signal["cityZh"]}'
            city_info_dict[city_signal["cityZh"]] = city_signal
    return city_info_dict

ALL_CITY_INFO = fill_city_info()


def get_city_id(city_name: str) -> str:
    """根据城市名称, 获取城市id"""
    city_id = ''
    info = ALL_CITY_INFO.get(city_name)
    if info:
        city_id = info["id"]

    return city_id


def get_weather(city_name, only_today=True):
    """调用接口，获取天气信息"""
    # weather_info = ''
    cityid = ''
    url_params = {
        "version": "v6" if only_today else "v1", # v1 大而全， v6今日实时
        "city": city_name,
        "cityid": cityid
    }
    url = "https://www.tianqiapi.com/api/?version={version}&city={city}&cityid={cityid}"
    data = requests.get(url.format(**url_params)).json()
    # weather_info = json.dumps(data, ensure_ascii=False)
    import ipdb; ipdb.set_trace()
    if only_today:
        rsp_msg = """今日({date}{week}){city}{wea}.\n
{win}{win_speed},空气质量{air_level}: {air_tips}\n
{update_time}时更新气温{tem},今日最高{tem1},最低{tem2}""".format(**data)
        if data["alarm"]["alarm_type"]:
            alarm = data["alarm"]
            alarm_msg = """今天天气不太好欸！\n
            {alarm_level}级{alarm_type}预警, {alarm_content}""".format(**alarm)
            rsp_msg = f'{alarm_msg}\n\n{rsp_msg}'
    else:
        data = data["data"]
        counter = 0
        for i in data:
            if i.get("alarm") and i["alarm"]["alarm_type"]:
                alarm = i["alarm"]
                base_msg = f'{i["day"]}天气不大好欸！\n'
                alarm_msg = "{alarm_level}级{alarm_type}预警,{alarm_content}\n".format(**alarm)
                counter += 1
        rsp_msg = f'{base_msg}{alarm_msg}. 将持续{counter}天' if counter else ''

    return rsp_msg

if __name__ == "__main__":
    print(get_weather("襄汾", False))
    print(get_weather("清徐"))
    print(get_weather("西安"))
