keep_going = 'y'
while keep_going == 'y':
    sales = float(input('Enter the amonut of sales: '))
    com_rate = float(input('Enter the commission rate: '))
    comimissinon = sales * com_rate
    print(f'The commission is ${comimissinon: .2f}')
    keep_going = input('Do you want to clculate another' + \
                       'commission (Enter y for yes): ') 
                       
                       