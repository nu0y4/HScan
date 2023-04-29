import random

from colorama import Fore

from HScan.main import print_green, print_red, print_yellow
from HScan import Run
from HScan import JsScan, logo

info = {
    '0': '退出',
    '1': 'OA漏洞扫描',
    '2': 'JS爬虫',
    '3': '权重查询',
}


def print_logo():
    dic = [
        logo.logo1,
        logo.logo2,
        logo.logo3,
    ]
    print(random.choice(dic))


def print_title():
    print_green('菜单:')
    for i in info:
        print_yellow(f'  {Fore.YELLOW}{i}.{Fore.GREEN}{info[i]}{Fore.RESET}')


def main():
    print_logo()
    print_title()
    print()
    while True:
        key = input('[+]请输入菜单选项: ')
        if key == '1':
            Run.main()
        if key == '2':
            JsScan.main()
        if key == '3':
            print('权重')
        if key == '0':
            print_red('[+]再见~ 祝，我们都每天都美好')
            break


if __name__ == '__main__':
    main()
