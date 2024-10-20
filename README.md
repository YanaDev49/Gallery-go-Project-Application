# Welome to Gallery go! 

 **Gallery go!** is an aesthetic and interactive web application where every visit earns you points! I built this as a way to integrate my keen eye for design with some docker principles I've been learning: **Flask**, **Redis**, and **Docker Compose**. This web application is simple, but with dynamic backgrounds and a live leaderboard, which is an engaging way to track visits and make the experience more visual. Hope you enjoy exploring it!

## Features 

- **Earn Points**: Every time you visit or hit the **‘Earn Points’ button**, you collect points. After accessing the web page for the first time, you can earn points by simply restarting the page!

- **Live Leaderboard**: See how your score stacks up against other visitors in real-time. (adds a competitive edge, am i right?)

- **Dynamic Backgrounds**: Each refresh or point earned gives you a new background from the world's most stunning galleries. This adds the aesthetic element of the appllication that i was going for!

- **Gamified Experience**: Just a fun, interactive way to make visiting the site more engaging! i wanted to add an additional feature of gamification to my application to engage users and encourage participation.

## Tech Stack ���️

- **Flask**: Handles the web app, routes, and user interactions.

- **Redis**: Tracks visit counts and user points in real-time using an in-memory database.

- **Docker & Docker Compose**: Powers the app in a multi-container setup, with separate containers for Flask and Redis.

## Getting Started 

### Prerequisites
- **Docker** and **Docker Compose** installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-container-flask-app.git
   cd multi-container-flask-app

### Build and run the containers:
2. docker-compose up --build

### Access:
4. Open your browser and go to http://localhost:5001

