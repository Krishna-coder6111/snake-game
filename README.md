# snake-game
class 11 project -> new improved with college concepts
\n
\nI was looking at the final project I made when I was in grade 11.
\nAt the time it felt like such a challenge. I needed to debug for a lot of time before it actually started working.
\nLooking back 300 lines of code is basically nothing when you're a CS major.
\nHere are some of the pros and cons of my design
\n
\nPros:
\n
\nSimple and clear code structure: The code is organized into functions that handle specific tasks, making it easier to understand and maintain.
\nModular design: The game loop, snake movement, food generation, and other game aspects are separated into different functions, allowing for easier modification and expansion.
\nAdditional features: The implementation includes a start menu, pause functionality, and restart option, which enhances the game experience.
\n
\nCons:
\n
\nGlobal variables: The code relies heavily on global variables, which can make it more challenging to maintain and debug. Encapsulating the game logic in classes would improve code organization and reduce the reliance on global variables.
\nInefficient collision detection: The snakesnake() function checks for collisions between the snake's head and its body by iterating through the entire body. A more efficient approach would be to check for collisions only with the snake's head.
\nLack of comments and documentation: The code lacks comments and documentation, which can make it difficult for others to understand and modify the code. Adding comments and docstrings would improve code readability.
\nHard-coded values: The code contains hard-coded values for dimensions, colors, and positions. Using constants or configuration files would make the code more adaptable and easier to modify.
\nInconsistent formatting: The code has inconsistent formatting (e.g., indentation, spacing, and naming conventions). Following a consistent style, such as the PEP 8 style guide, would improve code readability and maintainability.

