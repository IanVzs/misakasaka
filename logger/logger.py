"""日志记录"""
import json
import datetime

class LogRecoder:
    """日志记录器类"""
    def __init__(self, mode):
        self.mode = mode

    def get_mode(self):
        """获取日志模式"""
        mode_dict = {1: "记录"}
        return mode_dict[self.mode]

    def write_dict2json(self, data):
        """记录json数据"""
        if self.mode == 1:
            if isinstance(data, dict):
                with open("/home/ubuntu/misaka_back/logger/log_json.log", 'a') as log_file:
                    json_str = json.dumps(data, ensure_ascii=False)
                    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                    log_str = f'{date_str}|||{json_str}\n'
                    log_file.write(log_str)
        return 1

LOGGER = LogRecoder(1)
