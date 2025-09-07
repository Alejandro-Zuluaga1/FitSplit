from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_youtube_video_for_plan(days, experience):
    # Normalize inputs to ensure consistent matching
    experience = experience.capitalize()  # Capitalize first letter for consistency

    video_url_mapping = {
        ("1", "Beginner"): "https://www.youtube.com/embed/Jn_C5AqWDNw",
        ("1", "Intermediate"): "https://www.youtube.com/embed/oiwCBlxIqdQ",
        ("1", "Advanced"): "https://www.youtube.com/embed/yAoscPCvY2k",
        ("2", "Beginner"): "https://www.youtube.com/embed/ZKKrqB57Lu4",
        ("2", "Intermediate"): "https://www.youtube.com/embed/tWKnF1K4rlU",
        ("2", "Advanced"): "https://www.youtube.com/embed/F6m6y6uRJQg",
        ("3", "Beginner"): "https://www.youtube.com/embed/MVb6_p6ThQM",
        ("3", "Intermediate"): "https://www.youtube.com/embed/ruVywF1y-Fk",
        ("3", "Advanced"): "https://www.youtube.com/embed/ijKRBjOGImo",
        ("4", "Beginner"): "https://www.youtube.com/embed/WTwVmw4SXA4",
        ("4", "Intermediate"): "https://www.youtube.com/embed/3h39ZSe5JTM",
        ("4", "Advanced"): "https://www.youtube.com/embed/bFCH1ISJkKg",
        ("5", "Beginner"): "https://www.youtube.com/embed/r_f6hdZrPsw",
        ("5", "Intermediate"): "https://www.youtube.com/embed/cepu0PrvBUc",
        ("5", "Advanced"): "https://www.youtube.com/embed/tw1lxpBQK1E",
        ("6", "Beginner"): "https://www.youtube.com/embed/wwZvrdB82vc",
        ("6", "Intermediate"): "https://www.youtube.com/embed/_Ce-oDTgKNg",
        ("6", "Advanced"): "https://www.youtube.com/embed/WvZhDEaT_8Q",
        ("7", "Beginner"): "https://www.youtube.com/embed/JetDtRVRVGw",
        ("7", "Intermediate"): "https://www.youtube.com/embed/PPgW4kah1p8",
        ("7", "Advanced"): "https://www.youtube.com/embed/nipDqK7S6Rk",
    }

    # Return the YouTube video URL if found, otherwise return Beginner embed
    return video_url_mapping.get((str(days), experience), "https://www.youtube.com/embed/Jn_C5AqWDNw")


workout_plans = {
    # Beginner Workouts
    ("beginner", 1): {
        "split": "Full Body Split",
        "workouts": [
            "Seated Chest Press",
            "Seated Low Row",
            "Machine Shoulder Press",
            "EZ Bar Curls",
            "Tricep Kickback",
            "Leg Extension",
        ],
    },

    ("beginner", 2): {
        "split": "Upper/Lower Split",
        "workouts": {
            "upper": [
                "Seated Chest Press",
                "Seated Low Row",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Tricep Kickback",
            ],
            "lower": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("beginner", 3): {
        "split": "Push/Pull/Legs",
        "workouts": {
            "push": [
                "Seated Chest Press",
                "Pec Deck",
                "Machine Shoulder Press",
                "Tricep Kickback",
            ],
            "pull": [
                "Seated Low Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("beginner", 4): {
        "split": "Upper/Lower Split (x2)",
        "workouts": {
            "upper": [
                "Seated Chest Press",
                "Seated Low Row",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Tricep Kickback",
            ],
            "lower": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "upper_2": [
                "Seated Chest Press",
                "Seated Low Row",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Tricep Kickback",
            ],
            "lower_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("beginner", 5): {
        "split": "Isolation Split",
        "workouts": {
            "chest": [
                "Smith Machine Bench Press",
                "Seated Chest Press",
                "Incline Seated Press",
                "Pec Deck",
            ],
            "back": [
                "Seated Low Row",
                "Seated Cable Row",
                "Wide Grip Lat Pulldown",
                "Close Grip Lat Pulldown",
            ],
            "legs": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "shoulders": [
                "Machine Shoulder Press",
                "Cable Front Raises",
                "Shoulder Shrugs",
                "Reverse Pec Deck",
            ],
            "arms": [
                "EZ Bar Bicep Curls",
                "Tricep Kickback",
                "Seated Cable Bicep Curls",
            ],
        },
    },

    ("beginner", 6): {
        "split": "Push/Pull/Legs (x2)",
        "workouts": {
            "push_1": [
                "Seated Chest Press",
                "Pec Deck",
                "Machine Shoulder Press",
                "Tricep Kickback",
            ],
            "pull_1": [
                "Seated Low Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "push_2": [
                "Seated Chest Press",
                "Pec Deck",
                "Machine Shoulder Press",
                "Seated Tricep Pushdowns",
            ],
            "pull_2": [
                "Seated Low Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("beginner", 7): {
        "split": "Push/Pull/Legs (x2) + CABS",
        "workouts": {
            "push_1": [
                "Seated Chest Press",
                "Pec Deck",
                "Machine Shoulder Press",
                "Tricep Kickback",
            ],
            "pull_1": [
                "Seated Low Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "cardio_abs": [
                "Cardio",
                "Flutter Kicks",
                "Russian Twists",
            ],
            "push_2": [
                "Seated Chest Press",
                "Pec Deck",
                "Machine Shoulder Press",
                "Tricep Kickback",
            ],
            "pull_2": [
                "Seated Low Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    # Intermediate Workouts
    ("intermediate", 1): {
        "split": "Full Body Split",
        "workouts": [
            "Bench Press",
            "Bent-over Rows",
            "Machine Shoulder Press",
            "EZ Bar Curls",
            "Rope Tricep Pushdowns",
            "Squats",
        ],
    },

    ("intermediate", 2): {
        "split": "Upper/Lower Split",
        "workouts": {
            "upper": [
                "Bench Press",
                "Bent-over Rows",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Rope Tricep Extensions",
            ],
            "lower": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("intermediate", 3): {
        "split": "Push/Pull/Legs",
        "workouts": {
            "push": [
                "Bench Press",
                "Incline Seated Press",
                "Machine Shoulder Press",
                "Rope Tricep Extensions",
            ],
            "pull": [
                "Bent-over Rows",
                "Seated Cable Row",
                "Lat Pulldown",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("intermediate", 4): {
        "split": "Upper/Lower (x2)",
        "workouts": {
            "upper_1": [
                "Bench Press",
                "Bent-over Rows",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Rope Tricep Extensions",
            ],
            "lower_1": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "upper_2": [
                "Bench Press",
                "Bent-over Rows",
                "Machine Shoulder Press",
                "EZ Bar Curls",
                "Rope Tricep Extensions",
            ],
            "lower_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("intermediate", 5): {
        "split": "Isolation Split",
        "workouts": {
            "chest": [
                "Bench Press",
                "Incline Seated Press",
                "Seated Chest Press",
                "Pec Deck",
            ],
            "back": [
                "Bent-over Rows",
                "Seated Cable Row",
                "Lat Pulldown",
                "Face Pulls",
            ],
            "legs": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "shoulders": [
                "Arnold Press",
                "Machine Shoulder Press",
                "Shoulder Shrugs",
                "Reverse Pec Deck",
            ],
            "arms": [
                "Close-grip Bench Press",
                "Rope Tricep Extensions",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
        },
    },

    ("intermediate", 6): {
        "split": "Push/Pull/Legs (x2)",
        "workouts": {
            "push_1": [
                "Bench Press",
                "Incline Bench Press",
                "Machine Shoulder Press",
                "Rope Tricep Extensions",
            ],
            "pull_1": [
                "Barbell Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "push_2": [
                "Bench Press",
                "Incline Bench Press",
                "Seated Shoulder Press",
                "Rope Tricep Extensions",
            ],
            "pull_2": [
                "Bent-over Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("intermediate", 7): {
        "split": "Push/Pull/Legs (x2) + CABS",
        "workouts": {
            "push_1": [
                "Bench Press",
                "Incline Bench Press",
                "Machine Shoulder Press",
                "Rope Tricep Extensions",
            ],
            "pull_1": [
                "Bent-over Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "cardio_abs": [
                "Cardio",
                "Flutter Kicks",
                "Russian Twists",
            ],
            "push_2": [
                "Bench Press",
                "Incline Bench Press",
                "Seated Shoulder Press",
                "Rope Tricep Extensions",
            ],
            "pull_2": [
                "Bent-over Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "EZ Bar Curls",
                "Seated Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    # Advanced Workouts
    ("advanced", 1): {
        "split": "Full Body Split",
        "workouts": [
            "Bench Press",
            "Squats",
            "Deadlift",
            "Bent-over Rows",
            "Military Press",
            "Decline Bicep Curls",
            "Tricep Pushdowns",
        ],
    },

    ("advanced", 2): {
        "split": "Upper/Lower Split",
        "workouts": {
            "upper": [
                "Bench Press",
                "Bent-over Rows",
                "Military Press",
                "Decline Bicep Curls",
                "Tricep Pushdowns",
            ],
            "lower": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("advanced", 3): {
        "split": "Push/Pull/Legs",
        "workouts": {
            "push": [
                "Bench Press",
                "Military Press",
                "Dumbbell Incline Bench Press",
                "Arnold Press",
                "Tricep Pushdowns",
            ],
            "pull": [
                "Bent-over Rows",
                "T-bar Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
            "legs": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("advanced", 4): {
        "split": "Upper/Lower (x2)",
        "workouts": {
            "upper_1": [
                "Bench Press",
                "Military Press",
                "Incline Dumbbell Bench Press",
                "Arnold Press",
                "Decline Bicep Curls",
                "Tricep Pushdowns",
            ],
            "lower_1": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "upper_2": [
                "Bent-over Rows",
                "T-bar Rows",
                "Lat Pulldown",
                "Decline Bicep Curls",
                "Tricep Pushdowns",
                "Pull-ups",
            ],
            "lower_2": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("advanced", 5): {
        "split": "Isolation Split",
        "workouts": {
            "chest": [
                "Bench Press",
                "Incline Bench Press",
                "Incline Dumbbell Bench Press",
                "Cable Chest Press",
                "Pec Deck",
            ],
            "back": [
                "Bent-over Rows",
                "T-bar Rows",
                "Seated Cable Rows",
                "Lat Pulldown",
                "Lat Pushdowns",
                "Pull-ups",
            ],
            "legs": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "shoulders": [
                "Military Press",
                "Arnold Press",
                "Shoulder Shrugs",
                "Standing Lateral Raises",
                "Rear Delt Cable Flyes",
            ],
            "arms": [
                "Close-grip Bench Press",
                "Tricep Pushdowns",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
        },
    },

    ("advanced", 6): {
        "split": "Push/Pull/Legs (x2)",
        "workouts": {
            "push_1": [
                "Bench Press",
                "Military Press",
                "Dumbbell Incline Bench Press",
                "Arnold Press",
                "Tricep Pushdowns",
            ],
            "pull_1": [
                "Bent-over Rows",
                "T-bar Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "push_2": [
                "Bench Press",
                "Military Press",
                "Dumbbell Incline Bench Press",
                "Arnold Press",
                "Tricep Pushdowns",
            ],
            "pull_2": [
                "Bent-over Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },

    ("advanced", 7): {
        "split": "Push/Pull/Legs (x2) + CABS",
        "workouts": {
            "push_1": [
                "Bench Press",
                "Military Press",
                "Dumbbell Incline Bench Press",
                "Arnold Press",
                "Tricep Pushdowns",
            ],
            "pull_1": [
                "Bent-over Rows",
                "T-bar Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
            "legs_1": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
            "cardio_abs": [
                "Cardio",
                "Decline Weighted Sit-ups",
                "Plank",
            ],
            "push_2": [
                "Bench Press",
                "Military Press",
                "Dumbbell Incline Bench Press",
                "Arnold Press",
                "Tricep Pushdowns",
            ],
            "pull_2": [
                "Bent-over Rows",
                "T-bar Rows",
                "Lat Pulldown",
                "Seated Cable Row",
                "Decline Bicep Curls",
                "Standing Cable Bicep Curls",
            ],
            "legs_2": [
                "Squats",
                "Deadlift",
                "Lunges",
                "Leg Extension",
                "Leg Curls",
                "Calf Raises",
            ],
        },
    },
}


@app.route("/")
def index():
    return render_template("index.html")  # Main page with the start button


@app.route("/experience", methods=["GET", "POST"])
def experience():
    if request.method == "POST":
        experience = request.form.get("experience")
        if not experience:
            return render_template("experience.html", error="Please select an experience level.")
        # Redirect to /days with the experience as a query parameter
        return redirect(url_for("days", experience=experience))
    return render_template("experience.html")


@app.route("/days", methods=["GET"])
def days():
    experience = request.args.get("experience")  # Get the experience parameter
    if not experience:
        return redirect(url_for("experience"))  # Redirect back if no experience selected
    # Get the number of days (assuming it's passed in the URL later)
    days = request.args.get("days")
    return render_template("days.html", experience=experience, days=days)


# Function to generate the workout plan
def get_workout_plan(experience, days):
    experience = experience.lower()  # Always use lowercase to match keys
    days = int(days)  # Ensure days is an integer

    # Get the workout plan from your workout_plans dictionary
    plan = workout_plans.get((experience, days))

    if plan:
        # Add the YouTube video URL to the plan
        youtube_video_url = get_youtube_video_for_plan(days, experience)
        plan["youtube_video_url"] = youtube_video_url
        return plan
    return None


# Route to render results
@app.route("/results", methods=["GET"])
def results():
    experience = request.args.get("experience")
    days = request.args.get("days")

    workout_plan = get_workout_plan(experience, days)  # Call function to fetch plan

    if isinstance(workout_plan, str):  # If workout_plan is an error string
        return render_template("index.html", message=workout_plan)  # Render error page

    # If workout_plan is found and is not an error, render the results page
    return render_template("results.html", workout_plan=workout_plan)


if __name__ == "__main__":
    app.run(debug=True)
