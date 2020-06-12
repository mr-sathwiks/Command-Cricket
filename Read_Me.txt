Command Cricket


This code is to simulate a game called HAND CRICKET played by children in school days ( a great childhood memory ). 
In this game user can give a user diffined number of over he wants to play, and also the number of players he wants to play with.
In this game user is supposed to call for toss either heads or tails and the computer will do the coin flip. 
For batting or bowling user has to select a number between 1 to 6 , so will the computer by using RANDOM function, 
	to generate a random number between 1 to 6. 
	If the user gives any number other than 1 to 6 the score will not be counted but as a penalty the ball will be counted.

In case the number selected by the user and computer match, the player (user or computer) will loose their batting chance 
	and the next player will walk in, ones all the players from the batting team are eliminated or the specified overs are finnished 
	batting is shifted to the opponent team to reach the target.
	the batting and bowling functions are defined in a module named by "cricket_app_module.py".

Since, I had kept a test cricket match in mind even if the second player reaches the required target, 
	he will be allowed to continue batting till the complete over is finished or player gets out.
	After both the teams are done batting the scores that where stored in a list are used to calculate the total score.
	Finally, both the scores are compared with each other, and a winner is selected, or a draw match is declared.

To enjoy the game the code comes with music option which will be played in the banground. 
	The song will be selected by the computer on a random basis from the list of songs that are listed in its directry.
	This code comes with two musics to be played. In order to play music you need to have "pygame" library files.
	Make sure to keep all the songs in '.ogg' formate. 'pygame' supports this formate without any problem, '.mp3','.waw' might show few problems to play.
	Link to downlode the songs: " https://drive.google.com/drive/folders/1V5aXEZZr9xJteqIsHlX8hjD2mHMSRrll?usp=sharing " -drive_link
	Link generate .ogg formate: "https://audio.online-convert.com/convert-to-ogg" - online-convert.com 

Make sure to keep "cricket_app.py","cricket_app_module.py",all the listed songs in a single directry.

HAPPY PLAYING.

created by SATHWIK S