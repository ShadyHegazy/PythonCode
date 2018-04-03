# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
monthlyPaymentRate=0.04
annualInterestRate=0.2
b=42
month=11
monthlyInterestRate=annualInterestRate / 12.0
def up(month):
    """
    input: month= months of credit card usage
    output:remaining balance at end of usage period
    """    
    if month==0:
        return (1-monthlyPaymentRate)*b
    else:
        return (1-monthlyPaymentRate)*((annualInterestRate+12)/12)*(up(month-1))
print('Remaining balance: ' + str(round(up(month),2)))
        
    