lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [alpha1+alpha2+str(digit1)+str(digit2) for alpha1 in lowercase for alpha2 in lowercase for digit1 in digits for digit2 in digits]
print(correct_answer == answer)
# print (correct_answer)[10]
# print (answer)[10]