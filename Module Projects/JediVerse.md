# Project 3 - JediVerse

A high-level overview of the project purpose:

## :memo: Situation

The JediVerse is frontend web application that I created during the Multiverse Frontend Module. The JediVerse is a complete encyclopedia of all the people, planets, films, species, and starshps that make up the Star Wars Universe. 

## :pushpin: Task 

- There are multiple components that make up this application. The <code>components</code> folder housea all of the components that make up the individual pages of the application. 

- The <code>App.js</code> file is the main page that serves as the entry point and root component of the application. This is where I defined the main structure and layout for my UI. 

- I used Semantics UI for React to style all of the buttons and the navbar. I also created a wireframe help me visualize how I wanted the application to look. 

<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jediverse-wireframe.png" alt="animated"/>
</p>


## :computer: Action 

<li> I built the JediVerse by using React and linking the Star Wars API better known as SWAPI. I followed the documentation listed on the API website and following the examples on to reach each endpoint. Using a navbar component, I was able to create a navbar that holds individual tabs that navigate to each endpoint.</li>

<li>In the <code>App.js</code>, I established all of the state variables needed to fetch all of the information needed from the Star Wars API. I created multiple fetch calls in order to fetch all of the information that I needed from the different endpoints in the API. Each component has a different endpoint in which data is being fetched. The data from each endpoint was passed as a prop to each component, under the name of <code>data</code>. Each instance of <code>data</code> held the value of the different state variables that created for each component.</li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jv-app.png" alt="animated"/>
</p>

<li> Each state variable manages the state for each individual component that I created. I also used pagination, as each endpoint, contains between 30-80 objects. I wanted to use pagination to design a dynamic UI that allows the user to flip through each page of data. Upon initially fetching the data, the page is always set to 1. I also created the event handlers (<code>handleNextPage</code> & <code>handlePreviousPage</code>) needed to move through each page of data for each endpoint. The event handlers were passed as props, <code>next</code> and <code>previous</code>.
</li>

***add screenshots of pagination here***


<li> I followed the same data structure for each of the components, pulling only specific key-values that I wanted to be visible to the user. I used the map function to map through each object so that they could easily be displayed in an array. In order to display the information. For each component I created the variables <code>totalPages</code> and <code>isLastPage</code>. Each data component follows this structure, the Navbar and Home components were built slightly different.
</li>

<br>

<p align="center" >
<img  width=600 src="Project Visuals/screenshots/swapi-data.png" alt="animated"/>
</p>
<p align="center"><i>This is how the data looks when grabbed from the API directly, as you can see in the photo below, I only grabbed certain key values in order to display specific pieces of information.</i></p>
<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jv-people.png" alt="animated"/>
</p>

<p align="center"><i> As shown in the photo above, on line 20, I styled each piece of data that was I mapping in a grid so that I could display the data in a way that was readable to the user. Each card has a header, a title, and a description, which includes the individual atrributes that are present for the People component.</i></p>


<li> For the look and feel on the UI, I used Semantics UI and Semantics CSS, to style the buttons as well give the color scheme to the Navbar. I used CSS to add a background image and also used a cursor website that allowed me to set the cursor as R2-D2.</li> 

<li>Last but not least, I made my homepage very interactive. On the homepage I added each movie poster for each Star Wars movie. In order to have each poster show up on after the other, I created and array called <code>posters</code>, that held 9 different objects with the key-value pairs of <code>image</code> and <code>video</code>. </li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jv-home-page.jpg" alt="home-page"/>
</p>
<p align="center"><i>Here you can see how the movie posters and home page has been designed. At the top included a gif and provided a brief description of wjat can be found on my application. The navbar can be seen at very top portion of the page and clearly maps out each tab to each API endpoint.</i></p>

<li> Next, I was given the task of making the posters clickable so when the user hovers over the poster a message pops up that says "Click me!" and then takes the user to an external link. In order to complete this, I create two pieces of state <code>hoveredIndex</code> and <code>setHoveredIndex</code> this piece of state changes each time a user hovers over an image.</li>
 
 ***add screenshot of state here***

<li>I used the map function to go through each index of the <code>posters</code> array and diplayed each one in a grid column in the form of a card. Once this was established, I used the event handler, onMouse and created logic that would display the "Click me!" message each time the cursor was over the poster image. I also created logic that when the user navigated over to the poster image and clicked on it, it would then take them to an external link, this link being the <code>poster.video</code> attribute. </li>



***add screen of map function and onMouse event logic here***


## :movie_camera: Result (Video Presentation + Project Repo) 

- [JediVerse Repository](https://github.com/jedi-verse-MV/jediverse-MV/tree/main)
- [JediVerse Project Board](https://github.com/orgs/jedi-verse-MV/projects/1)

[![Watch the video](https://i.imgur.com/cHE8DU8.jpg)](https://www.youtube.com/watch?v=xO90thlEhC8)


## :floppy_disk: Technologies

Front End 
<ul>
<li>React</li>
<li>React Router</li>
<li>Semantics UI React</li>
<li>Semantics UI CSS</li>
</ul>

Linked API 
 
- [Star Wars API](https://swapi.dev/)

## :book: Competencies

