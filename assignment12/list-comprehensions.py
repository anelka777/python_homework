import pandas as pd

df = pd.read_csv("../csv/employees.csv")

full_names = [row['first_name'] + ' ' + row['last_name'] for _, row in df.iterrows()]
print("All Names:", full_names)

names_with_e = [name for name in full_names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)