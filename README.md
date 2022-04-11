# Income-Tax-Calculator
Helps compare between New and Old Tax Regime.

## Sample Console Input/Output
```
saanika@gupta:~/Desktop$ python3 income_tax_calculator.py 
Enter Gross income: 1200000
Enter exemptions for old tax regime excluding 50k of standard deduction: 222000
Enter exemption for new tax regime (Employer PF amount): 72000
Income Tax for Old tax regime = 98100.0
Income Tax for New tax regime = 100600.0
===============================================================================
Please opt for Old Tax Regime as you will have to pay Rs. 2500.0 lesser
===============================================================================
```

Here in Old Regime, 2,22,000 includes 1.5 lac 80C, 72k of Employer PF. You can also include HRA amount here if paying rent.
Formula for calculating HRA exemption is min(HRA given, 50%/40% basic depending on the city, Rent paid - 10% basic)

In New Regime, we only have Employer PF exempted.
