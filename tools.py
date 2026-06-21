import os
import smtplib
import json
from email.mime.text import MIMEText
from datetime import datetime

# 天气查询

def weather_inquir(city):
    dic = {
        "北京":{
           "weather":"晴","temperatrue":"23℃"
            },
        "上海":{
            "weather":"小雨","temperatrue":"27℃"
            }
    }
    r = dic.get(city)
    result = '查询完毕，' + city + '天气是：' + r['weather'] +',' + r['temperatrue']
    print(result)
    return result


# AI每次提供的“当天”日期不准确
# # 天气查询
# def weather_inquir(city, time):
#     dic = {
#         "北京":{
#             "2026-06-21":{"weather":"晴","temperatrue":"23℃"},
#             "2026-06-20":{"weather":"晴","temperatrue":"20℃"},
#             },
#         "上海":{
#             "2026-06-21":{"weather":"晴","temperatrue":"32℃"},
#             "2025-10-28":{"weather":"小雨","temperatrue":"27℃"},
#             }
#     }
    
#     if time is None:
#         time = format(datetime.date(datetime.now()),"%Y-%m-%d")
#     return dic.get(city).get(time)



# 邮件发送
def send_email(from_email,to_email,subject,body):
    try:
        with open('config.json', 'r', encoding='utf-8') as file:
            email_config = json.load(file)
        password = email_config.get('password')
        ## ---
        from_email = email_config.get('from_email') # 测试用，正式使用需要删除
        to_email = email_config.get('to_email') # 测试用，正式使用需要删除
        ## ---
        email_url = email_config.get('email_url') 
        email_port = email_config.get('email_port') 
        
        # 创建邮件对象
        message = MIMEText(body, "plain", "utf-8")
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject

        # 初始化服务器连接
        server = smtplib.SMTP_SSL(email_url, email_port)
        # server.starttls()  # 启用加密
 
        server.login(from_email, password) # 登录邮件服务器

        server.sendmail(from_email, to_email, message.as_string()) # 发送邮件

        # 关闭连接
        server.quit()

        return "邮件发送成功，还有什么需要帮助您的吗？"
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return "发送失败，请检查授权或网络"
