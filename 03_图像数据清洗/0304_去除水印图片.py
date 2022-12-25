import base64
import glob
import os

import requests

from common import project_path, config


def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': 'UbvVGoQtHDqVZuNGYGkkGjtP',  # 在开放平台注册后所建应用的API Key
        'client_secret': 'bT3tOuGs9QEPlwDNv6QUo6VuSTO3cqiV'  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    # print(res)
    access_token = res['access_token']
    return access_token

#通用文字识别
def is_pure_pic(img_path):
    #通用文字识别接口url
    general_word_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    #获取执行路径
    # path = os.getcwd()
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())
    # print(img)
    params = {"image":img,
              "language_type":"CHN_ENG"}
    access_token = get_access_token()
    request_url = general_word_url + "?access_token=" + access_token
    # print(request_url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # print(response)
    # res = response.json()
    res = []
    if response:
        res = response.json()["words_result"]
        # print(res)
    flag = (res == [])
    return flag
        # file_name = "菜鸟小白.txt"
        # with open(file_name, 'w', encoding='utf-8') as f:
        #     for j in res:
        #         print(j["words"])
        #         f.write(j["words"]+"\n")

if __name__ == '__main__':
    line_list = config['keyword']
    for word in line_list:
        dir1 = os.path.join(project_path, config['save_path'], word)
        paths = glob.glob(os.path.join(dir1, '*.jpg'))
        count = 0
        # 输出所有文件和文件夹
        for file in paths:
            if not is_pure_pic(file):
                print(file)
                os.remove(file)
                count += 1
        print('第三步：' + word + '去除有水印的图片中...')
        print("------------------------------------------")
        print("一共删除了" + str(count) + "张有水印的图片")
        print("------------------------------------------\n\n")

    # img_path = os.path.join(project_path, config['save_path'], '桥梁损伤/000010.jpg')
    # print(is_pure_pic(img_path))
