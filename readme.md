#	Offline Cloud Functions

	This project contains all the offline cloud functions which can be emulated on the local machine for any bugs or errors and then can be pushed on the Google Cloud Platform. The functions have been implemented in **Python 3.7**.

##	Dependencies

* Python 3.7
* Internet Browser
* Flask (can be imported directly in the project)

##	How to Run

	To run these files just run normally by navigating to the directory and deploying the python command.
	gcloud functions deploy total_content --runtime python37 --trigger-http
	pip freeze > requirements.txt

##	Files

* users.csv
* quiz_data
* xxy.json

All these files are used to fetch the respective data from the firebase and outputs the csv as a downloadable file.

###	users.csv

This file contains the User IDs of the users for which the following data need to be fetched.

###	main.py

This python file fetches the quiz consumed by the users specified in the CSV and the timestamp when they were consumed.

The initial part consists of structuring the CSV for the row and column headers from the firebase using `get` request.
The	`info_data` function is the main function which is called by the cloud.

This function iterates through the `users.csv` file with the User IDs and provides the information about inforgraphics by every user.
A dictionary object is created to fill the cells with the timestamp when the infographics was consumed.
The `count` variable stores the count of the infographics and appends at the end of the row.

After iterating the loop, all the data is pushed into a DataFrame which is then converted to a CSV file.

This csv file is then pushed into the google cloud storage using the bucket name specified which can be accessed from the bucket.


###	xxy.json

This file contains the firebase admin credentials which are needed to authenticate in order to be able to write to the cloud bucket.

