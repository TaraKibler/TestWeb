import pytest
import urllib.request

# This method will check to be sure that the given URL will return a 200 status code
def test_websiteIsUp():
	url = "http://www.google.com"

	# Used to test a failure
	# url2 = "http://www.trythisbecauseitwontwork.com"

	try: status_code = urllib.request.urlopen(url).getcode()
	except urllib.error.URLError as e:
		assert "status_code" == 200,"ERROR: The url is not valid"
		print(e.reason) 
	else:
		website_is_up = status_code == 200
		print(website_is_up)
		assert status_code == 200,"ERROR: Expecting url to return status 200" 