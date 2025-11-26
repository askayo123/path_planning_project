import pandas as pd
import os
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

file_path= 'data\BrandsHatchLayout.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")  
#    print(df.to_string())

else:
    print(f"File not found: {file_path}")

route=pd.DataFrame({'side': ['left','right']})
right_route=df[df['side']=='right'].copy()
right_route['x']=pd.to_numeric(right_route['x'], errors='coerce')
right_route['y']=pd.to_numeric(right_route['y'], errors='coerce')
right_route=right_route.interpolate(method='linear', limit_direction='both' )
right_route=right_route.ffill().bfill()
first_row=right_route.iloc[[0]]
right_route=pd.concat([right_route, first_row], ignore_index=True)
right_route=right_route.reset_index(drop=True)


left_route=df[df['side']=='left'].copy()
left_route['x']=pd.to_numeric(left_route['x'], errors='coerce')
left_route['y']=pd.to_numeric(left_route['y'], errors='coerce')
left_route=left_route.interpolate(method='linear', limit_direction='both' )
left_route=left_route.ffill().bfill()
first_row=left_route.iloc[[0]]
left_route=pd.concat([left_route, first_row], ignore_index=True)
left_route=left_route.reset_index(drop=True)

min_length=min(len(right_route), len(left_route))
right_route=right_route.iloc[:min_length]   
left_route=left_route.iloc[:min_length]

mid_x= (right_route['x'] + left_route['x']) / 2
mid_y= (right_route['y'] + left_route['y']) / 2

mid_route=pd.DataFrame({'x': mid_x, 'y': mid_y})


plt.plot(left_route['x'], left_route['y'],label='Left Route',color='blue', alpha=0.3 )
plt.plot(right_route['x'], right_route['y'], label='Right Route',color='red', alpha=0.3 )
plt.plot(mid_route['x'], mid_route['y'], color='green', label='Mid Route' )
plt.legend()
plt.show()

