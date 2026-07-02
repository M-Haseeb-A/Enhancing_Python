
import webbrowser
import subprocess

k = "Welcome to Jarvis assistant"
print(k.center(50))

print("Enter your command like, open google, open youtube, etc.")

command = input("Enter your command or 'e' to exit :").lower().strip()

if command == "open google":
    webbrowser.open("https://www.google.com")

elif command == "open youtube":
    webbrowser.open("https://www.youtube.com")

elif command == "open notepad":
    subprocess.run("notepad.exe")

elif command == "open calculator":
    subprocess.run("calc.exe")

elif command == "e":
    print("Exiting the program...")
    exit()

else:
    print("Command not recognized!")