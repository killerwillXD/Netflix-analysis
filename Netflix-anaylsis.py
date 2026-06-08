# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a Dataframe
netflix_df = pd.read_csv("netflix_data.csv")

#subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s
# Start by filtering out movies that were released in or after 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# And then do the same to filter out movies released before 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Another way to do this step is to use the & operator to which allows you to do this type of
#filtering in one step
# movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value< this doesn"t need to be exact !
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

# use a for loop and a counter to count how many short action movies there were in the 1990s

# Filter the 1990s movies for action titles
action_movie_1990s = movies_1990s[movies_1990s["listed_in"].str.contains("Action", case=False, na=False)]

#Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less
# than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movie_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1

print(short_movie_count)

#A quicker way of counting values in a column is to use .sum() on the desired column
#(action_movie_1990s["duration"] < 90).sum()