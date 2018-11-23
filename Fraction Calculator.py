
# Begining text:

print('''
	===========================
	=== Fraction Calculator ===
	===========================
	V: 1.1.1
	''')

repeat = True

# Loops and Things:

while repeat == True:

 # The Numbers that are in the Math:

 top_1 = int(input('Type the First Numerator: '))
 bottom_1 = int(input('Type in the First Denominator: '))
 symbol = input('Type an Equation: ')
 top_2 = int(input('Type the Second Numerator: '))
 bottom_2 = int(input('Type in the Second Denominator: '))

 # Preventing 0 or Null:

 def check(the_var):
	 if the_var == 0:
		 print('Error, Invalid Number(s) or Null Value.')
		 exit()	

 check(top_1)
 check(top_2)
 check(bottom_1)
 check(bottom_2)

 # The math:

 if symbol == '+':
	
	 if bottom_1 == bottom_2:
		 multi_add = bool(False)
		 top_answer = top_1 + top_2
		 bottom_answer = bottom_1

	 elif bottom_1 != bottom_2:

		 multi_add = bool(True)
		 original_top_1 = top_1
		 original_top_2 = top_2
		 original_bottom_1 = bottom_1
		 original_bottom_2 = bottom_2

		 bottom_answer = bottom_1 * bottom_2
		 top_1 = top_1 * bottom_2
		 top_2 = top_2 * bottom_1
		 top_answer = top_1 + top_2
		 bottom_1 = bottom_answer
		 bottom_2 = bottom_answer

	 else:
		 print('Error, Unown Error')
		 exit()

 elif symbol == '-':
	 if bottom_1 == bottom_2:
		 multi_sub = bool(False)
		 top_answer = top_1 - top_2
		 bottom_answer = bottom_1

	 elif bottom_1 != bottom_2:

		 multi_sub = bool(True)
		 original_top_1 = top_1
		 original_top_2 = top_2
		 original_bottom_1 = bottom_1
		 original_bottom_2 = bottom_2

		 bottom_answer = bottom_1 * bottom_2
		 top_1 = top_1 * bottom_2
		 top_2 = top_2 * bottom_1
		 top_answer = top_1 - top_2
		 bottom_1 = bottom_answer
		 bottom_2 = bottom_answer

	 else:
		 print('Error, Unown Error')
		 exit()

 elif symbol == '*':
	 original_top_1 = top_1
	 original_top_2 = top_2
	 original_bottom_1 = bottom_1
	 original_bottom_2 = bottom_2

	 top_answer = top_1 * top_2
	 bottom_answer = bottom_1 * bottom_2

 elif symbol == '/':
	 original_top_2 = top_2
	 original_bottom_2 = bottom_2
	 top_2 = bottom_2
	 bottom_2 = original_top_2
	 top_answer = top_1 * top_2
	 bottom_answer = bottom_1 * bottom_2

 else:
	 print('===Error, invalid Symbol. (symbol != +, - * or /)')

 # Printing the answer code:

 if symbol == '+':
	 if multi_add == False:
		 print('''
			  %s     %s    %s
			 --- %s --- = ---
			  %s     %s    %s
			 ''' % (top_1, top_2, top_answer, symbol, bottom_1, bottom_2, bottom_answer))

	 elif multi_add == True:
		 print('''
			  Original Equation:

			  %s     %s
			 --- %s ---
			  %s     %s
			''' % (original_top_1, original_top_2, symbol, original_bottom_1, original_bottom_2))

		 print('''
			  Answer:

			  %s     %s    %s
			 --- %s --- = ---
			  %s     %s    %s
			 ''' % (top_1, top_2, top_answer, symbol, bottom_1, bottom_2, bottom_answer))

	 else:
		 print('Error, Unown Error.')
		 exit()

 elif symbol == '-':
	 if multi_sub == False:
		 print('''
			  %s     %s    %s
			 --- %s --- = ---
			  %s     %s    %s
			 ''' % (top_1, top_2, top_answer, symbol, bottom_1, bottom_2, bottom_answer))

	 elif multi_sub == True:
		 print('''
			 Original Equation:

			  %s     %s
			 --- %s ---
			  %s     %s
			 ''' % (original_top_1, original_top_2, symbol, original_bottom_1, original_bottom_2))

		 print('''
			  Answer:
			 
			  %s     %s    %s
			 --- %s --- = ---
			  %s     %s    %s
			 ''' % (top_1, top_2, top_answer, symbol, bottom_1, bottom_2, bottom_answer))

	 else:
		 print('Error, Unown Error.')
		 exit()

 elif symbol == '*':
	 print('''
		  Answer:
		
		   %s     %s    %s
		  --- %s --- = ---
		   %s     %s    %s
		 ''' % (top_1, top_2, top_answer, symbol, bottom_1, bottom_2, bottom_answer))

 elif symbol == '/':
	 print('''
		  Original Equation:
		   %s     %s
		  --- %s ---
		   %s     %s
		 ''' % (top_1, original_top_2, symbol, bottom_1, original_bottom_2))
	
	 print('''
		  Answer:
		   %s    %s     %s
		  --- * --- = ---
		   %s    %s     %s
		 ''' % (top_1, top_2, top_answer, bottom_1, bottom_2, bottom_answer))

 else:
	 exit()

print('Exiting...')	
exit()