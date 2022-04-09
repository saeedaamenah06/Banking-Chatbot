#making functions for the automated messages	
def open_account(): #TO OPEN AN ACCOUNT.
	print("To open an account, first create a login using your gmail in the top right corner of the website screen. Then, use the dropdown menu under your username and click the option for \"Account Setup.\"")
def not_looking_for():
	print("If this is not what you are looking for, please call the Knabdoog Help Desk. The number is 123-456-7890.")
def close_account(): #TO CLOSE/DESTROY AN ACCOUNT.
	print("To close an existing bank account, open the dropdown menu under your username in the top right corner of the website screen, then click the option for \"Account Settings\". Note that the option will only appear if you have an account in use.")
def deposit_money(): #TO DEPOSIT MONEY INTO AN ACCOUNT.
	deposit_question = (input("Please choose which account to deposit in from your 2 existing accounts in a number format: "))
	if "1" in deposit_question:
		deposit_sum=int(input("Please enter a sum of money to deposit in Account #1: "))
		print(str(deposit_sum) + ("$ have been deposited into Account #1."))
	elif "2" in deposit_question:
		deposit_sum=int(input("Please enter a sum of money to deposit in Account #2: "))
		print(str(deposit_sum) + ("$ have been deposited into Account #2."))
	else:
		print("That's not a valid account. Please exit and reopen the chatbot to ask the question again or ask another question.")
def withdrawal(): #TO WITHDRAW FROM AN ACCOUNT.
	withdrawal_question=input("Please choose which account to withdraw from, from your 2 existing accounts in a number format: ")
	accounts_withdrawal=withdrawal_question.split()
	withdrawal_limit=200
	if "1" in accounts_withdrawal:
		withdrawal_sum=int(input("Please enter a sum of money to withdraw from Account #1: "))
		if withdrawal_sum>withdrawal_limit:
			print ("You don't have that much money.")
			not_looking_for()
		else:
			print(str(withdrawal_sum) + ("$ has been withdrawed from Account #1."))
			not_looking_for()
	elif "2" in accounts_withdrawal:
		withdrawal_sum=int(input("Please enter a sum of money to withdraw from Account #2: "))
		if withdrawal_sum>withdrawal_limit:
			print ("You don't have that much money.")
			not_looking_for()
		elif withdrawal_sum<withdrawal_limit:
			print(str(withdrawal_sum) + ("$ has been withdrawed from Account #2."))
			not_looking_for()
	else:
		print("That's not a valid account.")
def card_info():
	print("To register for a new card, you will have to either call the number provided (123-456-7890), or go to your nearest Knabdoog Bank and manually register.")
def debit():
	print("To look at the information for an existing card in your posession, please go to the dropdown option labeled \"Account Information\". The page for your account settings will have an option to look at information for any and all existing cards connected to your account.")
def credit():	
	print("To look at the information for an existing card in your posession, please go to the dropdown option labeled \"Account Information\". The page for your account settings will have an option to look at information for any and all existing cards connected to your account.")
def passcode():
	print("If you have forgotten or would like to reset your card PIN, please contact the number provided (123-456-7890) or visit your nearest Knabdoog Bank and manually reset/recover it.")
	not_looking_for()
def occupations():
	print("To apply for a job in the bank, please email knabdoogplano@gmail.com with your information and what occupation you wish to apply for.")
	not_looking_for()
def reciepts():
	print("To see purchase history on any of your cards, select the \"Account Information\" option in the dropdown menu under your username in the top right corner of the website screen. The page will have an option to look at card transaction history.")
	not_looking_for()
def settings():
	print("To alter settings for anything in your account, please go to the dropdown option labeled \"Account Settings\" under your username in the top right corner of the website screen.")
def transfer():
	print("To tranfer money from you account to someone else's, please use the Knabdoog app on your mobile device.")
def redeem_info():
	print("To see our available possibilities to win cash prizes and subscriptions, check out our website's home menu.")
def redeem():
	answer = input('''**The chatbot is about to launch a reward redeeming website with a partner bank. Are you sure you want to allow this?***
	''')
	if "yes" in answer:
		import webbrowser
		webbrowser.open('https://www.yesrewardz.com/')
	elif "no" in answer:
		print("Website launch cancelled. To cash in or redeem prize money and rewards, please visit www.yesrewardz.com.")
	else:
		redeem_info()
def budget():
	print("To set up a budget for a certain account, select the \"Account Settings\" option in the dropdown menu under your username in the top right corner of the website screen. There will be a budgeting option in the section where all your accounts are listed.")
def borrowing():
	print("To take out a loan, you will need to either go to your nearest Knabdoog Bank in-person, or call the Knabdoog Help Desk (123-456-7890).")
def bills():
	print("To see all of your bills and their due dates, select the \"Account Information\" option in the dropdown menu under your username in the top right corner of the website screen. The page will have an option to see all of your bills.")
def account():
	print("To see your bank accounts, select the \"Account Information\" option in the dropdown menu under your username in the top right corner of the website screen. To create a new one, there will be an option inside of the same page.")
def income():
	print("To look at your monthly/yearly income, select the \"Account Information\" option under your account username, and then click the Income tab on the page.")
