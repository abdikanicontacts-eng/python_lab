def main():
    name = input("Enter your name: ")
    print(greet(name))
    
    try:
        user_input = float(input("Enter a number: "))
        
        sq = square(user_input)
        fahrenheit = celsius_to_fahrenheit(user_input)
        print(f"Square: {sq}")
        print(f"Number is: {even_status}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
