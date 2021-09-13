import re
import csv
import pandas as pd
FILE_PATH = './cian_data_1608639118.csv'
filtred_data = []
with open(FILE_PATH) as fl:
  for line in fl:
    if re.match(r'[0-9]+[,][0-9]+[,][0-9]+[,][0-9]+[/]', line):
      line = re.sub(r'(^[0-9]+,[0-9]+[^,]*),', r'\1.', line)
      #line = re.sub(r'(^[0-9]+,[0-9]*[0-9]+),', r'\1.', line)
      print(line)
    filtred_data.append(line)
df = pd.DataFrame(filtred_data)
df = df.drop_duplicates()
print(df.shape)
df.to_csv('prepared_data.csv', index=False, encoding='utf-8')