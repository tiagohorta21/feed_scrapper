# Modules
import sqlite3
import feedparser

# Example Feeds
# CNN News - http://rss.cnn.com/rss/edition.rss
# Fox News - http://feeds.foxnews.com/foxnews/latest
# USA Today - http://rssfeeds.usatoday.com/UsatodaycomNation-TopStories


def getActiveState(active):
  if(active):
    return "Activated"
  else:
    return "Deactivated"


def listFeeds():
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # List all feeds from the database
    cursor.execute("SELECT * FROM Feeds")
    feeds = cursor.fetchall()

    print("\nCurrent feeds:")
    for count, feed in enumerate(feeds):
      print(str(count + 1) + " - " + feed[1] + " | " + getActiveState(feed[4]) + " | URL: " + feed[2])


def addFeed(feed):
    # Parse received feed
    response = feedparser.parse(feed)
    
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # Insert feed into database
    cursor.execute("INSERT INTO Feeds VALUES (?,?,?,?,?)", (None, response.feed.title, response.href, response.updated, 1))
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


def removeFeed(feed):
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # Delete all feeds
    cursor.execute("PRAGMA FOREIGN_KEYS = ON")
    cursor.execute("DELETE FROM Feeds WHERE url=?", (feed,))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.s
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def activateFeed(feed):
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()
    
    # Activate feed
    cursor.execute("UPDATE Feeds SET active='1' WHERE url=?", (feed,))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.s
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def deactivateFeed(feed):
    # Open database connection
    connection = sqlite3.connect("tp1.db")
    cursor = connection.cursor()

    # Activate feed
    cursor.execute("UPDATE Feeds SET active='0' WHERE url=?", (feed,))

    # Save (commit) the changes
    connection.commit()
    # We can also close the connection if we are done with it.s
    # Just be sure any changes have been committed or they will be lost.
    connection.close()


def addFeedsFromTextFile():
  # Open file and read each line
  file = open('feeds.txt', 'r')
  lines = file.readlines()

  for line in lines:
    print(f"Adding feed: {line}")
    addFeed(line)


def menu():
    while True:
        print("\n1 - List all feeds")
        print("2 - Add feed from url")
        print("3 - Remove feed from url")
        print("4 - Activate Feed")
        print("5 - Deactivate Feed")
        print("6 - Add feeds from text file")
        print("x - Exit Application\n")
        op = input().split()
        if op:
            if op[0] == "1":
                listFeeds()
            elif op[0] == "2":
                print("\nPaste the RSS feed you want to add: ")
                feed = input()
                addFeed(feed)
            elif op[0] == "3":
                print("\nPaste the RSS feed you want to remove: ")
                feed = input()
                removeFeed(feed)
            elif op[0] == "4":
                print("\nPaste the RSS feed you want to activate: ")
                feed = input()
                activateFeed(feed)
            elif op[0] == "5":
                print("\nPaste the RSS feed you want to deactivate: ")
                feed = input()
                deactivateFeed(feed)
            elif op[0] == "6":
                print("\nAdd feeds from text file: ")
                addFeedsFromTextFile()
            elif op[0] == "x":
                break

if __name__ == "__main__":
    menu()
