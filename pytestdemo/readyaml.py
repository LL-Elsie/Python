# -*- coding: utf-8 -*-
import json

import yaml
import os
# 引入封装类
from sendrequests import SendRequests


# 编写一个方法
def get_testcase_yaml(file):
    """
    获取yaml文件的数据
    :param file: yaml文件的路径
    :return: 返回读取到的yaml文件
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            yaml_date = yaml.safe_load(f)
            return yaml_date
    except Exception as e:
        print(e)


# 封装一个类将其读取到的接口返回值写入指定Yaml文件
class ReadYamlDate:
    """读取yaml数据，以及写入数据到yaml文件"""

    # 读取yaml文件
    def __init__(self, yaml_file=None):
        if yaml_file is not None:
            self.yaml_file = yaml_file
        else:
            self.yaml_file = 'login.yaml'

    # 封装一个写入数据到yaml文件的方法
    def write_yaml_data(self, value):
        """
        写入数据到yaml文件
        :param value: 写入的数据（dict-字典型）
        :return:
        """
        file = None
        file_path = r'extract.yaml'
        if not os.path.exists(file_path):
            os.system(file_path)

        try:
            file = open(file_path, 'a', encoding='utf-8')
            if isinstance(value, dict):
                write_data = yaml.dump(value, allow_unicode=True, sort_keys=False)
                file.write(write_data)
            else:
                print('写入到【extract.yaml】的数据必须为字典类型！')
        except Exception as e:
            print(e)
        finally:
            file.close()


if __name__ == '__main__':
    res = get_testcase_yaml('login.yaml')[0]
    url = res['baseInfo']['url']
    new_url = 'http://127.0.0.1:8787' + url
    method = res['baseInfo']['method']
    data = res['testCase'][0]['data']

    # 实例化
    send = SendRequests()
    # 调用主函数run_main()
    res = send.run_main(url=new_url, data=data, header=None, method=method)
    print(res)

    # 获取res的token值
    token = res.get('token')

    # 因为要传入一个字典类型的数据，因此需要定义一个字典
    write_data = {}
    write_data['Token'] = token

    # 获取类中的写入数据方法----先实例化类
    read = ReadYamlDate()
    read.write_yaml_data(write_data)


    # python 常用的数据类型：str list dict set tuple
    # json序列化和反序列化
    # json序列化，其实就是将python的字典类型转换为字符串类型
    json_str = json.dumps(res,ensure_ascii=False)
    print(json_str)
    print(type(json_str))
    # json反序列化，其实就是将字符串类信号转换为字典类型
    json_dict = json.loads(json_str)
    print(json_dict)
    print(type(json_dict))