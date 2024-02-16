import json
import config.setting as conf

def load_token():
    with open(conf.token_path, 'w') as file:
        conf.user_token = json.loads(file.read())

def save_token():
    # 将字典保存为JSON文件
    with open(conf.token_path, 'w') as file:
        json.dump(conf.user_token, file)