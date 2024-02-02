Instagram accounts - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Guide to Instagram accounts data
================================

You can perform searches for Instagram creator, business, and certain personal accounts by calling the Meta Content Library API client's `search_ig_accounts()` method.

For personal accounts, only those that have account privacy set to public, and have either a verified badge or 50,000 or more followers are included. This document describes the `search\_ig\_accounts()` method and its syntax and parameters, and shows how to perform basic queries using the method.
All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See Getting started to learn more.

See Data dictionary for detailed information about the fields that are available on an Instagram account node.

search\_ig\_accounts() method
-----------------------------

This is the syntax of the `search_ig_accounts()` method:

```
search_ig_accounts(
    q=Q,
    fields=FIELDS,
    account_ids=ACCOUNT_IDS,
    account_types=ACCOUNT_TYPES,
    is_verified=IS_VERIFIED,
    since=SINCE,
    until=UNTIL      
)
```
The following table describes the parameters:

 Parameter
  | 
 Type
  | 
 Description
  || `Q`
*Optional* | String | Keyword(s) to search Instagram accounts for. See Advanced search guidelines for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`
*Optional* | List | A comma-separated list of Instagram account fields you want included in search results. See Data dictionary for descriptions of all available fields. |
| `ACCOUNT_IDS`
*Optional* | List | Comma-separated list of Meta Content Library Instagram account IDs to include in the search results. Maximum of 250 IDs. |
| `ACCOUNT_TYPES`
*Optional* | List | Comma-separated list of account types of the Instagram accounts to be included in the search results. Possible values are `creator`, `business` and `personal`.
Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. |
| `IS_VERIFIED`
*Optional* | Boolean | Whether the Instagram account is verified. An Instagram account with a legacy blue verified badge means that Instagram has confirmed that it is the authentic presence for that person or brand. Learn more. |
| `SINCE`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
| `UNTIL`
*Optional* | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.* If both SINCE and UNTIL are included, the search includes the time range defined by those values.
* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.
* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.
* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.
* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.
* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day.
 |
Sample queries
--------------

### Search for Instagram accounts by keyword

To search for Instagram accounts that contain a specific keyword, create a search object using the `search_ig_accounts()` method with the `q` parameter. See Advanced search guidelines for information about how multiple keyword searches are handled.

RPython
```
# Create a client object if you have not already done so:
library(contentlibraryapi)
client <- ContentLibraryAPIClient$new(version='2')
# Create a search object:
ig_account_search <- client$search_ig_accounts(q='cybercrime')        
# No results are displayed until you provide display instructions:        
print(ig_account_search$query_next_page())
```
```
# Create a client object if you have not already done so:
from contentlibraryapi import ContentLibraryAPIClient
client = ContentLibraryAPIClient.get_instance(version='2')
# Create a search object:
ig_account_search = client.search_ig_accounts(q='cybercrime')
# No results are displayed until you provide display instructions:
display(ig_account_search_search.query_next_page())
```
This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See Search guide for other display and storage options.

### Request specific fields

To have the API return only specific fields on any Instagram accounts in the response, create a search object using the `search_ig_accounts()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython
```
# Create a search object including a list of fields:
ig_account_search <- client$search_ig_accounts(q='cybercrime', fields='id,name,biography')        
# Specify DataFrame response format:       
print(ig_account_search$query_next_page('dataframe'))
```
```
# Create a search object including a list of fields:
ig_account_search = client.search_ig_accounts(q='cybercrime', fields='id,name,biography')
# Specify DataFrame response format:        
display(ig_account_search.query_next_page('dataframe'))
```
DataFrame response format has clear columns:

### Search for Instagram accounts by account ID

You can search for Instagram accounts using specific account IDs obtained from previous account searches.

To get data on specific Instagram accounts that contain specific keywords or phrases, create a search object using the `search_ig_accounts()` method with the `q` parameter (specifying the keywords or phrases) and the `account_ids` parameter (specifying the list of account IDs you want included). If you omit the `q` argument, all accounts in the list of IDs are included, not just those with a specific keyword or phrase.

RPython
```
# Create a search object limiting the response to specific account IDs 
        account_search <- client$search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)
```
```
# Create a search object limiting the response to specific account IDs 
        account_search=client.search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)
```
For using Instagram account IDs to search for posts from specific Instagram accounts, see Guide to Instagram posts data.

Learn more
----------

* Getting started
* Search guide
* Data dictionary
* Advanced search guidelines
* Guide to Instagram posts data