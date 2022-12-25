import os
from datetime import datetime

import yaml
def get_project_path():
	project_path = os.path.dirname(os.path.abspath(__file__))
	return project_path
project_path = get_project_path()


def get_yaml_config():
	# 读取配置文件
	f = open(project_path+"/00_算法参数配置/config.yaml", 'r', encoding='utf-8')
	# cont返回文件中的所有内容，包括注释字符等。
	cont = f.read()
	# config返回python字典
	# 即：{'gama': 0.001, 'sigma': 8.5}
	config = yaml.safe_load(cont)
	return config
config = get_yaml_config()


def get_now_date():
	nowTime = datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
	return nowTime
now_time = get_now_date()


if __name__ == '__main__':
	print(project_path)
	print(config['pic_need_num'])
	print(now_time)