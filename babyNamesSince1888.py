import pandas as pd
import numpy as np
import glob

sorted_txt_files = sorted([filename for filename in glob.glob("names/*.txt")])
all_df = []

for filename in sorted_txt_files:
    # current_year is formated as "names/yobXXXX.txt", where XXXX is the year
    current_year = int(filename.split("names/yob")[1][:4])
    curr_df = pd.read_csv(filename, sep=',', names=["Name", "Gender", "Number"])
    curr_df["Year"] = current_year
    all_df.append(curr_df)

df = pd.concat(all_df, axis=0)
print(df.head())
print(df.info())

# Dataset summary statistics
summary = df.describe(include="all").T
print(summary)

# Summary stats for non-numerical columns
non_numerical_summary = df.describe(exclude=np.number).T
print(non_numerical_summary)

# Checking for missing values
missing_values = df.isnull().sum()
print(missing_values)