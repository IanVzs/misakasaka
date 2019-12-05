"""读取数据"""
try:
    import base
except:
    from dbgo import base

@base.connect_base_uer_info
def get_city(**kwargs) -> str:
    """使用wx_user_id 获取信息"""
    db_cursor = kwargs.get("db_cursor")
    wx_user_id = kwargs.get("wx_user_id")
    select_line = f'SELECT city from base_info WHERE wx_user_id = "{wx_user_id}"'
    rlt_cur = db_cursor.execute(select_line)
    rlt = {}
    for i in rlt_cur:
        rlt = i[0]
        break
    return rlt


@base.connect_base_uer_info
def get_base_info(**kwargs) -> dict:
    """使用wx_user_id 获取信息"""
    db_cursor = kwargs.get("db_cursor")
    wx_user_id = kwargs.get("wx_user_id")
    select_line = f'SELECT nickname, wx_user_id, city \
            from base_info WHERE wx_user_id = "{wx_user_id}"'
    rlt_cur = db_cursor.execute(select_line)
    rlt = {}
    para_name_list = ["nickname", "wx_user_id", "city"]
    for i in rlt_cur:
        rlt = dict(zip(para_name_list, i))
        break
    return rlt


@base.connect_base_uer_info
def get_all_nickname(**kwargs) -> dict:
    """获取全部基础信息中的昵称"""
    db_cursor = kwargs.get("db_cursor")
    select_line = f'SELECT nickname, wx_user_id, city from base_info'
    rlt_cur = db_cursor.execute(select_line)
    rlt = {}
    para_name_list = ["nickname", "wx_user_id", "city"]
    for i in rlt_cur:
        rlt[i[0]] = dict(zip(para_name_list, i))
    return rlt


@base.connect_base_uer_info
def get_all_baseinfo(**kwargs) -> tuple:
    """获取全部基础信息中的昵称"""
    db_cursor = kwargs.get("db_cursor")
    select_line = f'SELECT nickname, wx_user_id, city from base_info'
    rlt_cur = db_cursor.execute(select_line)
    return rlt_cur

@base.connect_base_uer_info
def get_one_by_a_dict(**kwargs) -> tuple:
    """通过一个一级字典查询数据"""
    db_cursor = None
    db_want = []
    for i in kwargs.keys():
        if i == "db_cursor":
            # 执行器
            db_cursor = kwargs[i]
        elif i == "db_want":
            # 期望返回列表
            db_want = kwargs[i]
            if not (isinstance(db_want, tuple) or isinstance(db_want, list)):
                # TODO
                pass

        else:
            #TODO
            # 查找条件
            pass
            

if __name__ == '__main__':
    WXID = "@a19ff839f448b16142d241db6e20c609cf193b983a977f2833e8cea6e1bb35f9"
    III = get_city(wx_user_id="@a19ff839f448b16142d241db6e20c609cf193b983a977f2833e8cea6e1bb35f9")
    III = get_base_info(wx_user_id=WXID)
    NICKNAMELIST = get_all_nickname()
    print(III, NICKNAMELIST)
