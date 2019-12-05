"""基本步骤命令"""
import time
import pandas as pd
import sqlite3


def connect_base_uer_info(func):
    """链接基本信息数据文件，返回指针和库"""
    conn = sqlite3.connect("/home/ubuntu/misaka_back/user_info/base_info.db")
    db_cursor = conn.cursor()
    def wrapper(*args, **kwargs):
        data = None
        start_time = time.time()
        kwargs = {**kwargs, **{"db_cursor": db_cursor}}
        data = func(*args, **kwargs)
        conn.commit()
        end_time = time.time()
        msecs = (end_time - start_time)*1000
        print(msecs)
        conn.close()
        return data
    return wrapper

@connect_base_uer_info
def do_execute(**kwargs):
    """
    执行，返回结果
    key: com_line 执行命令
         com_para 参数
    """
    db_cursor = kwargs["db_cursor"]
    com_line = kwargs["com_line"]
    com_para = kwargs["com_para"]
    rlt_cur = db_cursor.execute(com_line, com_para)
    kwargs["rlt_cur"] = rlt_cur
    return kwargs


@connect_base_uer_info
def create_table(**kwargs):
    """
    创建表
    key: table_str 中写入创建语句
    """
    db_cursor = kwargs.get("db_cursor")
    table_str = kwargs.get("table_str")
    """ 以前创建的
    CREATE TABLE base_info(
    id INT PRIMARY KEY not null,
    nickname CHAR(36) not null,
    wx_user_id CHAR(72),
    city CHAR(16),
    other_info TEXT
    )"""
    sign = db_cursor.execute(table_str)
    return 1


@connect_base_uer_info
def create_base_info(**kwargs):
    """
    创建信息
    key: table_name str
         col_name tuple(str)
         values typle(any)
    """
    db_cursor = kwargs.get("db_cursor")
    com_line = "INSERT INTO {table_name} {col_name} VALUES {values}".format(**kwargs)
    insert_id = db_cursor.execute(com_line)
    return insert_id


@connect_base_uer_info
def show_all_table(**kwargs):
    db_cursor = kwargs.get("db_cursor")
    print(db_cursor.execute("select name from sqlite_master where type='table' order by name").fetchall())


@connect_base_uer_info
def show_desc_table(**kwargs):
    db_cursor = kwargs.get("db_cursor")
    table_name = kwargs.get("table_name") or ''
    table_info = f"PRAGMA table_info({table_name})"
    table_desc = db_cursor.execute(table_info).fetchall()
    fm_data = pd.DataFrame(table_desc)
    print(fm_data)

@connect_base_uer_info
def show_head_table(**kwargs):
    db_cursor = kwargs.get("db_cursor")
    table_name = kwargs.get("table_name") or ''
    limit = "limit " + str(kwargs.get("limit")) or ''
    table_info = "select * from friends_info {limit}".format(limit=limit)
    table_desc = db_cursor.execute(table_info).fetchall()
    print(table_desc)


if __name__ == "__main__":
    FRIENDS_INFO = """CREATE TABLE friends_info(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName CHAR(72) not null,
        NickName CHAR(36),
        HeadImgUrl CHAR(16),
        ContactFlag CHAR(16),
        RemarkName CHAR(16),
        Sex CHAR(16),
        Signature CHAR(16),
        PYInitial CHAR(16),
        PYQuanPin CHAR(16),
        RemarkPYInitial CHAR(16),
        RemarkPYQuanPin CHAR(16),
        StarFriend CHAR(16),
        Statues CHAR(16),
        AppAccountFlag CHAR(16),
        AttrStatus CHAR(16),
        Province CHAR(16),
        City CHAR(16),
        Alias CHAR(16),
        SnsFlag CHAR(16),
        UniFriend CHAR(16),
        DisplayName CHAR(16),
        ChatRoomId CHAR(16),
        KeyWord CHAR(16),
        EncryChatRoomId CHAR(16),
        IsOwner CHAR(16),
        OtherInfo TEXT
    )"""
    # table_info = "DROP TABLE friends_info"
    # create_table(table_str=table_info)
    # 删除
    #create_table(table_str=FRIENDS_INFO)
    #create_base_info(table_name = "friends_info", col_name = ("UserName", "NickName"), values = ("测试", "成功/失败"))
    show_head_table(limit = 1)
