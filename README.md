# vulInfPush
漏洞信息推送脚本，目前支持企业微信机器人消息通知
![image](https://user-images.githubusercontent.com/125625659/224922268-88b404c4-dcab-46df-8410-cb94935e7960.png)

## 使用
> 需要有requests库
- 下载vulInfPush.py文件
- `WEBHOOK_URL`处填写企业微信机器人WEBHOOK
- `VULDATE`处填写想更新的天数

可使用`crontab`或`windows定时任务`来做定时执行

## 说明
数据来源于国内安全厂商漏洞库，主要是一些关键漏洞，个人觉得不会占用太多的时间在漏洞筛选上

关于企业微信机器人：

使用text格式而不用markdown或其他格式的原因：其他格式的链接跳转会使用内置浏览器


## 更新计划
添加模块化漏洞源

数据持久化

docker支持

等.....


## 反馈
提交issues
