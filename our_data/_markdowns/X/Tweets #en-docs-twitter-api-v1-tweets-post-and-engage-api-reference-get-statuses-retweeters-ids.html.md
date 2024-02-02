
GET statuses/retweeters/ids | Docs | Twitter Developer Platform 

GET statuses/retweeters/ids

get-statuses-retweeters-ids
GET statuses/retweeters/ids
===========================

Returns a collection of up to 100 user IDs belonging to users who
have retweeted the Tweet specified by the `id` parameter.

This method offers similar data to GET
statuses / retweets / :id.

Resource URL¶
-------------

`https://api.twitter.com/1.1/statuses/retweeters/ids.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75 |
| Requests / 15-min window (app auth) | 300 |

Parameters¶
-----------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| id | required | The numerical ID of the desired status. |  | `327473909412814850` |
| count | optional | Specifies the number of records to retrieve. Must be less than or
equal to 100. |  | `5` |
| cursor | semi-optional | Causes the list of IDs to be broken into pages of no more than
100 IDs at a time. The number of IDs returned is not guaranteed to be
100 as suspended users are filtered out after connections are queried.
If no cursor is provided, a value of `-1` will be assumed,
which is the first "page."The response from the API will include
a `previous_cursor` and `next_cursor` to allow
paging back and forth. See our
cursor docs for more information.While this method supports
the cursor parameter, the entire result set can be returned in a single
cursored collection. Using the `count` parameter with this
method will not provide segmented cursors for use with this
parameter. |  | `12893764510938` |
| stringify\_ids | optional | Many programming environments will not consume Tweet ids due to
their size. Provide this option to have ids returned as strings
instead. |  | `true` |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=327473909412814850&count=100&stringify_ids=true`

Example Response¶
-----------------

```
{ "previous_cursor": 0, "ids": [ "1382021622", "931150754", "1364953914", "92313481",
  "1398853771", "268642828", "1393765387", "417614795", "1401282895", "1319566290",
 "1398546265", "1332481988", "295679474", "967380524", "1278983791", "711759314",
 "1396957736", "1400099804", "1400006540", "307434897", "531100534", "553765661",
 "1398911250", "342624342", "629452817", "117815404", "137706363", "200935461",
 "387409391", "1361168810", "1368343309", "613471026", "439924515", "36049728",
 "1274405064", "1389815384", "1392424261", "577940232", "876175585", "510085789",
 "410346647", "1393727204", "1394189851", "1387201657", "1393950540", "900169760",
 "69572684", "517788963", "386168676", "1378242152", "18442587", "848640758",
 "1366022899", "25457359", "257764557", "795253765", "1170975386", "1229598968",
 "204528531", "954414061", "533154335", "580732530", "350798999", "427506664",
 "527674954", "1389957769", "496054455", "1338136910", "1390051482", "1252565820",
 "815941296", "1357349460", "1214535374", "1192879201", "1353712213", "229798008",
 "1382909124", "1026779562", "917199121", "1388715336", "1388417048", "106315621",
 "109159559", "523186040", "1256627971", "1137979866", "424946721", "1387875991" ],
 "previous_cursor_str": "0", "next_cursor": 0, "next_cursor_str": "0" }
```

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies