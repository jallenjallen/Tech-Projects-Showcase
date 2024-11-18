# Discovering Gravity Pygame


#Files used to Run the code:

Python - 3.6 (32 bit)
Pygame  
Main.py
requirements.txt
.gitignore
Resources:
	Images:
		Apple.png
		Grass.png
		Isaac.png
		Sky.png
		Tree.png
	Fonts:
		X-Files.tff


#Libraries Used:

Pygame: 
pygame.init()
pygame.image.load()
pygame.display.set_mode()
pygame.display.set_caption()
pygame.time.Clock()
pygame.Rect()
pygame.event.get()

Random:
random.randint()






#How to Play:
To play used the left and right arrows to move the person into the path of the apples before they touch the ground.
If the apples touch the ground they will take away health from your overall value, when this value reaches 0 the game will end.
The score is calculated on how many apples you catch.
Green apples add health to you if you catch them.
Press the p button to pause the pygame.
At any time you can click the red x button in the top right to quit the game.



Starting the pygame = https://www.pygame.org/docs/tut/ImportInit.html
Defining Colours = https://www.youtube.com/watch?v=P8bx4nits-o
Loading Images = https://www.pygame.org/docs/ref/image.html#pygame.image.load
Setting the name of the window = https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window
Moving PLayer = https://gamedev.stackexchange.com/questions/54841/rpg-movement-holding-down-button
Apples Falling = https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
Boundary for player to not go off screen = https://stackoverflow.com/questions/45659626/how-to-set-boundaries-in-pygame
Rendering Text to the screen = https://stackoverflow.com/questions/44860885/how-to-render-text-on-screen-using-pygame
Deleting Apples off Screen = https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
Help creating boundary for catching apples (fully understanding how pygame.rect works) = https://stackoverflow.com/questions/19215233/how-to-use-the-pygame-rect
Loading and playing music = https://pythonprogramming.net/adding-sounds-music-pygame/

