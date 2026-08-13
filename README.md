# Movie Night Picker

## Team Members

- Fatima
- Reem

## Project Overview

Movie Night Picker helps users find movies based on their preferences.

The user chooses:

- Genre
- Minimum rating
- Maximum runtime

The project uses the TMDB API to find movies that match these preferences.

## How It Works

1. The user enters a movie genre.
2. The user enters a minimum rating.
3. The user enters a maximum runtime.
4. The program gets movie data from the TMDB API.
5. It filters the movies based on the user’s preferences.
6. It displays the matching movies.

## Challenge Concept Used

- API (Application Programming Interface)

This project uses the TMDB API to get movie data such as titles, ratings, genres, release dates, and runtime.

## Tools Used

- Python
- Pandas
- Requests
- python-dotenv
- TMDB API
- VS Code

## AI Model Used

OpenCode Model: Big Pickle

## Testing and Validation

We tested the project using different genres, ratings, and runtimes.

During testing, we found that one movie exceeded the user’s maximum runtime. We added an extra filter in Pandas to remove movies that were longer than the selected runtime.

We tested the project again and confirmed that the final results matched the user’s preferences.

## Limitations

- Movie recommendations depend on the data available from TMDB.
- Some movies may have missing or incomplete information.
- The project currently uses only genre, rating, and runtime as user preferences.

## What Broke and What We Fixed

During testing, a movie with a runtime of 94 minutes appeared even though the user selected a maximum runtime of 90 minutes.

We checked the movie runtime and added an additional Pandas filter to make sure the final recommendations do not exceed the user’s selected runtime.

## How We Used AI

We used AI to help us:
- Break the project into small steps.
- Generate and explain Python code.
- Debug errors during development.
- Improve the filtering logic.
- Test and validate the results.

We reviewed and tested the code after each change to make sure we understood how it worked.

## Key Lessons Learned

- How to connect Python to an API.
- How to use user input to filter movie data.
- How to test API results instead of assuming they are correct.
- How to use Pandas for additional filtering.
- How to keep an API key private using a .env file.

## Initial Plan / Pseudocode

1. Connect to the TMDB API.
2. Get the available movie genres.
3. Ask the user to choose a genre.
4. Ask the user for a minimum rating.
5. Ask the user for a maximum runtime.
6. Request movies that match the user’s preferences.
7. Get the runtime for the recommended movies.
8. Validate and filter the results.
9. Display the final movie recommendations.

