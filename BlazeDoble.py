from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)
#nav = webdriver.Chrome(executable_path=r'./chromedriver.exe')

#acessar site
nav.get('https://blaze.com/pt/games/double')

#pegar informações
pegar = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]/div').text
texto=pegar.split()
print (texto)

#converter de string para numero

org = texto[0:16]

pwm = map(number, org)

finalnum = list(pwm)

print(finalnum)

def number(x):

    if x =='1':
        return 1

    if x =='2':
      return 2
      
    if x=='3':
        return 3

    if x=='4':
      return 4

    if x=='5':
        return 5

    if x=='6':
      return 6
      
    if x=='7':
        return 7

    if x=='8':
      return 8
      
    if x=='9':
     return 9

    if x=='10':
      return 10

    if x=='11':
        return 11

    if x=='12':
      return 12
      
    if x=='13':
     return 13

    if x=='14':
      return 14

    if x=='15':
      return 15

    if x=='16':
     return 16

