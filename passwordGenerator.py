#Passward Generator
import sys
import random

def complex(n_chars):
    upper =[
        'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','M',
        'N','O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X','Y', 'Z'
        ]
    lower = [
        'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m',
        'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z'
        ]
    syb= [
        '!', '@', '#', '$', '%', '^','&', '*', '(', ')', '-', '_','=', '+', '{',
        '}', '[', ']','|', '\\', ':', ';', '"', "'",'<', '>', ',', '.', '?', '/'
        ]
    digits=[
        0,1,2,3,4,5,6,7,8,9
        ]
    password =[]
    password.append(random.choice(lower))
    password.append(str(random.choice(digits)))
    password.append(random.choice(upper))
    password.append(random.choice(syb))
    for _ in range(n_chars-4):
        choice =random.choice(["digits","lower","upper","syb"])
        if choice == "digits":
            password.append(str(random.choice(digits)))
        if choice == "lower":
            password.append(random.choice(lower))
        if choice =="upper":
            password.append(random.choice(upper))
        if choice == "syb":
            password.append(random.choice(syb))
    random.shuffle(password)
    _password = "".join(password)
    return _password



def medium(n_chars):
    upper =[
        'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L','M',
        'N','O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X','Y', 'Z'
        ]
    lower = [
        'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m',
        'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x','y', 'z'
        ]
    digits=[
        0,1,2,3,4,5,6,7,8,9
        ]
    password =[]
    password.append(random.choice(lower))
    password.append(str(random.choice(digits)))
    password.append(random.choice(upper))
    for _ in range(n_chars-3):
        choice =random.choice(["digits","lower","upper",])
        if choice == "digits":
            password.append(str(random.choice(digits)))
        if choice == "lower":
            password.append(random.choice(lower))
        if choice =="upper":
            password.append(random.choice(upper))

    random.shuffle(password)
    _password = "".join(password)
    return _password

def simple(n_chars):
    digits=[
        0,1,2,3,4,5,6,7,8,9
        ]
    password =""
    for _ in range(n_chars):
        password +=str(random.choice(digits))

    return password


def main():
    try:
        print("Hai, welcome to Password Generator")
        value =int(input("1.Simple \n 2.Medium \n 3.Complex\nChoose the Complexity for your password:"))

        if value > 3 or value < 1:
             sys.exit("Choose complexity  between  1-3")

        chars=int(input("choose number of characters would be present in your password:"))
        if chars < 4:
            sys.exit("Alteast 4 no of character resent in password")
        if chars > 15 :
            sys.exit("Maximum number of charcters is 15 ")
    except ValueError:
        sys.exit("Numeric values only accepted")
    password =""
    if value == 1:
        password =simple(chars)
    if value == 2:
        password= medium(chars)
    if value == 3:
        password=complex(chars)
    print(password)




if __name__ == "__main__":
    main()
