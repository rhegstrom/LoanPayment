# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:56:43 2022

@author: rhegstrom ( Roger Hegstrom  )

The formula for how much your loan payment would be(Pmt), If were you to borrow (PV) dollars at APR of (r)% for (n) months:
Pmt =  r/1200*PV/(1-(1+(r/1200))**(-n))       

# r/1200 because we have annual percentage rate and we need rate/time period, 
i.e. rate/month and we need it as a decimal, not a percent... 
For example APR = 5.5, expressed as a decimal is 5.5/100, 
and then express this as a monthly amount 5.5/(100*12)

Assignment: write a Python program that takes
  1. how much you borrow (PV),
  2. the annual percentage rate, r, and
  3. how many months you pay on the loan

- Compute and print the monthly payment

You submit the loanPmt.py file, I"ll load it and run it to see if you got it right

Run program in a loop until pv is '0', then exit loop

"""

def calculatePayment(principle, apr, term):
    """
    

    Parameters
    ----------
    principle : float
        Amount to borrow.
    apr : float
        Annual percentage rate.
    term : int
        Length of the loan in months.

    Returns
    -------
    float
        Calculated monthly payment.

    """
    return apr / 1200 * principle / (1 - (1 + (apr / 1200 )) ** (-term))


print('Loan payment calculator script\n')

while True:
    inp = input('Enter the loan amount(ex: 5000.00): ')
    if inp == '0':
        print('Exiting...')
        break
    
    principle = float(inp)
    apr = float(input('Enter the APR%(ex: 5.0): '))
    term = int(input('Enter the term in months(32): '))

    pmt = calculatePayment(principle, apr, term)

    print(f'Your monthly payment is ${pmt:,.2f}/month\n')


