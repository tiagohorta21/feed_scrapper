# Modules
import sqlite3
import feedparser

# TODO: Based on the parameter get the feed but do not save it in the database

# Used RSS CNN News - http://rss.cnn.com/rss/edition.rss
response = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
for entry in response.entries:
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()
    # Insert feed and parameters into database
    cursor.execute("INSERT INTO Feeds VALUES (?,?,?)", (None, entry.link, entry.title))
    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def menu():
    while True:
        print("1 - List feed")
        print("2 - Add feed")
        print("3 - Remove feed")
        print("x - Exit Application")
        op = input().split()
        if op:
            if op[0] == "1":
                print("List feed")
                break
            elif op[0] == "2":
                print("Add feed")
                break
            elif op[0] == "3":
                print("Remove feed")
                break
            elif op[0] == "x":
                break


if __name__ == "__main__":
    menu()
