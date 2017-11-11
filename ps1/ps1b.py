r = 0.04

annual_salary=int(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percentage to save, as a decimal: "))
total_cost=int(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: "))

starting_salary=annual_salary
portion_down_payment=0.25
down_payment=portion_down_payment*total_cost
monthly_salary=annual_salary/12
current_savings=0
months=0

while(current_savings<down_payment):
    current_savings+=current_savings*(r/12)
    current_savings+=monthly_salary*portion_saved
    months+=1
    if(months%6==0):
        monthly_salary+=monthly_salary*semi_annual_raise
    
print("Number of months:", months)
    