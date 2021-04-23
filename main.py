# Modules
import sqlite3
import feedparser

# Used Feeds
# CNN News - http://rss.cnn.com/rss/edition.rss
# Fox News - http://feeds.foxnews.com/foxnews/latest
# USA Today - http://rssfeeds.usatoday.com/UsatodaycomNation-TopStories

def listFeeds():
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()
    # List all feeds from the database
    cursor.execute("SELECT * FROM Feeds")
    feeds = cursor.fetchall()

    print("\nCurrent feeds:")
    for count, feed in enumerate(feeds):
      print(str(count + 1) + " - " + feed[1])

def addFeed():
    # Get CNN feed
    response = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # Insert feed into database
    cursor.execute("INSERT INTO Feeds VALUES (?,?,?,?)", (None, response.feed.title, response.href, response.updated))
    feedId = cursor.lastrowid
    # Insert feed entries into database
    for entry in response.entries:
        # Insert feed and parameters into database
        cursor.execute("INSERT INTO FeedEntries VALUES (?,?,?,?,?,?)", (None, getattr(entry, 'title', None), getattr(entry, 'summary', None), getattr(entry, 'published', None), getattr(entry, 'link', None), feedId))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()

def removeFeed():
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # Delete all feeds
    cursor.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor.execute("DELETE FROM Feeds WHERE url='http://rss.cnn.com/rss/edition.rss'")

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def menu():

    while True:
        print("\n1 - List all feeds")
        print("2 - Add CNN feed")
        print("3 - Remove CNN feed")
        print("x - Exit Application\n")
        op = input().split()
        if op:
            if op[0] == "1":
                listFeeds()
            elif op[0] == "2":
                addFeed()
            elif op[0] == "3":
                removeFeed()
            elif op[0] == "x":
                break


if __name__ == "__main__":
    menu()
