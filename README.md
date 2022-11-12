Title: Knuth Morris Pratt (Web service)
Description: Flask REST web service that shows an API that allows to submit a short 
	nucleotide sequence and returns the number of occurrences and the position(s) 
	of the short sequence in the genome of SARS-COV-2.
Author: Marco Bianchi (marco30.bianchi@mail.polimi.it)	
Dependencies: Flask

#######################
RUNNING THE APPLICATION (being in the source folder):

- 'flask run' in command line will automatically run the application in localhost and
	on the default port:5000;
	
- 'export FLASK_RUN_PORT=8000' will change the port configuration from 5000 to 8000.
	After using this command use 'flask run' to run the application on the new port;
	
- 'flask run --port=8000' will run the application on the specified port.
