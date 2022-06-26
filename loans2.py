ga = [1000, 5.00]
gb = [1000, 5.00]
gc = [1000, 5.00]
gd = [1000, 5.00]
ge = [1000, 5.00]
gf = [1000, 5.00]

loans = [ga, gb, gc, gd, ge, gf]

def calculate_total(loan_array):
    total = 0
    for loan in loan_array:
        total += loan[0]
        print("Outstanding: $" + str(loan[0]) + " | interest: "  + str(loan[1]) + "%")
    print("\ttotal: " + str(total))
    return total

def increment_year(loan_array):
    for loan in loan_array:
        loan[0] += (loan[0] * (loan[1] / 100))

monthly_payment = [100.00, 100.00, 100.00, 100.00, 100.00, 100.00]
def make_monthly_payment(monthly_payment, loans):
    ret_total_payment = 0
    for i in range(0, len(loans)):
        loans[i][0] -= monthly_payment[i]
        ret_total_payment += monthly_payment[i]
    return ret_total_payment

if __name__ == '__main__':
    first_yr = calculate_total(loans)
    increment_year(loans)
    first_yr2 = calculate_total(loans)
    print("\n ||| " + str(first_yr2 - first_yr) + " |||")
    #over x years
    years = 20
    total_payment = 0
    for year in range(0, years):
        print("*** YEAR " + str(year) + " ***")
        curr_sum = calculate_total(loans)
        if(curr_sum < 0):
            print("\ncompletely paid off at " + str(year) + " years")
            print(str("total payment: " + str(total_payment)))
            exit("success")
        increment_year(loans)
        for i in range(0, 12):
            total_payment += make_monthly_payment(monthly_payment, loans)
        #assuming interest triggers at flat % on last day of every year
