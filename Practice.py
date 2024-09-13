def validate (serial_no):
    digits = list(map(int,str(serial_no)))
    second_elements = digits[0::2]
    remaining_elements = digits[1::2]
    double = [x*2 for x in second_elements]
    singularize = []
    for x in double:
        if x >9 :
            # single_digit =list(map(int,str(x)))
            singularize.append(x % 9)
        else:
            singularize.append(x)
    New_list = sum(singularize + remaining_elements)
    if New_list % 10 == 0 :
        print("Valid card number")
    else:
        print("invalid card number")


custom = validate (123547896354)

