import undetected_chromedriver as chr
from selenium.webdriver.chrome.options import Options
from xvfbwrapper import Xvfb
import sys
import time
import base64

def loadarr(path):
  res = '['
  names = open(path, mode='r',encoding="utf-8")
  rln = names.readlines()
  for w in rln:
    res+='\"'
    res+=w.replace("\n", "")
    res+='\",'
  res += '\"nigger\"'
  res += ']'
  return res

def gethtml(d):
  d.get("https://ficbook.net/home/myfics")
  try:
    print(d.page_source)
  except:
    print("unicode symbols!")

vd = Xvfb()
vd.start()
    
f = open("cf/1.js", "r", encoding='utf-8')
js = f.read()
f.close()

file = open('cf/logins.txt',mode='r',encoding="utf8")
r = file.read().splitlines()
file.close()

acc = int(sys.argv[1])

js+='\n'
js+="await q(\""+r[acc].split(':')[0]+"\",\""+r[acc].split(':')[1]+"\","+loadarr('cf/messages.txt')+", "+loadarr('cf/errors.txt')+", "+loadarr('cf/starts.txt')+", "+loadarr('cf/ends.txt')+")"

chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--no-sandbox")
d = chr.Chrome(version_main = 110, options = chrome_options)
gethtml(d)
d.get("https://ficbook.net")

message_bytes = js.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)

d.set_script_timeout(6*1000*60)
d.execute_script(js)

vd.stop()
