import numpy as np

def customers_greatest_wealth(customers_accounts):
    sum_credits = []
    for account in customers_accounts :
        customers_credit = 0;
        for position in account:
            customers_credit += position
        sum_credits.append(customers_credit)    
    return max(sum_credits)    

 # main
def main():
    print("ergebnis {}".format(customers_greatest_wealth( [[1, 2, 3], [4, 5, 6], [2 ,5, 7]])))

if __name__ == "__main__":
    main()
