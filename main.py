from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    name = input("Enter your name: ")
    print(greet(name))
    
    try:
        user_input = float(input("Enter a number: "))
        
        sq = square(user_input)
        even_status = "even" if is_even(user_input) else "odd"
        fahrenheit = celsius_to_fahrenheit(user_input)
        
        print(f"Square: {sq}")
        print(f"Number is: {even_status}")
        print(f"Fahrenheit equivalent: {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
