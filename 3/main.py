'''
    注意请求头的顺序
'''

import requests
def main():
    s = requests.session()

    s.headers = {
        'Host': 'match.yuanrenxue.com', 'Connection': 'keep-alive', 'Content-Length': '0',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"', 'sec-ch-ua-mobile': '?0',
        'User-Agent': 'yuanrenxue.project',
        'sec-ch-ua-platform': '"Windows"', 'Accept': '*/*', 'Origin': 'https://match.yuanrenxue.com',
        'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://match.yuanrenxue.com/match/3', 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1676360889; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1676360888; qpfccr=true; no-alert3=true; sessionid=6hudqxs4b6gfzs1z6jt8gmiofz4bse5z; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1676362698; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1676362820',
    }
    nums = []
    for page in range(1, 6):
        s.post('https://match.yuanrenxue.com/jssm')

        response = s.get(f'https://match.yuanrenxue.com/api/match/3?page={page}')
        result = response.json()
        for item in result['data']:

            nums.append(item['value'])
        print(page, nums)
    print(max(nums,key=nums.count))

if __name__ == '__main__':
    main()
