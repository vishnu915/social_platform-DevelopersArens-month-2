class UnitConverter:
    def run(self):
        print("\n--- Unit Converter ---")
        try:
            km = float(input("Enter kilometers: "))
            print("Meters:", km * 1000)
            print("Miles:", km * 0.621371)
        except:
            print("Invalid input")

        input("Press Enter to continue...")
