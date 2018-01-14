if [ -f venv/bin/activate ]
then
	echo "As virtualenv exists, we'll only be setting up the virtual environment now!"
	echo "ACTIVATING........"
	chmod 777 build.sh	#Gives reading, writing and execution power to all users on system
	. venv/bin/activate	#helps you enter into virtual environment
	pip install --editable .
else
	echo "Since you don't have Virtualenv installed already, we'll install it for you!"
	echo "After installing, we'll also be setting it up for you!"
	echo "Please wait for a few moments! :)"
	echo "INSTALLING......."
	sudo apt-get install virtualenv		#install virtualenv
	virtualenv venv		#creates your virtualenv by the name venv
	chmod 777 build.sh	#Gives reading, writing and execution power to all users on system
	. venv/bin/activate	#helps you enter into virtual environment
	pip install --editable .
fi
