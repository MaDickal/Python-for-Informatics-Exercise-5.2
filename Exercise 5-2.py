total = 0
count = 0
maximum = None
minimum = None
while True:
    numinput = raw_input('Enter a number: ')
    if numinput == 'done':						# repeatedly reads numbers until 'done' is entered
        break
    else:
        try:
            numinput = int(numinput)
            total = total + numinput			# runs a total on all numbers entered
            count = count + 1					# counts how many numbers are entered
            if maximum is None and minimum is None:	# first number becomes both the min and max
                maximum = numinput
                minimum = numinput
            elif numinput > maximum:
                maximum = numinput
            elif numinput < minimum:
                minimum = numinput
        except:
            print 'Invalid input'				# error message if input is not 'done' or a number
print 'Total:', total, 'Count:', count, 'Maximum:', maximum, 'Minimum:', minimum