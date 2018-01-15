from bs4 import BeautifulSoup
import mechanize
import click


email = raw_input('Enter your Email ID: ')
pwd = raw_input('Enter your password: ')

def authenticate(browser,url,email,pwd):
	browser.open(url)
	browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
	browser.form['email'] = email
	browser.form['pass'] = pwd
	response = browser.submit()
	return BeautifulSoup(response,'html.parser')

@click.command()

@click.option('--login',is_flag=True,help='Allows you to login to Facebook')



def cli(login):
	browser = mechanize.Browser()
	browser.set_handle_robots(False)	#Allows everything to be written
	cookies = mechanize.CookieJar()
	browser.set_cookiejar(cookies)
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.set_handle_refresh(False)	#Sometimes hangs without this
	try:
		url = 'http://www.facebook.com/login.php'
		soup = authenticate(browser,url,email,pwd)	#Parses the html and stores in 'soup'
		if(login):			#To find number of new friend request
			fr_num_box = soup.find('span',attrs={'id':'requestsCountValue'})		#Finds span tags with the given ID
			if(fr_num_box != None):
				click.echo("\n\nLOGIN SUCCESSFUL!\n" )
			else:
				click.echo("\n\nLOGIN UNSUCCESSFUL!\nEither the password or email id you've entered is wrong!\nPlease try again!")
	except AttributeError:
		click.echo("Either the password or email id you've entered is wrong")



