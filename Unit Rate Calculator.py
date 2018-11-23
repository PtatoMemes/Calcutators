
# First Message:

print('''
	Unit Rate Calculator:
	''')
print()

while 1 == 1:
 # Some user Data:

 top = float(input('Type the Top Number: '))
 bottom = float(input('Type the Bottom Number: '))

 # Calculation:

 bottom_unit_rate = 1
 top_unit_rate = top / bottom

 # Printing:

 print('''
	  %s    %s
	 --- = ---
	  %s    %s
	 ''' % (top, top_unit_rate, bottom, bottom_unit_rate))