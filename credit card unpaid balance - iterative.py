# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:31:04 2016

@author: Shady Hegazy
"""

balance=42
monthlyPaymentRate=0.04
annualInterestRate=0.2
monthlyInterestRate=annualInterestRate / 12.0
month=0
while month<12:
        mp=monthlyPaymentRate*upb
        balance=(1+monthlyInterestRate)*upb
        upb=balance-mp
        month+=1
print('Remaining balance: ' + str(round(upb,2)))