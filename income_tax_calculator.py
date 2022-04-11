# Global Variables
FIFTEEN_LAKH = 1500000
TWELVE_HALF_LAKH = 1250000
TEN_LAKH = 1000000
SEVEN_HALF_LAKH = 750000
FIVE_LAKH = 500000
TWO_HALF_LAKH = 250000
STANDARD_DEDUCTION = 50000

# Old tax regime calculation
def oldTaxRegimeCalculator(gross_income, tax_exemption):
	
	income_tax_old = 0
	gross_income -= STANDARD_DEDUCTION + tax_exemption

	if(gross_income > FIFTEEN_LAKH):
		remaining = gross_income - FIFTEEN_LAKH
		tax = (remaining * 30) / 100
		income_tax_old += tax
		gross_income -= remaining

	if(gross_income > TWELVE_HALF_LAKH):
		remaining = gross_income - TWELVE_HALF_LAKH
		tax = (remaining * 30) / 100
		income_tax_old += tax
		gross_income -= remaining

	if(gross_income > TEN_LAKH):
		remaining = gross_income - TEN_LAKH
		tax = (remaining * 30) / 100
		income_tax_old += tax
		gross_income -= remaining


	if(gross_income > SEVEN_HALF_LAKH):
		remaining = gross_income - SEVEN_HALF_LAKH
		tax = (remaining * 20) / 100
		income_tax_old += tax
		gross_income -= remaining

	if(gross_income > FIVE_LAKH):
		remaining = gross_income - FIVE_LAKH
		tax = (remaining * 20) / 100
		income_tax_old += tax
		gross_income -= remaining

	if(gross_income > TWO_HALF_LAKH):
		remaining = gross_income - TWO_HALF_LAKH
		tax = (remaining * 5) / 100
		income_tax_old += tax
		gross_income -= remaining

	return income_tax_old

# New tax regime calculation
def newTaxRegimeCalculator(gross_income, tax_exemption):
	
	income_tax_new = 0
	gross_income -= tax_exemption

	if(gross_income > FIFTEEN_LAKH):
		remaining = gross_income - FIFTEEN_LAKH
		tax = (remaining * 30) / 100
		income_tax_new += tax
		gross_income -= remaining

	if(gross_income > TWELVE_HALF_LAKH):
		remaining = gross_income - TWELVE_HALF_LAKH
		tax = (remaining * 25) / 100
		income_tax_new += tax
		gross_income -= remaining

	if(gross_income > TEN_LAKH):
		remaining = gross_income - TEN_LAKH
		tax = (remaining * 20) / 100
		income_tax_new += tax
		gross_income -= remaining


	if(gross_income > SEVEN_HALF_LAKH):
		remaining = gross_income - SEVEN_HALF_LAKH
		tax = (remaining * 15) / 100
		income_tax_new += tax
		gross_income -= remaining

	if(gross_income > FIVE_LAKH):
		remaining = gross_income - FIVE_LAKH
		tax = (remaining * 10) / 100
		income_tax_new += tax
		gross_income -= remaining

	if(gross_income > TWO_HALF_LAKH):
		remaining = gross_income - TWO_HALF_LAKH
		tax = (remaining * 5) / 100
		income_tax_new += tax
		gross_income -= remaining

	return income_tax_new

# Finds the preferred Tax Regime for you
def findBetterTaxRegime(income_tax_old, income_tax_new):

	print("===============================================================================")

	if(income_tax_new == income_tax_old):
		print("The income tax difference between Old and New Tax Regime is 0 in this case. You can opt either based on your preference.")

	else:
		preferred_income_tax = min(income_tax_new, income_tax_old)

		if(preferred_income_tax == income_tax_new):
			difference = income_tax_old - income_tax_new
			print("Please opt for New Tax Regime as you will have to pay Rs. {} lesser".format(difference))

		else:
			difference = income_tax_new - income_tax_old
			print("Please opt for Old Tax Regime as you will have to pay Rs. {} lesser".format(difference))

	print("===============================================================================")

gross_income = int(input("Enter Gross income: "))
tax_exemption_old = int(input("Enter exemptions for old tax regime excluding 50k of standard deduction: "))
tax_exemption_new = int(input("Enter exemption for new tax regime (Employer PF amount): "))

income_tax_old = oldTaxRegimeCalculator(gross_income, tax_exemption_old)
income_tax_new = newTaxRegimeCalculator(gross_income, tax_exemption_new)

print("Income Tax for Old tax regime = " + str(income_tax_old))
print("Income Tax for New tax regime = " + str(income_tax_new))

findBetterTaxRegime(income_tax_old, income_tax_new)
