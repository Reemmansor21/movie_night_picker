# Prompt Log

## Prompt 1: Connecting to the TMDB API

### What we asked
Help us connect our Python project to the TMDB API and retrieve movie data.

### What the AI returned
The AI suggested using the requests library to send a request to the TMDB API and check the response status code.

### What we changed or checked
We ran the code and confirmed that the API request returned status code 200, which means the request was successful.

## Prompt 2: Adding User Preferences

### What we asked
Help us allow the user to choose a genre, minimum rating, and maximum movie runtime.

### What the AI returned
The AI suggested using input() to collect the user’s preferences and using these values in the TMDB movie search.

### What we changed or checked
We tested the inputs using different genres, ratings, and runtimes to make sure the program returned matching movies.

## Prompt 3: Fixing the Runtime Problem

### What we asked
Help us display the runtime of the recommended movies and check that the results match the user’s maximum runtime.

### What the AI returned
The AI suggested retrieving the runtime for the recommended movies from TMDB.

### What we changed or corrected
During testing, we found a 94-minute movie even though the user selected a maximum runtime of 90 minutes. We added an extra Pandas filter to remove movies that exceeded the user’s selected runtime.

## Prompt 4: Protecting the API Key

### What we asked
How can we keep the TMDB API key private before uploading the project to GitHub?

### What the AI returned
The AI suggested storing the API key in a .env file and using python-dotenv to load it into the Python project.

### What we changed or checked
We created a .env file and added it to .gitignore. We tested the project again to confirm that the API still worked without storing the key directly in the Python file.