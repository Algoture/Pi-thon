import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]():;,.<>/?+=*$#@!"
all = lower + upper + number + symbol
length = 20
password = "".join(random.sample(all, length))
print("Your Majboot Password is :",password)