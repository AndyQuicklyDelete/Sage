# Sage

**What is Sage**
Sage is a Python Script/SEO utility designed to automate browser services in order to decrease the bounce rate in the analytics of a website to a reasonable percentage.

**How Sage Works**
Sage effectively utilizes free proxy lists and the Selenium API to navigate to a website with browser automation (Selenium). On each execution a request is made to the proxy list for a new IP address. During this process the client (web browser) waits for an appropriate amount of time before moving to a different page of your website or to a new domain in your domain list. You specify each URL for the browser to navigate to in the domain list (urls.txt).

If a proxy in the proxylist fails to load, the script will stop itself and relaunch with a new IP address. The script will wait for a total of 90 seconds to attempt to receive the connection. We do this simply because proxies can often be quite slow or offline.

**Install**
1) Install the Chrome Browser
2) Install a python 3 version. It is suggested to use python 3.8+
3) You will need to install Selenium:
	1) pip install Selenium
	2) pip install beautifulsoup4 for the proxyScraper.py 
	
You will need to place/replace the latest Chrome Driver (chromedriver.exe) in to the project directory. https://googlechromelabs.github.io/chrome-for-testing/#stable

**Build Proxy List**
1) Gather a working proxy list and name the file proxylist.txt. (With each proxy address on a separate line)
2) Sage will by default use the proxylist.txt file
3) You can download a list of http or https proxies from here: https://github.com/TheSpeedX/PROXY-List

**Modify Script**
1) Create a domain/url list in urls.txt
2) Modify runChrome.py specifying the amount of times you wish to run the script

**Launching**
1) Run the script with this command: python runChrome.py

**Notes**
1) You will not see results if browsing to a single page on a website. This has to do with how bounce rate is calculated from average session duration in Google Analytics.
2) After exiting the script 'runScript.py' you will need to do additional cleanup by killing any of the remaining Chrome processes still present.
3) Let it continue as it loops through your domain list using your Chrome browser, the script will pause between 90 and 120 seconds on each page it navigates to. When it finishes the loop the script will close and respawn with a new IP address.
4) **Timestopper.crx** is an addon that prevents alert() windows from appearing. In the early years of development sometimes a free proxy would force an alert() and block the script until it was closed. Timestopper.crx might not continue to work after Manifest v2 in chrome is completely gone, est year 2024.
5) The first connection in the script is directed to a domain of mine, and is just a blank page with a title, I do this to test the connection of each proxy. The address is here you can check it out if you like: https://www.techshinobi.com/browser/test-page.html 


