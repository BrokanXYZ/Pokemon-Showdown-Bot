from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random

def login(driver, username, password):
	driver.find_element_by_name('login').click()
	driver.find_element_by_name('username').send_keys(username)
	driver.find_element_by_xpath('//button[@type=\'submit\']').click()
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_xpath('/html[1]/body[1]/div[4]/div[1]/form[1]/p[5]/button[1]').click()
	
def challengePlayer(driver, username):
	sleep(1)
	driver.find_element_by_xpath('/html/body/div[@id=\'room-\']/div[@class=\'mainmenuwrapper\']/div[@class=\'leftmenu\']/div[@class=\'mainmenu\']/div[@class=\'menugroup\'][3]/p[2]/button[@class=\'button mainmenu5 onlineonly\']').click()
	driver.find_element_by_xpath('/html/body/div[@class=\'ps-popup\']/form/p[1]/label[@class=\'label\']/input[@class=\'textbox autofocus\']').send_keys(username)
	driver.find_element_by_xpath('/html/body/div[@class=\'ps-popup\']/form/p[@class=\'buttonbar\']/button[1]/strong').click()
	driver.find_element_by_xpath('/html/body/div[@class=\'ps-overlay\']/div[@class=\'ps-popup\']/p[@class=\'buttonbar\']/button[1]').click()
	driver.find_element_by_name('makeChallenge').click()
	
def acceptChallenge(driver):
	sleep(1)
	driver.find_element_by_name('acceptChallenge').click()

def selectRandomMove(driver):
	moveIsDisabled = True 
	
	# Pick a move
	while moveIsDisabled:
		# Pick random move
		moveChoice = random.randint(1, 4)
		selectedMove = driver.find_element_by_xpath('/html[1]/body[1]/div[4]/div[5]/div[1]/div[2]/div[2]/button[' + str(moveChoice) + ']')
		# If the move is not disabled, then click it
		if selectedMove.get_attribute('disabled') != 'disabled':
			moveIsDisabled = False;
			selectedMove.click()
	
def checkForDeadPokemon(driver, battleURL):
	try:
		driver.find_element_by_xpath("/html/body/div[@id=\'room-" + battleURL + "\']/div[@class=\'battle-controls\']/div[@class=\'controls\']/div[@class=\'movecontrols\']/div[@class=\'moveselect\']")
	except NoSuchElementException:
		print("Pokemon is dead")
		pokemonIsDead = True 
		# Pick a pokemon
		while pokemonIsDead:
			# Pick random pokemon
			choice = random.randint(1, 6)
			# WAIT EXPLICITLY HERE
			sleep(5)
			selectedPokemon = driver.find_element_by_xpath('/html/body/div[@id=\'room-' + battleURL + '\']/div[@class=\'battle-controls\']/div[@class=\'controls switch-controls\']/div[@class=\'switchcontrols\']/div[@class=\'switchmenu\']/button[' + str(choice) + ']')
			# If the pokemon is not dead, then click it
			if selectedPokemon.get_attribute('disabled') != 'disabled':
				print("Selecting new pokemon")
				pokemonIsDead = False;
				selectedPokemon.click()
		return True
	return False
		
	
username1 = "FatWeener"
password1 = "iamabot123"

username2 = "phat weener"
password2 = "iamabot123"


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


driverOne = webdriver.Chrome(chrome_options=chrome_options)
driverTwo = webdriver.Chrome(chrome_options=chrome_options)

driverOne.set_window_position(0,0)
driverTwo.set_window_position(950,0)

driverOne.implicitly_wait(2)
driverTwo.implicitly_wait(2)

driverOne.get('https://play.pokemonshowdown.com/')
driverTwo.get('https://play.pokemonshowdown.com/')

# Mute sounds
driverOne.find_element_by_name('openSounds').click()
driverOne.find_element_by_name('muted').click()
driverTwo.find_element_by_name('openSounds').click()
driverTwo.find_element_by_name('muted').click()

login(driverOne, username1, password1)
login(driverTwo, username2, password2)

challengePlayer(driverOne, username2)
acceptChallenge(driverTwo)

sleep(1)

# Get room number 
currentURL = driverOne.current_url
splitURL = currentURL.split('/')
battleURL = splitURL[3]
print('\n\n' + battleURL + '\n\n')

while True:
	aPokemonDied = False

	driverOne.find_element_by_name('goToEnd').click()
	driverTwo.find_element_by_name('goToEnd').click()
	
	aPokemonDied = checkForDeadPokemon(driverOne, battleURL)
	aPokemonDied = checkForDeadPokemon(driverTwo, battleURL)
	
	if not aPokemonDied:
		selectRandomMove(driverOne)
		selectRandomMove(driverTwo)
	else:
		sleep(5)
	
	
	

#sleep(5)

#driverOne.quit()
#driverTwo.quit()




