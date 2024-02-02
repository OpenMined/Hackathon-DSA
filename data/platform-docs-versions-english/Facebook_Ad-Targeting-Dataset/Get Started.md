Get started
===========

This tutorial will show you how to use our Researcher Platform to perform a basic SQL query against the Ad Targeting dataset.

Before you begin
----------------

* Make sure you have completed the [onboarding process](https://developers.facebook.com/docs/fort/get-access) which includes creating or joining a Research App, completing individual and academic verifications, and App review.
* [Install and configure OpenVPN](https://developers.facebook.com/docs/fort/get-access/vpn#vpn-low) and get connected.

Step 1: log in
--------------

While connected to our VPN, visit the Researcher Platform URL that was emailed to you and log into the site using your Facebook credentials. This will spin up a Jupyter Notebook server instance for your use.

You can access Researcher Platform user documentation [here](https://developers.facebook.com/docs/researcher-platform/).

Step 2: create a notebook
-------------------------

Click the **New** dropdown menu and select either **Python3** or **R**. This will create a new Jupyter Notebook in a new browser tab. Rename the Notebook if you wish.

Step 3: import the query module
-------------------------------

Import our query module (`execute`) by clicking in an empty notebook cell and entering the following code:

RPython

    library(fbrir)

    from fbri.private.sql.query import execute

Run the code by clicking **\>**. You won't see anything happen, but a new notebook cell will appear when it finishes importing.

Step 4: create and run a SQL query
----------------------------------

Enter the following code in the empty notebook cell to define a SQL query (`sql`) using variable substitution (`database` and `table`), and use the query module to execute the query:

RPython

    library(fbrir)
    athena = AthenaFacade$new()
    
    database <- "fbri_prod_atp"
    table <- "ad_targeting_dataset_siep_aug_2020"
    api_table <- "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql <- sprintf("SELECT * FROM %s.%s LIMIT 5", database, table)
    athena$QueryAthena(sql)

    from fbri.private.sql.query import execute
    
    database = "fbri_prod_atp"
    table = "ad_targeting_dataset_siep_aug_2020"
    api_table = "ad_archive_api"
    
    # Define your own SQL query and assign to variable 'sql' 
    sql = f"SELECT * FROM {database}.{table} LIMIT 5"
    
    execute(sql)

Run the code. This should return a dataframe of your results, similar to those shown below (screenshots of dataframe results blurred intentionally).

The dataframe result from the R example would look similar to this (blurred intentionally):

  
  

The dataframe result from the Python example would look similar to this (blurred intentionally):

  
  

You can scroll within the dataframe to see additional table columns.

Next steps
----------

If you are able to perform the query above, you are able to perform a basic search using our web app. We recommend that you now read a few [sample queries](https://developers.facebook.com/docs/fort-ads-targeting-dataset/sample-queries) to get an idea of how to build your own custom queries.

Learn more
----------

* [Researcher Platform](https://developers.facebook.com/docs/researcher-platform/)