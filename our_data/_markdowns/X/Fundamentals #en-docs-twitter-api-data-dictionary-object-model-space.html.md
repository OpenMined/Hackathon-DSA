
Space object | Docs | Twitter Developer Platform 

Space object

Space
-----

Spaces allow expression and interaction via live audio conversations. The Space data dictionary contains relevant metadata about a Space; all the details are updated in real time.

User objects can found and expanded in the user resource. These objects are available for expansion by adding at least one of host\_ids, creator\_id, speaker\_ids, mentioned\_user\_ids to the expansions query parameter.

Unlike Tweets, Spaces are ephemeral and become unavailable after they end or when they are canceled by their creator. When your app handles Spaces data, you are responsible for returning the most up-to-date information, and must remove data that is no longer available from the platform. The Spaces lookup endpoints can help you ensure you respect the users’ expectations and intent.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of the requested Space.
`"id": "1zqKVXPQhvZJB"` | Uniquely identify a Space returned in the response. |
| state (default) | string | Indicates if the Space has started or will start in the future, or if it has ended.
`"state": "live"`
 | Filter live or scheduled Spaces. |
| created\_at | date (ISO 8601) | Creation time of this Space.
`"created_at": "2021-07-04T23:12:08.000Z"` | Understand when a Space was first created and sort Spaces by creation time.  |
| ended\_at | date (ISO 8601) | Time when the Space was ended. Only available for ended Spaces. 
`"ended_at": "2021-07-04T00:11:44.000Z"` | Understand when a live Space ended in order to comput its runtime duration.  |
| host\_ids | array | The unique identifier of the users who are hosting this Space.
`"host_ids": [`
`"2244994945",
    "6253282"
 ]` | Expand User objects, understand engagement. |
| lang | string | Language of the Space, if detected by Twitter. Returned as a BCP47 language tag.
`"lang": "en"` | Classify Spaces by inferred language. |
| is\_ticketed | boolean | Indicates is this is a ticketed Space.
`"is_ticketed": false`
 | Create user experiences to highlight content of interest. |
| invited\_user\_ids | array | The list of user IDs that were invited to join as speakers. Usually, users in this list are invited to speak via the Invite user option.
`"mentioned_user_ids": [
   "2244994945",
    "6253282"
 ]` | Expand User objects, understand engagement. |
| participant\_count | integer | The current number of users in the Space, including Hosts and Speakers.
`"participant_count": 420`
  | Understand engagement, and create reports and visualizations for creators. |
| subscriber\_count | integer | The number of people who set a reminder to a Space.
`"subscriber_count": 36` | Understand how many people are interested in attending the event. This metric is available for scheduled Spaces and Spaces scheduled in the past that are currently live. |
| scheduled\_start | date (ISO 8601) | Indicates the start time of a scheduled Space, as set by the creator of the Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.
`"scheduled_start": "2021-07-14T08:00:00.000Z"` | Integrate with calendar notifications, filter and sort Spaces by time. |
| speaker\_ids | array | The list of users who were speaking at any point during the Space. This list contains all the users in **invited\_user\_ids** in addition to any user who requested to speak and was allowed via the Add speaker option.
`"speaker_ids": [
   "2244994945",
    "6253282"
 ]` | Expand User objects, understand engagement. |
| started\_at | date (ISO 8601) | Indicates the actual start time of a Space.
`"started_at": "2021-07-14T08:00:12.000Z"`
  | Determine start time of a Space. |
| title | string | The title of the Space as specified by the creator.
`"title": "Say hello to the Space data object!"` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| topic\_ids | array | A list of IDs of the topics selected by the creator of the Space.
`"topic_ids": [
   "2244994945",
    "6253282"
 ]` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| updated\_at | date (ISO 8601) | Specifies the date and time of the last update to any of the Space's metadata, such as its title or scheduled time.
`"updated_at": "2021-07-11T14:44:44.000Z"` | Keep information up to date. |

### 
Retrieving a Space object

#### Sample Request

In the following request, we are requesting fields for the Space on the Spaces lookup endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

```
      curl "https://api.twitter.com/2/spaces/1DXxyRYNejbKM?space.fields=created_at,creator_id,created_athost_ids,lang,is_ticketed,invited_user_ids,participant_count,scheduled_start,speaker_ids,started_at,state,title,updated_at&expansions=creator_id,host_ids,invited_user_ids,speaker_ids" --header "Authorization: Bearer $BEARER_TOKEN"
```

Code copied to clipboard

 **Sample Response**

```
      {
    "data": {
        "id": "1zqKVXPQhvZJB",
        "state": "live",
        "created_at": "2021-07-04T23:12:08.000Z",
        "host_ids": [
          "2244994945",
          "6253282"
        ],
        "lang": "en",
        "is_ticketed": false,
        "invited_user_ids": [
          "2244994945",
          "6253282"
        ],
        "participant_count": 420,
        "scheduled_start": "2021-07-14T08:00:00.000Z",
        "speaker_ids": [
          "2244994945",
          "6253282"
        ],        
        "started_at": "2021-07-14T08:00:12.000Z",
        "title": "Say hello to the Space data object!",
        "updated_at": "2021-07-11T14:44:44.000Z"
    },
    "includes": {
        "users": [
            {
                "id": "2244994945",
                "name": "Twitter Dev",
                "username": "TwitterDev"
           },
           {
            "id": "6253282",
            "name": "Twitter API",
            "username": "TwitterAPI"
          }
    ]
    }
}
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