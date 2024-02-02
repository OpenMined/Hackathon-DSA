


















































LinkedIn API Pagination - LinkedIn | Microsoft Learn













Skip to main content



This browser is no longer supported.


Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.



Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge





















Table of contents 



Exit focus mode
































Read in English




Save













Table of contents

Read in English




Save

Edit




Print


Twitter
LinkedIn
Facebook
Email











Table of contents




Pagination
==========




* Article
* 05/08/2023
* 3 contributors








Feedback





In this article
---------------




API calls that return a large number of entities are broken up into multiple pages of results. You might need to make multiple API calls with slightly varied paging parameters to iteratively collect all the data you are trying to gather.


Use the following query parameters to paginate through results:


Parameters
----------




| Name | Description | Default |
| --- | --- | --- |
| start | The index of the first item you want results for. | 0 |
| count | The number of items you want included on each page of results. There could be fewer items remaining than the value you specify. | 10 |


To paginate through results, begin with a `start` value of 0 and a `count` value of N. To get the next page, set `start` value to N, while the `count` value stays the same. Subsequent pages start at 2N, 3N, 4N, and so on.


Samples
-------


#### Sample Request



```
GET https://api.linkedin.com/v2/{service}

```

#### Sample Response



```
"elements": [
    {"Result #0"},
    {"Result #1"},
    {"Result #2"},
    {"Result #3"},
    {"Result #4"},
    {"Result #5"},
    {"Result #6"},
    {"Result #7"},
    {"Result #8"},
    {"Result #9"}
],
"paging": {
    "count": 10,
    "start": 0
}

```

#### Sample Request



```
GET https://api.linkedin.com/v2/{service}?start=10&count=10

```

#### Sample Response



```
"elements": [
    {"Result #10"},
    {"Result #11"},
    {"Result #12"},
    {"Result #13"},
    {"Result #14"},
    {"Result #15"},
    {"Result #16"},
    {"Result #17"},
    {"Result #18"},
    {"Result #19"}
],
"paging": {
    "count": 10,
    "start": 10
}

```

### End of the Dataset


You have reached the end of the dataset when your response contains fewer elements in the `entities` block of the response than your `count` parameter request.













---


Feedback
--------



Was this page helpful?







Yes





No





Provide product feedback




Feedback
--------



Submit and view feedback for



This product
This page



View all page feedback








---


Additional resources
--------------------












California Consumer Privacy Act (CCPA) Opt-Out Icon





Your Privacy Choices







Theme





* Light
* Dark
* High contrast






* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2023







Additional resources
--------------------






### In this article






















California Consumer Privacy Act (CCPA) Opt-Out Icon





Your Privacy Choices







Theme





* Light
* Dark
* High contrast






* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2023







