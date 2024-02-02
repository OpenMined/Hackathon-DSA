Get started - Ad Targeting dataset - Documentation - Meta for Developers

Ad Targeting dataset* Get access
* Overview
* Get started
* Sample queries
* Table schema
* Support
Get started
===========

This tutorial will show you how to get set up to the point that you can use Meta's Researcher Platform to perform basic SQL queries on the Ad Targeting dataset.

Before you begin
----------------

Make sure you have completed the onboarding process which includes creating or joining a Research App, completing individual and academic verifications, and App review.

Install and configure OpenVPN
-----------------------------

Our products can only be accessed through our Virtual Private Network (VPN). This guide shows you how to install and configure the OpenVPN client and connect to our VPN server. You use your Apps Dashboard to set up your VPN access.

While you are connected to our VPN server, all of your internet traffic is routed through it, so be sure to disconnect when you are finished.

### Step 1: Access your Apps Dashboard

 Go to your Apps Dashboard.
### Step 2: Select the app

Select the app that has been granted access to the dataset of interest.

If your App has not been approved please refer to App Review for instructions.

### Step 3: Install OpenVPN

Download the latest version of the OpenVPN Client and install the application on your computer.
### Step 4: Generate Credentials

In your App Dashboard, navigate to **Settings** > **Basic**. In the new page that displays, scroll down to the "Connect to our VPN" section and click **Generate Credentials**. The button looks similar to this:

This downloads a credentials file that you can import into the OpenVPN Client you installed.

If the Generate Credentials button is grayed out, your selected app has not completed app review. You can navigate to **Dashboard** from the left side navigation panel to check on the status.

### Step 5: Launch and connect

Launch **OpenVPN** and import the file you generated.

Check the **Connect after import** checkbox, then click **Add** to add the imported file to your profile.

Once the import is complete and the connection to the VPN is established, OpenVPN displays a clock indicating that you are connected. You should then be able to access Researcher Platform and the Ad Targeting dataset.

Get started in Researcher Platform
----------------------------------

### Step 1: log in

While connected to our VPN, visit the Researcher Platform URL that was emailed to you and log into the site using your Facebook credentials. This will spin up a Jupyter Notebook server instance for your use.

You can access Researcher Platform user documentation here.

### Step 2: Create a notebook

Click the **New** dropdown menu and select either **Python3** or **R**. This will create a new Jupyter Notebook in a new browser tab. Rename the Notebook if you wish.

### Step 3: Import the query module

Import our query module (`execute`) by clicking in an empty notebook cell and entering the following code:

RPython
```
library(fbrir)
```
```
from fbri.private.sql.query import execute
```
Run the code by clicking **>**. You won't see anything happen, but a new notebook cell will appear when it finishes importing.

### Step 4: Create and run a SQL query

Enter the following code in the empty notebook cell to define a SQL query (`sql`) using variable substitution (`database` and `table`), and use the query module to execute the query:

RPython
```
library(fbrir)
athena = AthenaFacade$new()
database <- "fbri_prod_atp"
table <- "ad_targeting_dataset_siep_aug_2020"
api_table <- "ad_archive_api"
# Define your own SQL query and assign to variable 'sql' 
sql <- sprintf("SELECT * FROM %s.%s LIMIT 5", database, table)
athena$QueryAthena(sql)
```
```
from fbri.private.sql.query import execute
database = "fbri_prod_atp"
table = "ad_targeting_dataset_siep_aug_2020"
api_table = "ad_archive_api"
# Define your own SQL query and assign to variable 'sql' 
sql = f"SELECT * FROM {database}.{table} LIMIT 5"
execute(sql)
```
Run the code. This should return a dataframe of your results, similar to those shown below (screenshots of dataframe results blurred intentionally).

The dataframe result from the R example would look similar to this (blurred intentionally):

The dataframe result from the Python example would look similar to this (blurred intentionally):

You can scroll within the dataframe to see additional table columns.

Next steps
----------

If you are able to perform the query above, you are able to perform a basic search using our web app. We recommend that you now read a few sample queries to get an idea of how to build your own custom queries.

Learn more
----------

* Researcher Platform