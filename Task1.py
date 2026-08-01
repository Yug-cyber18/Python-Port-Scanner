import string

password = input("Enter a password: ")

print("\nPassword Audit Report")
print("-" * 25)

if len(password) >= 8:
    print("Minimum Length (8): Passed")
else:
    print("Minimum Length (8): Failed")

if any(c.isupper() for c in password):
    print("Uppercase Letter: Present")
else:
    print("Uppercase Letter: Missing")

if any(c.islower() for c in password):
    print("Lowercase Letter: Present")
else:
    print("Lowercase Letter: Missing")

if any(c.isdigit() for c in password):
    print("Number: Present")
else:
    print("Number: Missing")

if any(c in string.punctuation for c in password):
    print("Special Character: Present")
else:
    print("Special Character: Missing")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password) and
    any(c in string.punctuation for c in password)):
    print("\nPassword Strength: STRONG")
else:
    print("\nPassword Strength: WEAK")