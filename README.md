# Election_Analysis

## Project Overview
The Colorado Board of Elections has provided election data and requested the following tasks be performed to complete an election audit of the recent local congressional election.

1. Open the data file.
2. Write down the names of all the candidates.
3. Add a vote count for each candidate.
4. Get the total votes for each candidate.
5. Get the total votes cast for the election.

## Resources
* Data Source: election_results.csv
* Software: Python 3.9.6, Visual Studio Code 1.61.1

## Summary
The [analysis](https://github.com/coleherman370/Py_Poll/blob/main/Analysis/election_results.txt) of the election show that:

* There were a total of 369,711 votes cast in this election
* The county with the highest voter turnout was Denver with 82.6% (306,055)
* The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane
* The candidate results were: 
  * Charles Casper Stockham received 23.0% of the vote with 85,213 total votes.
  * Diana DeGette received 73.8% of the vote with 272,892 total votes.
  * Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes.
* The winner of this election was:
  * Diana DeGette received 73.8% of the vote with 272,892 total votes.

## Challenge Overview
The csv provided for analysis was a simple three column table consisting of voter ballot ID, County, and Candidate name. Each row in the table therefor represents one ballot (or vote) with the Candidate name being the candidate voted for. The purpose of the PyPoll_Challenge script is to automate the counting of these votes and provide a statistical analysis of both voter turnout in the each county and tally the votes for the candidates.

## Suggestions
PyPoll was written with the thought in mind that opening the analysis results text file in the beginning would optimize the script. This did make writting the script more simple as it allowed for writting to the text at any point without concern for overwritting. PyPoll did have a faster [runtime](https://github.com/coleherman370/Py_Poll/blob/main/Resources/PyPoll_Runtime.png) than the [runtime of PyPoll_Challenge.](https://github.com/coleherman370/Py_Poll/blob/main/Resources/PyPoll_Challenge_Runtime.png) However, I believe this difference is due PyPoll not tracking County Voter Turnout and overall having fewer prints. PyPoll accomplishes printing out the analysis results to cmd by performing a final read of the analysis results and thus only needs to print once. PyPoll_Challenge accomplishes this same print out by print individual strings as the data is derived within the script. By reducing the numerous prints of PyPoll_Challenge into a single print, it is possible that PyPoll_Challenge would run faster. Especially with larger datasets as the memory storage of the csv is dropped once the csv no longer needs to be called.

One final thing to note is that the "County Turnout" percentage is not a true turnout figure. With the data provided, it is only possible to count how many votes occurred within a county. A true turnout figure would require comparing that number of votes for each to size of the voting populace for that county. Population data is not available for this data making such analysis not possible.

Given the data provided, a more informative analysis that could be achieved would be detailing to number of votes won by the candidates in each county. This analysis would provide the popularity of the competing candidates within each county.
