
import webbrowser

file = "websites.txt"

def get_input():
    return input("Enter websites separated by spaces: ").split()

def save_to_file(websites):
    with open(file, "w") as f:
        f.write(" ".join(websites))

def open_saved():
    try:
        with open(file, "r") as f:
            websites = f.read().split()
            for website in websites:
                webbrowser.open(website)
    except FileNotFoundError:
        print("No websites saved yet.")

if __name__ == "__main__":
    open_saved()
    
    user_websites = get_input()
    save_to_file(user_websites)
    
    print("Websites opened and saved successfully.")