def main():
    # Prompt the user for input
    user_input = input("Please eneter your text: ")
    # split the input into a list of words at whitespaces
    user_input = user_input.split()
    # Join the texts with three dots
    user_output = "...".join(user_input)
    # print the result
    print(user_output)

# Call the main function
main()