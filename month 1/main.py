from modules.calculator import Calculator
from modules.notes_manager import NotesManager
from modules.timer import Timer
from modules.file_organizer import FileOrganizer
from modules.unit_converter import UnitConverter
from modules.utils import clear_screen, pause


def main_menu():
    print("=" * 45)
    print("     PERSONAL PRODUCTIVITY SUITE")
    print("=" * 45)
    print("1. Calculator")
    print("2. Notes Manager")
    print("3. Timer")
    print("4. File Organizer")
    print("5. Unit Converter")
    print("6. Exit")


def main():
    calculator = Calculator()
    notes = NotesManager()
    timer = Timer()
    organizer = FileOrganizer()
    converter = UnitConverter()

    while True:
        clear_screen()
        main_menu()
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            calculator.run()
        elif choice == "2":
            notes.run()
        elif choice == "3":
            timer.run()
        elif choice == "4":
            organizer.run()
        elif choice == "5":
            converter.run()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice")
            pause()


if __name__ == "__main__":
    main()
