import pandas as pd
data = pd.read_csv('big_mart_sales.csv')
#df = pd.DataFrame ({
 # 'roll_no': [101,102,103,104,105,106],
 # 'name':['John','Anna','Peter','Linda','Robert','Lisa'],
 # 'marks': [20,22,15,50,15,4],
 # 'city':['New York','Paris','Berlin','London','Tokyo','Mumbai'],
 # 'grade' :['A', 'B', 'C', 'B', 'C', 'A']
#})
#print(df)
#df.sort_values(by=['marks', 'grade'],ascending=[False, True],  inplace=True)
#df.reset_index(drop=True,inplace=True)
#phone_no = pd.DataFrame({'phone_no':[123456789, 987654321, 123456789, 987654321, 12345345, 6784570348]})
#combined_data = pd.concat([df, phone_no] , axis= 1)
#print(combined_data)
##SQL JOINS
#city_state_mapping = pd.DataFrame({
 # 'city':['New York','Paris','Berlin','bangalore','Tokyo','Mumbai'],
  #'state':['NY','FR','BR','BG','TK','MH']
#})
#print(city_state_mapping)
#print(df.merge(city_state_mapping, how='left', on='city'))
#roll_no = pd.DataFrame(
 # {
  #'roll_no': [101, 103]
  #}
#)
#print(df.merge(roll_no, how='right', on='roll_no'))
#student_placement= pd.DataFrame({
 # 'roll_no': [102,104,106],
  #'company':['Google','Amazon','Facebook'],
  #'package': [3, 4, 5  ]
#})
#print(df.merge(student_placement, how='outer'))
#print(data.head())
#print(data['Outlet_Type'].mode())
#print(data.describe())

#numeric_cols = data.select_dtypes(include=['number']).columns
#d = data.groupby(['Item_Type', 'Outlet_Size'])[numeric_cols].mean()
#print(d['Item_MRP'])
#print(pd.pivot_table(data, index=['Item_Type', 'Outlet_Size'], values=['Item_MRP'], aggfunc= 'mean'))
print(pd.crosstab(data['Item_Type'], data['Outlet_Size']))

