print('Buongiorno e Benevuti, Usario !')
import random
#password generator
def password_generator(password):
	'''
	The function is created to generate strong passwords for users at covenience
	'''
	cipher =(len(password))
	if cipher<8:
		print('Your password is weak, up the ante !')
	else:
		print('Fortuna !')
		return str(cipher)

L = ['4','C','d','6','7','e','5','T','O','x','9','3','a','y','8','D','E','m','n']			
password = random.choice(L)
password = input('enter your password: ')
password_generator(password)
print('Grazie e Arriverderci ')