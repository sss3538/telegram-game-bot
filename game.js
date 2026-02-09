// game.js - Flappy Bird-like Game Logic with Telegram Web App Integration

// Game variables
let bird; // Represents the bird
let pipes = []; // Array of pipes
let score = 0; // Player's score
const gravity = 0.6; // Gravity effect on the bird

// Initialize the game
function setup() {
    createCanvas(windowWidth, windowHeight);
    bird = new Bird();
    pipes.push(new Pipe());
}

// Main draw loop
function draw() {
    background(135, 206, 250); // Sky blue
    bird.update();
    bird.show();
    
    // Pipe management
    if (frameCount % 75 === 0) {
        pipes.push(new Pipe());
    }
    
    for (let i = pipes.length - 1; i >= 0; i--) {
        pipes[i].show();
        pipes[i].update();
        
        // Check for collision
        if (pipes[i].hits(bird)) {
            console.log("Game Over!");
            noLoop(); // Stop the game
        }
        
        // Increase score
        if (pipes[i].offscreen()) {
            pipes.splice(i, 1);
            score++;
        }
    }
    
    // Display score
    fill(255);
    textSize(32);
    text("Score: " + score, 10, 30);
}

// Class representing the bird
class Bird {
    constructor() {
        this.y = height / 2;
        this.x = 64;
        this.gravity = 0.6;
        this.lift = -15; // Jump lift
        this.velocity = 0;
    }
    
    // Update the bird's position
    update() {
        this.velocity += this.gravity;
        this.y += this.velocity;
        
        // Prevent bird from falling out of bounds
        if (this.y > height) {
            this.y = height;
            this.velocity = 0;
        }
        if (this.y < 0) {
            this.y = 0;
            this.velocity = 0;
        }
    }

    // Show the bird
    show() {
        fill(255, 204, 0);
        ellipse(this.x, this.y, 32, 32);
    }
    
    // Jump method
    jump() {
        this.velocity += this.lift;
    }
}

// Class representing pipes
class Pipe {
    constructor() {
        this.spacing = 100; // Space between pipes
        this.top = random(height / 6, (3 / 5) * height);
        this.bottom = height - (this.top + this.spacing);
        this.x = width;
        this.w = 40; // Pipe width
        this.speed = 6; // Pipe speed
    }

    // Show pipes
    show() {
        fill(0, 255, 0);
        rect(this.x, 0, this.w, this.top);
        rect(this.x, height - this.bottom, this.w, this.bottom);
    }

    // Update pipe position
    update() {
        this.x -= this.speed;
    }

    // Check for collision
    hits(bird) {
        if (bird.y < this.top || bird.y > height - this.bottom) {
            if (bird.x > this.x && bird.x < this.x + this.w) {
                return true; // Collision detected
            }
        }
        return false;
    }

    // Check if pipe is off screen
    offscreen() {
        return this.x < -this.w;
    }
}

// Event listener for Telegram Web App integration
window.Telegram.WebApp.onEvent('backButtonClicked', function() {
    // Handle the back button click event
});

// Function to start the game
function startGame() {
    setup();
    window.Telegram.WebApp.MainButton.show();
}

// Call 'startGame' function through Telegram Web App
startGame();