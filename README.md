# movie-recommender
# Check out the app here: https://movierec-ak.herokuapp.com

Main libraries used: numpy, pandas, sklearn; 

This app is a content-based movie-recommendation system. The base dataset was obtained from the tmdb_5000_movies and tmdb_5000_credits. The first step in the process was cleaning up the data and preprocessing to obtain tags for each element/movie. The model used was bag-of-words on the tags. The next step was vectorizing the tags and finding the similarity scores. Once the similarity scores were achieved, the top five movies were recommended based on this score. The app uses the streamlit framework and is deployed on Heroku. The tmdb api was used to display the banners/images for the movies using their 'id' which was an attribute in the refined data frame at the end.
