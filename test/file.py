import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(1000, 2000):
    os.remove(f'{i}.json')