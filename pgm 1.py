def calculate_compound_interest(principal, rate, time):
    """
    Calculate the compound interest.
    :param principal:the initial amount of money(float or int).
    :param rate:the annual interest rate(float or int).
    :param time:the number of periods the money is invested for(float or int).
    :rerturn:the compound interest(float).
    """
    #Convert rate from percentage to decimal
    rate_decimal=rate/100
    #Calculate the compound interest
    amount=principal*(1+rate_decimal)**time
    compound_interest=amount-principal
    return compound_interest
#input values
principal=float(input("enter the principal amount:"))
rate=float(input("enter the annual interest rest(in percentage):"))
time=float(input("enter the number of periods:"))
#Calculate compound interest
interest=calculate_compound_interest(principal, rate, time)
#output the result
print(f"the compound interest is:{interest:.2f}")
