# Project 1 - The Inventory App 

<p align="center" >
<img  width=400 src="Project Visuals/inventory-app.gif" alt="animated"/>
</p>

The Inventory App was one of the first full-stack group projects that I completed as part of my apprenticeship. For this project, myself and my group were tasked with creating a fullstack RESTful CRUD application. In order to complete this project, we had to design wireframes, in order to produce a layout of how we wanted the application to look. 

This project provided a lesson for not only my group, but for myself, as to what it means to practice Agile development as we had to function as if we were a fullstack development team. We particpated in various Agile techniques such as pair programming and code reviews. 


## How this project was completed

In order to build out this application, we first had to build our backend. My team consisted of myself, and my fellow apprentices: Serkadis Dubale, Lauren Richardson, and Dar-Ci Calhoun. Together, we created a kanban board so that all tasks related to the project could be delegated accordingly. 

I built out the models that were need for the project. Using Express, Sequelize, and SQLite. In using these technologies I was able to define our models, their attributes, as well as their data types. You can see an example of this below: 

<p align="center" >
<img  width=400 src="Project Visuals/fun-code2.png" alt="animated"/>
</p>

As show in the above photo, each item will have one of the following attributes: title, which is the name of the item, the price of the item, an item description, an item category, and lastly an item image. Each attribute has its own data type based on what we want the user to see. For example, for the price attribute you can see that the data type is listed as <code>NUMBER</code>, which will show the price as a number versus as a string. Once the model was created, we moved on to creating the routes so that the user could interact with our application.

<p align="center" >
<img  width=400 src="Project Visuals/fun-code1.png" alt="animated"/>
</p>
<p align="center"> 
<i> Here are the CRUD routes that we created so that a user is able to view all of the items in our inventory as an endpoint that allows the user to see one invidiual item and it's contents. </i>
</p>

You may have seen in the photo above, some of the routes (endpoints) that we created as well. This tasks was completed by my fellow apprentice Serkadis Dubale. Each endpoint allows the user to view all of the items, to view an individual item, to create an item, and updating and deleting items as well. Lauren Richardson created our front end, of which I have included a photo below: 

<p align="center" >
<img  width=400 src="Project Visuals/fun3.png" alt="animated"/>
</p>

The front end was created using React, along with HTML and CSS for styling. Dar-Ci Calhoun, performed all debugging, and we also worked together to write out all of the tests as well. The test were written in order to make sure that our routes were working and pulling the correct information based on the seed data that we had created. For this, we used the Jest testing framework, as this is what we were taught, through this I was able to better understand why it is so important to create unit tests for any project that you are working on. Unit tests allow you to see if the code that you are going to right is going to function as intended and really allows you to refactor your code if you find that something does not work properly for your application.

The Inventory App was one of the more challenging projects that I have had to work on. Working on a team can be diffucult if the rapport, as well as the group-work ethic, is not established from the start. I found that this was never an issue, I really enjoyed working on this project with my peers. I learned alot from each of them, each lesson enhancing my technical ability as well as my soft skills in working on a team. We worked together very well and worked with one another to resolve any issues that may have come up along the way. 

This specific project was also a really great way for me to practice building out a backend in JavaScript and really working with the tech stack that we were taught by Multiverse. This projects helped to properly develop my skills with version control, mastering pull requests and merging prepared me to continually practice great version control. It was an honor working along side this group of talented apprentices and I look forward to collaborating with them in the future! 

You can view more of this project here:

[Inventory App](https://github.com/F-U-N-mv/inventory-app)

You can also find the project presentation here: 

[Cisco SWE Multiverse: Team F.U.N Inventory App Presentation](https://youtu.be/q2yERO9hfsk)


## Ackowledgements 

I would like this opportunity to thank my teammates: Serkadis Dubale, Lauren Richardson, Dar-Ci Calhoun. I truly enjoyed working with you all, every part of this project was a learning experience. Each one of you have taught me a lesson that I will carry with me throughout my career. I loved our group dynamic and how cohesively we worked together. Thank you all for being great! 
