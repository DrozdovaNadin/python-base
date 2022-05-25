import os

directory = r'C:\Users\1\Downloads\some_data'

groups = [100, 1000, 10000, 100000, 1000000]
result = dict.fromkeys(groups, 0)

for name, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(name, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1
print(result, sep='\n')

# for key, value in result.items():
#     print({"{0}: {1}".format(key,value)})
