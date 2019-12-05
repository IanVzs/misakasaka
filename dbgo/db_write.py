"""读取数据"""

from dbgo import base

@base.connect_base_uer_info
def create_or_update_friend_info(**kwargs) -> bool:
    """有则更新，无则创建"""
    db_cursor = kwargs.get("db_cursor")
    write_line = ''
    rlt_cur = db_cursor.execute(write_line)
    return rlt_cur

"""
{'MemberList': [],
 'Uin': 0,
  'UserName': '@90028d0612f32752b9eefdf4dce7efa90c97a62477976f3625ae2e6a6123a3f9',
   'NickName': '十六',
    'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=683445713&username=@90028d0612f32752b9eefdf4dce7efa90c97a62477976f3625ae2e6a6123a3f9&skey=@crypt_b2a08667_3c7d324990a70cf7777bc833b98e8922',
     'ContactFlag': 67,
      'MemberCount': 0,
       'RemarkName': '✨苏苏姑娘',
        'HideInputBarFlag': 0,
         'Sex': 2,
          'Signature': '生活的理想，就是理想的生活',
           'VerifyFlag': 0,
            'OwnerUin': 0,
             'PYInitial': 'SL',
              'PYQuanPin': 'shiliu',
               'RemarkPYInitial': 'SPANCLASSEMOJIEMOJI2728SPANSSGN',
                'RemarkPYQuanPin': 'spanclassemojiemoji2728spansusuguniang',
                 'StarFriend': 1,
                  'AppAccountFlag': 0,
                   'Statues': 0,
                    'AttrStatus': 4197,
                     'Province': '山西',
                      'City': '临汾',
                       'Alias': '',
                        'SnsFlag': 1,
                         'UniFriend': 0,
                          'DisplayName': '',
                           'ChatRoomId': 0,
                            'KeyWord': '',
                             'EncryChatRoomId': '',
                              'IsOwner': 0}
"""
