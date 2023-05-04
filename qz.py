import json

import requests

from main import print_green, print_red


def extract_weight(json_text):
    weight_dict = {}
    data = json.loads(json_text)
    for site in data:
        weight = data[site]["权重"]
        weight_dict[site] = weight
    print_green(str(weight_dict))


def check(url):
    try:
        qz = requests.get(f'http://www.tooapi.com/api/seo/?url={url}', timeout=6)
        extract_weight(qz.text)
    except Exception:
        print_red('[!]请求url失败')

def main():
    print_green('[+]当前模式为权重查询')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            check(url)
            print('=' * 10)


if __name__ == '__main__':
    main()
