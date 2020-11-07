import os
import shutil
import random
import json

dataPath = './data'

shutil.rmtree(dataPath, ignore_errors=True)

os.mkdir(dataPath)

startYear = 2000
endYear = 2020

startMonth = 1
EndMonth = 12

for year in range(startYear, endYear+1):
    os.mkdir(f"{dataPath}/{year}")
    for month in range(startMonth, EndMonth+1):
        os.mkdir(f"{dataPath}/{year}/{month}")
        for userIndex in range(1, random.randrange(10, 50)):
            #f = open(f"{dataPath}/{year}/{month}/user{userIndex}.json", 'w+')
            # f.write(f"{year:{year}}")
            # f.close()
            with open(f"{dataPath}/{year}/{month}/user{userIndex}.json", 'w+') as json_file:
                user = {
                    "birthYear": year,
                    "birthMonth": month,
                    "name": f"User{userIndex}",
                }
                json.dump(user, json_file)
