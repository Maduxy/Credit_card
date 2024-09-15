def validate (serial_no):
    digits = list(map(int,str(serial_no)))
    second_elements = digits[0::2]
    print(second_elements)
    remaining_elements = digits[1::2]
    print(remaining_elements)
    double = [x*2 for x in second_elements]
    print(double)
    singularize = []
    for x in double:
        if x >9 :
            # single_digit =list(map(int,str(x)))
            singularize.append(x % 9)
        else:
            singularize.append(x)
    print (singularize)
    New_list = sum(singularize + remaining_elements)
    print (New_list)
    if New_list % 10 == 0 :
        result = True
    else:
        result = False

    print("Valid card number" if result == True else "invalid card number")
    return result


custom = validate (1378946258794531)

