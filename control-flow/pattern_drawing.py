while True:
   try:
       size = int(input("Enter the size of the pattern:  "))
       if size > 0:
          break
       else:
           print("Enter a positive integer")
   except:
       print("Invalid input. Please enter a valid positive integer.")

row = 0

while row < size:
    for col in range(size):
        print("*", end=" ")
    print()
    row += 1
