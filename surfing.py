import sys
import os
import time

html = raw_input("What website do you want to visit? ")

print("LOADING WEBSITE: {}  ".format(html))
print("PLEASE WAIT...")

os.system("firefox %s&" % (html))
time.sleep(2)
print("Loaded!")
time.sleep(3)

os.system("clear")
sys.exit()

