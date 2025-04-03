# # Ask users for their names
# name = input("What is your name? ").strip().title()  # Everything can be chained in one line thus reducing lines of code

# # Remove whitespaces from str and Capitalize first letters
# # name = name.strip().title()

# # Capitalize first letters
# # name = name.title()

# # split user's name to first and last names
# first, name = name.split()

# # Say hello to the user
# print(f"hello, {first}")
# Define the main function
def main():
    hello()
    name = input("What is your name? ").strip().title()
    first, last = name.split()
    hello(first)

# Define the hello function
def hello(to="dear,"):
    print("Hello", to)

# Call the main function which in turn calls the hello function
main()



