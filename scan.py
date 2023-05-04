import random

from colorama import Fore

import JsScan
import Run
import qz
from main import print_green, print_red, print_yellow
from logo import logo1, logo2, logo3, banner

info = {
    '0': '退出',
    '1': 'OA漏洞扫描',
    '2': 'JS爬虫',
    '3': '权重查询',
    '4': '显示菜单',
}


def print_logo():
    dic = [
        logo1,
        logo2,
        logo3,
    ]
    print(random.choice(dic))


def print_title():
    print_green('菜单:')
    for i in info:
        print_yellow(f'  {Fore.YELLOW}{i}.{Fore.GREEN}{info[i]}{Fore.RESET}')


def main():
    print_logo()
    print(banner)
    print_title()
    print()
    while True:
        key = input('[+]请输入菜单选项: ')
        if key == '1':
            Run.main()
        if key == '2':
            JsScan.main()
        if key == '3':
            qz.main()
        if key == '0':
            print_red('[+]再见~ 祝，我们都每天都美好')
            break
        if key == '4':
            print_title()

if __name__ == '__main__':
    main()
