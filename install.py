import os
import time

os.system('touch data.db')
os.system('sudo apt install python3 python3-pip')
os.system('pip3 install pysqlite3')
os.system('clear')
print('Continuing to program')
time.sleep(2.3)
os.system('python3 script.py')
os.system('rm install.py')