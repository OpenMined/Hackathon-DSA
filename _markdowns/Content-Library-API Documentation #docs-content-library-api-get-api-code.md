
Get API Code - Content Library and API - Documentation - Meta for Developers









Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Get API Code
============


Get API Code is a tool within Meta Content Library that automatically generates a Python or R code snippet corresponding to your current search that you can copy and paste into your Meta Content Library API Jupyter notebook.


**Remember the limits**


If you submit a synchronous query in the Content Library API that would return more than 1000 results, you will only see the top 1000.


If you submit an asynchronous query in the API that would return more than 100,000 results, the API will give you an error message and will not complete the query.


The automatically generated R or Python code might return more than 100,000 results. Be sure to check the very top of the Content Library search results to see the size of the results before you use the same search in the API.


In Content Library
------------------


### Define your search


Select the parameters for your search. The **About** page in the web UI describes all the filters that are available.

### Open the Get API Code tool


Click **</>** in the top menu bar (mouse over the button to see the label).


  
  
### Select Python or R


A new window opens in which your search parameters are listed, and the automatically-generated Python and R code that corresponds to your current search parameters is displayed in a tabbed code block. Click the tab corresponding to your language selection.


### Copy the code snippet


With the correct tab selected, click **Copy to Clipboard** below the code block.


The code block also includes instructions for submitting the code to the API as an asynchronous search which processes in the background. See Search guide to learn about the difference between synchronous (default) and asynchronous searches.


### Go to Content Library API


At the bottom of the **Get API Code** window, there is a **Go to Content Library API** button that opens the Content Library API sign-in window.


VPN connection is required for Content Library API:


* The **Go to Content Library API** button is clickable if you are connected to VPN.
* If you believe you are connected, but the button is not clickable, try refreshing your browser.
* For Content Library API getting started information including VPN access, see Getting started.


In Content Library API
----------------------


### Paste the snippet into a notebook cell


Paste the code representing your search (query) into a blank cell in your Jupyter notebook. Be sure the language (R or Python) of the notebook matches the language of the code you copied. If you have not already set up your Jupyter environment, see Getting started for guidance.


### Run the code


Click the triangular button to run the code and display the results.


Learn more
----------


* API documentation home page
* Search guide
* Getting started


































 
