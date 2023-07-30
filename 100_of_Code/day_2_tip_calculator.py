print('Welcome to the tip calculator|')
bill = float(input('What is the total bill? $'))
percentage = int ( input ( 'How much tip would you like to give? 10, 12, or 15? ' ) )
persons = int ( input('How many people to split the bill?' ) )
tip_percentage = (100 + percentage) / 100
bill_with_tip = bill * tip_percentage
tip_each = round((bill_with_tip / persons),2)
print('Each person should pay: $' + str(tip_each))
