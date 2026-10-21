# Script to update song of the week

# Libraries
import os
from git import Repo

# Set working directory to script's location
os.chdir(os.path.dirname(__file__))

# Open text file containing weblinks
with open("sotw.txt") as l:
    links = l.read().splitlines()

# Identify next song in list
with open("about.qmd") as f:
    d = f.read() # Read in about page
    found = -1 # Changes to a positive value when current song is found
    ind = 0 # Track what index has been reached
    while found == -1 and ind < len(links): # Continue to loop when current song isn't found, and list hasn't been exceeded
        found = d.find(links[ind]) # -1 if not the current song, otherwise a positive value
        ind += 1 # Increase index count
    if ind == len(links): # When end of list is reached
        d = d.replace(links[ind - 1], links[0]) # Go back to the beginning of the list
        print("Looped back to beginning")
    else:
        d = d.replace(links[ind - 1], links[ind]) # Replace current song with next song in the list

# Write about file with new song in its place
with open("test.qmd",'w') as o:
    o.write(d)
    print("Successful write")


# Push about file to github
repo = Repo(os.getcwd()) # Access git repo inside working directory
repo.index.add(['about.qmd']) # Add about file to queue
repo.index.commit('Song of the week update') # Commit change
origin = repo.remote(name='origin') # Make sure commit is pushed to origin
origin.push() # Push commit
print("Pushed to Github")