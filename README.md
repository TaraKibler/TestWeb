# TestWeb

This is an example of a python test which checks to see if a website is up and running.

To run the test, you must have python and pytest installed.
pytest needs to be in your path.

For example, install Python v3.9.4 to:
C:\Users\Home\AppData\Local\Programs\Python\Python39\

Add this to your PATH:
C:\Users\Home\AppData\Local\Programs\Python\Python39\Scripts

To run the test:
Open a command prompt.
Go to the directory where the python test sits.
  For example, cd C:\Users\Home\git\TestWeb
pytest checkURL.py

If the url returns a status_code of 200, the test will pass
If the url does not return a status_code of 200, the test will fail with:
  ERROR: Expecting url to return status 200
If attempting to open the url returns an exception, the test will fail with:
  ERROR: The url is not valid

