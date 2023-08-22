Here's a step-by-step documentation on how to integrate and use the webpage_summarizer_plugin in other Flask applications:

1. Install Dependencies:
   I have provided the 'requirements.txt' file in this repo.
   Just open the terminal and run the following command to install the required dependencies.
   The command is: "pip install -r requirements.txt".

   This will install all the necessary dependencies.

2. Create a New Flask Application:
   If you don't already have a Flask application, create a new one by setting up the directory structure and creating the necessary files (app.py, templates folder, static folder, etc.).

3. Copy the Plugin Files:
   Copy the 'webpage_summarizer_plugin' directory (including '**init**.py', 'routes.py', templates folder, and static folder) into your project's root directory.

4. Update HTML Templates:
   If your existing templates reference CSS or JavaScript files, make sure to update the URLs to use the static route provided by Flask, like this:

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}" />
    <script src="{{ url_for('static', filename='script.js') }}"></script>

5. Run the Application:
   You can run your application using the development server provided by Flask.
   The command to run is: "flask run" OR "python app.py"

   If you want to deploy it on any webserver, then just copy the files from the static folder into that of your webserver's public directory.

   Alternatively, for production deployment, you can use a WSGI server like Gunicorn: gunicorn app:app

6. Access the Plugin:
   Open a web browser and navigate to http://localhost:8000 (or the appropriate address if you're running on a different port). You should see the plugin integrated into your application.

7. Customize and Extend:
   You can customize the plugin's behavior, appearance, and functionality to fit your application's requirements. You can modify the routes in routes.py, update the CSS in styles.css, and adjust the JavaScript in script.js.

By following these steps, you should be able to seamlessly integrate the webpage_summarizer_plugin into your existing Flask application and utilize its features for summarizing web content.
