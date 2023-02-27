import subprocess

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from sklearn.feature_extraction.text import CountVectorizer
import os
import jieba
import pickle

# 禁用jieba分词库的log
jieba.setLogLevel(20)
os.environ['JIEBA_LOG_FILE'] = 'jieba.log'
warnings.filterwarnings('ignore', category=UserWarning)
data = pd.read_csv('data.csv', encoding='utf-8')


# 分词
def tokenize(text):
    return list(jieba.cut(text))


# 构建词袋模型
vectorizer = CountVectorizer(tokenizer=tokenize)
X = vectorizer.fit_transform(data['问题'])

# 训练模型
clf = RandomForestClassifier()
clf.fit(X, data['回答'])

# 保存模型和词袋模型
with open('clf.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

import re


def find_first_url(context):
    # 支持匹配多种URL格式，包括http、https、ftp等协议
    url_regex = r'(https?|ftp)://[^\s/$.?#].[^\s]*'
    match = re.search(url_regex, context)
    if match:
        return match.group(0)
    else:
        return None


# 测试模型
def get_best_answer(input_question):
    input_vec = vectorizer.transform([input_question])
    pred = clf.predict(input_vec)
    return pred[0]


while True:
    inputp = input('请输入问题：')
    out = get_best_answer(inputp)
    if out == 'auto_url':
        url = find_first_url(inputp)
        result = subprocess.run(['python', 'Run.py', '-u', url, '-s'], capture_output=True, text=True,encoding='utf-8')
        print(result.stdout)
    if out == 'search_poc_url':
        url = find_first_url(inputp)
        result = subprocess.run(['python', 'Run.py', '-u', url], capture_output=True, text=True,encoding='utf-8')
        print(result.stdout)
    if out == 'auto_baidu':
        url = find_first_url(inputp)
        result = subprocess.run(['python', 'Run.py', '-u', 'http://www.baidu.com/', '-s'], capture_output=True, text=True,encoding='utf-8')
        print(result.stdout)
    # print('回答：', out)
    if '拜拜' in out:
        exit()
