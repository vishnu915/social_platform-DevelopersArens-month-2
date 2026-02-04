import os
import shutil


class FileOrganizer:
    def run(self):
        path = input("Enter directory path: ")

        if not os.path.exists(path):
            print("Invalid path")
            return

        for file in os.listdir(path):
            if "." in file:
                ext = file.split(".")[-1]
                folder = os.path.join(path, ext)

                os.makedirs(folder, exist_ok=True)
                shutil.move(os.path.join(path, file), os.path.join(folder, file))

        print("✅ Files organized")
        input("Press Enter to continue...")
