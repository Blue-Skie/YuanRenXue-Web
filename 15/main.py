# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 23:27
# @Author  : Blue
# @File    : main.py
'''
    二进制文件的调用
'''
import random
import time

import pywasm
import requests


def get_m():
    t1 = int(time.time() / 2)
    t2 = int(time.time() / 2 - random.randint(1, 50))
    vm = pywasm.load('./main.wasm')
    result = vm.exec("encode", [t1, t2])

    return f'{result}|{t1}|{t2}'


def main():
    s = requests.session()
    s.headers = {
        'cookie': 'sessionid=gpbv85lqrj3cy31jqatn55l9lvu2ook9;',
        'user-agent': 'yuanrenxue.project',
    }

    num = 0
    for page in range(1, 6):
        params = (
            ('page', page),
            ('m', get_m()),
        )

        response = s.get('https://match.yuanrenxue.com/api/match/15', params=params)
        result = response.json()
        for item in result['data']:
            num += item['value']
        print(page, num)

    print(num)


if __name__ == '__main__':
    main()
