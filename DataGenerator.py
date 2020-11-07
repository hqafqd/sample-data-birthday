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
        for userIndex in range(1, random.randint(10, 50)):
            # f = open(f"{dataPath}/{year}/{month}/user{userIndex}.json", 'w+')
            # f.write(f"{year:{year}}")
            # f.close()
            with open(f"{dataPath}/{year}/{month}/user{userIndex}.json", 'w+') as json_file:
                user = {
                    "birthYear": year,
                    "birthMonth": month,
                    "name": f"User{userIndex}",
                    "height": random.randint(50, 100),
                    "weight": round(random.uniform(1.5, 4.0), 2),
                    "gender": ("female" if random.randint(1, 2) == 1 else "male")
                }
                json.dump(user, json_file)
