print("📘 Welcome to Your Notes Keeper")
def load_notes () :
    try :
        with open("notes.txt","r") as file :
            notes = [note.strip() for note in file.readlines()]
        return notes
    except FileNotFoundError :
        return[]
    
def view_notes (notes):
    if not notes:
        print("Sorry file not found")
    else:
        print("\n Your notes are displayed below!")
        for i,note in enumerate(notes,start=1):
            print(f"{i}.{note.upper()}")
        print()

def add_note(notes):
    new_note = input("Enter a new note:")
    notes.append(new_note.lower())
    print(f"✅ Note added : {new_note}")

def search_note(notes):
    keyword = input("Enter a keyword to search :").lower()
    found = False
    print("\n 🔍 Search results :")
    for i,note in enumerate(notes,start=1):
        if keyword in note.lower():
            print(f"{i}.{note.upper()}")
            found = True
    if not found :
        print("❌ No matching notes found")

def save_note(notes):
    with open("notes.txt","w") as file:
        for note in notes :
            file.write(note+"\n")
        print("💾 Tasks saved to file")

def delete_note(notes):
    view_notes(notes)
    try:
        choice = int(input("Enter the number of the note you want to delete:"))
        if 1 <= choice <= len(notes):
            removed = notes.pop(choice-1)
            print(f"Deleted note: {removed}")
        else:
            print("Enter a valid number")
    except ValueError:
        print("❌ Kindly enter a number")

def main():
    notes = load_notes()

    while True :
        print("\n📋 To-Do List Menu:")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Save Note")
        print("4. Delete Note")
        print("5. Search Notes")
        print("6. Exit")

        choice = int(input("Enter your choice(1-6):"))

        if choice == 1:
             view_notes (notes)
        elif choice == 2:
             add_note(notes)
             save_note(notes)
        elif choice == 3:
             save_note(notes)
        elif choice == 4:
             delete_note(notes)
             save_note(notes)
        elif choice == 5:
             search_note(notes)
        elif choice == 6:
            print("👋 Exiting the Notes Keeper. Goodbye!")
            break
        else:
          print("Enter a valid number")
        
    

    main()
if __name__ == "__main__":
    main()            
             
             
             
             
             
        

    



