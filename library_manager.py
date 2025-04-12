import os

LIBRARY_FILE = 'library.txt'

def load_library():
    library = []
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 5:
                    title, author, year, genre, read_str = parts
                    library.append({
                        "title": title,
                        "author": author,
                        "year": year,
                        "genre": genre,
                        "read": read_str.lower() == 'yes'
                    })
    return library

def save_library(library):
    if not library:
        if os.path.exists(LIBRARY_FILE):
            os.remove(LIBRARY_FILE)  # Optional: Clean up old file if emptied
        return
    with open(LIBRARY_FILE, 'w', encoding='utf-8') as file:
        for book in library:
            line = f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{'yes' if book['read'] else 'no'}\n"
            file.write(line)

def display_menu():
    print("" + "="*40)
    print("📚 Personal Library Manager")
    print("" + "="*40+"\n")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Display All Books")
    print("5. Display Statistics")
    print("6. Exit")

def add_book(library):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = input("Publication Year: ").strip()
    genre = input("Genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower()

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read == 'yes'
    }
    library.append(book)
    print(f"✅ Book Added: '{title}' Successfully.")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for i, book in enumerate(library):
        if book["title"].lower() == title:
            del library[i]
            print(f"🗑️ Book removed '{book['title']}' Successfully .")
            return
    print("❌ Book not found.")

def search_books(library):
    print("\nSearch by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        keyword = input("Enter the title: ").strip().lower()
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == '2':
        keyword = input("Enter the author: ").strip().lower()
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("❌ Invalid choice.")
        return

    if results:
        print("\n📚 Matching Books:")
        for i, book in enumerate(results, start=1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ No matching books found.")

def display_book(book):
    print(f"- {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Read: {'Yes' if book['read'] else 'No'}")

def view_all_books(library):
    if not library:
        print("📂 Library is empty.")
    else:
        print("\n📖 Your Book Collection:")
        for book in library:
            display_book(book)

def view_statistics(library):
    total = len(library)
    read = sum(1 for book in library if book["read"])
    unread = total - read
    genres = {}
    for book in library:
        genres[book["genre"]] = genres.get(book["genre"], 0) + 1

    print(f"\n📊 Statistics:")
    print(f"Total books: {total}")
    print(f"Books read: {read}")
    print(f"Books unread: {unread}")
    print("Books by genre:")
    for genre, count in genres.items():
        print(f"  - {genre}: {count}")

def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            view_all_books(library)
        elif choice == '5':
            view_statistics(library)
        elif choice == '6':
            if library:
                save_library(library)
                print("💾 Library saved to TXT file. Goodbye!")
            else:
                print("📂 No books in library. Nothing saved.")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
