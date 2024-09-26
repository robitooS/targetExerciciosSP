def fibonacci_verification(number):
    fibo_seq = [0, 1]
    
    while number not in fibo_seq:
        
        fibo_seq.append((fibo_seq[-1] + fibo_seq[-2]))
        
        if fibo_seq[-1] > number:
            print('The number is not in the sequence\n')
            print(fibo_seq)
            break
        
        if fibo_seq[-1] == number:
            print('The number is in the sequence ')
            print(fibo_seq)
            break
        
inputUser = int(input('Type the number: '))
fibonacci_verification(inputUser)