# Modules
import sqlite3
import feedparser

def listFeeds():
    # Used RSS CNN News - http://rss.cnn.com/rss/edition.rss
    response = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    print("\nCurrent feeds:")
    for count, entry in enumerate(response.entries):
      print(str(count + 1) + " - " + entry.title)

def addFeed():
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

def removeFeeds():
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()
    # Delete all feeds
    cursor.execute("DELETE FROM Feeds")
    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def menu():
    while True:
        print("\n1 - List feed")
        print("2 - Add feed")
        print("3 - Remove feeds")
        print("x - Exit Application\n")
        op = input().split()
        if op:
            if op[0] == "1":
                listFeeds()
            elif op[0] == "2":
                addFeed()
            elif op[0] == "3":
                removeFeeds()
            elif op[0] == "x":
                break


if __name__ == "__main__":
    menu()
