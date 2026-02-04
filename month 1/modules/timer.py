import time


class Timer:
    def run(self):
        print("\n--- Timer ---")
        try:
            seconds = int(input("Enter seconds: "))
            print("Timer started...")
            time.sleep(seconds)
            print("⏰ Time's up!")
        except:
            print("Invalid input")

        input("Press Enter to continue...")
