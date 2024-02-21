import yaml
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
        with open(file,'r',encoding='utf-8') as f:
            yaml_date = yaml.safe_load(f)
            return yaml_date
    except Exception as e:
        print(e)

if __name__ == '__main__':
    res = get_testcase_yaml('login.yaml')[0]
    url=res['baseInfo']['url']
    new_url = 'http://127.0.0.1:8787'+url
    method = res['baseInfo']['method']
    data = res['testCase'][0]['data']

    # 实例化
    send = SendRequests()
    # 调用主函数run_main()
    res = send.run_main(url=new_url, data=data, header=None, method=method)
    print(res)

