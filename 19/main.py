# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 15:16
# @Author  : Blue
# @File    : main.py

'''
    注意pyhttpx库 直接这样设置请求头无效 s.headers = {}
'''

import json

import pyhttpx


def main():
    s = pyhttpx.HttpSession()
    headers = {
        'cookie': 'sessionid=ae3dxj9czchdy30em99f6ixvdfwudmif;',
        'User-Agent': 'yuanrenxue.project',
    }

    num = 0
    for page in range(1, 6):

        response = s.get(f'https://match.yuanrenxue.com/api/match/19?page={page}', headers=headers)
        result = json.loads(response.text)
        for item in result['data']:
            num += item['value']
        print(page, num)

    print(num)


if __name__ == '__main__':
    main()
