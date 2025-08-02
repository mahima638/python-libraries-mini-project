import numpy as np


def show_options():
   print("Choose numbers to perform an task:")
   print("Choose 1 for addition")
   print("Choose 2 for subraction")
   print("Choose 3 for multiplication")
   print("Choose 4 for transpose")
   print("Choose 5 for exit")



def take_user_input():
     rows = int(input("Enter the numbers of rows:"))
     cols = int(input("Enter the numbers of columns:"))
     Elements= []
     for _ in range(rows):
       row = list(map(int,input().split()))
       Elements.append(row)
     return np.array(Elements)  
      

def addmatrix():
  print("Matrix A:")
  A = take_user_input()
  print("Matrix B:")
  B = take_user_input()
  print("Resultant Matrix:", A +B)
def submatrix():
    print("Matrix A:")
    A = take_user_input()
    print("Matrix B:")
    B = take_user_input()
    print("Resultant Matrix:", A -B)
def mulmatrix():
  print("Matrix A:")
  A = take_user_input()
  print("Matrix B:")
  B = take_user_input()
  print("Resultant Matrix:", A * B)
def  transposematrix():
  print("Matrix A:")
  A = take_user_input()
  print("Matrix B:")
  B = take_user_input()
  print("Resultant Matrix:", A.T)
while(True):
  show_options()
  choice = int(input("Enter your choice:"))
  if choice == 1:
    addmatrix()
  elif choice == 2:
    submatrix()
  elif choice == 3:
    mulmatrix()
  elif choice == 4:
    transposematrix()
  elif  choice==5:
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please try again.")