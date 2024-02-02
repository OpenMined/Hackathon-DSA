::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to one of
the timelines endpoints with a set of specified fields using
[Postman](/en/docs/tools-and-libraries/using-postman) .

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
GitHub repository.\
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
To complete this guide, you will need to have a set of [keys and
tokens](/en/docs/authentication) to authenticate your request. You can
generate these keys and tokens by following these steps:

-   [Sign up for a developer account](/en/apply-for-access) and receive
    approval.
-   Create a [Project](/en/docs/projects) and an associated [developer
    App](/en/docs/apps) in the developer portal.
-   Navigate to your App\'s "Keys and tokens" page to generate the
    required credentials. Make sure to save all credentials in a secure
    location.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
*For this example, we will make a request to the user Tweet timeline by
ID endpoint, but you can apply the learnings from this quick start to
user mention timelines requests as well.*

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you
can use to make a request to this endpoint, but we are going to use the
Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please
click on the following button:
:::
:::

::: b03-button-v3
[](https://t.co/twitter-api-postman){.chirp-btn .twtr-spacing--mb-500
.chirp-btn--primary .chirp-btn--icon .chirp-btn--icon-end
.twtr-scribe-clicks}

::: chirp-btn__icon
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/m1_vnext/carat.svg){.chirp-btn__icon--img}
:::

Add Twitter API v2 to Postman
:::

::: c01-rich-text-editor
::: is-table-default
\
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the \"T imelines\" folder and find the \"Reverse chronological home
timeline\" request.

####  Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so with this endpoint, you must authenticate
your request with either [OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
, or [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
authentication methods.

You must add your keys and tokens to Postman. You can do this by
selecting the environment named "Twitter API v2" in the top-right corner
of Postman and adding your keys and tokens to the \"initial value\" and
\"current value\" fields (by clicking the eye icon next to the
environment dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.

#### Step three: Identify and specify which user from which you would like to retrieve their home timeline for

You must specify a user you would like to retrieve recent Tweets for
within the request. In this example, we will be passing a single user
ID.

User IDs are simply the numerical value that represents an account
handle that you can find within an account\'s profile URL. For example,
the following account's username is ` TwitterDev ` .

` https://twitter.com/TwitterDev `

To convert this username to the user ID, you will have to use the [users
lookup endpoint](/en/docs/twitter-api/users/lookup/quick-start) with the
username and find the numerical user ID in the payload. In the case of
\@TwitterDev, the user ID is [ 2244994945 ]{.code-inline} .

In Postman, navigate to the \"Params\" tab and enter this user ID into
the \"Value\" column of the [ id ]{.code-inline} parameter.

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default [Tweet
object](/content/developer-twitter/en/docs/twitter-api/object-reference/tweet)
fields in your response: [ id ]{.code-inline} , [ text ]{.code-inline} ,
and [ edit_history_tweet_ids ]{.code-inline} .

If you would like to receive additional fields, you will have to specify
those fields in your request with the
[field](/content/developer-twitter/en/docs/twitter-api/fields) and/or
[expansion](/content/developer-twitter/en/docs/twitter-api/expansions)
parameters.

For this exercise, we will request three additional different sets of
fields from different objects:

1.  The additional [ tweet.created_at ]{.code-inline} field in the
    primary user objects.\
2.  The associated authors' user object's default fields for the
    returned Tweets: [ id ]{.code-inline} , [ name ]{.code-inline} , and
    [ username ]{.code-inline}
3.  The additional [ user.created_at ]{.code-inline} field in the
    associated user objects.\

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:\

  ------------------------------- --------------------- -------------------------------------------------------------------------------
  **Key**                         **Value**             **Returned fields**
  ` tweet.fields `                ` created_at `        ` tweets.created_at `
  ` expansions `                  ` author_id `         ` includes.users.id ` , ` includes.users.name ` , ` includes.users.username `
  ` user.fields `                 ` created_at `        ` includes.users.created_at `
  [ max_results ]{.code-inline}   [ 5 ]{.code-inline}   
  ------------------------------- --------------------- -------------------------------------------------------------------------------

\
You should now see the following URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://api.twitter.com/2/users/:id/timelines/reverse_chronological?tweet.fields=created_at&expansions=author_id&user.fields=created_at&max_results=5
    
```
:::
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:**

In Postman, the path parameter [ :id ]{.code-inline} in the URL field
will **not** automatically update to the value that you enter into the
` id ` params field, which is why the above URL includes ` :id ` and not
[ 2244994945 ]{.code-inline} .
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, hit the \"Send\" button and you will
receive the following response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "created_at": "2022-05-12T17:00:00.000Z",
            "text": "Today marks the launch of Devs in the Details, a technical video series made for developers by developers building with the Twitter API.  🚀\n\nIn this premiere episode, @jessicagarson walks us through how she built @FactualCat #WelcomeToOurTechTalk\n⬇️\n\nhttps://t.co/nGa8JTQVBJ",
            "author_id": "2244994945",
            "id": "1524796546306478083"
        },
        {
            "created_at": "2022-05-11T19:16:40.000Z",
            "text": "📢 Join @jessicagarson @alanbenlee and @i_am_daniele tomorrow, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots https://t.co/sQ2bIO1fz6",
            "author_id": "2244994945",
            "id": "1524468552404668416"
        },
        {
            "created_at": "2022-05-09T20:12:01.000Z",
            "text": "Do you make bots with the Twitter API? 🤖\n\nJoin @jessicagarson @alanbenlee and @iamdaniele on Thursday, May 12  | 5:30 ET / 2:30pm PT as they discuss the future of bots and answer any questions you might have. 🎙📆⬇️\n\nhttps://t.co/2uVt7hCcdG",
            "author_id": "2244994945",
            "id": "1523757705436958720"
        },
        {
            "created_at": "2022-05-06T18:19:54.000Z",
            "text": "If you’d like to apply, or would like to nominate someone else for the program, please feel free to fill out the following form:\n\nhttps://t.co/LUuWj24HLu",
            "author_id": "2244994945",
            "id": "1522642324781633536"
        },
        {
            "created_at": "2022-05-06T18:19:53.000Z",
            "text": "We’ve gone into more detail on each Insider in our forum post. \n\nJoin us in congratulating the new additions! 🥳\n\nhttps://t.co/0r5maYEjPJ",
            "author_id": "2244994945",
            "id": "1522642323535847424"
        }
    ],
    "includes": {
        "users": [
            {
                "created_at": "2013-12-14T04:35:55.000Z",
                "name": "Twitter Dev",
                "username": "TwitterDev",
                "id": "2244994945"
            }
        ]
    },
    "meta": {
        "result_count": 5,
        "newest_id": "1524796546306478083",
        "oldest_id": "1522642323535847424",
        "next_token": "7140dibdnow9c7btw421dyz6jism75z99gyxd8egarsc4"
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the previous response, you will find a [ meta ]{.code-inline} data
object at the bottom that includes the following fields:

-   [ oldest_id ]{.code-inline}
-   [ newest_id ]{.code-inline}
-   [ results_count ]{.code-inline}
-   [ next_token ]{.code-inline}
-   [ previous_token ]{.code-inline}

In step four, we passed a [ max_results ]{.code-inline} value of 5,
meaning that each page will only include up to five results. To access
the additional pages of data, we will be taking the value of the [
next_token ]{.code-inline} field from our last results and adding that
string as the value of the [ pagination_token ]{.code-inline} parameter
on the Postman params page, keeping everything else constant.

  ---------------------- -------------------------------------------------
  **Key**                **Value**
  ` pagination_token `   [ t3buvdr5pujq9g7bggsnf3ep2ha28 ]{.code-inline}
  ---------------------- -------------------------------------------------

Once this is all set up, you can click \"Send\" again and you should
receive the next page of results.

We have put together a guide on
[pagination](/en/docs/twitter-api/pagination) to further explain this
concept.
:::
:::
:::
