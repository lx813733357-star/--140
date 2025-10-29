import requests
import execjs
import subprocess,os
import json
import re
import time,random
import jsonpath
ctx = execjs.compile(open('password.js','r',encoding='utf-8').read())
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://xindafengche.souche.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Storage-Access': 'active',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
def ali_140(o):
    temp_js = 'temp_exec.js'
    try:
        js_code = open('140.js','r',encoding='utf-8').read()
        # 添加执行代码
        with open(temp_js, 'w', encoding='utf-8') as f:
            f.write(js_code)
            f.write('\n\n// 执行代码\n')
            # 添加参数处理逻辑
            f.write(f'''
            o = "{o}";
            main(o)
            ''')
        # 执行临时文件
        result = subprocess.run(
            ['node', temp_js],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        if result.returncode != 0:
            raise RuntimeError(f"Node.js执行错误: {result.stderr}")

        output = result.stdout.strip()
        try:
            return json.loads(output) if output.startswith('{') or output.startswith('[') else output
        except json.JSONDecodeError:
            return output
    finally:
        if os.path.exists(temp_js):
            os.remove(temp_js)
def get_140(o):
    _140 = re.findall('AWSCInner(.*)', ali_140(o).replace('\n', '').replace(' ', ''))[0]
    return _140
if __name__ == '__main__':
    o = {
    "SendInterval": 5,
    "SendMethod": 8,
    "isSendError": 1,
    "MaxMCLog": 12,
    "MaxKSLog": 14,
    "MaxMPLog": 5,
    "MaxGPLog": 1,
    "MaxTCLog": 12,
    "GPInterval": 50,
    "MPInterval": 4,
    "MaxFocusLog": 6,
    "Flag": 2980046,
    "OnlyHost": 1,
    "MaxMTLog": 500,
    "MinMTDwnLog": 30,
    "MaxNGPLog": 1,
    "sIDs": [
        "_n1t|_n1z|nocaptcha|-stage-1"
    ],
    "mIDs": [
        "nc-canvas",
        "click2slide-btn"
    ],
    "hook": 1,
    "font": 1,
    "api": 1
}
    _140 = get_140(o)
    print(_140)
    t = f"{'FFFF0000000001780657'}:{int(time.time() * 1000)}:{random.random()}"
    params = {
        'a': 'FFFF0000000001780657',
        't': t,
        'n': _140,
        'p': '{"ncSessionID":"642590e92d0e","umidToken":"T2gAFRskkn_MIYr490KgomkMoRJL77HIUXzQDnZNFe1Dqyjs5W-SNYZhlR6krcpXgsY="}',
        'scene': 'login',
        'asyn': '0',
        'lang': 'cn',
        'v': '1099',
    }
    response = requests.get('https://cf.aliyun.com/nocaptcha/analyze.jsonp', params=params, headers=headers)
    data = response.text.replace('onJSONPCallback(','').replace(');','')
    print(data)
    json_data = json.loads(data)
    csessionid = jsonpath.jsonpath(json_data,'$..csessionid')[0]
    sig = jsonpath.jsonpath(json_data,'$..value')[0]
    username = input('账号:')
    password = input('输入密码:')
    password = ctx.call('get_password', password)
    params = {
        'csessionid': csessionid,
        'value': 'pass',
        'sig': sig,
        'token': t,
        'username': username,
        'password': password,
    }

    response = requests.get('https://danube-tenant-web.souche.com/account/login.json', params=params, headers=headers)

    print(response.text)
