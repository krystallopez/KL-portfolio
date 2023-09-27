# Project 1 - The Inventory App 

An enchanced breakdown of the project purpose:

## :memo: Situation

The Inventory App is a fullstack web application created for Bootcamp Part 2, Week 8 of the Multiverse curriculum. The main concept of the Inventory App is a mock e-commerce app in which the e-commerce company can track the inventory of the items that are listed on the website.

## :pushpin: Task 

- There are a lot of core parts to this project, specifically the <code>public</code> and <code>server</code> files. The <code>public</code> folder houses all of the code for the frontend UI. The <code>server</code> folder houses all of the code for the backend.

<br>
<p align="center" >
<img  width=600 src="Project Visuals/inventory_app/fun1.png" alt="animated"/>
</p>



- The design for this project was mainly focused on user readability and the backend codebase. We wanted to make sure that all of information that was needed was being fetched properly from the backend. My team and I held sessions in which we delegated each task necessary to complete the project.

<br>

<p align="center" >
<img  width=600 src="Project Visuals/inventory_app/funkanban.png" alt="animated"/>
</p>

## :computer: Action 
<li>My main contributions revolved around the backend development and TDD.</li>

<li>  Backend Development
<ul style="list-style-type: square">
   <li> Express for creating the backend routing and handling of <code>HTTP</code> requests, creating the API, and integrating middleware.
   </li>
   <li> Sequelize/SQLite to set up the relational database using JavaScript objects and methods. SQLite was used to help create the <code>server</code> and seed the database
   </li>
   <li> Jest was used to create the tests needed to make sure that all routes were functional and fetched the data from the DB properly.
   </li>
</ul>
</li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/inventory_app/inventory-test.png" alt="animated"/>
</p>

<p align="center"><i>This a small snippet of the test that were written for this project.</i></p>
<br>

<p align="center" >
<img  width=600 src="Project Visuals/inventory_app/fun-code1.png" alt="animated"/>
</p>
   
<p align="center"><i>Here is a snippet of the Items routes that I assisted with for this application.</i></p>

## :movie_camera: Result (Video Presenation + Project Repo) 

- [Team F.U.N. Repo](https://github.com/F-U-N-mv/inventory-app)
- [Original Team F.U.N README](https://github.com/F-U-N-mv/inventory-app/blob/main/README.md)
- [Team F.U.N Kanban Board](https://github.com/orgs/F-U-N-mv/projects/1)
- [Cisco SWE Multiverse: Team F.U.N Inventory App Presentation](https://youtu.be/q2yERO9hfsk)

<p align="center"><i>Click the thumbnail below to be redirected to the presentation video!</i></p>

[![Watch the video](https://i.imgur.com/Ska6lJz.gif)](https://www.youtube.com/watch?v=q2yERO9hfsk)

## :floppy_disk: Technologies

Front End 
<ul>
  <li> React <code>(v18.2.0)</code> </li>
  <li> CSS </li>
  <li> HTML5 </li>
  <li> Babel <code>(v7.15.0)</code></li>
  <li> Parcel <code>(v2.8.3)</code> </li>
  
  
</ul> 

Backend
<ul>
<li>Node <code>(v19.6.0)</code></li>
<li>Express <code>(v4.17.1)</code></li>
<li>Sequelize <code>(v6.23.2)</code></li>
<li>SQLite3 <code>(5.1.1)</code></li>
<li>Jest <code>(v27.1.0)</code></li>  
<li>Nodemon <code>(v2.0.19)</code></li>
</ul>

## :book: Competencies

### JF 1.5

#### Can work effectively and contribute appropriately on a team to produce software

 Not only did I work independently on the parts that I added to this project but I also effectively collaborated with my team. In order to complete this action, I helped to facilitate weekly meetings not only to discuss project topics but to also to discuss how to begin the SDLC for our project. I would work with my team to assign individual tasks to each member of the group, make sure that they were comfortable with the task, and also offered help should the need arise. I also created a group WebEx space so that we could all effectively communicate with each other.


### JF 1.6

#### Can follow software designs and functional/technical specifications

By reviewing all project requirements, myself and my team were able to break down how this project needed to be completed. By following the guidelines that were laid out for each tier of the project, I was able to complete each component of the project that was assigned to me. In doing so I was not only able to complete my assigned tasks but also assist with other tasks that were assigned to the team. 


### JF 2.1 

#### Can create and analyze artefacts, such as use cases and/or user stories

While implementing the code for the backend, i.e defining the models, I thought of ways the user could interact with the application. An example, being that a user could add an item to the store through the use of a form. What if a worker was notified that the company was receiving a new item to the inventory and wanted to have a way to add it directly to the website? Not having a procedure to complete this action could slow down the momentum of the company. If a worker wants to add an item directtly to the company inventory then they can do so through the use of the form. 


### JF 2.4 

#### Can create simple software designs to effectively communicate understanding of the program

I collaborated and took the lead on multiple tasks throughout this project, including the way in which our code was structured. I first started by building out the model for our backend so that we could accurately list all of the data that we needed to. I participated in various creating the logic around some of the endpoints as well as creating the logic for the test for each endpoint. I collaborated with my team on how the UI would be designed as well. 

### JF 3.4

#### Can create a logical and maintainable codebase

Throughout this project, I assisted in merging pull requests from various branches that were created for each component of the project. I collaborated and took the lead on multiple tasks that were assigned through the duration of this project as well. Through code reviews, I was able to review code with my team to merge and approve pull requests. By creating brances for specific components of the project, I was able to help maintain readability within the code base. 


### JF 3.6 

#### Can implement a RESTful API 

In order to complete this task, I followed the software architecture that makes an API RESTful, this includes:

- Having a client-server architecture, in this case, a front end that communicates directly with a backend that is made up of a server and HTTP requests 
- Using multiple endpoints such as GET, POST, PUT, AND DELETE 
- Using middleware to have access to sending requests and receieving responses via HTTP requests 
- Having stateless-client communication 
- Having data represented in the form of JSON 
- Using resource-based data retrieval, For example, '/items' represents a list of items, but "/items/1" represents a specific item. 


### JF 4.8 

#### Can identify and create test scenarios

For this project, I was able to create a test for each endpoint to ensure that all of the data requested by each endpoint was accurately shown on the UI. This involved creating individual test for each endpoint and in those tests calling on specific pieces of data such as an item's description or an item's price. 


<p align="center" >
<img  width=600 src="Project Visuals/inventory_app/inventory-test-3.png" alt="animated"/>
</p>

<p align="center"><i>As you can see, each endpoint, GET, POST, PUT, and DELETE are being tested to ensure that all of the requested information is received properly </i></p>


</ol>

## Collaborators
<ul>
<li> Lauren Richardon: <a href="https://github.com/l-Rich">@l-Rich</a></li>
<li> Dar-Ci Calhoun: <a href="https://github.com/dcalhoun286">@dcalhoun286</a></li>
<li> Serkadis Dubale: <a href="https://github.com/serki12">@serki12</a></li>
<li> Krystal Lopez: <a href="https://github.com/krystallopez">@krystallopez</a></li>
</ul>