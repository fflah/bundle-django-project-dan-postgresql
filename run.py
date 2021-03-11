import webbrowser
import os
from pathlib import Path           
import requests                              
from requests.exceptions import ConnectionError                                 

def run():
    print('Memulai Services...')
    home = str(Path.home())  
    dir_app =  home + '\mysite'
    cmd_path = 'cmd /c "C: & cd {} & docker-compose start"'.format(dir_app)  
    os.system(cmd_path) 
    url = '127.0.0.1:8000'
    status = True
    while status:
        try:
            if requests.get('http://localhost:8000/').status_code == 200:
                try:
                    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)
                except Exception as e:
                    try:
                        webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
                        webbrowser.get('firefox').open(url)  
                    except Exception as e:
                        webbrowser.open(url)
                status = False
        except ConnectionError as e:
            pass
run()