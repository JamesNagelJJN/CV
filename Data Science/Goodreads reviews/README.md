Goodreads is a website where users can review books. Although the source dataset
was interesting and contained a range of data, one thing it lacked was genres.
So I set up a web scraping script using Selenium to search Google with the title
of a book and collect the genre of the book. I did this for publishers with over 1,000,000
total reviews across all their published books in the dataset.

Once I obtained a new dataset that contained the title of a book, the publisher the book
was published with and the genres. With this I created a wordcloud that displays
the most published genres of each publisher. 

![Houghton Mifflin Harcourt](https://user-images.githubusercontent.com/84214589/167647498-2edad6f8-ec01-4b13-8698-0701f4895b64.PNG)
![Penguin Books](https://user-images.githubusercontent.com/84214589/167647505-87e68176-482b-422e-b540-ed36c4ea1d0d.PNG)
![Scholastic Inc](https://user-images.githubusercontent.com/84214589/167647509-50b657e7-d596-43cc-b3ec-5efe6f432591.PNG)
![Tor Books](https://user-images.githubusercontent.com/84214589/167647515-2d219fc8-bed3-4c37-898f-0cfabe455490.PNG)
