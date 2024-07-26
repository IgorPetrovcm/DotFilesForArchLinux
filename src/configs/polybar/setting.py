import configparser
import os

BACKLIGHT_PATH = '/sys/class/backlight/'
POWER_SUPPLY = '/sys/class/power_supply/'

config = configparser.ConfigParser()

config.read('bars.ini')

for file_path in os.listdir(BACKLIGHT_PATH):
    if os.path.isdir(BACKLIGHT_PATH + file_path) == True:
        config['module/backlight']['card'] = os.path.basename(file_path)
        os.system('sudo chmod 777 ' + BACKLIGHT_PATH + file_path + '/brightness')
        break

for file_path in os.listdir(POWER_SUPPLY):
    if os.path.isdir(POWER_SUPPLY + file_path) == True:
        for sub_file_path in os.listdir(POWER_SUPPLY + file_path):
            if os.path.basename(sub_file_path) == 'online':
                config['module/battery_bar']['adapter'] = file_path
                break
            if os.path.basename(sub_file_path) == 'alarm':
                config['module/battery_bar']['battery'] = file_path
                break
        
with open('bars.ini', 'w') as barsfile:
    config.write(barsfile)
