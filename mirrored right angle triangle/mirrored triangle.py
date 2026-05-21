height=(int(input("what is the height?")))
for row_number in range(1, height+1):
    num_stars=row_number
    num_spaces=(height-row_number)
    print(" "*num_spaces+"*"*num_stars)