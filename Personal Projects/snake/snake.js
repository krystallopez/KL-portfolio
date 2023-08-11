import { getInputDirection } from "./input.js";

export const SNAKE_SPEED = 5;
const snakeBody = [{ x: 11, y: 11 }];
let newSegments = 0;


// updates the snake
export function update() {
  // adds the new segments to the snake
  addSegments();

  // sets up the position
  const inputDirection = getInputDirection();
  for (let i = snakeBody.length - 2; i >= 0; i--) {
    snakeBody[i + 1] = { ...snakeBody[i] };
  }

  snakeBody[0].x += inputDirection.x;
  snakeBody[0].y += inputDirection.y;
}

//appends the snake to the gameboard 
export function draw(gameBoard) {
  snakeBody.forEach((segment) => {
    const snakeElement = document.createElement("div");
    snakeElement.style.gridRowStart = segment.y;
    snakeElement.style.gridColumnStart = segment.x;
    snakeElement.classList.add("snake");
    gameBoard.appendChild(snakeElement);
  });
}

//expands the snake each time a new segment is added 
export function expandSnake(amount) {
  newSegments += amount;
}

//takes in a positions and will determine if a position is on the snake. This will check each segment to see if its on the snake, then we compare the position of the snake with the segment position to see if they are equal. We add ignoreHead so that we are looping over the head 
export function onSnake(position, { ignoreHead = false } = {}) {
  return snakeBody.some((segment, index) => {
    if (ignoreHead && index === 0) return false;
    return equalPositions(segment, position);
  });
}
//This gives us the head of the snake so that we can check to see where the head is at and include this in our outsideGrid function so we can see if the snake head has touched an area outside of the grid 
export function getSnakeHead() {
  return snakeBody[0];
}

//This function checks to see if the snake has intersected itself by determining if the head of the snake is touching any of the other body parts on the snake. We want to ignore the head of the snake so that we don't loop over the head of the snake 
export function snakeIntersection() {
  return onSnake(snakeBody[0], { ignoreHead: true });
}

// This function will make sure that the first position at either axis is equalt to the second position at either axis. If the two positions are exactly the same this will return true, if not then it will return false. 
function equalPositions(pos1, pos2) {
  return pos1.x === pos2.x && pos1.y === pos2.y;
}

//add segments to the snake each time good is eaten, adding the new segments to the snake each time food is eaten. The for loop will run each time the snake eats the food and will append the new segment to end of the snake (an array) using the .push() method. We then reset the newSegments back to 0 so that no more new segments get added 
function addSegments() {
  for (let i = 0; i < newSegments; i++) {
    snakeBody.push({ ...snakeBody[snakeBody.length - 1] });
  }

  newSegments = 0;
}
//This page houses all of the functions that allow the snake to be drawn, the position of the snake to be updated as well as it's current position on the x and y axis of the grid.
