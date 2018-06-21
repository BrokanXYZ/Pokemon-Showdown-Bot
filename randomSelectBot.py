from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

# username2 = phatweener
# password2 = iamabot123

username = 'FatWeener'
password = 'iamabot123'



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.implicitly_wait(400)
driver.get('https://play.pokemonshowdown.com/')


driver.find_element_by_name('login').click()


driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_xpath('//button[@type=\'submit\']').click()


driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html[1]/body[1]/div[4]/div[1]/form[1]/p[5]/button[1]').click()

sleep(2)
print("Searching for match")

driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/form[1]/p[3]/button[1]/strong[1]').click()

print("Actively searching for match")

turnCount = 1



driver.find_element_by_name('openTimer').click()
driver.find_element_by_name('timerOn').click()


while True:
	
	moveIsDisabled = True 
	
	# Pick a move
	while moveIsDisabled:
		
		print("PICKING A MOVE!!!!!!!!!")
		
		# Later: try catch for two turn moves
		#
		#try:
		#	driver.find_element_by_xpath('/html[1]/body[1]/div[4]/div[5]/div[1]/div[2]/div[2]/button[]')
			
			
		# Pick random move
		moveChoice = random.randint(1, 4)
		selectedMove = driver.find_element_by_xpath('/html[1]/body[1]/div[4]/div[5]/div[1]/div[2]/div[2]/button[' + str(moveChoice) + ']')

		# If the move is not disabled, then click it
		if selectedMove.get_attribute('disabled') != 'disabled':
			moveIsDisabled = False;
			selectedMove.click()
	
	turnCount += 1
	
	try:
		element = WebDriverWait(driver, 300).until(
			EC.presence_of_element_located((By.NAME, 'goToEnd')) or EC.presence_of_element_located((By.NAME, 'closeAndMainMenu'))
		)
	except:
		print("Unexpected error:", sys.exc_info()[0])
		break
	
	if EC.presence_of_element_located((By.NAME, 'goToEnd')):
 
		driver.find_element_by_name('goToEnd').click()
		print("CLICKED ON GO TO END")
	
		# 1. Pokemon can attack again
		if EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[4]/div[5]/div[1]/div[2]')):
			print("MOVE CONTROLS APPEARED!!!")
			continue
		# 2. Our pokemon died
		elif pokemon == ded:
			print("PICKING NEW POKEMAN!!!")
		# 3. Game over
		elif EC.presence_of_element_located((By.NAME, 'closeAndMainMenu')):
			print("2222")
			break
			
	# Forfeit
	elif EC.presence_of_element_located((By.NAME, 'closeAndMainMenu')):
		print("33333")
		break

	
print("Number of turns: %d" % (turnCount))
sleep(15)

driver.quit()
