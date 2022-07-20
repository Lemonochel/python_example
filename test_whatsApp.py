import pywhatkit
import os

def send_message():
    mobile = input("Введите номер получателя: ")
    message = input("Введите текст сообщения: ")

    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)

def main():
    send_message()

if __name__=='__main__':
    main()
