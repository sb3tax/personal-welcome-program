#welcome banner 
print("==================================")
print("MY PERSONAL PROGRAM")
print("==================================")

#ask the user for his information 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
lucky_number = int(input("What is your lucky number: "))

#age checker 
if age < 13 :
    print("You're a kid! 🧒")
elif age >= 18 :
    print("You're an adult! 👨")
else :
    print("You're a teenager! 🧑")

#Counting the lucky number
print("Counting to your lucky number...")
for i in range(lucky_number):
    print(f"{i+1}")

#counting down
print("Now counting down...")
while lucky_number != 0 :
    print(f"{lucky_number} ...🚀")
    lucky_number = lucky_number - 1
    

#Final message
print(f"Thanks, {name}! Have a great day! ✨")

