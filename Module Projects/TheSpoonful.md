# Project 3 - The Spoonful Blog

 An enhanced breakdown of the project purpose:

## :memo: Situation

The Spoonful Blog is a full-stack application created for Module 2 - Deployment, week 5 of the Multiverse Curriculum. The main concept of the Spoonful Blog is to create a full-stack web application that demonstrates proficiency in frontend technologies such as React, and backend technologies like Express and successfully deploying an application using GitHub Actions.

## :pushpin: Task

<li>There are multiple core parts to this project, specifically the backend architecture and deployment architecture. The backend architecture is housed in the <code>server</code> folder and the CI/CD for deployment is housed in the <code>.github/workflows</code> folder. The front end, a wonderful addition to the project is housed in the <code> public </code> folder. </li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/spoonful_app/spoonful-home page .png" alt="animated"/>
</p>

<li> The design for this project was mainly focused on user readability and executing CI/CD properly. We wanted to make sure that our backend architecture fell in line with the vision that we had for the front end as well. My team and I held weekly meetings where we had planning sessions and delegated each task necessary to complete the project.</li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/spoonful_app/spoonful-kanban.png" alt="animated"/>
</p>

## :computer: Action

<li> My main contributions to the application revolved around backend and frontend development</li>

<li> Backend Development
<br>
<ul style="list-style-type: square">
  <li>Establishing the server and models using <code>Sequelize</code> and <code>Sqlite3</code></li>

  <li>Creating the db file to instantiate the database</li>
  <br>
  <p align="center" >
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-db-setup.png" alt="animated"/>
  </p>

  <li>Creating the <code>User</code> and <code>Post</code> models that establish the data types for the user and the posts.</li>
  <br>
 <p align="center">
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-post-model.png" alt="animated"/>
  <br>
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-user-model.png" alt="animated"/>
  </p>  
  <br>

  <li>Creating a file to handle all middleware so that <code>HTTP</code> requests could be made and form input data could be handled from the front-end</li>
  <br>
  <p align="center">
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-middleware.png" alt="animated"/>
  </p>  
  <br>

  <li>Installed all necessary dependencies and packages needed to complete the project</li>
  <br>
  <p align="center">
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-dependencies.png" alt="animated"/>
  </p>
  <br>

  <li>Setting up CI/CD files</li>
  <br>
  <p align="center">
  <img  width=600 src="Project Visuals/spoonful_app/spoonful-ci-cd.png" alt="animated"/>
  </p>  

</ul>
</li>

<li> Front End

<ul style="list-style-type=square">
<br>
<li>Setting up front-end folder and installing all front-end dependencies</li>

<li>Created <code> App, Form, Post, </code> and <code> PostList</code> components</li>

<li> Established logic and state for the <code> App, Form, Post, </code> and <code>
PostList</code> components</li>
<br>
<p align="left" >
<img  width=600 src="Project Visuals/spoonful_app/spoonful-app-js.png" alt="animated"/>
<br>
<img  width=600 src="Project Visuals/spoonful_app/spoonful-react-form.png" alt="animated"/>
<br>
<img  width=600 src="Project Visuals/spoonful_app/spoonful-form-handlesubmit.png" alt="animated"/>
</p>
<br>
<li>Set up the file that would link the backend to the front end</li>
<br>
<p align="left" >
<img  width=600 src="Project Visuals/spoonful_app/spoonful-backend-link.png" alt="animated"/>
</p>
<br>
<li>Set up the root file for the front end</li>
<p align="left" >
<img  width=600 src="Project Visuals/spoonful_app/spoonful-react-root.png" alt="
</ul>
</li>

<li> Other contributions
<ul style="list-style-type=square">
<li>Helped to create logos for the application</li>
<li>Created and updated repo README file</li>
</ul>
</li>

## :movie_camera: Result (Video Presenation + Project Repo)

- [The Spoonful Blog Repo](https://github.com/the-spoonful-blog/spoonful-fullstack)
- [Spoonful Blog README](https://github.com/the-spoonful-blog/spoonful-fullstack#readme)
- [Spoonful Blog Kanban Board](https://github.com/orgs/the-spoonful-blog/projects/1/views/1?layout=board)

<p align="center"><i>Click the thumbnail below to be redirected to the presentation video!</i></p>

[![Watch the video](https://i.imgur.com/VuBVagh.png)](https://www.youtube.com/watch?v=w9821OUwI6Q)

## :floppy_disk: Technologies

Front End
<ul>
<li>React <code>(v18.2.0)</code></li>
<li>Bootstrap <code>(v5.2.3)</code></li>
<li>CSS</li>
<li>HTML</li>
<li>Parcel <code>(v2.8.3)</code> </li>
<li> Parcel-Bundler <code>(v1.8.1)</code></li>
<li>Babel <code>(v6.23.0)</code></li>
</ul>

Back End
<ul>
<li>Express <code>(v4.18.2)</code></li>
<li>CORS(Cross-origin resource sharing) <code>(v2.8.5)</code></li>
<li>Jest <code>(v29.5.0)</code></li>
<li>Sequelize <code>(v6.31.0)</code></li>
<li>Sqlite3 <code>(v5.1.6)</code></li>
</ul>

Other dependencies
<ul>
<li>Concurrently <code>(v8.0.1)</code></li>
<li>Dotenv <code>(v16.0.3)</code></li>
<li>Morgan <code>(v1.10.0)</code></li>
</ul>

## :book: Competencies

### JF 1.5

#### Can work effectively and contribute appropriately on a team to produce software

 Not only did I work independently on the parts that I added to this project but I also effectively collaborated with my team. In order to complete this action, I helped to facilitate weekly meetings not only to discuss project topics but also to discuss how to begin the SDLC for our project. I would work with my team to assign individual tasks to each member of the group, make sure that they were comfortable with the task, and also offer help should the need arise. I also created a group WebEx space so that we could all effectively communicate with each other.

### JF 1.6

#### Can follow software designs and functional/technical specifications

By reviewing all project requirements, myself and my team were able to break down how this project needed to be completed. By following the guidelines that were laid out for each tier of the project, I was able to complete each component of the project that was assigned to me. In doing so I was not only able to complete my assigned tasks but also assist with other tasks that were assigned to the team.

### JF 2.1

#### Can create and analyze artifacts, such as use cases and/or user stories

While implementing the code for the backend, i.e. defining the models, I thought of ways the user could interact with the application. An example is that a user could add a post to the site through the use of a form. If a user wanted to share a dish that they had recently, they are able to do so by submitting their photo and text through the use of a form.

### JF 2.3

#### Can develop effective user interfaces

This project was a huge challenge for me. I have never built a React application from scratch before. I researched different ways to make an effective React application and tried to place myself in the position of a user. In doing so, I was able to establish a great structure for the front end. My teammates and I were able to use various components to help bring this application to life. I was also able to teach my team how to start a React application from scratch and how to create a form component.

### JF 2.4

#### Can create simple software designs to effectively communicate understanding of the program

I collaborated and took the lead on multiple tasks throughout this project, including the way in which our code was structured. I first started by building out the model for our backend so that we could accurately list all of the data that we needed. I participated in various sessions that led to the creation of the logic around some of the endpoints as well as creating the logic for the test for each endpoint. I collaborated with my team on how the UI would be designed as well.

### JF 2.6

#### Can translate wireframes into User Interfaces

For this project, I and my team used a wireframe to lay out how we wanted our front end to interact with the backend. Using a wireframe allowed us to really think about what we wanted from this application and how we all wanted it to look. Through this, I was also able to communicate, break down, and visualize how I thought users should interact with the application. While the application is simplistic in its design, using a wireframe for the planning portion of the project was very useful.

### JF 3.4

#### Can create a logical and maintainable codebase

Throughout this project, I assisted in merging pull requests from various branches that were created for each component of the project. I collaborated and took the lead on multiple tasks that were assigned throughout the duration of this project as well. Through code reviews, I was able to review code with my team to merge and approve pull requests. By creating branches for specific components of the project, I was able to help maintain readability within the code base.

### JF 3.6

#### Can implement a RESTful API

In order to complete this task, I followed the software architecture that makes an API RESTful, this includes:

- Having a client-server architecture, in this case, a front end that communicates directly with a backend that is made up of a server and HTTP requests
- Using multiple endpoints such as GET, POST, PUT, AND DELETE
- Using middleware to have access to sending requests and receiving responses via HTTP requests
- Having stateless-client communication
- Having data represented in the form of JSON
- Using resource-based data retrieval, For example, '/posys' represents a list of posts, but "/posts/1" represents a specific item.

### JF 5.5

#### Understands and can apply structured techniques to problem-solving, can debug code, and can understand the structure of programs to identify and resolve issues

When creating this application, there were a lot of obstacles that I and my team faced, specifically when it came to debugging. In order to make sure that I was getting the desired information from each endpoint, my team and I used console logs to verify that the data was in fact being retrieved in the browser. My team and I also utilized our weekly team meetings to have debugging sessions to make sure that our application was working the way that we wanted.

### JF 6.5

#### Works collaboratively with a wide range of people in different roles, internally and externally, with a positive attitude to inclusion & diversity

For this project I worked with two other people, it has never been difficult for me to work in a group and collaborate with others. I find that for certain projects this is the easiest approach, especially with projects that require multiple stages of development. Throughout the time that I worked with my teammates on this project, we all worked together to establish effective lines of communication and talk to resolve any issues that we may have had. We held team meetings twice a week to discuss any tasks that we were working on and worked to solve any bugs that came up as well. I made myself available to my teammates whenever they needed me.

## Collaborators

<ul>
<li> Addy Rodriguez: <a href="https://github.com/AddyRdz">@AddyRdz</a></li>
<li> Deja Clarke: <a href="https://github.com/dejac17">@dejac17</a></li>
<li> Krystal Lopez: <a href="https://github.com/krystallopez">@krystallopez</a></li>
</ul>
