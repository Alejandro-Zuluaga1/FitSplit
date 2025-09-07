styles.css:

The styles.css file creates a visually appealing, modern, and responsive design for the web application. It uses the "Montserrat" font and a dynamic linear gradient background with a parallax effect. Interactive elements like buttons and pills have hover effects, including color changes, scaling, and a ripple effect on click. Cards which display workout information, have a dark background with rounded corners and shadows for a polished look. A preloader spinner appears while the page is loading, providing feedback to the user. The stylesheet also includes a media query to ensure the design adapts to smaller screens. Overall, the file enhances both functionality and aesthetics, providing an engaging user interface.


index.html:

My index.html file serves as the homepage for "FitSplit," introducing users to the platform and inviting them to begin their fitness journey. The central content includes a bold title, "FitSplit," accompanied by the subtitle, "Start Your Fitness Journey". Below the subtitle, a white "Start" button invites users to proceed, clicking the button redirects users to the /experience page to continue their journey. 


experience.html:

My experience.html template allows users to select their gym experience level as the first step in customizing their fitness plan. The page title, "Select Your Gym Experience Level" reflects its purpose, and it uses a linked styles.css file for custom styling. The text is followed by a form with buttons for three experience levels: Beginner, Intermediate, and Advanced. Each button is styled as a pill-shaped element, providing a clean and user-friendly design. When a user clicks on a button, the selected experience level is sent as a query parameter to the days route, guiding users to the next step, where they can choose the number of workout days. This page acts as an entry point for tailoring workout plans to users' fitness experience.


days.html:

My days.html template is used for selecting the number of workout days for a fitness plan. The page title is "Select Number of Workout Days" and custom styles are applied by linking a styles.css file. The form on the page submits the selected number of workout days while also passing the user's experience level through a hidden input field to the results page. The page dynamically generates buttons for selecting between 1 and 7 workout days using a for loop, where each button corresponds to a different number of days, and when clicked, redirects the user to the results page with the selected number of days as a query parameter. The buttons are styled as pill-shaped elements using the pill-container class, allowing users to easily choose their desired workout split. This page is part of a multi-step user flow for generating a personalized workout plan based on both experience level and the number of days selected.


results.html:

The results.html file dynamically generates and displays a tailored workout plan for users based on their selected preferences. The page's title dynamically updates to reflect the specific workout split, ensuring user relevance. Below the heading, an embedded YouTube video provides a tutorial related to the selected workout, enhancing the user's understanding and engagement. The workout days are displayed as interactive pills, which, when clicked, reveal the corresponding workouts for that day. For multi-day splits the file organizes the workouts into distinct sections, each revealed only when its respective pill is selected. For the three "Full Body Split" a single list of workouts is shown by default. A hidden div structure paired with a JavaScript function handles the seamless toggling between different workout days. This template uses Jinja2 templating to dynamically render data, such as the workout plan name, YouTube video URL, and workout details, provided by the server. 


video.html: 

My video.html file is designed to embed a video in the webpage if a valid video URL is provided. It uses an iframe to display the video, where the src attribute is dynamically populated with the video_url variable passed from the Flask route. If a video_url is available, the video is embedded with specified dimensions and allows fullscreen playback. If no video_url is provided, a message "Video not available for the selected plan" is displayed to the user instead. This template conditionally renders the video content based on whether the video_url is passed to it, the video displayed is one of 21 based on user input regarding experience level and the number of days they are planning on working out.

app.py:

    lines 1-3:

My app.py starts by importing necessary modules from Flask: Flask to create the app, render_template to render HTML templates, request to handle incoming requests, redirect to redirect users, and url_for to generate URLs dynamically. The app is then initialized with app = Flask(__name__), setting up the foundation for the app's routes and logic.

    lines 5-34:

The get_youtube_video_for_plan function takes two parameters: days and experience. It first normalizes the experience by capitalizing the first letter to ensure consistency in matching. The function then uses a dictionary, video_url_mapping, to map combinations of days and experience levels to corresponding YouTube video URLs. If a matching video URL is found, it returns the URL; otherwise, it defaults to a specific Beginner video URL.

    lines 36-701:

The code defines a dictionary, workout_plans, that maps combinations of experience level and workout days to specific workout plans. Each entry contains the workout split and a list of exercises associated with that plan. 

    lines 703-758:

The code defines several routes for the Flask web application. The index() route renders the main page (index.html). The experience() route handles the user’s selection of an experience level via a form, and redirects to the days() route with the selected experience as a query parameter. The days() route then retrieves the experience and number of days from the URL parameters and renders the days.html template. The get_workout_plan() function uses the experience and days inputs to fetch a corresponding workout plan from the workout_plans dictionary, adding a YouTube video URL to the plan. The results() route fetches the workout plan based on the experience and days parameters, rendering either the results.html page with the workout details or the index.html page in case of an error. 