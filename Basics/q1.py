'''
  Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
   they need to put down 20%.
  Print the down payment.
'''

price = 100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment : ${down_payment}")