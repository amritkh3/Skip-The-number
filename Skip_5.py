"""wap to print from 1-30. but skip all the number divisible by 5
1.declare a variable num and asssign it with value 1
2.run while condition to run until the value of num is lesser than 31
3.use if condition uder while loop which is 
     if num%5==0: then continue
     continue in while loop skip the rest of the code when the condition is true.
4. print the value of num when the if condition is not  true .
5.increment the value of num to num=num+1    
"""
num=1
while num<31:
    if num%5==0:#(if the modulus is 0 then it will skip the number)
        num=num+1
        continue
    
    print(num)
    num=num+1    
    



