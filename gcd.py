def gcd(a,b):
    """
    compute the greatest common divisor(GCD)of two numbers using the Euclidean algorithm.
    :param a:Fist number(integer).
    :param b:second number(integer).
    :return:GCD of a and b.
    """
    while b!=0:
     a,b=b,a%b
        #Update a to b and b to the remainder of a divided by b
     return a
#example usage
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=gcd(num1,num2)
print(f"The GCD of {num1}and{num2} is:{result}")
    
    
