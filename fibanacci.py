#Python program to print the fibonacci sequence using while loop
#Number of terms to display
n_terms=int(input("enter the number of fibanacci terms to display:"))
#First two terms
a,b=0,1
count=0
#check if the number of terms is valid
if n_terms==1:
    print("please enter a positive integer.")
elif n_terms==1:
     print("fibanacci sequence:")
     print(a)
else:
     print("fibanacci sequence:")
     while count<n_terms:
        print(a,end="")
        #updating values
        a,b=b,a+b
        count+=1
                
