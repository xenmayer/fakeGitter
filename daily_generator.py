#!/usr/local/bin/python
import os
from datetime import datetime
from datetime import timedelta
from random import randint

count = 1
today = datetime.now()
gitFake = randint(1, 10)

while gitFake > 0:
    today = today - timedelta(0, count * randint(1, 3), count * randint(2, 9), count * randint(3, 6))
    strtoday = today.strftime('%a %b %d %H:%M:%S %Y -0600')
    command = 'git commit --allow-empty -m "' + strtoday + '" --date="' + strtoday  + '"'
    print command
    os.system(command)
    gitFake -= 1

os.system('git push origin -f master')
