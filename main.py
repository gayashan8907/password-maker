from random import sample,shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the Password maker")

user_letters = int(input("How many letters? "))
user_symbols = int(input("How many symbols? "))
user_numbers = int(input("How many numbers? "))


password_list =sample(letters,k=user_letters)+sample(symbols,k=user_symbols)+sample(numbers,k=user_numbers)

shuffle(password_list)

print("your password is",''.join(password_list))
print("Thank you for using Password maker")