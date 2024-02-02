About Research API
==================

TikTok's Research API allows independent and academic researchers who work for a non-profit institution to access certain data, including the following information about public account owners who are aged 18 and over.

* **Videos** - Videos configured to "Everyone" for who can watch, and for such videos, the total number of likes, total number of comments, voice-to-text, subtitles, the time of creation and video length.
* **Comments -** comment text, and total number of likes, replies, and the time the comment was posted.
* **Accounts -** bios, profile pictures, the total number of followers and the number of people who are followed by the account.

This Research API supports research in areas such as misinformation, disinformation, violent extremism, social trends, and community building. In order to obtain access to TikTok's Research API, researchers must submit an application, be approved, and adhere to our [Community Guidelines](https://www.tiktok.com/community-guidelines), [TikTok Research API Services Terms of Service](https://www.tiktok.com/legal/page/global/terms-of-service-research-api/en), as well as be approved by their research institution's ethics committee.

Additional information about TikTok's Research API can be found on [TikTok for Developers](https://developers.tiktok.com/products/research-api/).

Getting Started
===============

This guide will show you how to use the Research API. Learn how to use the Research API to query video data and fetch public TikTok account data in the following use case example.

View your client registration
=============================

Once your application is approved, a research client will be generated for your project. You can view your approved research projects [here](https://developers.tiktok.com/research/). Select a project from the list to see the research client details.

The provided **Client key** and **Client secret** are required to connect to the Research API endpoints. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).

The client secret is a credential used to authenticate your connection to TikTok's APIs. Do not share this with anyone!

Obtain a client access token
============================

Once you have obtained the client key and secret for your project, [generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Research API endpoints.

Query TikTok public content data
================================

The cURL command below shows an example of how you can query the TikTok ID and like count of videos created in the US or Canada with the keyword `hello world` in the video description.

     
    curl -X POST \
      'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "query": {
                  "and": [
                       { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                       { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
                   ]
              }, 
              "start_date": "20220615",
              "end_date": "20220628",
              "max_count": 10
    }'
    

Query condition
---------------

Similar to the WHERE clause in SQL, a condition can be used to filter data returned in a query operation. The above request is equivalent to the following SQL query:

     SELECT id,like_count FROM video_table WHERE region_code IN ["US", "CA"] AND create_date > 20220615

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required?** |
| field\_name | string | The field name this condition is restricting | "region\_code" | TRUE |
| operation | string | The comparison logic of this condition. One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" | "GT" | TRUE |
| field\_values | list\[string\] | A list of values to be compared with | \["US", "IN"\] | TRUE |

Note: approximate string matching (or fuzzy string searching) is used to match conditions.

### field\_name

The following are the `field_name` values:

* `keyword`
* `create_date`
* `username`
* `region_code`
* `video_id`
* `hashtag_name`
* `music_id`
* `effect_id`
* `video_length`

### operation

The following are the `operation` values:

`IN`: Tests if an expression matches any value in a list of values.`EQ`: Tests if an expression matches the specified value.`GT`: Tests if an expression is strictly greater than the specified value.`GTE`: Tests if an expression is greater than or equal to the specified value.`LT`: Tests if an expression is strictly less than the specified value.`LTE`: Tests if an expression is less than or equal to the specified value.

### AND, OR or NOT

Conditions are grouped by the following boolean operators:

`AND`: Displays a record if all the conditions separated by `AND` are `TRUE`.`OR`: Displays a record if any of the conditions separated by `OR` is `TRUE`.`NOT`: Displays a record if all the conditions separated by `NOT` are `FALSE`.

Pagination
----------

If the total number of videos that match the query criteria is larger than the max number of videos that can be returned in a single request, the response data will be returned with different requests.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Field** | **Type** | **Description** | **Example** | **Required?** |
| max\_count | number | The max count of TikTok videos in response. default: 10, max: 100 | 12  | FALSE |
| cursor | number | The starting index of TikTok videos in response. default: 0 | 100 | FALSE |
| search\_id | string | The ID of a previous search to provide sequential calls for paging | "7167072234702738478" | FALSE |

### First page

When you send the first request, you do not need to set the `search_id` or `cursor` in the request body. In the http response, `cursor` and `search_id` are returned, which are used in the subsequent requests.

    Try out this request:
    
    curl -X POST \
      'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "query": {
                  "and": [
                       { "operation": "IN", "field_name": "region_code", "field_values": ["US", "IN"] },
                       { "operation": "GT", "field_name": "hashtag_name", "field_values": ["hello"] }
                   ]
              }, 
              "start_date": "20220615",
              "end_date": "20220628",
              "max_count": 10
    }'
    

The following example data is returned from the response.

    {
        "data": {
            "cursor": 10,
            "has_more": true,
            "search_id": "7160776277492814854",
            "videos": [
                ...
            ]
        },
        "error": {
            ...
        }
     }
    

### Next page

With the cURL command below, you can get the next page of query results.

    curl -X POST \
      'https://open.tiktokapis.com/v2/research/video/query/?fields=id,like_count' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "query": {
                  "and": [
                       { "operation": "IN", "field_name": "region_code", "field_values": ["US", "IN"] },
                       { "operation": "GT", "field_name": "hashtag_name", "field_values": ["hello"] }
                   ]
              }, 
              "max_count": 10,
              "cursor": 10,
              "start_date": "20220615",
              "end_date": "20220628",
              "search_id": "7160776277492814854",
    }'
    

The following example data is returned from the response.

    {
        "data": {
            "cursor": 20,
            "has_more": true,
            "search_id": "7160776277492814854",
            "videos": [
                ...
            ]
        },
        "error": {
            ...
        } 
    }
    

Query TikTok public account information
=======================================

With the cURL command below, you can query public TikTok account information by a TikTok handle.

    curl --location --request POST 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
    --header 'Authorization: bearer {{access_token}}' \
    --header 'Content-Type: text/plain' \
    --data-raw '{
        "username": "joe1234567"
    }'
    

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required?** |
| username | string | TikTok user's username | "Joe123" | FALSE |

  

The following example data is returned from the response.

    
    {
        "data": {
            "username": "joe1234567",
            "video_count": 64,
            "avatar_url": "https://my-awesome-avatar",
            "display_name": "joe 1234567",
            "follower_count": 111,
            "likes_count": 4146,
            "bio_description": "joe joe",
            "following_count": 103,
            "is_verified": false
        },
        "error": {
            ...
        }
    }

Frequently Asked Questions
==========================

1. **What data is available as part of the Research** **API****?**

1. More information on the Research API can be found [here](https://developers.tiktok.com/products/research-api/). Once approved for access to the Research API, researchers can access public data on:

1. **Accounts**: This includes user profiles, and other data such as the number of likes of creator's content, followers and following count.
2. **Content**: This includes comments, captions, subtitles, and number of comments, shares, likes, and favorites that a video receives.

3. For more info on the data returned via our APIs, check out the [Research API codebook](https://developers.tiktok.com/doc/research-api-codebook/)

3. **How do I know if I qualify for Research** **API** **access?**

1. Applicants must fulfill the following criteria to qualify for access:

1. Have demonstrable academic experience and expertise in the research area specified in the application
2. Have no conflicts of interest with respect to using the services
3. Be employed by a non-profit academic institution in the U.S. or Europe
4. Be able to provide a clearly defined research proposal
5. Be committed to only using data for non-commercial purposes, as set out in our [Research API Terms of Service](https://www.tiktok.com/legal/page/global/terms-of-service-research-api/en)

5. **How do I apply for Research** **API** **access?**

1. If you meet the eligibility criteria outlined above and have prepared a research proposal, click [here](https://developers.tiktok.com/application/research-api) to apply.

7. **Can I work with a group of researchers to collaborate on a research topic? How do I ensure we all get access to the Research** **API** **in order to collaborate on our approved project?**

1. We now support lab-level access to the Research API. The application form should be submitted by the project's principal researcher. Once the application is approved, the principal researcher can log in and view the approved "Organization" on the TikTok for Developers (TT4D) home page. Here, the principal researcher will have the ability to manage access, including adding and removing collaborators.
2. The principal researcher can add up to 9 collaborators to work together on a research topic. It is preferable that the principal researchers submit the details of all anticipated collaborators during the application process. TikTok will review any collaborators that are invited to join an approved research project prior to granting them access. Further, it is the responsibility of the principal researcher to remove and revoke access to collaborators who are no longer working on the approved research project.
3. If the collaborators are from a different university, an application should be submitted with a list of collaborators for each university.
4. The collaborators need to ensure that they have setup their TT4D account in advance prior to getting an invite.

9. **Where is the Research** **API** **available?**

1. The Research API is currently available to qualifying researchers located in the United States and Europe.

11. **When will the Research** **API** **be available in my country?**

1. TikTok is actively working to expand eligibility to additional regions. Please check [this page](https://developers.tiktok.com/products/research-api/) for updates.

13. **I am a researcher working for a non-profit organization, in civil society, or at an** **NGO****. Can I apply for access?**

1. At present, eligibility is restricted to those employed by not-for-profit academic institutions in the United States, and Europe. We are actively working to expand eligibility globally as well as for the civil society sector. Please check [this page](https://developers.tiktok.com/products/research-api/) for updates.

15. **I am a creator, advertiser, or commercial user. Am I eligible for access to the Research** **API****?**

1. At present, eligibility is restricted to those employed by not-for-profit academic institutions in the United States, and Europe who meet our eligibility criteria. [Click here](https://developers.tiktok.com/) to learn more about API access for non-academic purposes.

17. **What are the daily quota limits? Can I request an increase in the quota limit?**

1. Currently, the daily limit is set at 1000 requests per day, allowing you to obtain up to 100,000 records per day across our APIs. (Video and Comments API can return 100 records per request). The daily quota gets reset at 12 AM UTC.
2. If you believe a quota limit increase is necessary for your research, please email us at Research-API@tiktok.com. We can't grant exceptions, but we're eager to better understand use cases from the research community to evaluate and take your requests into account for the future.

19. **I have a developer account with** **TikTok****. Can I start using the Research** **API****?**

1. Your developer account alone is not sufficient to grant you access to the Research API. In order to access the Research API, you will need to meet our eligibility requirements, submit an application, and be approved for a specific research project.

Research API Usage FAQs
-----------------------

1. **Why does User** **API** **not return responses sometimes even though the user name is accurate?**

1. TikTok's Research API does have some filters. To cite some examples, public data of users under the age of 18 and data from Canada is not returned in the responses

3. **Why is my access token invalid?**

1. Access tokens are set to expire every two hours. If you experience an invalid token error within two hours of generating it, please submit a support ticket to us with your token and client key, and we will investigate the issue.

5. **Why did I receive a response back with code: "scope\_not\_authorized" and message: "The user did not authorize the scope required for completing this request?"**

1. This indicates that you have not yet submitted your Research API application for our review and have not passed the necessary approval evaluations. If you are interested in accessing the Research API, visit our [Research API](https://developers.tiktok.com/products/research-api/) page to learn more, check eligibility requirements and apply for access.

7. **Why is the query video data (view\_count, comment\_count, like\_count, share\_count) significantly inaccurate, often showing lower numbers than what is live at the moment?**

1. The User info API only retrieves data for an individual user, so we use online data. However, the video query API searches for the full dataset, so we use archived data instead of the current online data. New videos take up to 48 hours to be added to the search engine, and statistics such as view count and follower count can take up to 10 days to update.

**Codebook**
============

**Introduction**
----------------

TikTok supports independent research about our platform. Through our Research API, academic researchers from non-profit universities in the U.S. And Europe can apply to study public data about TikTok content and accounts. This document describes the Research API functionality provided to researchers by TikTok.

**Eligibility and Data Access**
-------------------------------

To check your eligibility and determine the process to get access to this data, check [our product page](https://developers.tiktok.com/products/research-api/).

**Content Made Available for Research**
---------------------------------------

### **Videos**

#### **Unit of Analysis**

A public TikTok video posted by a public creator (who is aged 18 and over), who wants to expose his/her videos to all users of TikTok

#### **Scope**

All the videos from TikTok that are:

1. made public by a creator who is aged 18 and over;
2. AND, are posted in the regions of US, Europe and Rest of the World;
3. AND do not belong to Canada.

#### **Details**

1. **Region Code** : This describes the code of the country where the video was created. [Click here](https://developers.tiktok.com/doc/research-api-specs-query-videos/) to learn more about the region codes returned.
2. **User Name** : This is the user name of the creator.
3. **Video Description** : This is the description of the video.
4. **View Count** : This is the total number of views for a video on TikTok.
5. **Comment Count** : This is the total number of comments posted on a video.
6. **Create Time** : This is the time when the video was created.
7. **Video ID** : This is a unique video ID for each video posted on TikTok. This is a number that can be used to reconstruct the URL link to access the video.
8. **Like Count** : The total number of likes on a TikTok video, created by users by clicking the “Heart” icon.
9. **Share Count** : The total number of times a TikTok video has been shared by clicking the "Share" button with the video.

### **Comments**

#### **Unit of Analysis**

A comment OR a reply to a comment posted for a public video on TikTok.

#### **Scope**

The information provided here includes text extracted from comments and a serial number (i.e. comment IDs) that help identify original comments posted on a video and any replies to comments. To protect the privacy of our users, other information is removed.

#### **Details**

1. **Create Time** : This is the time when the comment was posted on a video.
2. **ID** : This is the unique comment ID for a comment posted on a video.
3. **Like Count** : The total number of likes for a comment under a video, created by users by clicking the “Heart” icon.
4. **Parent Comment ID** : This is the unique ID of the parent comment when the user responds to another user's comment. If the comment was directly entered for a video, this ID is the same as the Video ID.
5. **Text** : This is the actual text of the comment entered on a video. To protect the privacy of our users, other information is removed.
6. **Video\_ID** : This is the video ID for which the comment was entered.

### **Users**

#### **Unit of Analysis**

User information of all TikTok users that have set their account to public and are aged 18 and over.

#### **Scope**

The public details of a public user who is aged 18 and over can be accessed via this particular API.

#### **Details**

1. **Following Count** : This is the number of people that a public user follows.
2. **Likes Count** : This is the total number of likes accumulated by the user.
3. **Video Count** : This is the total number of videos that the user has posted on his/her TikTok account.
4. **Bio Description** : This is the description in the bio of the user. If the user does not have a description, this will be returned blank.
5. **Display Name** : This is the user's display name that is found under the user name.
6. **Follower Count** : This is the total number of followers that follow the user.
7. **Avatar****URL** : This is the URL of the user's profile picture.
8. **Is Verified** : This returns the information on whether the user has been verified. All verified users will have "blue tick" next to their user name. If the user has a blue tick, this variable will return a "true" in the response.