const GRID_SIZE = 21;

export function randomGridPosition() {
  return {
    x: Math.floor(Math.random() * GRID_SIZE) + 1,
    y: Math.floor(Math.random() * GRID_SIZE) + 1,
  };
}

export function outsideGrid(position) {
  return position.x < 1 || position.x > GRID_SIZE || position.y < 1 || position.y > GRID_SIZE;
}

//The random grid function provides us with a random grid location each time the snake reaches the food. This allows the grid location of the food to change after it is eaten by the snake 

//The outsideGrid function checks to see if the snake head has touched an area outside of the grid. It checks to see if the position that we pass into the function is greater that our grid size or if its less than 1 which is our grid size. 