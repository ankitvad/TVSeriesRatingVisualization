# TVSeriesRatingVisualization
Visualizing the TV Series Rating over the run of the Program.<br>
-----
The program visualizes the TV Series ratings over the season run.<br>
IMDB parsed JSON files are obtained that gives us the following data:<br>
<ul>
<li>Name of TV Show</li>
<li>Average Rating of the Series</li>
<li>Episode Information</li>
<ul>
<li>Season Numbering</li>
<ul>
<li>Episode Name</li>
<li>Episode Number in Season</li>
<li>Air Date</li>
<li>Episode Rating</li>
</ul>
</ul>
</ul>
<br>
We Extract the rating after converting the JSON to a dictioary structurea and then use matplotlib to visualize the range of the rating, updating 
various parameters like axis value, and the plot line style.<br>
------<br>
Use: Just change the &lt;SeasonName&gt;.json to anny value and see the visualization, along with the structure of the JSON.<br>
License: Do What You Want With It License.<br><br>
ImageOutput:<br>
<ul>
<li>House Of Cards:</li>
<img src="test.png"><br><br>
<li>Friends:</li>
<img src="test1.png"><br><br>
<li>The Big Bang Theory:</li>
<img src="test2.png"><br><br>
</ul>
