# Python Feed Scrapper Console Application

The objective of this programming assignment is to code a feed alerter. Your program should:
  1. {1/20} Store the program parameter in a database
  2. {5/20} Store feed’s data in a database. If necessary choose some of the usual fields (e.g., title, summary etc.)
  3. {10/20} Interact with a user allowing him to do some commands, e.g.: 
  
    (a) List/add/remove feeds on run time (memory and database)
      • $ list-feeds
      • $ add-feed http://rss.cnn.com/rss/edition.rss
      • $ remove-feed http://rss.cnn.com/rss/edition.rss
  
    (b) Feeds from the list can be activated/deactivated in runtime
      • $ activate-feed http://rss.cnn.com/rss/edition.rss
      • $ deactivate-feed http://rss.cnn.com/rss/edition.rss 
      
    (c) Load feeds from a file containing a list of urls (one per line)
      • $ load list-of-feeds-file.txt
    
    (d) Ask the database for news containing given words. E.g.:
      • $ title-contains cryptocurrency
      • $ summary-contains cryptocurrency
      • $ contains cryptocurrency (* check all stored fields *)
    
    (e) Create alerts so that when a keywords appears in the feed a message is shown
      • $ add-alert cryptocurrency
      • $ remove-alert cryptocurrency
      • $ show-alerts
      
   4. {4/20} For full credits, code a threaded implementation . E.g.:

    (a) For each feed run a thread which checks for new entries on the active feeds every x seconds (program parameter)
    
    (b) Create (active) alerts’ threads that every x seconds (program parameter) looks for key- words on the database, showing a message if a new message appeared
    with that keyword. An alert should only be displayed once.
