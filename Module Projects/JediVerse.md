# Project 3 - JediVerse

A high-level overview of the project purpose:

## :memo: Situation

The JediVerse is frontend web application that I created during the Multiverse Frontend Module. The JediVerse is a complete encyclopedia of all the people, planets, films, species, and starshps that make up the Star Wars Universe. 

## :pushpin: Task 

- There are multiple components that make up this application. The <code>components</code> folder housea all of the components that make up the individual pages of the application. 

- The <code>App.js</code> file is the main page that serves as the entry point and root component of the application. This is where I defined the main structure and layout for my UI. 

- I used Semantics UI for React to style all of the buttons and the navbar. 

## :computer: Action 

<li> I built the JediVerse by using React and linking the Star Wars API better known as SWAPI. I followed the documentation listed on the API website and following the examples on to reach each endpoint.</li>

<li>In the <code>App.js</code>, I established all of the state variables needed to fetch all of the information needed from the Star Wars API.I created multiple fetch calls in order to fetch all of the information that I needed from the different endpoints in the API. Each component has a different endpoint in which data is being fetched. The data from each endpoint was passed as a prop to each component, under the name of <code>data</code>. Each instance of <code>data</code> held the value of the different state variables that created for each component.</li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jv-app.png" alt="animated"/>
</p>

<li> Each state variable manages the state for each individual component that I created. I also used pagination, as each endpoint, contains between 30-80 object. I wanted to use pagination to design a dynamic UI that allows the user to flip through each page of data. Upon initially fetching the data, the page is always set to 1. I also created the event handlers (<code>handleNextPage</code> & <code>handlePreviousPage</code>) needed to move through each page of data for each endpoint. The event handlers were passed as props, <code>next</code> and <code>previous</code>
</li>

<li> I followed the same data structure for each of the components, pulling only specific key-values that I wanted to be visible to the user. I used the map function to map through each object so that they could easily be displayed in an array. In order to display the information. For each component I created the variables <code>totalPages</code> and <code>isLastPage</code>. Each data component follows this structure, the Navbar and Home components were built slightly different.
</li>

<br>
<p align="center" >
<img  width=600 src="Project Visuals/screenshots/jv-people.png" alt="animated"/>
</p>

<p align="center"><i> As shown in the photo above, on line 20, I styled each the data that was I mapping in a grid so that I could display the data in a way that was readable to the user. Each card has a header, a title, and a description, which includes the individual atrributes that is present for the People component.</i></p>





## :movie_camera: Result (Video Presenation + Project Repo) 



## :floppy_disk: Technologies

- list front end tech
- list dependencies

## :book: Competencies

-