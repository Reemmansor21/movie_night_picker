# Movie Night Picker

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

