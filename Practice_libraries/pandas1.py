import pandas as pd
data = {
   'Name':['Mahima','Rajshree','sushma','karishma'],
   'Maths':[90,78,90,56],
   'Science':[87,34,87,90],
   'English':[56,76,23,98]
}
df = pd.DataFrame(data)


df['Average']= df[['Maths','Science','English']].mean(axis=1)
df['Total'] = df[['Maths','Science','English']].sum(axis=1)

while True:
  print("1. Display Data")
  print("2.Display Average")
  print("3.Total marks")
  print("4.sort student by marks")
  print("5.display topper")
  print("6.filter student by more than 80")
  print("7.Exit")

  choice = int(input("Enter your choice:"))
  if choice ==1:
    print("\n Full data \n ",df)
  elif choice ==2:
    print("Name and average: \n", df[['Name','Average']])
  elif choice ==3:
    print("Name and Total : \n", df[['Name','Total']])
  elif choice ==4:
    print("Sorted marks: \n", df.sort_values(by='Total', ascending=False))
  elif choice==5:
    topper = df.loc[df['Average'].idxmax()]
    print("Topper:\n", topper)
  elif choice==6:
    print("Students who scored more than 80:\n", df[df['Average'] > 80])
  elif choice==7:
    print("Exiting....")
    break

  else:
    print("Invalid choice. Please try again.")