import sys, pygame #Importing the pygame funtions to be used.
import random #Importing so I can use the libraries functions.
import math 


pygame.init() #Initialising the game to start.

#Setting colours used (Using RGB method)
black = 0, 0, 0
white = 255, 255, 255
red = 139, 0, 0

#Setting screen size
display_width = 1000
display_height = 900
SIZE = (display_width, display_height) #Simply above 2 lines by naming it SIZE.
screen = pygame.display.set_mode(SIZE) #Setting the screen size to the variables defined above.

#Timer for Apple Spawning
appletimer = 20 #When this reaches zero a new apple will spawn.
appletimer1 = 0
apples = [[640, 100]]
healthvalue = 3 #Health value
score = 0 #Setting the variable for apples caught.

#Loading Font onto game.
score_font = "Resources/Fonts/X-Files.ttf"  #Externally downloaded font from the internet.
health_font = "Resources/Fonts/X-Files.ttf"

#Loading Background Music to play throughout.
background_music = pygame.mixer.music.load("Resources/Sounds/Background.wav") #Pulling the sound from the same folder my game is located in.
pygame.mixer.music.play(-1) #Plays the background music continuously. 

#Loading Sounds to be used on impact.
squelch_sound = pygame.mixer.Sound("Resources/Sounds/Squelch.wav")
ping_sound = pygame.mixer.Sound("Resources/Sounds/Ping.wav")
game_over_sound = pygame.mixer.Sound("Resources/Sounds/Game_over_sound.wav")


#Loading pictures that will be used later on.
Sky = pygame.image.load("Resources\Images\Sky.png").convert_alpha() #Using '.convert_alpha' so that all the sprites are converted to same resolution.
Grass = pygame.image.load("Resources\Images\Grass.png").convert_alpha()
Tree = pygame.image.load("Resources\Images\Tree.png").convert_alpha()
Isaac = pygame.image.load("Resources\Images\Isaac.png").convert_alpha()
Game_over_screen_image = pygame.image.load("Resources\Images\Game_over_screen.png")
heartimg = pygame.image.load("Resources\Images\Heart1.png").convert_alpha()
appleimg1 = pygame.image.load("Resources\Images\Apple.png").convert_alpha()
appleimg = appleimg1 #Making copy of the apple so is easier to manipulate.

#Loading Wav Files (Sounds)

#Defining Score Text On-Screen
score_label = ("Isaac's Score:") #What the label will say.
score_label_font = pygame.font.Font(score_font, 30) #Picking the font and size of the message.
score_label_surf = score_label_font.render(str(score_label), 1, (red)) #Setting it as a string value to draw on screen in a red font.
score_label_pos = [50, 840] #The x and y co-ordinates of the labels position. 

#Defining the Health Label
health_label = ("Health:") #What the label will say.
health_label_font = pygame.font.Font(health_font, 30) #Picking the font and the size of the image.
health_label_surf = health_label_font.render(str(health_label), 1, (white)) #Setting it as a string value to draw on screen in a white font.
health_label_pos = [650, 840]

def drawheart (x,y): #Defining a function that I will use later on on the main loop.
	screen.blit(heartimg, (x+800, y+30)) #The +800 and +30 used to adjust position so is in the bottom right hand corner.


#Constants
playerposx = 0 #Needed to be named as is variable thats going to be changed.
playerspeedx = 10 #Will be speed that player moves when button held down.

#Default key states.
keys = [False, False, False, False] #This means up, down, left and right are all set to false automatically in their current state (up). This is needed when there is continous movement when button is held down.

#Setting a title to my pygame window
pygame.display.set_caption("Discovering Gravity")

#Setting a default clock.
clock = pygame.time.Clock() #Assigns a default clock so that all objects have a reference time.

game_over_screen = False #Making sure that the game goes straight to the 'else' loop when opened.

pause_screen = False

while True: #Start of the main loop, will keep running as long as the pygame us running 'True'.



	for event in pygame.event.get(): #Records the events in the pygame.
		#Quit game if we receive the quit request.
		if event.type == pygame.QUIT: 
			sys.exit()


	if game_over_screen:
		
		screen.fill(black) #Makes the screen black again so I can draw over it.
		screen.blit(Game_over_screen_image, (80,80)) #Drawing game over image on the screen.
		screen.blit(score_integer_surf, (570,450)) #Drawing the score again but re-positioning it.
		screen.blit(score_label_surf, (330,450))  #Drawing text on screen but re-positioning it.
		pygame.display.flip() #Update the pygames display.
		pygame.mixer.music.stop() #Will stop the background music (birds tweeting)

	elif pause_screen:
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pause_screen = False
		screen.fill(red)
		pygame.display.update()

	else: #As long as the health does not = 0 then this loop will run.
		appletimer -= 1 #For every frame that goes by this takes one away from the appletimer.
	
		screen.fill(black) #Fills the screen with black so that I can then draw over the top.


		#Drawing Background Sky
		screen.blit(Sky, (0,0))
		

		#Drawing Foliage.
		screen.blit(Grass, (0, 800)) #Draws the left side of the grass x 0-500.
		screen.blit(Grass, (500,800)) #Draws the right side of the grass x 500-1000.
		screen.blit(Tree, (-150,0)) #Draws the Tree on the screen.

		#Drawing Isaac
		screen.blit(Isaac, (playerposx, 670)) #Using 'playerposx' as the x value as this variable will change with button presses.
		
		#Drawing the Score Integer (will be updated with every apple that player catches)
		score_integer = [score]
		score_integer_font = pygame.font.Font(None,60) #Setting font and size of the integer.
		score_integer_surf = score_integer_font.render(str(score), 1, (white)) #Setting it to a string value and black.
		score_integer_pos = [330, 840] #x and y co-ordinates.
		screen.blit(score_integer_surf, score_integer_pos) #Actually drawing what is defined on the screen above.

		#Drawing the Health Integer (will be updated with every apple that hits ground)
		health_integer = [healthvalue]
		health_integer_font = pygame.font.Font(None, 60) #The font and size.
		health_integer_surf = health_integer_font.render(str(healthvalue), 1, (black)) #Setting it as a string value to draw on screen in a black font.
		health_integer_pos = [820,840] #Setting x and y co-ordinates.
		screen.blit(health_integer_surf, health_integer_pos) #Actually drawing what is defined above on screen.

		#Drawing the Score Label
		screen.blit(score_label_surf, score_label_pos)
		
		#Drawing the Health Label
		screen.blit(health_label_surf, health_label_pos)

		for heart in range (healthvalue): #Calculating a how hearts to draw.
			drawheart (heart*70, 800) #Function that was defined outside of the main loop.

		#Spawning of the apples.
		if appletimer == 0: #When the respawn timer is exactly equal to zero then this loop will run
			apples.append([random.randint(100, 800), 200]) #Draw a new apple with x value between 100-800 and y value of 200.
			appletimer = 100 - (appletimer1*2) #Makes the respawn of the apples faster as time goes on.
			if appletimer1>=35:
				appletimer1 = 35 #Limits the respawn time of the apples so doesn't become too challenging.
			else:
				appletimer1+=5

		index = 0
		for apple in apples:
			apple[1] += 7 #Speed at which the apples will move across the window (y-axis) continously
			applerect = pygame.Rect(appleimg.get_rect()) #Getting the rectangle measurements (co-ordinates) around the outside of the apple image.
			Isaacrect = pygame.Rect(Isaac.get_rect()) #Same fo the Isaac image.
			applerect.left = apple[0] #The x value is named as variable.
			applerect.top = apple[1] #The y value is named as variable.
			if (applerect.bottom >= (800 - Isaacrect.bottom)) and ((playerposx <= (applerect.right - 50)) and (playerposx >= applerect.left - 100)):
				score += 1 #Plusses one to the previous score.
				apples.pop(index) #Deletes the apple.
				pygame.mixer.Sound.play(ping_sound) #Plays the ping sound defined outside of the 'while' loop.
			elif applerect.top > 750: #If the y co-ordinate of the bottom (as it appears in screen) is touching the ground.
				healthvalue -=1 #Minus one from the previous health value.
				apples.pop(index) #Deletes the apple.
				pygame.mixer.Sound.play(squelch_sound) #Plays the squelch sound defined outside of the 'while' loop.
			index += 1
			screen.blit(appleimg, apple) #Once calculations above are worked out the apple images are then drawn.

		

		pygame.display.flip() #Update the pygames display.			

		
	#-------------------------------------------------------------------------------------
		
		#Movement Controls
		if event.type == pygame.KEYDOWN: #If a key is helod down then run this part of the code.
			if event.key == pygame.K_LEFT: #If right arrow is pressed.
				keys[0] = True
			elif event.key == pygame.K_RIGHT: #If right arrow is pressed.
				keys[1] = True
			elif event.key == pygame.K_p:
				pause_screen = True

		if event.type == pygame.KEYUP: #If a key is released then run this part of the code.
			if event.key ==  pygame.K_LEFT: #If left key is not pressed.
				keys[0] = False
			elif event.key == pygame.K_RIGHT: #If right key is not pressed.
				keys [1] = False
				
		if keys[0]:
			playerposx -= playerspeedx #Move the players position -10 in the y direction. As 
		elif keys[1]:
			playerposx += playerspeedx #Move the players position +10 in the y direction.


		#As these key states are set to true, as long as the button is held down the playerspeedx is being constantly added or taken away from the last value.


		#Setting Boundaries for player so can't go out of window display.
		if playerposx < 0 : playerposx = 0 #Boundary on left side of screen.
		if playerposx > 890 : playerposx = 890 #Boundary on right side of screen.


		pygame.display.flip() #Updating the screens contents.


		if healthvalue == 0: #If the health value integer on screen reaches exaclty zero then the game will close.
			pygame.mixer.Sound(game_over_sound) #Sound defined above will play.
			game_over_screen = True #Means in this event the first loop will be activated.


			#sys.exit()
	

	
 