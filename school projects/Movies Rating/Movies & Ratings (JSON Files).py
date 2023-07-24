# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:28:31 2021

@author: leen8
"""

#imports json as a special module used for this hw
import json

#reads and opens the movies and ratings json files, and takes in, converts, and prints the inputs given by the user
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())
    min_year = input('Min year => ')
    print(min_year)
    min_year = int(min_year)
    max_year = input('Max year => ')
    print(max_year)
    max_year = int(max_year)
    imdb_w = input('Weight for IMDB => ')
    print(imdb_w)
    w1 = float(imdb_w)
    twit_w = input('Weight for Twitter => ')
    print(twit_w)
    w2 = float(twit_w)
    
    #finds all the genres of movies and puts them into the set and converts it to a list to help determine valid genres of movies
    all_gen = set()
    for i in movies:
        genl = movies[i]['genre']
        for j in genl:
            all_gen.add(j.lower())
    agenl = list(all_gen)
    
#starts a while loop that prompts the user to see which genre of stats they want to see
while True:
    amkeys = []
    genkeys = []
    genre = input('\nWhat genre do you want to see? ')
    print(genre)
    #takes the genre in any case
    genre = genre.lower()
    # if the genre equals stop it breaks/stops the loop
    if genre == "stop":
        break
    # if the genre is not in the list of all the genres, it prints that there was no genre of hat movie between the max and min of that year
    elif genre not in agenl:
        print("\nNo {} movie found in {} through {}".format(genre.title(), min_year, max_year))
    # else, it continues and calculates the stats for the given genre
    else:
        # finds all the keys of movie years that are in between the maximum and minimum year
        # and adds them to a list
        for x in movies:
           if movies[x]['movie_year'] >= min_year and movies[x]['movie_year'] <= max_year:
               amkeys.append(x)
        # finds all the keys from the valid year keys that fit into the movie genre specificed by the user, taking the genre in any case,
        # and adds them to a list
        for i in amkeys:
           genl = movies[i]['genre']
           for j in genl:
               if j.lower() == genre:
                   genkeys.append(i)
        #finds all the imdb ratings from all the valid genre keys and adds them to a list
        avg = []
        for x in genkeys:
            avg.append(movies[x]['rating'])
        #finds all the valid rating keys in from the list of valid genre keys and adds them to a list
        rate = []
        for x in genkeys:
            if x in ratings.keys():
                rate.append(x)
        #sets the default average twitter 
        avg_twit = 0
        
        #determines whether or not to count and calculate the average twitter ratings of the movie (based on whether or not
        # there is a twitter rating for that movie's rating list is greater or less than 3 or if its not in the list)
        n_ratings = []
        v_name = []
        v_year = []
        for x in genkeys:
            # if it does not exist or there are less ratings than 3 it skips calculating the average twitter ratings
            if x not in ratings.keys() or len(ratings[x]) < 3:
                pass
            # if the ratings is larger than 3 or equal to 3 then it appends all the new valid movie names and years into lists, calculates the average twitter ratings
            # and appends it to a list 
            elif len(ratings[x]) >= 3:
                v_name.append(movies[x]['name'])
                v_year.append(movies[x]['movie_year'])
                avg_twit = sum(ratings[x])/len(ratings[x])
                wmax_rating = (w1 * movies[x]['rating'] + w2 * avg_twit) / (w1 + w2)
                n_ratings.append(wmax_rating)
        # finds the maximum value of all the new ratings, takes the index of the values and prints the year and movie based on the new lists created and prints the 
        # the average
        
        # reverses all the lists so that if there are averages that are the same, it takes the last movie in lexigraphical order
        n_ratings.reverse()
        v_name.reverse()
        v_year.reverse()
        max_avg = max(n_ratings)
        max_ind = n_ratings.index(max_avg)
        print("\nBest:")
        print("        Released in {}, {} has a rating of {:.2f}".format(v_year[max_ind], v_name[max_ind], max_avg))
        
        # finds the minimum value of all the new ratings, takes the index of the values and prints the year and movie based on the new lists created and prints the 
        # the average
        min_avg = min(n_ratings)
        min_ind = n_ratings.index(min_avg)
        print("\nWorst:")
        print("        Released in {}, {} has a rating of {:.2f}".format(v_year[min_ind], v_name[min_ind], min_avg))
