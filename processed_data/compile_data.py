
# Compiles turnstile data in raw_data directory into 'compiled_data_unsorted.csv'. 
# Text file order is arbitrary, does not sort.

import os
import pandas as pd
raw_data_directory= '../raw_data/'
data_frames_list=[]
index=0
for file in os.listdir(raw_data_directory):
	print(file)
	if file.endswith('.txt'):
		data_frames_list.append(pd.read_csv(raw_data_directory + file))
		print(type(file))

df=pd.concat(data_frames_list)
df.to_csv('compiled_data_unsorted.csv')