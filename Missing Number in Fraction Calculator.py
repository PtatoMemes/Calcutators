while True:
 top_1 = float(input('Type a top Number: '))
 bottom_1 = float(input('Type a bottom Number: '))
 which_side = input('Top X or Bottom X? (top or bottom): ')

 if which_side == 'bottom':
	 top_2 = float(input('Type the Top: '))
	 bottom_1_x_top_2 = bottom_1 * top_2
	 print('%sx = %s' % (top_1, bottom_1_x_top_2))
	 final_bottom_1_x_top_2 = bottom_1_x_top_2 / top_1
	 print('x = %s' % (final_bottom_1_x_top_2))

 elif which_side == 'top':
	 bottom_2 = float(input('Type the Bottom: '))
	 top_1_x_bottom_2 = top_1 * bottom_2
	 print('%sx = %s' % (bottom_1, top_1_x_bottom_2))
	 final_top_1_x_bottom_2 = top_1_x_bottom_2 / bottom_1
	 print('x = %s' % (final_top_1_x_bottom_2))

 else:
	 print('error')		