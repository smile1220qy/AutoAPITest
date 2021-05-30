"""读取数据"""
import os
import yaml

DATA_DIR = os.path.abspath(f'{__file__}/../../data')


def load_yaml(file_name):
    """读取yaml文件，自动拼接数据目录"""
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data