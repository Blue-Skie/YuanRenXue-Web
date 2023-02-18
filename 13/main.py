# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 23:03
# @Author  : Blue
# @File    : main.py
'''
这里是直接在第一个请求里直接用document.cookie=设置了cookie hook cookie set没用
'''
import re

import requests


def main():
    s = requests.session()



    s.headers = {
        'user-agent': 'yuanrenxue.project',
    }

    cookies = {
        'sessionid': 'gpbv85lqrj3cy31jqatn55l9lvu2ook9'
    }
    response = s.get('https://match.yuanrenxue.com/match/13', cookies=cookies)

    cookie = re.search('cookie=(.*?)\+\'', response.text)
    cookie = eval(cookie.group(1))
    k, v = cookie.split('=')
    cookies[k] = v
    num = 0
    for page in range(1, 6):
        params = (
            ('page', page),
        )

        response = s.get('https://match.yuanrenxue.com/api/match/13', params=params, cookies=cookies)
        result = response.json()
        for item in result['data']:
            num += item['value']
        print(page, num)

    print(num)


if __name__ == '__main__':
    main()
