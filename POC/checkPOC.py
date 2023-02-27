import requests

import main

# 设置默认的敏感关键词
DEFAULT_ERROR_KEYWORD = ['找不到文件或目录',
                         'Not Found',
                         '用户未登录',
                         '未找到']


# 定义函数 poc_check，传入参数包括 poc_name, target_url, poc_url, timeout, error_keyword, expected_keyword
def poc_check(poc_name,
              target_url,
              poc_url,
              timeout=6,
              error_keyword=None,
              expected_keyword=None):
    # 如果 error_keyword 参数没有传入，则将默认的敏感关键词赋值给 error_keyword
    error_keyword = error_keyword or DEFAULT_ERROR_KEYWORD
    # 如果 expected_keyword 是字符串，则将其转换为列表形式
    expected_keyword = [expected_keyword] if isinstance(expected_keyword, str) else (
        expected_keyword if isinstance(expected_keyword, list) else [])
    # 将 expected_keyword 转换为集合去除重复元素，再转换回列表
    expected_keyword = list(set(expected_keyword))

    # 输出正在检测的 poc 名称
    # print(f'正在检测 {poc_name}...')

    # 拼接完整的 url
    if target_url[-1] == '/':
        target_url = target_url[0:len(target_url) - 1]
    url = target_url + poc_url
    try:
        # 发送 GET 请求，设置请求超时时间
        res = requests.get(url, timeout=timeout)
        # 如果状态码不为 200，则输出警告信息并返回 False
        if res.status_code != 200:
            main.print_yellow(f'{poc_name} 状态码: {res.status_code}')
            return False
        # 遍历敏感关键词列表，如果存在敏感关键词，则输出警告信息并返回 False
        for keyword in error_keyword:
            if keyword in res.text:
                #  存在敏感关键词: {keyword}
                main.print_red(f'{poc_name}')
                return False
        # 如果期望关键词列表不为空，则遍历列表，如果存在期望关键词，则输出成功信息并返回 True；否则输出警告信息并返回 False
        if expected_keyword:
            if any(keyword in res.text for keyword in expected_keyword):
                # 存在漏洞！
                main.print_green(f'{poc_name} ====> 存在漏洞 ====> {url}')
                return True
            else:
                # 没有发现期望值，漏洞不存在
                main.print_red(f'{poc_name}')
                return False
        # 如果期望关键词列表为空，则输出成功信息并返回 True
        else:
            # 检测完成
            main.print_red(f'{poc_name}')
            return True
    # 如果请求超时，则输出警告信息并返回 False
    except requests.exceptions.Timeout:
        # 请求超时
        main.print_red(f'{poc_name}')
        return False
    # 如果连接错误，则输出警告信息并返回 False
    except requests.exceptions.ConnectionError:
        # 连接错误
        main.print_red(f'{poc_name}')
        return False
