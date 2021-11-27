import pandas as pd
import os

working_dir = r'C:\Users\ac812\Documents\GitHub\working_files'

f = os.path.join(working_dir, 'book1.xlsx')
df = pd.read_excel(f)


print(df)
