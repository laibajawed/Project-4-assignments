INCHES_PER_FOOT = 12
def main():
    feet: float = float(input("Enter number of feet: "))
    inches: float = feet * INCHES_PER_FOOT
    print("This is", inches, "inches")
if __name__ == '__main__':
    main()