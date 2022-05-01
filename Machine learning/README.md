## **Goodreads Book Dataset Cleaning**

Tableau Public - [Tableau](https://public.tableau.com/app/profile/james.nagel/viz/BookInformation/Dashboard1)
------------------------------------------------

**The Project**

I love reading and find it facinating how some books become huge and others seem to fade away. I
found a dataset on book reviews from the website goodreads. With this data I set out to create
a clear effective dashboard on tableau that anyone could understand and navigate.

For this project I displayed only publishers with over 1,000,000 reviews of their published books in total.
Along with this, authors is displayed with a matching colour scheme to the publishers. 
When a Publisher is selected on the left hand column, the subsiquent authors with books published with that publisher are displayed on the right section.
Along with the Author and book title, their rating count and average ratings of each book are displayed.

**Skills**: \
• Regex \
• Datetime \
• Lambda functions \
• EDA \
• Data cleaning \

Problems

• Some books in the dataset include the artists for the books along with the author in the Author column. 
    This is difficult as not only this, some of the books are co-written.
    Because of this only keeping the first Author in each row would mis represent Authors who may have written books. On the other hand, splitting the Authors
    up and saying all names included for each book were an Author there would be a mis representation of statistics due to there being mulitple instances of 
    the same book.

• How to approach fixing this. If I had full control of the data pipe line and how the data was scraped off the web then names of each Author (if multiple listed)
    could be looked into and if it is discovered they are an artist, leave them from the Author column and create another for artist. If they are a co-author then
    each instance of the book/series of books should include all names of co-authors, which is fine. This is alright because there should be no other version of the book
    where all the Authors didn't write that book, where as artists can change if a new cover design comes out.

----------------------------------------------------------
## **Youtube Trending**
----------------------------------------------------------
**The Project**

I set out to find which types, and why videos make the trending page on YouTube. As well as this,
I delved into the time a video takes to trend and that is spends on the trending page. 

Data

If a video were to trend it would get a single row for the day it trended. Each consecutive
day the video trends the video gets a new row in the dataset. This means to figure out how long
a video was on the trending page I had to find the first and last date that the video trended.

**Skills**: \
• Datetime \
• Regex \
• Lambda functions \
• Data visulisation \
• EDA \
• Data cleaning \
• Pivot tables \
