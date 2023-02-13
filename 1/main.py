# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 23:17
# @Author  : Blue
# @File    : main.py
import time

import execjs
import requests


def get_m():
    t = int(time.time()) * 1000 + 100000000
    # t = 1676143939000
    with open('md5.js') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    result = ctx.call("hex_md5", f'{t}')
    m = f'{result}丨{t // 1000}'
    return m

def main():
    s = requests.session()
    s.headers = {
        'cookie': 'sessionid=0fuwhnsg10832w44vvclf6y1ob7iu7s7;',
        'user-agent': 'yuanrenxue.project',
    }

    l = 0
    num = 0
    for page in range(1, 6):
        params = (
            ('page', page),
            ('m', get_m()),
        )

        response = s.get('https://match.yuanrenxue.com/api/match/1', params=params)
        result = response.json()
        l += len(result['data'])
        for item in result['data']:
            num += item['value']
        print(page, num)
    
    print(num//l)

if __name__ == '__main__':

    main()
