
GET /2/users/compliance/stream | Docs | Twitter Developer Platform 

GET /2/users/compliance/stream

 GET /2/users/compliance/stream
==============================
Connect to one of four partitions of the User compliance stream. 
Build request with API Explorer ❯### Endpoint URL
`https://api.twitter.com/2/users/compliance/stream`  
### Authentication and rate limits

|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 100 requests per 15-minute window shared among all users of your app |
### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `partition` Required  | number | Must be set to 1, 2, 3 or 4. User compliance events are split across 4 partitions, so 4 separate streams are needed to receive all events. |
| `backfill_minutes` Optional  | number | By passing this parameter, you can recover up to five minutes worth of data that you might have missed during a disconnection. The backfilled events will automatically flow through a reconnected stream, with older events generally being delivered before any newer events. You must include a whole number between 1 and 5 as the value to this parameter. nThis feature will deliver all events that published during the timeframe selected, meaning that if you were disconnected for 90 seconds, and you requested two minutes of backfill, you will receive 30 seconds worth of duplicate events. Due to this, you should make sure your system is tolerant of duplicate data. |

### Example code with offical SDKs

* TypeScript
* Java

 TypeScript

 Java

```
      (async () => {
  try {
    const userComplianceStream = await twitterClient.users.complianceStream();
    console.dir(userComplianceStream, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

```

```
      try {
    InputStream result = apiInstance.users().complianceStream(null, null, null, null, null, null, null);
    try{
        JSON json = new JSON();
        Type localVarReturnType = new TypeToken<StreamingUserCompliance>(){}.getType();
        BufferedReader reader = new BufferedReader(new InputStreamReader(result));
        String line = reader.readLine();
        while (line != null) {
          System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());
          line = reader.readLine();
        }
    } catch (Exception e) {
      e.printStackTrace();
      System.out.println(e);
    }
} catch (ApiException e) {
    System.err.println("Exception when calling TweetsApi#usersComplianceStream");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

```

### Example responses

* Successful response

 Successful response

```
      {
  "data": {
    "user_protect": {
      "user": {
        "id": "906948460078698496"
      },
      "event_at": "2022-07-01T21:44:57.895Z"
    }
  }
}
```

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `user_delete` | string | A delete user event. |
| `user_undelete` | string | A undelete user event. |
| `user_withheld` | string | A withheld user event. |
| `user_protect` | string | A protect user event. |
| `user_unprotect` | string | A unprotect user event. |
| `user_suspend` | string | A suspend user event. |
| `user_unsuspend` | string | A unsuspend user event. |
| `scrub_geo` | string | A geo scrub user event. |
| `user_profile_modification` | string | A modified user profile event. |
| `id` | string | The ID of the user triggering a compliance event. |
| `event_at` | date (ISO 8601) | Time of when event happended. |
| `withheld_in_countries` | string | Country where user is withheld. |
| `up_to_tweet_id` | string | Provided when a user removes their geo metadata. |
| `profile_field` | string | Indicates what Profile attribute was updated. |

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