# vulInfPush
漏洞信息推送脚本，目前支持企业微信机器人消息通知
![image](https://user-images.githubusercontent.com/125625659/219575569-1cb882aa-6658-4543-bc75-458ce4085f93.png)

## 使用
下载vulInfPush.py文件，WEBHOOK_URL处填写企业微信机器人WEBHOOK，在VULDATE处填写想更新的天数

可使用crontab或windows定时任务来做定时执行

## 说明
数据来源于xx信漏洞库，主要是一些关键漏洞，个人觉得不会占用太多的时间在漏洞筛选上

关于企业微信机器人：使用text格式而不用markdown或其他格式的原因是其他格式的链接跳转会使用内置浏览器:X


## 更新计划
添加模块化漏洞源

优化输入输出

docker支持

等.....


## 反馈
提交issues
