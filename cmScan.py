import hashlib
import json

import requests


def scan_cms_finger(url, headers, json_file):
    # 加载json文件
    with open(json_file) as f:
        data = json.load(f)

    # 遍历所有对象和行
    for obj in data['objects']:
        if obj['type'] != 'table':
            continue
        for row in obj['rows']:
            # 提取需要匹配的数据
            path = row[2]
            match_pattern = row[3]

            print(row[1])
            print(row[0])
            print(row[2])
            print(row[3])
            print(row[4])
            # 构造请求url
            full_url = url + path if path.startswith('/') else url + '/' + path

            # 发送HTTP请求，获取响应内容
            response = requests.get(full_url, headers=headers, verify=False)
            # 判断响应内容是否匹配指纹
            if response.status_code == 200:
                if row[4] == 'md5':
                    if str_to_md5(response.text) == row[3]:
                        return f'{row[1]}'
    return '检测不到'


def str_to_md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()