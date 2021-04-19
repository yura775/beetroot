phone=input('Please write down your number')
if len(phone)!=10:
    print('Your number must consist of 10 digits. Please try once again')
elif phone.isnumeric():
    print('Thank you! We will call you very soon')
else:
    print('Hmm, looks like your phone number contains letters... please try once more')

