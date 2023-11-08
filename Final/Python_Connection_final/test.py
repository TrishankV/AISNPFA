import re
def verify (s_phone,r_phone,s_add,r_add,email):
    r = False
    s = False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        print("Email Verfied")
    else:
        print("Wrong Email Format")
        return False
    if len(s_phone) == 10 and len(r_phone)== 10 :
        r = is_alpha_string(s_add)
        s = is_alpha_string(r_add)
    else:
        print("check phone number not 10 digits")
    if r == False or s == False :
        return False
    else:
        print("Verfied")
        return True

def con(email,ph):
    if len(ph) == 10 :
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern,email):
            print("Email Verfied")
            return True
        else:
            print("Wrong Email Format")
            return False
    else:
        print("Please Check Phone number 10 digits required !!!")
        return False


def is_alpha_string(input_string):
    for char in input_string:
        if not char.isalpha():
            print (f'{input_string} address is not pure alphabetical')
            return False
    return True

if __name__ == "__main__":
    p=verify('1020304040','7898989889','e','dje',"vedant@gmail.com")
    print(p)
