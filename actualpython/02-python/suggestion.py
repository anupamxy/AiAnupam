snack=input("Enter your snack")
print(f"your snack is {snack}")
if snack=="samosa" or snack=="cookies":

    print(f"You like savory snacks!,{snack}")
else:
    print(f"sorry we dod'nt serve this snacks,{snack}")


size=input("Enter the size of pizza")
if size=="small":
    print("You have ordered a small pizza")
elif size=="medium":
    print("You have ordered a medium pizza")
elif size=="large":
    print("You have ordered a large pizza")
else:
    print("Invalid size entered")