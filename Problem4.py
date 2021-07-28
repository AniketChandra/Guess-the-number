#You can change the value of n to be any number of your choice to make someone guess it
n = 105
k = 7
p = 0
while(k<=7):
    print("No. of attempts:", k)
    print("Guess the number:")
    num = int(input())
    if num < n - 10 and k != 1:
        print("Your number is less, Try again!")
        k = k - 1
        p = p+1
        continue
    elif n - 10 <= num <= n - 5 and k != 1:
        print("Your number is close. Try again!")
        k = k - 1
        p = p+1
        continue
    elif n - 5 < num < n and k != 1:
        print("Your number is very close. Try again! ")
        k = k - 1
        p = p+1
        continue
    elif num == n and k != 1:
        print("Congrats, you guessed the number")
        k = k - 1
        p = p+1
        print("Number of guesses you took:", p)
        break
    elif n < num < n + 5 and k != 1:
        print("Your number is very close. Try again! ")
        k = k - 1
        p = p+1
        continue
    elif n + 5 <= num <= n + 10 and k != 1:
        print("Your number is close. Try again!")
        k = k - 1
        p = p+1
        continue
    elif num > n + 10 and k != 1:
        print("Your number is big, Try again!")
        k = k - 1
        p = p+1
        continue
    elif k == 1:
        p = p+1
        if num == n:
            print("Congrats, you guessed the number")
            print("Number of guesses you took:", p)
            break
        else:
            print("Game Over!", "You run out of the no. of attempts")
            break

#Created by: Aniket Chandra
#Date: 29th July 2021