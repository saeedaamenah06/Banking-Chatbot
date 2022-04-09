#BANKING CHATBOT
exit = 0
name=input('''Hello! Can I have your name?
''')
while (exit!=1):
	help_question=input("Alright, " + (name) + '''. What can I help you with?
	''')
	words=help_question.split() #split the sentence into individual words
	if "open" in words: #see if the word "open" is in the question they asked
		from functions_bank import open_account
		open_account()
	#-----------------------------------------------------------------
	elif "close" in words:
		from functions_bank import close_account
		close_account()
	#-----------------------------------------------------------------
	elif "deposit" in words:
		from functions_bank import deposit_money
		deposit_money()
	#-----------------------------------------------------------------
	elif "withdrawal" in words: #FOR MAKING WITHDRAWALS. WILL BE SIMILAR TO DEPOSITS.
		from functions_bank import withdrawal
		withdrawal()
	elif "withdraw" in words:
		from functions_bank import withdrawal
		withdrawal()
	#----------------------------------------------------------------
	elif "card" in words:
		from functions_bank import card_info
		card_info()
	elif "debit" in words:
		from functions_bank import debit
		from functions_bank import card_info
		from functions_bank import not_looking_for
		debit()
		card_info()
		not_looking_for()
	elif "credit" in words:
		from functions_bank import credit
		from functions_bank import card_info
		from functions_bank import not_looking_for
		credit()
		card_info()
		not_looking_for()
	#----------------------------------------------------------------
	elif "passcode" in words:
		from function_bank import passcode
		passcode()
	elif "PIN" in words:
		from function_bank import passcode
		passcode()
	elif "security" in words:
		from function_bank import passcode
		passcode()
	#----------------------------------------------------------------
	elif "job" in words:
		from function_bank import occupations
		occupations()
	#----------------------------------------------------------------
	elif "history" in words:
		from functions_bank import reciepts
		reciepts()
	elif "reciept" in words:
		from functions_bank import reciepts
		reciepts()
	elif "transaction" in words:
		from functions_bank import reciepts
		reciepts()
	#----------------------------------------------------------------
	elif "settings" in words:
		from functions_bank import settings
		settings()
	#----------------------------------------------------------------
	elif "transfer" in words:
		from functions_bank import transfer
		transfer()
	elif "give" in words:
		from functions_bank import transfer
		transfer()
		from functions_bank import not_looking_for
		not_looking_for()
	#----------------------------------------------------------------
	elif "prize" in words:
		from functions_bank import redeem
		redeem()
	elif "reward" in words:
		from functions_bank import redeem
		redeem()
	#----------------------------------------------------------------
	elif "budget" in words:
		from functions_bank import budget
		budget()
	elif "limit" in words:
		from functions_bank import budget
		from functions_bank import not_looking_for
		budget()
		not_looking_for()
	#-----------------------------------------------------------------
	elif "borrow" in words:
		from functions_bank import borrowing
		from functions_bank import not_looking_for
		borrowing()
		not_looking_for()
	elif "loan" in words:
		from functions_bank import borrowing
		borrowing()
	#-----------------------------------------------------------------
	elif "bills" in words:
		from functions_bank import bills
		bills()
	elif "mortgage" in words:
		from functions_bank import bills
		bills()
	#-----------------------------------------------------------------
	elif "savings" in words:
		from functions_bank import account
		account()
	elif "retirement" in words:
		from functions_bank import account
		from functions_bank import not_looking_for
		account()
		not_looking_for()
	#-----------------------------------------------------------------
	elif "income" in words:
		from functions_bank import income
		income()
		from functions_bank import not_looking_for
		not_looking_for()
	elif "salary" in words:
		from functions_bank import income
		income()
		from functions_bank import not_looking_for
		not_looking_for()
	#------------------------------------------------------------------
	else:
		print("We could not find what you are asking in our key words.If you need further assistance, please call the Help Desk. (123-456-7890)")
	exit = int(input('''Do you want to exit? Enter 1 for yes and 0 for no.
	'''))
	
print("Thank you for visiting the Knabdoog website.")
