# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 22:49
# @Author  : Blue
# @File    : main.py
import base64

import requests


def main():
    s = requests.session()
    s.headers = {
        'cookie': 'sessionid=9tm1qnfektcikvx7urc4aqsa9d0lty09;',
        'user-agent': 'yuanrenxue.project',
    }

    num = 0
    for page in range(1, 6):
        params = (
            ('page', page),
            ('m', base64.b64encode(f'yuanrenxue{page}'.encode()).decode()),
        )

        response = s.get('https://match.yuanrenxue.com/api/match/12', params=params)
        result = response.json()
        for item in result['data']:
            num += item['value']
        print(page, num)

    print(num)


if __name__ == '__main__':
    main()