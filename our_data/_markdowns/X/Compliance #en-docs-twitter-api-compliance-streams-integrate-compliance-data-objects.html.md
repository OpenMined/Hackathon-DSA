
Compliance Data Objects | Docs | Twitter Developer Platform 

Compliance Data Objects

Possible types of compliance events will include Tweet events and User events, for which there are multiple types described below.    

Please note:

* Read more about Tweet visibility here and our developer policy around deleted Tweets here.
* The Tweet Compliance stream includes events triggered by Tweets getting edited. See the 'tweet\_edit' example event below.
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete, user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.  

Payload examples
----------------

See the payload examples below for each compliance event described in the table above.

#### Tweet delete

```
      {
	"data": {
		"delete": {
			"tweet": {
				"id": "601430178305220608",
				"author_id": "3198576760"
			},
			"event_at": "2022-12-23T12:34:56.789Z"
		}
	}
}
```

When a deleted Tweet has been Quote Tweeted, there will be an additional Tweet 'delete' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### Tweet edit

```
      {
	"data": {
		"tweet_edit": {
			"tweet": {
				"id": "1567233994734948354"
			},
			"initial_tweet_id": "1567233844205453313",
			"edit_tweet_ids": [
				"1567233844205453313",
				"1567233994734948354"
			],
			"event_at": "2022-09-06T19:31:16.801Z"
		}
	}
}
```

Code copied to clipboard

#### Tweet withheld

```
      {
	"data": {
		"withheld": {
			"tweet": {
				"id": "601430178305220608",
				"author_id": "3198576760"
			},
			"withheld_in_countries": [
				"XY"
			],
			"event_at": "2022-12-23T12:34:56.789Z"
		}
	}
}
```

When a withheld Tweet has been Quote Tweeted, there will be an additional Tweet 'withheld' event with a "quote\_tweet\_id" attribute for each Quote Tweet. 

#### 

#### Tweet Drop

```
      {
	"data": {
		"drop": {
			"tweet": {
				"id": "601430178305220600",
				"author_id": "3198576760"
			},
			"event_at": "2022-12-23T12:34:56.789Z"
		}
	}
}
```

#### Tweet Undrop

```
      {
  "data": 
     {
       "undrop": {
          "tweet": {
             "id": "601430178305220600",
             "author_id": "3198576760"
           },
         "event_at": "2022-12-23T12:34:56.789Z"
        }
     }
}

```

#### User scrub geo

```
      {
   "data": 
    {
      "scrub_geo": {
        "user": {
          "id": "1375036644"
        },
      "up_to_tweet_id": "411552403083628544",
      "event_at": "2022-06-27T23:49:41.839+00:00"
      }
    }
}

```

#### User delete

```
      {
	"data": {
		"user_delete": {
			"user": {
				"id": "1375036644"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User undelete

```
      {
	"data": {
		"user_undelete": {
			"user": {
				"id": "1375036644"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User withheld

```
      {
	"data": {
		"user_withheld": {
			"user": {
				"id": "1375036644"
			},
			"withheld_in_countries": [
				"XY"
			],
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User protect

```
      {
	"data": {
		"user_protect": {
			"user": {
				"id": "3182003550"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User unprotect

```
      {
	"data": {
		"user_unprotect": {
			"user": {
				"id": "3182003550"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User suspend

```
      {
	"data": {
		"user_suspend": {
			"user": {
				"id": "1375036644"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

#### User unsuspend

```
      {
	"data": {
		"user_unsuspend": {
			"user": {
				"id": "1375036644"
			},
			"event_at": "2022-06-27T23:49:41.839+00:00"
		}
	}
}
```

**User profile modification**

```
      {
  "data": {
    "user_profile_modification": {
      "user": {
        "id": "906948460078698496"
      },
      "event_at": "2022-07-12T19:47:59.442Z",
      "profile_field": "profile.description",
      "new_value": "Home of the @SnowbotDev chatbot."
    }
  }
}
```

Code copied to clipboard

The "profile\_field" attribute indicates what in the User profile changed, and can contain the following values: 

* "profile.name"
* "profile.location"
* "profile.description"
* "profile.url"
* "profile.profileBanner"
* "profile.profileBanner.url"
* "profile.profileImage"
* "profile.profileImage.url"

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