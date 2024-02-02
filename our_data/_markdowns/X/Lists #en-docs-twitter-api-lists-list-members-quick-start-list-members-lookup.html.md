
List members lookup quick start guide | Docs | Twitter Developer Platform 

List members lookup

**Please note:** This guide assumes you have completed the prerequisites from the quick start overview.

### Steps to build a List members lookup request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List members”, and then choose "Members lookup".  

#### Step two: Identify and specify which List you would like to retrieve members from

You must specify a List that you would like to receive members from. You can find the List ID by navigating to twitter.com and clicking on a List and then looking in the URL. For example, the following URL's List ID is 84839422.

https://twitter.com/i/lists/84839422

The target ID can be any valid List ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Be sure not to include any spaces before or after any ID.

|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | 84839422 (List ID) |

#### Step three: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default user object fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the field and/or expansion parameters.

For this exercise, we will request three additional sets of fields from different objects:

* The additional user.created\_at field in the primary user objects.
* The full Tweet object using the expansion parameter.
* The additional tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at |  `created_at` |
| expansions | pinned\_tweet\_id |  `includes.tweets.id, 
 includes.tweets.text` |
| tweet.fields | created\_at |  `includes.tweets.created_at` |

You should now see a similar URL next to the “Send” button:

```
      https://api.twitter.com/2/lists/84839422/members?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at
```

Code copied to clipboard

Step four: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

```
      {
  "data": [
    {
      "pinned_tweet_id": "1353789891348475905",
      "id": "1319036828964454402",
      "created_at": "2020-10-21T22:04:47.000Z",
      "name": "Birdwatch",
      "username": "birdwatch"
    },
    {
      "id": "1244731491088809984",
      "created_at": "2020-03-30T21:02:29.000Z",
      "name": "Twitter Thailand",
      "username": "TwitterThailand"
    },
    {
      "id": "1194267639100723200",
      "created_at": "2019-11-12T14:56:22.000Z",
      "name": "Twitter Retweets",
      "username": "TwitterRetweets"
    },
    {
      "id": "1168976680867762177",
      "created_at": "2019-09-03T19:59:02.000Z",
      "name": "Twitter Able",
      "username": "TwitterAble"
    },
    {
      "pinned_tweet_id": "1451239134798942208",
      "id": "1065249714214457345",
      "created_at": "2018-11-21T14:24:58.000Z",
      "name": "Spaces",
      "username": "TwitterSpaces"
    },
    {
      "id": "1049385226424786944",
      "created_at": "2018-10-08T19:45:09.000Z",
      "name": "Twitter Miami",
      "username": "TwitterMiami"
    },
    {
      "pinned_tweet_id": "1438533888498876420",
      "id": "1004367799588880384",
      "created_at": "2018-06-06T14:21:58.000Z",
      "name": "Twitter México",
      "username": "TwitterMexico"
    },
    {
      "pinned_tweet_id": "1370178223846297602",
      "id": "773578328498372608",
      "created_at": "2016-09-07T17:47:00.000Z",
      "name": "Twitter Together",
      "username": "TwitterTogether"
    },
    {
      "id": "766296039036948480",
      "created_at": "2016-08-18T15:29:47.000Z",
      "name": "Moments MENA",
      "username": "momentsmena"
    },
    {
      "id": "738118487122419712",
      "created_at": "2016-06-01T21:22:15.000Z",
      "name": "Twitter Asians",
      "username": "TwitterAsians"
    }
  ],
  "includes": {
    "tweets": [
      {
        "created_at": "2021-01-25T19:40:36.000Z",
        "id": "1353789891348475905",
        "text": "Want to help build a new community-driven approach to tackling misleading information? Join us — sign up for Birdwatch! \n\nhttps://t.co/FSsqNznPy1"
      },
      {
        "created_at": "2021-10-21T17:29:07.000Z",
        "id": "1451239134798942208",
        "text": "the time has arrived -- we’re now rolling out the ability for everyone on iOS and Android to host a Space\n\nif this is your first time hosting, welcome! here’s a refresher on how https://t.co/cLH8z0bocy"
      },
      {
        "created_at": "2021-09-16T16:03:00.000Z",
        "id": "1438533888498876420",
        "text": "Algunos le dicen amor, pero yo le digo:\n\n‌    ∧＿∧　 \n（｡･ω･｡)つ━☆・*\n⊂     　ノ 　　　・゜+.\n　しーＪ　　　°。+ *´¨)\n　　　　　 　　　☆ RECALENTADO ☆ \n#VivaMéxico"
      },
      {
        "created_at": "2021-03-12T01:01:59.000Z",
        "id": "1370178223846297602",
        "text": "Still, We Fly\n\n... because no matter how many times 2020 tried to knock us down, we got back up and responded with empathy, agility, innovation, and leadership.\n\nRead more in our 2020 Inclusion &amp; Diversity Annual Report #UntilWeAllBelong"
      }
    ]
  },
  "meta": {
    "result_count": 10,
    "next_token": "5349804505549807616"
  }
}
```

Code copied to clipboard

Next steps
----------

Customize your request using the API Reference

Reach out to the community for help

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