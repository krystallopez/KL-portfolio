# Project 4 - Hackathon: Python Projects 

A high-level overview of the project purpose:

## :memo: Situation

For this project, we were tasked with learning a new programming language and creating a project built using that language. For my programming language I chose Python, as that is the language that my team uses. 

## :pushpin: Task 

The core of this project is to demonstrate understanding of the programming lanuaguage/framework that you have chose to build your project with. 

## :computer: Action 

For this project, I built a series of different Python games:

<li>The first game, called the Star Wars Interactive Quiz, I created using only if conditionals, print statements and some ASCII art. The game can be run on the command line. Every time the user guesses the correct answer, they earn a point. However, each time they guess the wrong answer they don't earn any points. Using a score counter, the program is able to keep track of the user's score.
</li>
<br> 
<p align="center"><b><i>Click the image below to view the quiz!</i></b></p>

[![Check out the quiz here!](https://i.imgur.com/anSx3Uy.png)](https://github.com/krystallopez/kl-portfolio/blob/main/Module%20Projects/python_projects/starwarsquiz.py)
<br>

<li>The second game in the series, is Rock, Paper, Scissors! In this game you can choose Rock, Paper, or Scissors and see if you can beat the computer. This game was written in Python using lists and utilizing the random module to generate a random item from the list each time the user enters their choice. </li>
<br>

<p align="center"><b><i>Click the image below to view the quiz!</i></b></p>

[![Check out the quiz here!](https://i.imgur.com/C3yoane.png)](https://github.com/krystallopez/python-projects/blob/main/batmanquiz.py)
<br>

<li> The third game in this series, is the Batman Quiz. Similar to the Star Wars quiz, I followed the same steps using if conditionals and print statements to build the questions and answers. I also implemented a counter here, however, instead of tracking the user's score, I instead tracked how many questions the user answered correctly and printed out that number at the end of the quiz.</li>
<br>

<li> The fourth item in the series that I created for this proeject is a random password generator. In the file labeled <code>passwordgen2.py</code>, you enter in the length of the password and then the program will generate a password for you that consists of random letters, symbols, and numbers. I used the random module and the string module so that I could define the data I was looking for and randomly sample different characters so that none of the characters are repeated, making for a very secure password. Once all of those characters are randomly generated, they are then joined together in order to create the password. 
</li>
<br>

<li> The last item in the series is also a random password generator. However i used a different process to build out this generator. In the file <code>passwordgen.py</code>, I used three different lists compiled of letters, numbers, and symbols. There are two different ways that the problem could be solved. One way, we could just simply use a for loop and the range function, as well as the random module to randomly choose the specific letter, number, and symbol we want in the password. The password, a variable, being set as an empty string, we can then add each character to that variable. The second way that we can solve this problem is instead of storing the items from each list to an empty string, I stored each random character to a new list, and then shuffled through that list. After that, I then created a new password variable that is an empty string. I used a for loop to iterate through each separate character and added each character to the new password variable, them generating a new password for the user based on the number of letters, symbols, and numbers they have entered in the command line.
</li>



## :movie_camera: Result (Video Presentation + Project Repo) 

- [Original Python Repo](https://github.com/krystallopez/python-projects)
- [Original Python Project README](https://github.com/krystallopez/python-projects/blob/main/README.md)

[![Watch the video](https://i.imgur.com/14fpFtm.png)](https://www.youtube.com/watch?v=O_lS1W7XlJA)

## :floppy_disk: Technologies

This entire project was built using only <code>Python 3</code>. 

## :book: Competencies

### JF 1.6

#### Can follow software designs and functional/technical specifications

By reviewing all project requirements, I was able to break down how this project needed to be completed. By following the guidelines that were laid out for the project, which allowed me to properly complete the project. This allowed me to properly lay out each task that was needed for this project. 


### JF 2.1

#### Can create and analyze artifacts, such as use cases and/or user stories

While implementing the code for the quizzes, I thought of an interactive way for the user to enjoy the quizzes, which was why I decided to add a score counter to each of the quizzes. Depending on the quiz the score counter functions differently, it still allows for the user to interact with the quiz. 

### JF 2.4

#### Can create simple software designs to effectively communicate understanding of the program

I decided to make this project as simple as possible, as during the time that this project was created, I was just learning Python. I started by planning out how I wanted the quizzes to look and what Python libraries/modules I would be using so that I could meet the requirments of this project. Once I had my plan in place, then I got to work on creating each of the quizzes and games. 

### JF 3.4

#### Can create a logical and maintainable codebase

Throughout this project, I committed my changes each time I changed something within my code base. This would allow me to be able to keep track of all of my commits and pushes. Through code reviews, I was able to review my code and push all of the changes directly to my main branch.