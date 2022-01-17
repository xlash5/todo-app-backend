
# TODO APP

## About App

This is a fullstack TODO app. Frontend is implemented by using react, backend is implemented by using Flask. Because I recently learned about Flask I wanted to make this app and practice my skills.

You can create a new user and authenticate yourself to start using the app.

IMPORTANT: because it uses SQLite for database and backend is deployed to heroku whenever server goes sleep database is resetting!


## Tech Stack

**Client:** React, styled-components, react-cookie

**Server:** Flask, Flask-JWT-Extended, SQLite

Here is link for the live frontend application: https://quirky-austin-fdfaf5.netlify.app/

Here is link for the live backend application: https://flask-todo-xlash.herokuapp.com/

Link for the frontend repo: https://github.com/xlash5/todo-app-frontend

Might add endpoints for the backend later on!

## To Run the App Locally

Clone this repository

Firstly you need to start the backend

Required packages: CORS, flask_jwt_extended, flask_restfull, werkzeug.security, flask_sqlalchemy

```bash
    cd flask-doto
    python app.py
```
Backend will start working on you local machine port 5000

Now we can start frontend and use the application

```bash
    cd react-todo
    yarn install
    yarn start
```
Your app will start working and will open in your browser automatically.

Happy coding 👨‍💻