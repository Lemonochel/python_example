#----БИБЛИОТЕКИ----
from selenium import webdriver #импорт библиотеки
from selenium.webdriver.chrome.service import Service #импорт вебдрайвера хром
from selenium.webdriver.common.by import By #импорт модуля By
#------------------
path = Service(r'D:\PythonScripts\chromedriver.exe') #корректная функция пути
driver = webdriver.Chrome(service = path)
url_auth = 'https://wotan.amocrm.ru/' #необходимый url для входа 
driver.get(url_auth) # обращение к странице

# ВВОД ЛОГИНА
login = driver.find_element(By. ID, 'session_end_login') # поиск айди поля логина
login.clear() # очистка поля логина
login.send_keys("i2crm-manager-29@yandex.ru") # ввод данных логина

#ВВОД ПАРОЛЯ
password = driver.find_element(By. ID,'password') # поиск айди поля пароля
password.clear() # очистка поля пароля
password.send_keys("47qF4vOf") # ввод данных пароля

#ВХОД В УЧЕТНУЮ ЗАПИСЬ
driver.find_element(By. ID,'auth_submit').click() # нажатие кнопки входа

#ОЖИДАНИЕ ССЫЛКИ НА СДЕЛКУ

url_target = input('Введите ссылку на сделку amoCRM:')
while url_target != '-':
    driver.get(url_target)

#ПОЛУЧЕНИЕ ID
    choice = input('Искать данные?:')
    if choice == 'да' or choice == 'da' or choice == 'ДА' or choice == 'DA' or choice == 'lf':
        ID = driver.find_element(By. CLASS_NAME, 'linked-form').get_attribute("id") # получение ID
    #ПРОПИСАННЫЕ ПУТИ
        xpath_name = '//*[@id="'+ ID +'"]/div[1]/div[2]/div/a/div/div/input[1]' # путь к имени
        xpath_last_name = '//*[@id="'+ ID +'"]/div[1]/div[2]/div[1]/a/div/div/input[2]' # путь к фамилии
        xpath_phone_number = '//*[@id="'+ ID +'"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/input' # путь к номеру телефона
        xpath_email = '//*[@id="'+ ID +'"]/div[2]/div[3]/div[1]/div[2]/div/div[1]/input' # путь к емейлу
        xpath_source = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[1]/div[2]/input'
        xpath_medium = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[2]/div[2]/input'
        xpath_campaign = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[3]/div[2]/input'
        xpath_term = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[4]/div[2]/input'
        xpath_content = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[5]/div[2]/input'
        xpath_referer = '/html/body/div[7]/div[1]/div[1]/div[1]/form/div/div[5]/div[6]/div[2]/input'
        
    # ПОЛУЧЕНИЕ ДАННЫХ
        name = driver.find_element(By. XPATH, xpath_name).get_attribute('value') # получение значения имени
        last_name = driver.find_element(By. XPATH, xpath_last_name).get_attribute('value') # получение значения фамилии
        phone_number = driver.find_element(By. XPATH, xpath_phone_number).get_attribute('value') # получение значения номера телефона
        email = driver.find_element(By. XPATH, xpath_email).get_attribute('value') # получение значения емейла
    # ПОЛУЧЕНИЕ UTM МЕТОК
        utm_source = driver.find_element(By. XPATH, xpath_source).get_attribute('value')
        utm_medium = driver.find_element(By. XPATH, xpath_medium).get_attribute('value')
        utm_campaign = driver.find_element(By. XPATH, xpath_campaign).get_attribute('value')
        utm_term = driver.find_element(By. XPATH, xpath_term).get_attribute('value')
        utm_content = driver.find_element(By. XPATH, xpath_content).get_attribute('value')
        utm_referer = driver.find_element(By. XPATH, xpath_referer).get_attribute('value')

           
        print(name)
        print(last_name)
        print(ID)
        print(phone_number)
        print(email)
        print(utm_source)
        print(utm_medium)
        print(utm_campaign)
        print(utm_term)
        print(utm_content)
        print(utm_referer)
        url_target = input('Введите ссылку на сделку amoCRM:')

    else:
        print('команда не была введена')
     

    






#elem = driver.page_source записывает всю страницу кода в переменную
#print(elem) выводит всю эту страницу в консоль

