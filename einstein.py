def main():
    # Take user's input for mass in kilogram
    m = int(input("m: "))
    # Assign the default speed of light
    c = 300000000
    # Calculate the value of Energy
    E = m * pow(c,2)
    # Print the output
    print(f"E = {E:.2e} joules")

# Call the main function
main()





