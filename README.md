# Fantasy Stock - Football Player Investment Platform

## Overview
Fantasy Stock is a web application that allows users to invest in football players, similar to a stock market but for football players. Users can create accounts, view player statistics, and place bids on players they believe will perform well.

## Project Structure
```
FANTASY_STOCK/
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── App.js         # Main application component
│   │   ├── LoginForm/     # User authentication component
│   │   └── InvestPage/    # Main investment interface
│   └── package.json       # Frontend dependencies
├── backend/               # Flask backend application
│   ├── app.py            # Main API endpoints
│   ├── models.py         # Database models
│   ├── config.py         # Configuration settings
│   └── model-gpt.py      # AI model integration
└── marca-fantasy-scraper/ # Data scraping utility
```

## Features

### User Management
- User registration and authentication
- Session persistence using sessionStorage
- User profile management

### Player Management
- View player statistics and performance
- Player database with detailed information:
  - Player ID
  - Name
  - Team
  - Position (POR, DEF, CEN, DEL)
  - Current value
  - Previous scores
  - Total bids

### Investment System
- Place bids on players
- Track investment portfolio
- View player performance history
- Real-time bid updates

## Technical Stack

### Frontend
- React.js
- Modern JavaScript (ES6+)
- CSS for styling
- Session management for user persistence

### Backend
- Flask (Python)
- SQLAlchemy for database management
- RESTful API architecture
- JSON data format

### Database Models

#### User Model
- user_id (Primary Key)
- user_name
- players_bids (JSON)

#### Player Model
- player_id (Primary Key)
- player_name
- team
- position
- total_bids
- value
- prev_scores (JSON)

## API Endpoints

### Players
- GET /players - Get all players
- POST /players - Create new player
- GET /players/<id> - Get specific player
- PUT /players/<id> - Update player
- DELETE /players/<id> - Delete player

### Users
- GET /users - Get all users
- POST /users - Create new user
- PUT /users/<id> - Update user
- DELETE /users/<id> - Delete user

### Bids
- PUT /update_bid - Update player bid
- GET /get_user_bids/<id> - Get user's bids

## Setup and Installation

### Backend Setup
1. Create a Python virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database
4. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup
1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm start
   ```

## Future Enhancements
1. Implement player search functionality
2. Add real-time player statistics updates
3. Enhance user portfolio analytics
4. Implement player performance predictions
5. Add social features for user interaction

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 