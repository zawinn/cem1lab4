import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.mail.ru'
smtp_port = 587
username = 'LarisaKotovaoahq@inbox.ru' 
password = 'uf(Xdi!Dhz7el'  

msg = MIMEMultipart()
msg['From'] = username
msg['To'] = 'LarisaKotovaoahq@inbox.ru'
msg['Subject'] = 'Тестовое сообщение'

body = 'Это тестовое сообщение, отправленное через smtplib с Mail.ru!'
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  
    server.login(username, password)  
    server.send_message(msg)  
    print('Сообщение успешно отправлено!')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    server.quit()  
