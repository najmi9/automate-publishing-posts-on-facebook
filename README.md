# automate-publishing-posts-on-facebook



## What is this project about ?
After we enter the username and password of our Facebook account, the srcipt will be logged in and save the browser's
cookies in a file using **pickle** to use it in the next time to avoid a login again, after authentification, 
we will get the text and the image from a **csv file** that contains the content and the path to the image 
of all future publications, to be published  after fill in the publication form.
All this work will be scheduled to be done every day at specific time.

The `csv file` will contains for example 50 lines, each line contains the content and the path to the image 
of one post that will be published. Every day we will take a line from the csv file and publish it, 
and that will be in 50 days.
