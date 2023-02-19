from POC import CVE_2020_27986
from POC import CNVD_2021_30167
import argparse
from urllib.parse import urlparse

from colorama import init, Fore, Back, Style
from POC.用友NC目录遍历漏洞 import yonyou_path
from main import hprint
import main

par = argparse.ArgumentParser(description='未知版本(内测版)')
par.add_argument('--url', '-u', help='需要扫描的url', default=False)
par.add_argument('--timeout', '-t', help='指定超时数值,默认为6', default=6, type=int)
par.add_argument('--thead', '-n', help='线程数,默认为1', type=int, default=1)
par.add_argument('--file', '-f', help='批量url文本', default=False)
args = par.parse_args()

'''
检测这个傻逼是不是输入空的url
'''
if args.url is False and args.file is False:
    hprint(logo=True)
    par.print_help()
    exit()

url = args.url
timeout = args.timeout
thead = args.thead
file = args.file

# 检测到的漏洞数
check_num = 0


def check_POC(in_url, timeout=6):
    turl = in_url
    global check_num
    if not 'http' in in_url:
        turl = urlparse(in_url)
        if not turl.scheme:
            turl = turl._replace(scheme='http', path=turl.path.strip('/'))  # 填充http头部
            turl = turl.geturl().replace('///', '//')

    re = CVE_2020_27986.SonarQube_data_leak(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = CNVD_2021_30167.yonyou_nc(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = yonyou_path(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    main.print_yellow(f'一共检测到{check_num}个漏洞')

def url_check(in_url):
    main.print_yellow('检测到单链接模式')
    check_POC(in_url)

def file_check(in_file):
    main.print_yellow('检测到批量模式')
    try:
        file = open(in_file, 'r')
        while True:
            out_url = file.readline()
            if out_url == '':
                break
            check_POC(out_url)
    except IOError as e:
        main.print_red('读取错误：' + e)
    except Exception as e:
        main.print_red('未知错误：' + str(e))


# 如果file不为空
if args.file:
    # 批量检测
    args.url = False
    file_check(file)
if args.url:
    # 单url检测
    if args.url and args.file:
        hprint('不能两个同时检测啊！操你妈')
        exit()
    else:
        url_check(url)
