## **Goodreads Book Dataset Cleaning**

Tableau Public - [Tableau](https://public.tableau.com/app/profile/james.nagel/viz/BookInformation/Dashboard1)
------------------------------------------------
Problems

1 ) Some books in the dataset include the artists for the books along with the author in the Author column. 
    This is difficult as not only this, some of the books are co-written.
    Because of this only keeping the first Author in each row would mis represent Authors who may have written books. On the other hand, splitting the Authors
    up and saying all names included for each book were an Author there would be a mis representation of statistics due to there being mulitple instances of 
    the same book.
    
    How to approach fixing this. If I had full control of the data pipe line and how the data was scraped off the web then names of each Author (if multiple listed)
    could be looked into and if it is discovered they are an artist, leave them from the Author column and create another for artist. If they are a co-author then
    each instance of the book/series of books should include all names of co-authors, which is fine. This is alright because there should be no other version of the book
    where all the Authors didn't write that book, where as artists can change if a new cover design comes out.


-------------------------------------------------
## **Goodreads Book Dataset Cleaning**
------------------------------------------------
**The Project**

This project is on a dataset which includes thousands of books from Goodreads.
Goodreads is a website where users can review and give books a rating.

**Skills**: \
• EDA \
• Regex \
• Lambda functions 

## **YouTube Trending**
------------------------------------------------

**The Project**

YouTube's trending page is an imfamous part of YouTube that creators strive to reach.
When a video reaches "trending" status it means an algorithm has picked out
that video due to a wide range of factors, and deemed it worthy for the YouTube
trending page. In this project I explore the data of the YouTube trending page
for the UK from 2017-2018.

**Skills**: \
• EDA \
• Regex \
• Lambda functions \
• Data visualisation \
• Pivot Tables

## **Fish CNN**
------------------------------------------------
**The Project**

For fishermen it may be an easy task when asked to differencitate between fish. For most it
is not so easy. Even if there were to be a task that was easy for most, it may be time consuming.
That's where machine learning comes in, more specifically, a convolutional neural network.
For this project I set out with developing a basic CNN to classify 9 different species of fish wiht
a dataset I found on Kaggle.

**Skills**: \
• Importing images and reducing their resolution \
• Developed a CNN that can classify 9 different species of fish with a 99% accuracy \
• Data visualisation

## **Predicting the IMDb rating of a movie, based on other popular websites**
----------------------------------------------------------
**The Project**

Predicting the IMDb rating of a movie, based on other popular websites. The website in question are
Rotten Tomatoes, Metacritic, Hidden Gem. This prediction can be made using linear regression.

**Skills**: \
• Normalisation \
• Linear regression \
• Data visualisation

