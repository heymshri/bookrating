# Bookrating

Implement the program in Python. Comment on your code as necessary to explain it clearly.
Your task for this project is to write a program that takes people's book ratings and makes book
recommendations to others using the average rating technique.
The program will read customers data from a text file (you find the text file on Canvas site for this
unit) that contains sets of three lines about each customer. The first line will have the customer's
username, the second line book title, and the third line the rating that is given to the book. See, below
text file as an example:

When the program starts, it should read through the text file and create a list
with one occurrence of each book in the file. For example, the produce list
might look like the following:
[' Coding Fundamentals', ' Jobs in Tech', ' Java','JavaScript’, Python', ' HTML and CSS']
Once the list is created, you need to create a dictionary to store the rating
data and loop through the file again. Add each customer's username in the
file as a key to the dictionary. The value associated with the keys should be a
list the same length as the books list you created above. You should store the
rating at the same index that the book's name appears in the books' list. 0s
should represent books that the customer has not rated. For example, the
dictionary would be as follows:
{ ' Alice': [5, 3, 0, 0, 4, 0], ' Tom': [0, 2, 4, 0, 0,4],' Jon': [0, 4, 1, 0, 0, 1], ' Josh': [0, 1, 5, 3, 0,1] }

The program should have a menu as below:
    Welcome to the EduWra Book Recommendation System
    1: All books average ratings
    2: Recommend books for a particular user
    q: Exit the page
    
The above menu should be repeated after every task is finished.

Option 1: All books average ratings
If the user selects option 1, the program should show all of the books in the file sorted by average rating
from highest to lowest. For example, for the file above, the program should provide the following
output:
  Select one of the options above:1
    The average ratings for Coding Fundamentals is 5.00
    The average ratings for Python is 4.00
    The average ratings for Java is 3.33
    The average ratings for JavaScript is 3.00
    The average ratings for Jobs in Tech is 2.50
    The average ratings for HTML and CSS is 1.50

To calculate all books average ratings, you can create a list of tuples containing the average rating for
a book first and the title of that book second. You can create this list by iterating over the books list one
at a time, and for each customer in the dictionary add their rating of that book and counting how many
customers in the dictionary rated it greater than 0. The average score for that book is the sum of the
scores divided by the count of non-zero ratings. Once this list is created, you can sort it by using the
list's sort function.

The averages will stay the same throughout the program's run, so you can calculate them once at the
start of the program.

Option 2: Recommend books for a customer
If the user selects option 2, the program should first prompt the user for the name of the customer that
the program wants recommendations for as follows:

 Select one of the options above:2
 Please enter the customer name: Hello
 
    The average ratings for Coding Fundamentals is 5.00
    The average ratings for Python is 4.00
    The average ratings for Java is 3.33
    The average ratings for JavaScript is 3.00
    The average ratings for Jobs in Tech is 2.50
    The average ratings for HTML and CSS is 1.50
    
If the name that the user enter is not in the dictionary of ratings, the program should output the same
list of books as when the user selects option 1.
Suppose the name the user enters is in the dictionary of ratings. In that case, the program should use the
data in the dictionary to find the other customers that are most similar to the customer you are looking
for recommendations.

 Select one of the options above:2
 Please enter the customer name: Jon
 
    The average ratings for Coding Fundamentals is 5.00
    The average ratings for Python is 4.50
    The average ratings for Java is 3.33
    The average ratings for JavaScript is 3.00
    The average ratings for Jobs in Tech is 2.50
    The average ratings for HTML and CSS is 2.00

The first step to do this is to calculate the similarities between your customer and the other customers.
You can multiply each element in the customer's list with the element at the same index in the other
customer's list and sum the result. For example, if you are looking for a recommendation for Alice you
can do the following to calculate his similarity to Tom:
(5 * 0) + (3 * 2) + (0 * 4) + (0 * 0) + (4 * 0) + (0 * 4) = 0 + 6 + 0 + 0 +
0 + 0 = 6
Compute this similarity for each customer in the dictionary—store tuples containing first the similarity
number and second the other user's name in a list. You can use the list sort function to sort this list.
Now that you have a list of the most similar customers, you can use this to find out which books to
recommend. To generate recommendations, take an average of the ratings of the three customers with
the highest similarity to the user you are looking for.
To average the ratings, create a new list the same length as the list of books and filled with 0s. Loop
through this list, and for every index of this list, loop through the first three customers, find the sum of
their ratings and then divide by the number of non-zero ratings. If there are no non-zero ratings for a
book, you should not divide as you will get a divide by 0 error.
Once you have calculated these averages, create a list of tuples containing the average rating and then
the book title for all books with non-zero ratings in the averages list. Then, sort this list. Now you have
a list of books to recommend.
The user can enter q to exist the program:

The program should have a menu as below:
    Welcome to the EduWra Book Recommendation System
    1: All books average ratings
    2: Recommend books for a particular user
    q: Exit the page
   Select one of the options above:3
>>>
