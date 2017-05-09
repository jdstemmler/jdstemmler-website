Title: MLS Standings
Date: 2016-02-05
Category: Data
Tags: soccer, python

In June of 2015 I attended Seattle Data Day in downtown Seattle and learned a number of interesting new things about python and data science. One of the sessions I attended was a workshop on <a href="http://shop.oreilly.com/product/0636920034391.do" target="_blank">web scraping with python</a> presented by <a href="http://www.pythonscraping.com/node/5" target="_blank">Ryan Mitchell</a>. At the end, we were encouraged to pick a site and play around with scraping and getting the data into python.

My site of choice was the Major League Soccer <a href="http://www.mlssoccer.com/results" target="_blank">results map</a> for the current season. As a big fan of soccer (specifically, the Seattle Sounders) I thought it would be fun to play around with some of the league standings for the current season and make some plots of not only the most recent standings, but the standings throughout the season. With that, I'll show some plots and talk a little bit about how the W/L/D gets converted into points. Oh, and all the code for this can be found over on my personal GitHub page <a href="https://github.com/jdstemmler/mls-standings" target="_blank">in this repository</a>.

## The web scraper

The function of the web scraper is actually pretty simple. It goes out to the page and fetches the table. From there, the python code parses the table by going through each of the rows and collecting the win-loss-draw information for each game number. It then converts each win, loss, and draw into 3, 1, or zero points respectively. It then saves this information out to a .csv file.

## Plots

Now the fun part. Here is a plot of the standings by team for each game in the season. It's a little bit messy, but rather informative. On the x-axis is the game number with the cumulative number of points each team has on the y-axis. Lines are colored by team in the legend on the right side of the plot.
<!-- [![MLS Point Standings][points]][points] -->
[points]: https://raw.githubusercontent.com/jdstemmler/mls-standings/master/example/standings_by_game.png "MLS Point Standings"

I have a lot of fun looking at this plot. You can clearly see in some teams when they went on winning or losing streaks, how many games each team has played, and generally get a sense of the performance throughout the season. However, the plot is quite cluttered. I chose the colors for each team based off of a best-guess of the representative color for the team, but there are obviously some similarities in the colors which makes it difficult to differentiate between some teams.

If we don't really care about how a team has performed throughout the season, we can take a look at only the most recent reporting of the number of points for each team. Additionally, it is of interest to know which teams will make the playoffs at the end of the season (top 6 from both the Western and Eastern conferences) and how well the conferences are doing compared to one another.

<!-- [![Current Point Standings][standings]][standings] -->
[standings]: https://raw.githubusercontent.com/jdstemmler/mls-standings/master/example/current_points_standings.png "Current Point Standings"

This plot clearly shows all those metrics. Western conference in red on the left, Eastern in blue on the right, sorted by total number of points with dotted black lines on each of the conferences to show the cutoff point of the playoffs. What this figure doesn't really convey as well as the first plot is the disparity between the teams with respect to the number of games played. D.C. United, for example, has played 7 more games (at the time of this writing) than the Montreal Impact and thus has the potential to have 21 additional points simply because they've played more games.

This next figure shows similar information as above, but with a few small tweaks. To help address the issue of the games-played difference, these standings show the number of points each team had at the most recent game that all teams have played. The lighter colors, then, show how many points each team has earned since that game, if they've played additional games.

<!-- [![Level Game Points Standings][level]][level] -->
[level]: https://raw.githubusercontent.com/jdstemmler/mls-standings/master/example/level_game_points_standings.png "Level Games"

This plot could really use some additional information, such as just exactly how many additional games each team has played and not just points. But it does give you a better sense of the standings at the most recent point in time when all teams had played the same number of games.

One way to get around this issue entirely is to look at average points per game (PPG). This is exactly what it sounds like - total number of points divided by the total number of games played. This essentially ranks teams by the mean <em>slope</em> of the line shown all the way back in the first plot. Doing this gives you yet another way to look at the standings:

<!-- [![Points per Game Standings][ppg]][ppg] -->
[ppg]: https://raw.githubusercontent.com/jdstemmler/mls-standings/master/example/ppg_standings.png "Points per Game"

## Summary

These plots are obviously a little bit out of date by this point, but they get the points across. However, if you click-through to the linked images those should be updated within the last 6 hours. I have this script running on a server that pulls down the standings and makes the plots at that frequency, so you can never be without the most recent standings!

I hope you enjoyed looking through this. It was a really great learning experience to combine the web scraping component with some sports. There is so much more you could do with this data, such as looking at the performance of Western conference teams vs Eastern when they play in-conference or out, longest winning or losing (or tying) streaks, or even looking at data from previous seasons.

Feel free to comment with any suggestions for things to look at or improvements to any of my methods. I welcome your feedback!
