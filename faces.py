# Define main
def main():
    # Promp the user for input
    user_input = input("Enter text and your emoticon here:   ")
    # Call the convert function and print the output
    print(convert(user_input))

# Define the convert function
def convert(text):
    # replace every instance of the emoticons with the respective emojis
    string = text.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    # Return the outputs
    return string

# Call the main function
main()
    
