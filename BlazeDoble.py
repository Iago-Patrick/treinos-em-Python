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
print()
print ('SEM CONVERSAO')
print (texto)

#converter de string para numero
org = texto[0:9]

#############################################################

def number(x): 
    if x =='0':
        return 'red'

    if x =='1':
        return 'red'

    if x =='2':
      return 'red'
      
    if x=='3':
        return 'red'

    if x=='4':
      return 'red'

    if x=='5':
        return 'red'

    if x=='6':
      return 'red'
      
    if x=='7':
       return 'red'

    if x=='8':
      return 'black'
      
    if x=='9':
     return 'black'

    if x=='10':
      return 'black'

    if x=='11':
        return 'black'

    if x=='12':
      return 'black'
      
    if x=='13':
     return 'black'

    if x=='14':
      return 'black'

    if x=='15':
      return 'black'

    if x=='16':
     return 'black'

def color(x):
  if x < 7:
    return 'Red'
  if x > 9:
   return 'black'
  if x == 0:
    return 'white'

def time(x):
  if x =='5:00':
   return 1
  if x =='5:01':
   return 1
  if x =='4:90':
   return 1
  if x =='4:91':
   return 1
  if x =='4:92':
   return 1
  if x =='4:93':
   return 1
  if x =='4:94':
   return 1
  if x =='4:95':
   return 1
  if x =='4:99':
   return 1
  if x =='4:98':
   return 1
  if x =='4:99':
   return 1
  if x =='4:97':
   return 1
  if x =='4:96':
   return 1
  else:
   return 0

#############################################################

while 1: 
 pegartempo = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div').text
 texto2=pegartempo.split()

 print()
 print(texto2)
 print()

 pwm2 = map(time,texto2)
 tempofinal = list(pwm2)
 print(tempofinal)
 if tempofinal == [0,0,1]:
   pegar = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]/div').text
   texto=pegar.split()
   pwm = map(number, org)
   finalnum = list(pwm)
   print()
   print('COM CONVERSAO')
   print(finalnum)
   
   break
  
