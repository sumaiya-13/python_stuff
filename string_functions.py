name="sumaiya"
print(len(name))#used to know the length of the string
print(name.endswith("a"))#shows in boolean value from which letter the string ends
print(name.startswith("s"))#shows in boolean value from which letter the string starts
print(name.capitalize())#only capitalize the first letter of the string
# All Python String Methods – With Comments (Descriptive) 🧠

s = "  hello Pookie123\nWelcome to PYTHON world!  "  # sample string
print("Original String:\n", repr(s))

# ✅ Case Methods – used to change case of characters
print("\nCASE METHODS")
print("Upper:", s.upper())         # Converts entire string to UPPERCASE
print("Lower:", s.lower())         # Converts entire string to lowercase
print("Title:", s.title())         # Capitalizes first letter of every word
print("Capitalize:", s.capitalize())  # Capitalizes first letter of string only
print("Swapcase:", s.swapcase())   # Swaps case: lower ↔ upper

# 🔍 Search & Find Methods – used to locate substrings
print("\nSEARCH METHODS")
print("Find 'Python':", s.find("Python"))   # Returns index of first occurrence or -1 if not found
print("rFind 'o':", s.rfind("o"))           # Returns last occurrence index of 'o'
print("Index 'Welcome':", s.index("Welcome"))  # Like find() but raises error if not found
print("Startswith '  hello':", s.startswith("  hello"))  # Checks if string starts with given text
print("Endswith '!  ':", s.endswith("!  "))  # Checks if string ends with given text

# 🔧 Modify or Replace – for changing content
print("\nMODIFY METHODS")
print("Replace 'world' with 'universe':", s.replace("world", "universe"))  # Replaces 'world' with 'universe'
print("Strip:", repr(s.strip()))     # Removes whitespace from both ends
print("LStrip:", repr(s.lstrip()))   # Removes whitespace from left
print("RStrip:", repr(s.rstrip()))   # Removes whitespace from right

# 🧵 Splitting & Joining – for breaking and combining strings
print("\nSPLIT & JOIN")
print("Split:", s.split())           # Splits string into list using spaces
print("Splitlines:", s.splitlines()) # Splits string into list at line breaks
print("Join with '-':", "-".join(["Pookie", "loves", "Python"]))  # Joins list into string using "-"

# 🔎 Boolean Checks – to test type of characters
check_str = "Pookie123"
print("\nBOOLEAN CHECKS (on '{}')".format(check_str))
print("Is Alpha:", check_str.isalpha())   # Returns True if all are letters
print("Is Digit:", check_str.isdigit())   # Returns True if all are digits
print("Is Alnum:", check_str.isalnum())   # Returns True if all are letters or digits
print("Is Space:", check_str.isspace())   # Returns True if all are spaces
print("Is Lower:", check_str.islower())   # Returns True if all are lowercase
print("Is Upper:", check_str.isupper())   # Returns True if all are uppercase
print("Is Title:", check_str.istitle())   # Returns True if string is in Title Case

# 📏 Other Useful Methods – length, count, alignment, etc.
print("\nOTHER USEFUL METHODS")
print("Length of s:", len(s))             # Returns number of characters in string
print("Count of 'o':", s.count("o"))      # Counts how many times 'o' appears
print("zfill (width 20):", check_str.zfill(20))     # Pads string with leading 0s to reach width 20
print("Center (width 30):", check_str.center(30, "*"))  # Centers string with '*' padding
print("Ljust (width 20):", check_str.ljust(20, "-"))    # Left-justifies string in width 20
print("Rjust (width 20):", check_str.rjust(20, "-"))    # Right-justifies string in width 20

# Encoding
print("\nENCODE")
print("Encoded:", s.encode())            # Converts string to bytes (UTF-8 encoding)

# Formatting – inserting variables into strings
name = "Pookie"
language = "Python"
print("\nFORMATTING")
print("format(): Hello {}, welcome to {}!".format(name, language))  # Inserts variables using format()
print(f"f-string: {name} loves {language} ❤️")                      # Inserts variables using f-string (modern way)

# ✅ Done
print("\n✅ All string methods demo completed!")
