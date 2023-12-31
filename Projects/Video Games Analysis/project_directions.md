# Project 1: Video Game Data Analysis

## Introduction
This week and the next couple of weeks, we will be starting our first major project. It will consist of numerous parts that we will split up through the next couple of weeks.

### What is Data Analysis?
Python is one of the best languages to process large datasets and draw conclusions from them. Python is popular with data analysis because:
- Supports many libraries that can graph and plot data
- Lots of work with arrays and string, and Python syntax makes it easy to handle (i.e `append()`, `remove()`)
- Easy syntax allows anyone to use Python
- Does not really matter how fast the program works (Python is incredibly slow compared to other languages)

### What will we be doing?
In `data.txt` I have gathered from Wikipedia the dataset of the most popular video games (by games sold). We will be extracting information from this dataset and creating information from it. 
- Source: [Most Popular Video Games](https://en.wikipedia.org/wiki/List_of_best-selling_video_games)



## Table of Contents
All the parts will be split into milestones. Each week we will try and complete a milestone. All the milestones will be written here, so you are more than welcome to complete other milestones earlier. However, each milestone usually builds off the previous milestones, so do not go out of order
- [Milestone 0: Data Cleaning](#milestone-0-cleaning-the-data)
- [Unit Tests](#unit-testing)

## Milestone 0: Cleaning the Data
When analyzing large datasets, a common problem is that the data is not always formatted the way we wanted. For example, look at the first couple lines in `data.txt`:
```txt
Minecraft 300,000,000 Minecraft	Multi-platform	November 18, 2011
Grand Theft Auto V	185,000,000	Grand Theft Auto Multi-platform	September 17, 2013
```
The formatting is not that bad, but it could be better. For example, there are a lot of unwanted tabs and extra spaces that we could get rid of. This milestone will focus on removing them, and organizing the `data.txt` into a proper array.

Given to you in `project.py` are three lines of code:
```python
file = open(r'\Users\dchen\Desktop\CompSci\tutoring-files\Week8\data.txt')
src = file.read()
data = []
```

The first two lines are opening the `data.txt` and converting it into a string. Note, we will need to fix the file path so it reads from wherever `data.txt` is stored on your computer. The third line gives you an empty array to store the cleaned data in. 

I strongly suggest storing each game and its associated data as one string, and let `data` be an array of strings. In this milestone you have two requirements:
1. Remove any tabs in `src` and replace them with spaces
2. Separate each game into its own string

### Tips for Removing Tabs
Python has a handy function called `string.replace(old, new)`, which goes through `string` and replaces every instance of `old` with `new`. It returns the new string. 

For example,
```python
str1 = "Today will be a good day"
new_str = str1.replace("good","great")
print(new_str)
```

Output:
```
Today will be a great day
```

Tabs are represented by the character `\t`. 

### Tips for Parsing Each String
In `data.txt`, each game is already kind of separate (strong kind of). You'll notice each game is on it's own line in `data.txt`. So it would be great if we separate by line.

In any programming language, line breaks have their own character, `\n`. So to a computer:
```
Hello
World

Hello\nWorld
```

These are the same. Here's the basic outline for separating the string by the `\n`.
1. Use a loop to go through each character in `src`
2. Have a blank string variable that you add letters onto. Every character that isn't the `\n` character, you add onto the blank string
3. If the character is the `\n` character, add the concentanated string into `data` and set string back to blank.

In short, this milestone does not have a lot of code. But it can be harder to conceptualize. 

## Unit Testing
There is only one test to pass in this unit test. The test checks the first entry in `data` and checks:
- Each entry has the proper format like:
```
Minecraft |300,000,000| Minecraft Multi-platform November 18, 2011
```
- Each entry has all of it's tabs removed

## Milestone 1: Simple Data Analysis
In this milestone, you'll implement 3 simple data functions. 
1. Year Parse
2. Keyword Search
3. Most Popular Franchise

### Year Parse
When this function is called, it will get the years of each game released date and store them in a set. Note that the dates will be stored in set. A set is an array but every entry is unique, that is no entry will appear twice in the array. Once the set is completed, the set will be printed.

#### Hints for Year Parse
Note that for every entry, the year is always the last four characters in the string. Thus, you can always find the year by taking a substring of the last for characters. 

In order to maintain a set, you should search your entire set before inserting a new entry. I have provided you with a helper function called `search` which takes your set and entry-to-look-for as arguments. It returns `True` if the entry is found, and `False` otherwise. You should only insert entries into your set if the `search()` returns false.

### Keyword Search
When this function is called, it will search the entries of data and return the first entry that contain the associated keyword. For example, if the keyword was Wii, you would return
```python
Wii Sports	|82,900,000|	Wii	Wii	November 19, 2006
```

#### Hints for Keyword Search
This should feel relatively straightforward, and it is nothing more than a search. To perform a search, you should use a loop and iterate through your data set. 

To check if a keyword is in a set, you can use the `in` keyword for strings. It is used like

```python
substring = "hello"
string = "hello world"
if substring in string:
    print("True")
```

### Most Popular Franchise
When this function is called, it determines the most popular franchise in the dataset (i.e Mario, Halo, Call of Duty). To do this, I have given you an array in the function labelled `tracker`. It is a 2-D array that associates a franchise with a value. If the franchise title is found in the entry, increment the count.

#### Hints for Most Popular Franchise
This is extremely similar to `keyword_search()`. I would suggest finishing `keyword_search()` to get an idea how to do most popular franchise. While not neccesaary, you can use your `keyword_search()` function to complete `most_popular_franchise()`.

## Milestone 2: Advanced Data Analysis
In this milestone, we will go step further and implement harder functions. 

### Sort By Year
When viewing large lists, it would be nice to view the list in a different order. In this function you'll sort the entries by the year they came out, instead of the number copies sold. 

#### Hints for Sorting By Year
We will be using Python's built-in function `arr.sort()` to sort our array. This sorts an array by default alphabetically or numerically least to greatest.

We can specify it to sort by something else, by passing the `(key=____)` argument. 

### Create Your Own 
Now that you have implemented a couple functions on your own, you will create your own function that does its own unique action. This can be whatever you want, as long as its related to data analysis. 

Since this is your own function, you will also be responsible for making sure it works properly. Thus, you are responsible for testing your own code.