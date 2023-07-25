installments = 0
price = float(input('How much does it cost? '))
formpayment = float(input('''\n1) Cash/Check;
2) Debit card;
3) Credit card.\n
What is the payment method? '''))
if formpayment == 3:
    installments = int(input('\nHow many installments? '))

if formpayment == 1:
    print('\nYour buy will cost ${:.2f}. (10% off ${:.2f})'.format(price - price * 0.10, price))
elif formpayment == 2:
    print('\nYour buy will cost ${:.2f}. (5% off ${:.2f})'.format(price - price * 0.05, price))
elif formpayment == 3 and installments <= 2:
    print('\nYour buy will cost ${:.2f}.)'.format(price))
elif formpayment == 3 and installments > 2:
    print('''\nYour buy will cost ${:.2f}. (20% interest rate)
{} installments of ${:.2f}.'''.format(price + price * 0.20, installments, (price + price * 0.20) / installments))
else:
    print('\nError: 404 (Try again).')
