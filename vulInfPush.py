from datetime import datetime, timedelta
import requests
import json

# 获取天数
VULDATE = 1
# 企微机器人WEBHOOK_URL
WEBHOOK_URL = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=Your Keys'

# 漏洞数据处理函数
def qianxinVulProcess():
    url = "https://ti.qianxin.com/alpha-api/v2/nox/api/web/portal/key_vuln/list"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
        "Sec-Ch-Ua-Platform":"Windows"
    }
    data = {
        "page_no":1,"page_size":10,"tag":"","vuln_keyword":""
    }
    try:
        r=requests.post(url=url,headers=headers,json=data)
        r.raise_for_status()
        vuldata = (json.loads(r.content, strict=False))['data']['data']
        today = datetime.today()
        yesterday = today - timedelta(days=VULDATE)
        vul_list = []
        for vul in vuldata:
            publish_time = datetime.strptime(vul['publish_time'], "%Y-%m-%d") 
            if yesterday <= publish_time <= today:
                vullist = {
                    'vul_name': vul['vuln_name'],
                    'cve_code': vul['cve_code'],
                    'threat_category': vul['threat_category'],
                    'technical_category': vul['technical_category'],
                    'description': vul['description'],
                    'rating_level': vul['rating_level'],
                    'publish_time': vul['publish_time']
                }
                tag = []
                for tag_name in vul['tag']:
                    tag.append(tag_name["name"])
                vullist['tag'] = tag
                vul_list.append(vullist)
        return vul_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# 推送消息处理函数
def msgProcess(vullist):
    msg = ''
    for vul in vullist:
        msg += '漏洞名称：{}\n'.format(vul['vul_name'])
        msg += '漏洞等级：{}\n'.format(vul['rating_level'])
        msg += '威胁类型：{}\n'.format(vul['threat_category'])
        msg += '漏洞类型：{}\n'.format(vul['technical_category'])
        msg += 'CVE 编号：{}\n'.format(vul['cve_code'])
        msg += '标签：{}\n'.format(', '.join(vul['tag']))
        msg += '漏洞简述：{}\n'.format(vul['description'])
        msg += '公开日期：{}\n'.format(vul['publish_time'])
        msg += '\n'
    return msg

# 企业微信机器人推送函数
def send_wxwork_bot_msg(msg,webhook_url):
    headers = {"Content-Type": "text/plain"}

    data = {
        "msgtype":"text",
        "text": {
            "content":msg
        }
    }
    r = requests.post(webhook_url, headers=headers, json=data)
    if r.status_code != 200:
        print('Failed to send message: %s' % r.text)

def main():
    # 获取漏洞列表
    vul_list = qianxinVulProcess()
    if vul_list:
        send_wxwork_bot_msg(msgProcess(vul_list),WEBHOOK_URL)


if __name__ == '__main__':
    main()
