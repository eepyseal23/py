# Function that gets integers when picking options and entering data
def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Enter a positive number")
                continue

        except ValueError:
            print("Enter a valid number")
        else:
            return number

# Function that gets decimals when entering data
def get_float(prompt):
    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                print("Enter a positive number")
                continue
            
        except ValueError:
            print("Enter a valid number")
        else:
            return number
        
# Function to get sex 
def get_sex():
    while True:
        sex = input("Enter biological sex (M/F): ").upper()

        if sex in ["M", "F"]:
            return sex

        print("Sex must be either M or F")