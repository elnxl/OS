import os

while 1: 
    os.fork()
    os.system('ps -e | wc -l >> data.txt')