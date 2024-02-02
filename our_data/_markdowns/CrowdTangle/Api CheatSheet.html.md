API Cheat Sheet | CrowdTangle Help CenterGo to CrowdTanglePortuguês do BrasilEnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어简体中文Español繁體中文Tiếng Việt;EnglishGo to CrowdTanglePortuguês do BrasilEnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어简体中文Español繁體中文Tiếng Việt;EnglishAll CollectionsProduct OverviewsAPIAPI Cheat SheetAPI Cheat SheetShortcuts to understanding and using the CrowdTangle API.
CWritten by Christina Fan Updated over a week ago**Update July 2023:**
* Reddit announced changes to their API, which resulted in CrowdTangle losing access and the ability to serve Reddit data. You can find more information here and here.

---
The CrowdTangle API corresponds to several functions available through the Dashboard. It’s as if you were directly obtaining a CSV of your List or Saved Search, but in JSON or XML format. Please note that we don't have all filters available in the new Search surface in the API yet, but all the same posts are available.

Why would you use the CrowdTangle API instead of the UI?
========================================================
* If you're trying to get **post time-series data and post content information together,** in bulk.
* If you're more comfortable using a programming language than clicking around in the UI.
* If you want to download a **hosted image link** for any photos that appear in post content.

Tools and resources for getting started:
========================================
**Postman is a free API management software. This JSON file provides a template for each endpoint** (just right-click and select "Save Link As..." to save the file, and then import into Postman).

**Check out our full API documentation on GitHub**. 

Watch this training to learn more about getting the most out of the CrowdTangle API.

Please note that academic users currently don't have access to Reddit data through our API. Reddit announced changes to their API, which resulted in CrowdTangle losing access and the ability to serve Reddit data. 

Some helpful tips for getting the best API experience:
======================================================
**For all endpoints, use the *start date* and *end date* parameters to prevent CrowdTangle from crashing and to reduce load times.**

**Use a Facebook Dashboard token to call Facebook posts, and an Instagram Dashboard token to call Instagram posts** -- you unfortunately can't use the same token across different platforms.

**Number of posts returned and pagination** 
* /posts and /posts/search will max out at 10,000 posts returned. /links will max out at 1000 posts returned. You must paginate through those posts to reach the end of the query,
* You can see up to 100 posts at a time (*count* parameter goes up to 100). To see the next one hundred posts, paginate using the *offset* parameter. For example: set *count* = 100 to see posts 1-100. Then, set *count* = 100 and *offset* = 100 to see posts 101 - 200. Continue increasing the *offset* parameter in successive calls to see all posts.
* Each pagination will count against your rate limit. Slice thinly by date or SQL timeframe to separate your results into ~10k batches so you don't miss any data. To get more than 10k posts at a time, use Historical Data in the Dashboard rather than the API.
**Making sure you get all posts for a given time period**
* **Make sure to sort by Date to capture all posts.** If you don’t specify the *sortby* parameter, the API will by default return posts sorted by Overperforming. This will exclude posts that are Underperforming.
**Default rate limits and settings:**
* **/posts/search is not enabled by default.**
* **Rate limit defaults:** 6 calls/min for all but /links, which is 2 calls/min.
* **By default, the API object names do not match the CSV headers. This cannot be changed.**
* **The API uses the UTC timezone. This cannot be changed.** The CrowdTangle User Interface allows the user to change the time zone of their dashboard, so always account for time zone differences when comparing results in the API and UI.
* **By default, the subscriberCount property will show page Followers** (as of January 26, 2021). You can select either Page Likes or Followers in your Dashboard settings. Learn more here.
**Platform IDs**
* **Platform IDs are external IDs native to the selected platform (Facebook, Instagram).** You can use our API (/posts or /leaderboard, for example) to programmatically fetch platformIDs for each account in a List or Dashboard you're interested in. If the post is from Facebook, you can also find the Platform ID in the URL of the post. For example, this url https://www.facebook.com/81221197163/posts/10158939904512164 has a platformID of *81221197163\_10158939904512164.*

Endpoints Overview
==================
/posts
------
* This endpoint lets you stream data from posts in a List or Saved Search. It’s as if you were looking at a List or Saved Search in your Dashboard. **It does not let you search the entire CT database -- if you do not specify a ListID, this endpoint will search through all the lists in your dashboard.**
* You can search for terms within the List or Saved Search using Boolean syntax with the SearchTerm parameter.
* Make sure to grab your ListID from the URL or the /lists endpoint in order to pull in posts -- this ID exists for both Lists and Saved Searches.
* You can use Weights just like in a List or Saved Search in the Dashboard, on a scale of 1-10
* The default number of posts returned at a time is 10. The *count* parameter can only go to between 1-100 -- paginate using the *offset* parameter to view all posts.
* Use the *includeHistory* parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
* Use the *accounts* parameter to search by the account handle or platform ID.
/post/:id
---------
* Retrieves a specific post according to its Facebook ID. Read more about the endpoint here.
* Use the *includeHistory* parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
/ctpost/:id
-----------
* Retrieves a specific post according to its CrowdTangle ID. Read more about the endpoint here.
* Use the *includeHistory* parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
/posts/search
-------------
* This endpoint acts like Historical Data, but with more nuanced search terms. It lets you search **the entire CT database.** You can differentiate account types using the *accountTypes* parameter.
* The *SearchField* parameter allows you to search for URLs with query strings, image text only, and account names, in addition to the usual post text and image text.
* /posts/search does not support regular expressions, or any sort of wildcard search.
* You can pull in from Lists and Saved Search by using the *ListID* parameter, just like in the /posts endpoint. You can also pull in from Account using *AccountID* parameter.
* You can use "OR," “AND” and “NOT” for terms and Lists to search, but you cannot use Weights.
* Most of the functionality you’d want from this is easily available by setting up a Saved Search in your Dashboard, and pulling it in through the /posts endpoint.
* The default number of posts returned at a time is 10. The *count* parameter can only go to between 1-100 -- paginate using the *offset* parameter to view all posts.
* Use the *includeHistory* parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
* Use the *accounts* parameter to search by the account handle or platform ID.
* If you submit a query with a blank searchTerm (i.e., searchTerm=" "), the result set will be limited to the Dashboard associated with the supplied API token. System-wide blank searches are not supported by default. Please reach out to support@crowdtangle.com for more information.
/leaderboard
------------
* This acts like Lists Leaderboard -- **NOT** Search Leaderboard. You will not get a list of the number of posts that match your search parameters through this endpoint.
/links
------
* This endpoint acts like the Chrome Extension. However, it will pull in Facebook, Instagram
* You can specify the number of posts to pull in - the maximum is 1000.
* Set the *summary* parameter to “true” to get the top-line summary of interactions for the link.
* Use the *includeHistory* parameter to get time-series data for each post -- this is the same data you get when you download a single post CSV in the UI. Note that we will not have time-series data for posts that were created after the account was added to CrowdTangle.
* The *SearchField* parameter allows you to search for URLs with query strings.
/lists
------
* This endpoint tells you the names and IDs of all your Lists. This allows you to quickly pull List IDs for inclusion or exclusion in queries with other endpoints.
/lists/:listId/accounts
-----------------------
* This endpoint tells you the names of all the Pages or Groups in a given List.  This allows you to quickly pull Account IDs for inclusion or exclusion in queries with other endpoints.
​**For more information, please see this broader overview of the API, and check out our API documentation on GitHub.**

Did this answer your question?😞😐😃* 
* 