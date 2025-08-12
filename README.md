# Flask CRUD Blog - Training Project "Masterblog"

This project is a training exercise designed to demonstrate the fundamentals of building a web application with Python and the Flask micro-framework. It covers the core concepts of **CRUD** (Create, Read, Update, Delete) operations, rendering dynamic web pages using Jinja2 templates, and handling data storage with a simple JSON file.

This is a great exercise for beginners to understand how a back-end server handles requests, manages data, and interacts with a front-end interface.

A special thanks to **MasterSchool** for providing this valuable exercise and for the time taken to review and rate it.

## Project Structure

The project is organized into several key files and directories. 
- The core application logic, including all the routes for handling web requests, resides in the `main.py` file. 
- Blog posts are stored in a simple JSON file named `posts.json`. 
- A shell script, `devserver.sh`, is provided to easily start the Flask development server. 
- All Python package dependencies are listed in the `requirements.txt` file. 
- The `static` directory contains the application's CSS stylesheet, `style.css`. 
- The `templates` directory holds all the HTML files used for rendering pages: `index.html` for the main page that lists posts, `add.html` for the new post form, and `update.html` for the post editing form.

## How to Run the Project

This project is set up to run in a Nix-based development environment.

1.  **Activate the Environment:** First, ensure you are in the project's virtual environment.
    ```bash
    source .venv/bin/activate
    ```
2.  **Install Dependencies:** Install all the required Python packages using pip.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the Server:** Use the provided shell script to start the Flask development server.
    ```bash
    ./devserver.sh
    ```

The application will then be accessible in the web preview panel of your IDE.
