def printTheAarray(arr,n):
 for i in range(n):
    print(arr[i],end=" ")
    print()
    #function to generate all binary strings
    def generateAllBinaryStrings(n,arr,i):
        if i==n:
            printTheAarray(arr,n)
            return
        arr[i]=0
        generateAllBinaryStrings(n,arr,i+1)
        arr[i]=1
        generateAllBinaryStrings(n,arr,i+1)
        #Driver code
        if_name_=="_main_:"
             n=4
             arr=[none]*n
             generateAllBinaryStrins(n,arr,0)
  
