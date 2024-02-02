
Getting started - Content Library and API - Documentation - Meta for Developers










Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Getting started
===============


You will work with Meta Content Library API within the Researcher Platform. Researcher Platform runs a modified version of Jupyter and provides you with a virtual data clean room where you can securely search for and analyze data.


To get up and running with Content Library API:


* Set up OpenVPN
* Log in to the Content Library API URL
* Create a Jupyter notebook
* Import the Content Library API client
* Test with a basic search


Set up OpenVPN
--------------


Content Library API can only be accessed through a Virtual Private Network (VPN). This section shows you how to install and configure the OpenVPN client and connect to our VPN server. Once connected, you will be able to access Meta Content Library API.


#### Step 1: Download and install OpenVPN

When the setup wizard completes, OpenVPN Connect launches and you will be required to accept the OpenVPN Inc. Data Collection, Use and Retention policy to continue.


#### Step 2: Set up your profile


In the Import Profile window, select the **UPLOAD FILE** tab.


  
  
#### Step 3: Download the OpenVPN configuration file

Clicking this link downloads the OpenVPN configuration file (fortVpnCredentials.ovpn) to your computer (check your downloads folder). Once downloaded, drag and drop the file into the Import Profile window.


#### Step 4: Connect to the VPN


In the Imported Profile window, click **CONNECT**.


  
  
Once successfully connected, you will see this window:


While you are connected to our VPN server, all of your internet traffic is routed through it, so be sure to disconnect when you are finished.


Log in to the Content Library API URL
-------------------------------------


While connected to the VPN, go to the Content Library API URL. 

Log in to the site using your Facebook credentials. This will spin up an instance of JupyterHub server for your use in the Researcher Platform.


You will be offered the choice of CPU or GPU server. You can learn more about the difference between the two here and there is complete documentation on Researcher Platform here.

Create a Jupyter notebook
-------------------------


To create a new notebook:


1. In your Jupyter hub environment, click the blue "+" symbol in the upper left corner of the window.
2. Under **Notebook** in the Launcher tab, select **Python 3** or **R** according to your preferred language. This creates and opens a new Jupyter notebook.


To name the notebook, right-click the notebook in the left navigation bar and select **Rename**.


  
  
You enter queries in the blank cells of the notebook. To run a query, click the play icon.


Import the Content Library API client
-------------------------------------


All calls are made using the Content Library API Client object. You only need to import the Content Library API client once per Jupyter notebook server session.


In code block examples in this documentation, select the R or Python tab to see the corresponding code. You can copy the code and paste it into your notebook.


RPython
```
library(contentlibraryapi) 
client <- ContentLibraryAPIClient$new(version='1')
```

```
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version = "1")
```
Test with a basic search
------------------------


Test your setup by running a basic search query. Here's an example to try:


RPython
```
# Create a search object
my_page_search <- client$search_pages(
    q='mountains')
        
#Instructions for display:        
pages <- my_page_search$query_next_page()
print(pages)
```

```
# Create a search object
my_page_search = client.search_pages(
    q='mountains')

#Instructions for display:
pages = my_page_search.query_next_page()
print(pages)
```
Learn more
----------


* Jupyter
* JupyterLab Documentation
* Jupyter Notebook Basics
* Researcher Platform documentation

































 
