import requests
import re

DATA = []


def getHTMLtext(url, headers, timeout=10):
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return ''


def reParser(text):
    name_list = re.findall(r'<div class="yizhu".*?<b>(.*?)</b>', text, re.S)  # re.DOTALL

    dynasty_list = re.findall(r'<p class="source">.*?target="_blank">(.*?)</a>', text, re.S)

    author_list = re.findall(r'<p class="source">.*?target="_blank">.*?</a>.*?target="_blank">(.*?)</a>', text, re.S)

    row_content_list = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.S)
    content_list = []
    for content in row_content_list:
        temp = re.sub(r'<.*?>', '', content)  # 这里一定要记得不要写成了贪婪匹配哦
        content_list.append(temp.strip())  # 去除空格

    likes_list = re.findall(r'<span> (\d*?)</span>', text, re.S)

    for value in zip(name_list, dynasty_list, author_list, content_list, likes_list):
        name, dynasty, author, content, likes = value
        poetry_dict = {
            '诗词名': name,
            '朝代': dynasty,
            '作者': author,
            '内容': content,
            '点赞数': likes
        }
        DATA.append(poetry_dict)


def print_poetry(data):
    for every_poetry in data:
        print(every_poetry['诗词名'])
        print(every_poetry['朝代'] + ':' + every_poetry['作者'])
        print(every_poetry['内容'])
        print('有{}人喜欢这首诗(词)哦'.format(every_poetry["点赞数"]))
        print("\n" + '*' * 50 + "\n")


if __name__ == '__main__':
    row_url = 'https://www.gushiwen.org/default_{}.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
    num = input('请输入要爬取的页数（0001-100）:')
    for i in range(eval(num)):
        url = row_url.format(i + 1)
        text = getHTMLtext(url, headers)
        if text == '':
            print('url: {} 访问失败'.format(url))
        else:
            reParser(text)
    DATA.sort(key=lambda x: int(x['点赞数']), reverse=True)
    TOP10 = DATA[:10]
    print_poetry(TOP10)