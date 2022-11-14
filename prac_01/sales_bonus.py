"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales < 1000
        bonus = sales*0.1
    else
        bonus = sales*0.15
    display Your bonus is {bonus:.0f}
    get sales
"""

LOW_BONUS = 0.1
HIGH_BONUS = 0.15
SALES_LIMIT = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_LIMIT:
        bonus = sales*LOW_BONUS
    else:
        bonus = sales*HIGH_BONUS
    print(f"Your bonus is {bonus:.0f}")
    sales = float(input("Enter sales: $"))