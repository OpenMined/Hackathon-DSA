::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:**

If you are moving an app between any
[Projects](https://developer.twitter.com/en/docs/projects/overview) ,
any rules you have created on the filtered stream endpoint will be
reset. You will need to recreate these rules once it is associated with
its new Project. Prior to moving an app that has rules in place on the
filtered stream endpoint, you should save a local copy of all rules
using the [GET /2/tweets/search/stream/rules
endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules)
.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The filtered stream endpoints deliver filtered Tweets to you in
real-time that match on a set of rules that are applied to the stream.
Rules are made up of operators that are used to match on a variety of
Tweet attributes.

Multiple rules can be applied to a stream using the [POST
/tweets/search/stream/rules](/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules)
endpoint. Once you've added rules and connect to your stream using the
[GET
/tweets/search/stream](/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream)
endpoint, only those Tweets that match your rules will be delivered in
real-time through a persistent streaming connection. You do not need to
disconnect from your stream to add or remove rules.

To learn more about how to create high-quality rules, visit the
following tutorial:\
[Building high-quality filters for getting Twitter
data](/content/developer-twitter/en/docs/tutorials/building-high-quality-filters)\

### Table of contents

### Building a rule []{#build} 

#### Rule limitations []{#limits}

Limits on the number of rules will depend on which [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
is applied to your [Project](/en/docs/projects) .

You can see how these limits apply via the [filtered stream
introduction](/en/docs/twitter-api/tweets/filtered-stream) page.\

#### Operator availability []{#availability}

While most operators are available to any developer, there are several
that are reserved for those that have been approved for Basic, Pro, or
Enterprise access levels. We list which [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
each operator is available to in the [list of operators](#list) table
using the following labels:

-   **Essential operators:** Available when using any access level.
-   **Elevated operators:** Available when using a Project with Pro, or
    Enterprise access.\

#### Operator types: standalone and conjunction-required []{#types}

**Standalone operators** can be used alone or together with any other
operators (including those that require conjunction).

For example, the following rule will work because it uses the [ #hashtag
]{.code-inline} operator, which is standalone:

[ #twitterapiv2 ]{.code-inline}

**Conjunction required** operators cannot be used by themselves in a
rule; they can only be used when at least one standalone operator is
included in the rule. This is because using these operators alone would
be far too general, and would match on an extremely high volume of
Tweets.\

For example, the following rules are not supported since they contain
only conjunction required operators:

[ has:media ]{.code-inline}\
[ has:links OR is:retweet ]{.code-inline}

If we add in a standalone operator, such as the phrase [ \"twitter
data\" ]{.code-inline} , the rule would then work properly.

[ \"twitter data\" has:mentions (has:media OR has:links) ]{.code-inline}

####  Boolean operators and grouping []{#boolean}

If you would like to string together multiple operators in a single
rule, you have the following tools at your disposal:

  ----------------------------------- -----------------------------------
  **AND logic**                       Successive operators **with a space
                                      between them** will result in
                                      boolean \"AND\" logic, meaning that
                                      Tweets will match only if both
                                      conditions are met. For example, [
                                      snow day #NoSchool ]{.code-inline}
                                      will match Tweets containing the
                                      terms snow and day and the hashtag
                                      #NoSchool.

  **OR logic**                        Successive operators with OR
                                      between them will result in OR
                                      logic, meaning that Tweets will
                                      match if either condition is met.
                                      For example, specifying [ grumpy OR
                                      cat OR #meme ]{.code-inline} will
                                      match any Tweets containing at
                                      least the terms grumpy or cat, or
                                      the hashtag #meme.

  **NOT logic, negation**             Prepend a dash (-) to a keyword (or
                                      any operator) to negate it (NOT).
                                      For example, [ cat #meme -grumpy
                                      ]{.code-inline} will match Tweets
                                      containing the hashtag #meme and
                                      the term cat, but only if they do
                                      not contain the term grumpy. One
                                      common rule clause is [ -is:retweet
                                      ]{.code-inline} , which will not
                                      match on Retweets, thus matching
                                      only on original Tweets, Quote
                                      Tweets, and replies. All operators
                                      can be negated, but negated
                                      operators cannot be used alone.\

  **Grouping**                        You can use parentheses to group
                                      operators together. For example, [
                                      (grumpy cat) OR (#meme has:images)
                                      ]{.code-inline} will return either
                                      Tweets containing the terms grumpy
                                      and cat, or Tweets with images
                                      containing the hashtag #meme. Note
                                      that ANDs are applied first, then
                                      ORs are applied.\
  ----------------------------------- -----------------------------------
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**A note on negations**

All operators can be negated except for [ sample: ]{.code-inline} , and
[ -is:nullcast ]{.code-inline} must always be negated. Negated operators
cannot be used alone.

Do not negate a set of operators grouped together in a set of
parentheses. Instead, negate each individual operator.

For example, instead of using [ skiing -(snow OR day OR noschool)
]{.code-inline} , we suggest that you use [ skiing -snow -day -noschool
]{.code-inline} .
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
When combining AND and OR functionality, the following order of
operations will dictate how your rule is evaluated.

1.  Operators connected by AND logic are combined first
2.  Then, operators connected with OR logic are applied

For example:

-   [ apple OR iphone ipad ]{.code-inline} would be evaluated as [ apple
    OR (iphone ipad) ]{.code-inline}
-   [ ipad iphone OR android ]{.code-inline} would be evaluated as [
    (iphone ipad) OR android ]{.code-inline}

To eliminate uncertainty and ensure that your rule is evaluated as
intended, group terms together with parentheses where appropriate.

For example:

-   [ (apple OR iphone) ipad ]{.code-inline}
-   [ iphone (ipad OR android)\
    ]{.code-inline}

#### Punctuation, diacritics, and case sensitivity []{#punctuation}

If you specify a keyword or hashtag rule with character accents or
diacritics, it will match Tweets that contain the exact word with proper
accents or diacritics, but not those that have the proper letters, but
without the accent or diacritic.

For example, rules with the keyword [ diacrítica ]{.code-inline} or
hashtag [ #cumpleaños ]{.code-inline} will match Tweets that contain
*diacrítica* or *#cumpleaños* because they include the accent or
diacritic. However, these rules will not match Tweets that contain
*Diacritica* or *#cumpleanos* without the tilde í or eñe.

Characters with accents or diacritics are treated the same as normal
characters and are not treated as word boundaries. For example, a rule
with the keyword *cumpleaños* would only match Tweets containing the
word *cumpleaños* and would not match Tweets containing *cumplea* ,
*cumplean* , or *os* .

All operators are evaluated in a case-insensitive manner. For example,
the rule cat will match all of the following: *cat* , *CAT* , *Cat* .
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
The [Search Tweets](/en/docs/twitter-api/tweets/search) matching
behavior acts differently from filtered stream. When [building a Search
Tweets query](/en/docs/twitter-api/tweets/search/integrate/build-a-rule)
, know that keywords and hashtags that include accents or diacritics
will match both the term with the accents and diacritics, as well as
with normal characters.

For example, Search Tweets queries that include a keyword [ Diacrítica
]{.code-inline} or hashtag [ #cumpleaños ]{.code-inline} will match both
*Diacrítica* and *#cumpleaños* , as well as *Diacritica* or
*#cumpleanos* without the tilde í or eñe.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
When you start to build your rule, it is important to keep a few things
in mind.

-   Using broad, standalone operators for your rule such as a single
    keyword or #hashtag is generally not recommended since it will
    likely match on a massive volume of Tweets. Creating a more robust
    rule will result in a more specific set of matching Tweets, and will
    hopefully reduce the amount of noise in the payload that you will
    need to sift through to find valuable insights.
    -   For example, if your rule was just the keyword [ happy
        ]{.code-inline} you will likely get anywhere from 200,000 -
        300,000 Tweets per day.
    -   Adding more conditional operators narrows your search results,
        for example [ (happy OR happiness) place_country:GB -birthday
        -is:retweet ]{.code-inline}
-   Writing efficient rules is also beneficial for staying within the
    characters rule length restriction. The character count includes the
    entire rule string including spaces and operators.
    -   For example, the following rule is 59 characters long: [ (happy
        OR happiness) place_country:GB -birthday -is:retweet\
        ]{.code-inline}

####  Quote Tweet matching behavior []{#quote-tweets}

When using the filtered stream endpoints, operators will match on both
the content from the original Tweet that was quoted, as well as the
content included in the Quote Tweet.

However, please note that the [Search
Tweets](/en/docs/twitter-api/tweets/search) endpoints will not match on
the content from the original Tweet that was quoted, but will match on
the Quote Tweet\'s content.

#### Iteratively building a rule []{#iterative}

##### Test your rule early and often

Getting a rule to return the \"right\" results the first time is rare.
There is so much on Twitter that may or may not be obvious at first and
the rule syntax described above may be hard to match to your desired
search. As you build a rule, it is important for you to periodically
test it out with the stream endpoint to see what data it returns. You
can also test with one of the [Search
Tweet](/en/docs/twitter-api/tweets/search) endpoints, assuming the
operators that you are using are also available via that endpoint.

For this section, we are going to start with the following rule and
adjust it based on the results that we receive during our test:

[ happy OR happiness ]{.code-inline}

##### Use results to narrow the rule

As you test the rule, you should scan the returned Tweets to see if they
include the data that you are expecting and hoping to receive. Starting
with a broad rule and a superset of Tweet matches allows you to review
the result and narrow the rule to filter out undesired results.

When we tested the example rule, we noticed that we were getting Tweets
in a variety of different languages. In this situation, we want to only
receive Tweets that are in english, so we're going to add the [ lang:
]{.code-inline} operator:

[ (happy OR happiness) lang:en ]{.code-inline}

The test delivered a number of Tweets wishing people a happy birthday,
so we are going to add [ -birthday ]{.code-inline} as a negated keyword
operator. We also want to only receive original Tweets, so we've added
the negated [ -is:retweet ]{.code-inline} operator:

[ (happy OR happiness) lang:en -birthday -is:retweet ]{.code-inline}

##### Adjust for inclusion where needed

If you notice that you are not receiving data that you expect and know
that there are existing Tweets that should return, you may need to
broaden your rule by removing operators that may be filtering out the
desired data.

For our example, we noticed that there were other Tweets in our personal
timeline that expressed the emotion that we are looking for and weren't
included in the test results. To ensure we have greater coverage, we are
going to add the keywords, [ excited ]{.code-inline} and [ elated
]{.code-inline} .

[ (happy OR happiness OR excited OR elated) lang:en -birthday
-is:retweet ]{.code-inline}

##### Adjust for popular trends/bursts over the time period

Trends come and go on Twitter quickly. Maintaining your rule should be
an active process. If you plan to use a single rule for a while, we
suggest that you periodically check in on the data that you are
receiving to see if you need to make any adjustments.

In our example, we notice that we started to receive some Tweets that
are wishing people a "happy holidays". Since we don't want these Tweets
included in our results, we are going to add a negated [ -holidays
]{.code-inline} keyword.

[ (happy OR happiness OR excited OR elated) lang:en -birthday
-is:retweet -holidays ]{.code-inline}

#### []{#adding-removing} Adding and removing rules

You will be using the [POST
/2/tweets/search/stream/rules](/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules)
endpoint when both adding and deleting rules from your stream.

To add one or more rule to your stream, submit an [ add ]{.code-inline}
JSON body with an array that contains the value parameter including the
rule, and the optional [ tag ]{.code-inline} parameter including
free-form text that you can use to [identify which returned Tweets match
this
rule](/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets)
.

For example, if you were trying to add a set of rules to your stream,
your cURL command might look like this:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer $ACCESS_TOKEN" -d \
'{
  "add": [
    {"value": "cat has:media", "tag": "cats with media"},
    {"value": "cat has:media -grumpy", "tag": "happy cats with media"},
    {"value": "meme", "tag": "funny things"},
    {"value": "meme has:images"}
  ]
}'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Similarly, to remove one or more rules from your stream, submit a [
delete ]{.code-inline} JSON body with the array of that contains the [
id ]{.code-inline} parameter including the rule IDs that you would like
to delete.

For example, if you were trying to remove a set of rules from your
stream, your cURL command might look like this:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
  -H "Content-type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" -d \
  '{
    "delete": {
      "ids": [
        "1165037377523306498",
        "1165037377523306499"
      ]
    }
  }'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
We have sample code in different languages available via our
[Github](https://github.com/twitterdev/Twitter-API-v2-sample-code/tree/master/Filtered-Stream)
.

#### []{#examples} Rule examples

##### Tracking a natural disaster

The following rule matched on Tweets coming from weather agencies and
gauges that discuss Hurricane Harvey, which hit Houston in 2017. Notice
the use of the [matching
rules](/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets)
tag, and the JSON format that you will need to use when submitting the
rule to the [POST /2/tweets/search/stream/rules
endpoint](/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules)
.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
         {
            "value": "-is:retweet has:geo (from:NWSNHC OR from:NHC_Atlantic OR from:NWSHouston OR from:NWSSanAntonio OR from:USGS_TexasRain OR from:USGS_TexasFlood OR from:JeffLindner1)",
            "tag": "theme:info has:geo original from weather agencies and gauges"
        }

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The next rule could be used to better understand the sentiment of the
conversation developing around the hashtag, *#nowplaying* , but only
from Tweets published within North America.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
         {
            "value": "#nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place_country:US OR place_country:MX OR place_country:CA) -horrible -worst -sucks -bad -disappointing",
            "tag": "#nowplaying positive"
        },
        {
            "value": "#nowplaying (horrible OR worst OR sucks OR bad OR disappointing) (place_country:US OR place_country:MX OR place_country:CA) -happy -exciting -excited -favorite -fav -amazing -lovely -incredible",
            "tag": "#nowplaying negative"
        }

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
This rule was built to search for original Tweets that included an image
of a pet that is not a cat, where the language identified in the Tweet
is Japanese. To do this, we used the [ context: ]{.code-inline} operator
to take advantage of the [Tweet
annotation](/en/docs/twitter-api/annotations) functionality. We first
used the [Tweet lookup](/en/docs/twitter-api/tweets/lookup) endpoint and
[ the tweet.fields=context_annotations ]{.code-inline} fields parameter
to identify which domain.entity IDs we need to use in our query:

-   Tweets that relate to cats return **[ domain ]{.code-inline}** 66
    (Interests and Hobbies category) with [ entity ]{.code-inline}
    852262932607926273 (Cats).
-   Tweets that relate to pets return **[ domain ]{.code-inline}** 65
    (Interests and Hobbies Vertical) with [ entity ]{.code-inline}
    852262932607926273 (Pets).\

Here is what the rule would look like:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
         {
            "value": "context:65.852262932607926273 -context:66.852262932607926273 -is:retweet has:images lang:ja",
            "tag": "Japanese pets with images - no cats"
        }
    
```
:::
:::
:::

::: c01-rich-text-editor
<div>

-   **Essential:** Available when using any access level.
-   **Elevated:** Available when using a Project with Pro, or Enterprise
    access.
-    For some operators, an alternate name, or alias, is available.

+-----------------+-----------------+-----------------+-----------------+
| **Operator**    | [Type](#type)   | [Availability]  | Description     |
|                 |                 | (#availability) |                 |
+=================+=================+=================+=================+
| [ keyword       | Standalone      | Essential       | Matches a       |
| ]{.code-inline} |                 |                 | keyword within  |
|                 |                 |                 | the body of a   |
|                 |                 |                 | Tweet. This is  |
|                 |                 |                 | a tokenized     |
|                 |                 |                 | match, meaning  |
|                 |                 |                 | that your       |
|                 |                 |                 | keyword string  |
|                 |                 |                 | will be matched |
|                 |                 |                 | against the     |
|                 |                 |                 | tokenized text  |
|                 |                 |                 | of the Tweet    |
|                 |                 |                 | body.           |
|                 |                 |                 | Tokenization    |
|                 |                 |                 | splits words    |
|                 |                 |                 | based on        |
|                 |                 |                 | punctuation,    |
|                 |                 |                 | symbols, and    |
|                 |                 |                 | Unicode basic   |
|                 |                 |                 | plane separator |
|                 |                 |                 | characters. For |
|                 |                 |                 | example, a      |
|                 |                 |                 | Tweet with the  |
|                 |                 |                 | text "I like    |
|                 |                 |                 | coca-cola"      |
|                 |                 |                 | would be split  |
|                 |                 |                 | into the        |
|                 |                 |                 | following       |
|                 |                 |                 | tokens: I,      |
|                 |                 |                 | like, coca,     |
|                 |                 |                 | cola. These     |
|                 |                 |                 | tokens would    |
|                 |                 |                 | then be         |
|                 |                 |                 | compared to the |
|                 |                 |                 | keyword string  |
|                 |                 |                 | used in your    |
|                 |                 |                 | rule. To match  |
|                 |                 |                 | strings         |
|                 |                 |                 | containing      |
|                 |                 |                 | punctuation     |
|                 |                 |                 | (for example    |
|                 |                 |                 | coca-cola),     |
|                 |                 |                 | symbol, or      |
|                 |                 |                 | separator       |
|                 |                 |                 | characters, you |
|                 |                 |                 | must wrap your  |
|                 |                 |                 | keyword in      |
|                 |                 |                 | double-quotes.  |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | pepsi OR cola   |
|                 |                 |                 | OR \"coca       |
|                 |                 |                 | cola\"          |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ emoji         | Standalone      | Essential       | Matches an      |
| ]{.code-inline} |                 |                 | emoji within    |
|                 |                 |                 | the body of a   |
|                 |                 |                 | Tweet. Similar  |
|                 |                 |                 | to a keyword,   |
|                 |                 |                 | emojis are a    |
|                 |                 |                 | tokenized       |
|                 |                 |                 | match, meaning  |
|                 |                 |                 | that your emoji |
|                 |                 |                 | will be matched |
|                 |                 |                 | against the     |
|                 |                 |                 | tokenized text  |
|                 |                 |                 | of the Tweet    |
|                 |                 |                 | body. Note that |
|                 |                 |                 | if an emoji has |
|                 |                 |                 | a variant, you  |
|                 |                 |                 | must wrap it in |
|                 |                 |                 | double quotes   |
|                 |                 |                 | to add to a     |
|                 |                 |                 | rule.           |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [ (😃  |
|                 |                 |                 | OR 😡) 😬       |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ \"exact       | Standalone      | Essential       | Matches the     |
| phrase match\"  |                 |                 | exact phrase    |
| ]{.code-inline} |                 |                 | within the body |
|                 |                 |                 | of a Tweet.     |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | (\"Twitter      |
|                 |                 |                 | API\" OR #v2)   |
|                 |                 |                 | -\"filtered     |
|                 |                 |                 | stream\"        |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ \#            | Standalone      | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet           |
|                 |                 |                 | containing a    |
|                 |                 |                 | recognized      |
|                 |                 |                 | hashtag, if the |
|                 |                 |                 | hashtag is a    |
|                 |                 |                 | recognized      |
|                 |                 |                 | entity in a     |
|                 |                 |                 | Tweet.          |
|                 |                 |                 |                 |
|                 |                 |                 | This operator   |
|                 |                 |                 | performs an     |
|                 |                 |                 | exact match,    |
|                 |                 |                 | NOT a tokenized |
|                 |                 |                 | match, meaning  |
|                 |                 |                 | the rule [      |
|                 |                 |                 | #thanku         |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | will match      |
|                 |                 |                 | posts with the  |
|                 |                 |                 | exact hashtag   |
|                 |                 |                 | #thanku, but    |
|                 |                 |                 | not those with  |
|                 |                 |                 | the hashtag     |
|                 |                 |                 | #thankunext.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #thankunext     |
|                 |                 |                 | #fanart OR      |
|                 |                 |                 | \@arianagrande  |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ @             | Standalone      | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet that      |
|                 |                 |                 | mentions the    |
|                 |                 |                 | given username, |
|                 |                 |                 | if the username |
|                 |                 |                 | is a recognized |
|                 |                 |                 | entity          |
|                 |                 |                 | (including the  |
|                 |                 |                 | @ character).   |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | (@twitterdev OR |
|                 |                 |                 | \@twitterapi)   |
|                 |                 |                 | -@twitter       |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ \$            | Standalone      | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet that      |
|                 |                 |                 | contains the    |
|                 |                 |                 | specified       |
|                 |                 |                 | 'cashtag'       |
|                 |                 |                 | (where the      |
|                 |                 |                 | leading         |
|                 |                 |                 | character of    |
|                 |                 |                 | the token is    |
|                 |                 |                 | the '\$'        |
|                 |                 |                 | character).     |
|                 |                 |                 | Note that the   |
|                 |                 |                 | cashtag         |
|                 |                 |                 | operator relies |
|                 |                 |                 | on Twitter's    |
|                 |                 |                 | 'symbols'       |
|                 |                 |                 | entity          |
|                 |                 |                 | extraction to   |
|                 |                 |                 | match cashtags, |
|                 |                 |                 | rather than     |
|                 |                 |                 | trying to       |
|                 |                 |                 | extract the     |
|                 |                 |                 | cashtag from    |
|                 |                 |                 | the body        |
|                 |                 |                 | itself.         |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | \$twtr OR       |
|                 |                 |                 | \@twitterdev    |
|                 |                 |                 | -\$fb           |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ from:         | Standalone      | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet from a    |
|                 |                 |                 | specific user.  |
|                 |                 |                 | The value can   |
|                 |                 |                 | be either the   |
|                 |                 |                 | username        |
|                 |                 |                 | (excluding the  |
|                 |                 |                 | @ character) or |
|                 |                 |                 | the user's      |
|                 |                 |                 | numeric user    |
|                 |                 |                 | ID.             |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | username/ID [   |
|                 |                 |                 | from:           |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | from:twitterdev |
|                 |                 |                 | OR              |
|                 |                 |                 | from:twitterapi |
|                 |                 |                 | -from:twitter   |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ to:           | Standalone      | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet that is   |
|                 |                 |                 | in reply to a   |
|                 |                 |                 | particular      |
|                 |                 |                 | user. The value |
|                 |                 |                 | can be either   |
|                 |                 |                 | the username    |
|                 |                 |                 | (excluding the  |
|                 |                 |                 | @ character) or |
|                 |                 |                 | the user's      |
|                 |                 |                 | numeric user    |
|                 |                 |                 | ID.             |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | username/ID per |
|                 |                 |                 | [ to:           |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | to:twitterdev   |
|                 |                 |                 | OR              |
|                 |                 |                 | to:twitterapi   |
|                 |                 |                 | -to:twitter     |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ url:          | Standalone      | Essential       | Performs a      |
| ]{.code-inline} |                 |                 | tokenized match |
|                 |                 |                 | on any          |
|                 |                 |                 | va              |
|                 |                 |                 | lidly-formatted |
|                 |                 |                 | URL of a Tweet. |
|                 |                 |                 |                 |
|                 |                 |                 | This operator   |
|                 |                 |                 | can matches on  |
|                 |                 |                 | the contents of |
|                 |                 |                 | both the [ url  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | or [            |
|                 |                 |                 | expanded_url    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | fields. For     |
|                 |                 |                 | example, a      |
|                 |                 |                 | Tweet           |
|                 |                 |                 | containing      |
|                 |                 |                 | \"You should    |
|                 |                 |                 | check out       |
|                 |                 |                 | Twitter         |
|                 |                 |                 | Developer Labs: |
|                 |                 |                 | https://t.      |
|                 |                 |                 | co/c0A36SWil4\" |
|                 |                 |                 | (with the short |
|                 |                 |                 | URL redirecting |
|                 |                 |                 | to              |
|                 |                 |                 | https://develop |
|                 |                 |                 | er.twitter.com) |
|                 |                 |                 | will match both |
|                 |                 |                 | the following   |
|                 |                 |                 | rules:          |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | from:TwitterDev |
|                 |                 |                 | url:\"ht        |
|                 |                 |                 | tps://developer |
|                 |                 |                 | .twitter.com\"\ |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | (because it     |
|                 |                 |                 | will match the  |
|                 |                 |                 | contents of [   |
|                 |                 |                 | entities.ur     |
|                 |                 |                 | ls.expanded_url |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | )               |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | from:TwitterDev |
|                 |                 |                 | url:\"          |
|                 |                 |                 | https://t.co\"\ |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | (because it     |
|                 |                 |                 | will match the  |
|                 |                 |                 | contents of [   |
|                 |                 |                 | en              |
|                 |                 |                 | tities.urls.url |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | )               |
|                 |                 |                 |                 |
|                 |                 |                 | Tokens and      |
|                 |                 |                 | phrases         |
|                 |                 |                 | containing      |
|                 |                 |                 | punctuation or  |
|                 |                 |                 | special         |
|                 |                 |                 | characters      |
|                 |                 |                 | should be       |
|                 |                 |                 | double-quoted   |
|                 |                 |                 | (for example, [ |
|                 |                 |                 | url             |
|                 |                 |                 | :\"/developer\" |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ). Similarly,   |
|                 |                 |                 | to match on a   |
|                 |                 |                 | specific        |
|                 |                 |                 | protocol,       |
|                 |                 |                 | enclose in      |
|                 |                 |                 | double-quotes   |
|                 |                 |                 | (for example, [ |
|                 |                 |                 | url:\"h         |
|                 |                 |                 | ttps://develope |
|                 |                 |                 | r.twitter.com\" |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ).              |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | URL per [ url:  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
+-----------------+-----------------+-----------------+-----------------+
| [ retweets_of:  | Standalone      | Essential       | *Available      |
| ]{.code-inline} |                 |                 | alias:* [       |
|                 |                 |                 | re              |
|                 |                 |                 | tweets_of_user: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | that are        |
|                 |                 |                 | Retweets of the |
|                 |                 |                 | specified user. |
|                 |                 |                 | The value can   |
|                 |                 |                 | be either the   |
|                 |                 |                 | username        |
|                 |                 |                 | (excluding the  |
|                 |                 |                 | @ character) or |
|                 |                 |                 | the user's      |
|                 |                 |                 | numeric user    |
|                 |                 |                 | ID.             |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | username/ID per |
|                 |                 |                 | [ retweets_of:  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | retweet         |
|                 |                 |                 | s_of:twitterdev |
|                 |                 |                 | OR              |
|                 |                 |                 | retweet         |
|                 |                 |                 | s_of:twitterapi |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | See             |
|                 |                 |                 | [HERE]          |
|                 |                 |                 | (https://develo |
|                 |                 |                 | per.twitter.com |
|                 |                 |                 | /content/develo |
|                 |                 |                 | per-twitter/en/ |
|                 |                 |                 | docs/twitter-ap |
|                 |                 |                 | i/users/lookup) |
|                 |                 |                 | for methods for |
|                 |                 |                 | looking up      |
|                 |                 |                 | numeric Twitter |
|                 |                 |                 | Account IDs.    |
+-----------------+-----------------+-----------------+-----------------+
| [ context:      | Standalone      | Essential       | Matches Tweets  |
| ]{.code-inline} |                 |                 | with a specific |
|                 |                 |                 | domain id       |
|                 |                 |                 | and/or domain   |
|                 |                 |                 | id, enitity id  |
|                 |                 |                 | pair where \*   |
|                 |                 |                 | represents a    |
|                 |                 |                 | wildcard. To    |
|                 |                 |                 | learn more      |
|                 |                 |                 | about this      |
|                 |                 |                 | operator,       |
|                 |                 |                 | please visit    |
|                 |                 |                 | our page on     |
|                 |                 |                 | [Tweet a        |
|                 |                 |                 | nnotations](/en |
|                 |                 |                 | /docs/twitter-a |
|                 |                 |                 | pi/annotations) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | domain/entitie  |
|                 |                 |                 | per [ context:  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | ::: code-inline |
|                 |                 |                 | context:doma    |
|                 |                 |                 | in_id.entity_id |
|                 |                 |                 | conte           |
|                 |                 |                 | xt:domain_id.\* |
|                 |                 |                 | conte           |
|                 |                 |                 | xt:\*.entity_id |
|                 |                 |                 | :::             |
|                 |                 |                 |                 |
|                 |                 |                 | Examples:       |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | context:10.7990 |
|                 |                 |                 | 22225751871488\ |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ( [             |
|                 |                 |                 | doma            |
|                 |                 |                 | in_id.entity_id |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | returns Tweets  |
|                 |                 |                 | matching that   |
|                 |                 |                 | specific        |
|                 |                 |                 | domain-entity   |
|                 |                 |                 | pair)           |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | context:47.\*\  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ( [             |
|                 |                 |                 | domain_id.\*    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | returns Tweets  |
|                 |                 |                 | matching that   |
|                 |                 |                 | domain ID, with |
|                 |                 |                 | any             |
|                 |                 |                 | domain-entity   |
|                 |                 |                 | pair)           |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | context:\*.7990 |
|                 |                 |                 | 22225751871488\ |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ( [             |
|                 |                 |                 | \*.entity_id    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | returns Tweets  |
|                 |                 |                 | matching that   |
|                 |                 |                 | entity ID, with |
|                 |                 |                 | any             |
|                 |                 |                 | domain-entity   |
|                 |                 |                 | pair)           |
+-----------------+-----------------+-----------------+-----------------+
| [ entity:       | Standalone      | Essential       | Matches Tweets  |
| ]{.code-inline} |                 |                 | with a specific |
|                 |                 |                 | entity string   |
|                 |                 |                 | value. To learn |
|                 |                 |                 | more about this |
|                 |                 |                 | operator,       |
|                 |                 |                 | please visit    |
|                 |                 |                 | our page on     |
|                 |                 |                 | [annotations]   |
|                 |                 |                 | (/content/devel |
|                 |                 |                 | oper-twitter/en |
|                 |                 |                 | /docs/twitter-a |
|                 |                 |                 | pi/annotations) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | entity per [    |
|                 |                 |                 | entity:         |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | entity:\"string |
|                 |                 |                 | declaration of  |
|                 |                 |                 | entity/place\"\ |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | \               |
|                 |                 |                 | Examples: [     |
|                 |                 |                 | e               |
|                 |                 |                 | ntity:\"Michael |
|                 |                 |                 | Jordan\" OR     |
|                 |                 |                 | entit           |
|                 |                 |                 | y:\"Barcelona\" |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [               | Standalone      | Essential       | Matches Tweets  |
| c               |                 |                 | that share a    |
| onversation_id: |                 |                 | common          |
| ]{.code-inline} |                 |                 | conversation    |
|                 |                 |                 | ID. A           |
|                 |                 |                 | conversation ID |
|                 |                 |                 | is set to the   |
|                 |                 |                 | Tweet ID of a   |
|                 |                 |                 | Tweet that      |
|                 |                 |                 | started a       |
|                 |                 |                 | conversation.   |
|                 |                 |                 | As Replies to a |
|                 |                 |                 | Tweet are       |
|                 |                 |                 | posted, even    |
|                 |                 |                 | Replies to      |
|                 |                 |                 | Replies, the [  |
|                 |                 |                 | conversation_id |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | is added to its |
|                 |                 |                 | JSON payload.   |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | conversation ID |
|                 |                 |                 | per [           |
|                 |                 |                 | c               |
|                 |                 |                 | onversation_id: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | conve           |
|                 |                 |                 | rsation_id:1334 |
|                 |                 |                 | 987486343299072 |
|                 |                 |                 | (               |
|                 |                 |                 | from:twitterdev |
|                 |                 |                 | OR              |
|                 |                 |                 | f               |
|                 |                 |                 | rom:twitterapi) |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ bio:          | Standalone      | Essential       | *Available      |
| ]{.code-inline} |                 |                 | alias:* [       |
|                 |                 |                 | user_bio:       |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches a       |
|                 |                 |                 | keyword or      |
|                 |                 |                 | phrase within   |
|                 |                 |                 | the Tweet       |
|                 |                 |                 | publisher\'s    |
|                 |                 |                 | bio. This is a  |
|                 |                 |                 | tokenized match |
|                 |                 |                 | within the      |
|                 |                 |                 | contents of the |
|                 |                 |                 | [ description   |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | field within    |
|                 |                 |                 | the [User       |
|                 |                 |                 | object](/conte  |
|                 |                 |                 | nt/developer-tw |
|                 |                 |                 | itter/en/docs/t |
|                 |                 |                 | witter-api/data |
|                 |                 |                 | -dictionary/obj |
|                 |                 |                 | ect-model/user) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | bio:developer   |
|                 |                 |                 | OR bio:\"data   |
|                 |                 |                 | engineer\" OR   |
|                 |                 |                 | bio:academic    |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ bio_name:     | Standalone      | Essential       | Matches a       |
| ]{.code-inline} |                 |                 | keyword within  |
|                 |                 |                 | the Tweet       |
|                 |                 |                 | publisher\'s    |
|                 |                 |                 | user bio name.  |
|                 |                 |                 | This is a       |
|                 |                 |                 | tokenized match |
|                 |                 |                 | within the      |
|                 |                 |                 | contents of a   |
|                 |                 |                 | user's "name"   |
|                 |                 |                 | field within    |
|                 |                 |                 | the [User       |
|                 |                 |                 | object](/conte  |
|                 |                 |                 | nt/developer-tw |
|                 |                 |                 | itter/en/docs/t |
|                 |                 |                 | witter-api/data |
|                 |                 |                 | -dictionary/obj |
|                 |                 |                 | ect-model/user) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | bio_name:phd OR |
|                 |                 |                 | bio_name:md     |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ bio_location: | Standalone      | Essential       | *Available      |
| ]{.code-inline} |                 |                 | alias:* [       |
|                 |                 |                 | use             |
|                 |                 |                 | r_bio_location: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | that are        |
|                 |                 |                 | published by    |
|                 |                 |                 | users whose     |
|                 |                 |                 | location        |
|                 |                 |                 | contains the    |
|                 |                 |                 | specified       |
|                 |                 |                 | keyword or      |
|                 |                 |                 | phrase. This    |
|                 |                 |                 | operator        |
|                 |                 |                 | performs a      |
|                 |                 |                 | tokenized       |
|                 |                 |                 | match, similar  |
|                 |                 |                 | to the normal   |
|                 |                 |                 | keyword rules   |
|                 |                 |                 | on the message  |
|                 |                 |                 | body.           |
|                 |                 |                 |                 |
|                 |                 |                 | This location   |
|                 |                 |                 | is part of the  |
|                 |                 |                 | [User           |
|                 |                 |                 | object](        |
|                 |                 |                 | /content/develo |
|                 |                 |                 | per-twitter/en/ |
|                 |                 |                 | docs/twitter-ap |
|                 |                 |                 | i/enterprise/po |
|                 |                 |                 | wertrack-api/gu |
|                 |                 |                 | ides/operators) |
|                 |                 |                 | , matches on    |
|                 |                 |                 | the             |
|                 |                 |                 | \'location\'    |
|                 |                 |                 | field, and is a |
|                 |                 |                 | non-normalized, |
|                 |                 |                 | user-generated, |
|                 |                 |                 | free-form       |
|                 |                 |                 | string. It is   |
|                 |                 |                 | also different  |
|                 |                 |                 | from a Tweet\'s |
|                 |                 |                 | location (see [ |
|                 |                 |                 | place:          |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ).              |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | bio             |
|                 |                 |                 | _location:\"big |
|                 |                 |                 | apple\" OR      |
|                 |                 |                 | b               |
|                 |                 |                 | io_location:nyc |
|                 |                 |                 | OR              |
|                 |                 |                 | bio_loc         |
|                 |                 |                 | ation:manhattan |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ place:        | Standalone      | Elevated        | Matches Tweets  |
| ]{.code-inline} |                 |                 | tagged with the |
|                 |                 |                 | specified       |
|                 |                 |                 | location or     |
|                 |                 |                 | Twitter place   |
|                 |                 |                 | ID. Multi-word  |
|                 |                 |                 | place names     |
|                 |                 |                 | ("New York      |
|                 |                 |                 | City", "Palo    |
|                 |                 |                 | Alto") should   |
|                 |                 |                 | be enclosed in  |
|                 |                 |                 | quotes.         |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | place per [     |
|                 |                 |                 | place:          |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Note: See the   |
|                 |                 |                 | [GET            |
|                 |                 |                 | geo/search]     |
|                 |                 |                 | (/content/devel |
|                 |                 |                 | oper-twitter/en |
|                 |                 |                 | /docs/geo/place |
|                 |                 |                 | s-near-location |
|                 |                 |                 | /api-reference/ |
|                 |                 |                 | get-geo-search) |
|                 |                 |                 | standard v1.1   |
|                 |                 |                 | endpoint for    |
|                 |                 |                 | how to obtain   |
|                 |                 |                 | Twitter place   |
|                 |                 |                 | IDs.            |
|                 |                 |                 |                 |
|                 |                 |                 | Note: This      |
|                 |                 |                 | operator will   |
|                 |                 |                 | not match on    |
|                 |                 |                 | Retweets, since |
|                 |                 |                 | Retweet\'s      |
|                 |                 |                 | places are      |
|                 |                 |                 | attached to the |
|                 |                 |                 | original Tweet. |
|                 |                 |                 | It will also    |
|                 |                 |                 | not match on    |
|                 |                 |                 | places attached |
|                 |                 |                 | to the original |
|                 |                 |                 | Tweet of a      |
|                 |                 |                 | Quote Tweet.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | place:\"new     |
|                 |                 |                 | york city\" OR  |
|                 |                 |                 | place:seattle   |
|                 |                 |                 | OR              |
|                 |                 |                 | place:f         |
|                 |                 |                 | d70c22040963ac7 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [               | Standalone      | Elevated        | Matches Tweets  |
| place_country:  |                 |                 | where the       |
| ]{.code-inline} |                 |                 | country code    |
|                 |                 |                 | associated with |
|                 |                 |                 | a tagged        |
|                 |                 |                 | place/location  |
|                 |                 |                 | matches the     |
|                 |                 |                 | given ISO       |
|                 |                 |                 | alpha-2         |
|                 |                 |                 | character code. |
|                 |                 |                 |                 |
|                 |                 |                 | You can find a  |
|                 |                 |                 | list of valid   |
|                 |                 |                 | ISO codes on    |
|                 |                 |                 | [Wikipedia](htt |
|                 |                 |                 | p://en.wikipedi |
|                 |                 |                 | a.org/wiki/ISO_ |
|                 |                 |                 | 3166-1_alpha-2) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | ISO code per [  |
|                 |                 |                 | place_country:  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Note: This      |
|                 |                 |                 | operator will   |
|                 |                 |                 | not match on    |
|                 |                 |                 | Retweets, since |
|                 |                 |                 | Retweet\'s      |
|                 |                 |                 | places are      |
|                 |                 |                 | attached to the |
|                 |                 |                 | original Tweet. |
|                 |                 |                 | It will also    |
|                 |                 |                 | not match on    |
|                 |                 |                 | places attached |
|                 |                 |                 | to the original |
|                 |                 |                 | Tweet of a      |
|                 |                 |                 | Quote Tweet.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | p               |
|                 |                 |                 | lace_country:US |
|                 |                 |                 | OR              |
|                 |                 |                 | p               |
|                 |                 |                 | lace_country:MX |
|                 |                 |                 | OR              |
|                 |                 |                 | p               |
|                 |                 |                 | lace_country:CA |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ point_radius: | Standalone      | Elevated        | Matches against |
| ]{.code-inline} |                 |                 | the [           |
|                 |                 |                 | place.          |
|                 |                 |                 | geo.coordinates |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | object of the   |
|                 |                 |                 | Tweet when      |
|                 |                 |                 | present, and in |
|                 |                 |                 | Twitter,        |
|                 |                 |                 | against a place |
|                 |                 |                 | geo polygon,    |
|                 |                 |                 | where the Place |
|                 |                 |                 | polygon is      |
|                 |                 |                 | fully contained |
|                 |                 |                 | within the      |
|                 |                 |                 | defined region. |
|                 |                 |                 |                 |
|                 |                 |                 | [               |
|                 |                 |                 | point_rad       |
|                 |                 |                 | ius:\[longitude |
|                 |                 |                 | latitude        |
|                 |                 |                 | radius\]\       |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | -   Units of    |
|                 |                 |                 |     radius      |
|                 |                 |                 |     supported   |
|                 |                 |                 |     are         |
|                 |                 |                 |     miles (mi)  |
|                 |                 |                 |     and         |
|                 |                 |                 |     kilometers  |
|                 |                 |                 |     (km)\       |
|                 |                 |                 | -   Radius must |
|                 |                 |                 |     be less     |
|                 |                 |                 |     than 25mi\  |
|                 |                 |                 | -   Longitude   |
|                 |                 |                 |     is in the   |
|                 |                 |                 |     range of    |
|                 |                 |                 |     ±180\       |
|                 |                 |                 | -   Latitude is |
|                 |                 |                 |     in the      |
|                 |                 |                 |     range of    |
|                 |                 |                 |     ±90\        |
|                 |                 |                 | -   All         |
|                 |                 |                 |     coordinates |
|                 |                 |                 |     are in      |
|                 |                 |                 |     decimal     |
|                 |                 |                 |     degrees\    |
|                 |                 |                 | -   Rule        |
|                 |                 |                 |     arguments   |
|                 |                 |                 |     are         |
|                 |                 |                 |     contained   |
|                 |                 |                 |     within      |
|                 |                 |                 |     brackets,   |
|                 |                 |                 |     space       |
|                 |                 |                 |     delimited\  |
|                 |                 |                 |                 |
|                 |                 |                 | \               |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | geo polygon per |
|                 |                 |                 | [ point_radius: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator. Note: |
|                 |                 |                 | This operator   |
|                 |                 |                 | will not match  |
|                 |                 |                 | on Retweets,    |
|                 |                 |                 | since           |
|                 |                 |                 | Retweet\'s      |
|                 |                 |                 | places are      |
|                 |                 |                 | attached to the |
|                 |                 |                 | original Tweet. |
|                 |                 |                 | It will also    |
|                 |                 |                 | not match on    |
|                 |                 |                 | places attached |
|                 |                 |                 | to the original |
|                 |                 |                 | Tweet of a      |
|                 |                 |                 | Quote Tweet.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | point_ra        |
|                 |                 |                 | dius:\[2.355128 |
|                 |                 |                 | 48.861118       |
|                 |                 |                 | 16km\] OR       |
|                 |                 |                 | point_radi      |
|                 |                 |                 | us:\[-41.287336 |
|                 |                 |                 | 174.761070      |
|                 |                 |                 | 20mi\]          |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ bounding_box: | Standalone      | Elevated        | *Available      |
| ]{.code-inline} |                 |                 | alias:* [       |
|                 |                 |                 | ge              |
|                 |                 |                 | o_bounding_box: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches against |
|                 |                 |                 | the             |
|                 |                 |                 | place.          |
|                 |                 |                 | geo.coordinates |
|                 |                 |                 | object of the   |
|                 |                 |                 | Tweet when      |
|                 |                 |                 | present, and in |
|                 |                 |                 | Twitter,        |
|                 |                 |                 | against a place |
|                 |                 |                 | geo polygon,    |
|                 |                 |                 | where the place |
|                 |                 |                 | polygon is      |
|                 |                 |                 | fully contained |
|                 |                 |                 | within the      |
|                 |                 |                 | defined region. |
|                 |                 |                 | \               |
|                 |                 |                 |                 |
|                 |                 |                 | \               |
|                 |                 |                 | [               |
|                 |                 |                 | bounding_       |
|                 |                 |                 | box:\[west_long |
|                 |                 |                 | south_lat       |
|                 |                 |                 | east_long       |
|                 |                 |                 | north_lat\]\    |
|                 |                 |                 | ]               |
|                 |                 |                 | {.code-inline}\ |
|                 |                 |                 |                 |
|                 |                 |                 | -   [ west_long |
|                 |                 |                 |     south_lat   |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     represent   |
|                 |                 |                 |     the         |
|                 |                 |                 |     southwest   |
|                 |                 |                 |     corner of   |
|                 |                 |                 |     the         |
|                 |                 |                 |     bounding    |
|                 |                 |                 |     box where [ |
|                 |                 |                 |     west_long   |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     is the      |
|                 |                 |                 |     longitude   |
|                 |                 |                 |     of that     |
|                 |                 |                 |     point, and  |
|                 |                 |                 |     [ south_lat |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     is the      |
|                 |                 |                 |     latitude.\  |
|                 |                 |                 | -   [ east_long |
|                 |                 |                 |     north_lat   |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     represent   |
|                 |                 |                 |     the         |
|                 |                 |                 |     northeast   |
|                 |                 |                 |     corner of   |
|                 |                 |                 |     the         |
|                 |                 |                 |     bounding    |
|                 |                 |                 |     box, where  |
|                 |                 |                 |     [ east_long |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     is the      |
|                 |                 |                 |     longitude   |
|                 |                 |                 |     of that     |
|                 |                 |                 |     point, and  |
|                 |                 |                 |     [ north_lat |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |     is the      |
|                 |                 |                 |     latitude.\  |
|                 |                 |                 | -   Width and   |
|                 |                 |                 |     height of   |
|                 |                 |                 |     the         |
|                 |                 |                 |     bounding    |
|                 |                 |                 |     box must be |
|                 |                 |                 |     less than   |
|                 |                 |                 |     25mi\       |
|                 |                 |                 | -   Longitude   |
|                 |                 |                 |     is in the   |
|                 |                 |                 |     range of    |
|                 |                 |                 |     ±180\       |
|                 |                 |                 | -   Latitude is |
|                 |                 |                 |     in the      |
|                 |                 |                 |     range of    |
|                 |                 |                 |     ±90\        |
|                 |                 |                 | -   All         |
|                 |                 |                 |     coordinates |
|                 |                 |                 |     are in      |
|                 |                 |                 |     decimal     |
|                 |                 |                 |     degrees.\   |
|                 |                 |                 | -   Rule        |
|                 |                 |                 |     arguments   |
|                 |                 |                 |     are         |
|                 |                 |                 |     contained   |
|                 |                 |                 |     within      |
|                 |                 |                 |     brackets,   |
|                 |                 |                 |     space       |
|                 |                 |                 |     delimited.\ |
|                 |                 |                 |                 |
|                 |                 |                 | \               |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | geo polygons    |
|                 |                 |                 | per [           |
|                 |                 |                 | bounding_box:   |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator. Note: |
|                 |                 |                 | This operator   |
|                 |                 |                 | will not match  |
|                 |                 |                 | on Retweets,    |
|                 |                 |                 | since           |
|                 |                 |                 | Retweet\'s      |
|                 |                 |                 | places are      |
|                 |                 |                 | attached to the |
|                 |                 |                 | original Tweet. |
|                 |                 |                 | It will also    |
|                 |                 |                 | not match on    |
|                 |                 |                 | places attached |
|                 |                 |                 | to the original |
|                 |                 |                 | Tweet of a      |
|                 |                 |                 | Quote Tweet.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | bounding_bo     |
|                 |                 |                 | x:\[-105.301758 |
|                 |                 |                 | 39.964069       |
|                 |                 |                 | -105.178505     |
|                 |                 |                 | 40.09455\]      |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ is:retweet    | Conjunction     | Essential       | Matches on      |
| ]{.code-inline} | required        |                 | Retweets that   |
|                 |                 |                 | match the rest  |
|                 |                 |                 | of the          |
|                 |                 |                 | specified rule. |
|                 |                 |                 | This operator   |
|                 |                 |                 | looks only for  |
|                 |                 |                 | true Retweets   |
|                 |                 |                 | (for example,   |
|                 |                 |                 | those generated |
|                 |                 |                 | using the       |
|                 |                 |                 | Retweet         |
|                 |                 |                 | button). Quote  |
|                 |                 |                 | Tweets will not |
|                 |                 |                 | be matched by   |
|                 |                 |                 | this operator.  |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [ data |
|                 |                 |                 | \@twitterdev    |
|                 |                 |                 | -is:retweet     |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ is:reply      | Conjunction     | Essential       | Deliver only    |
| ]{.code-inline} | required        |                 | explicit        |
|                 |                 |                 | replies that    |
|                 |                 |                 | match a rule.   |
|                 |                 |                 | Can also be     |
|                 |                 |                 | negated to      |
|                 |                 |                 | exclude replies |
|                 |                 |                 | that match a    |
|                 |                 |                 | rule from       |
|                 |                 |                 | delivery. When  |
|                 |                 |                 | used with the   |
|                 |                 |                 | filtered        |
|                 |                 |                 | stream, this    |
|                 |                 |                 | operator        |
|                 |                 |                 | matches on      |
|                 |                 |                 | replies to an   |
|                 |                 |                 | original Tweet, |
|                 |                 |                 | replies in      |
|                 |                 |                 | quoted Tweets   |
|                 |                 |                 | and replies in  |
|                 |                 |                 | Retweets.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | from:twitterdev |
|                 |                 |                 | is:reply        |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ is:quote      | Conjunction     | Essential       | Returns all     |
| ]{.code-inline} | required        |                 | Quote Tweets,   |
|                 |                 |                 | also known as   |
|                 |                 |                 | Tweets with     |
|                 |                 |                 | comments.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | \"sentiment     |
|                 |                 |                 | analysis\"      |
|                 |                 |                 | is:quote        |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ is:verified   | Conjunction     | Essential       | Deliver only    |
| ]{.code-inline} | required        |                 | Tweets whose    |
|                 |                 |                 | authors are     |
|                 |                 |                 | verified by     |
|                 |                 |                 | Twitter.        |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #nowplaying     |
|                 |                 |                 | is:verified     |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ -is:nullcast  | Conjunction     | Elevated        | Removes Tweets  |
| ]{.code-inline} | required        |                 | created for     |
|                 |                 |                 | promotion only  |
|                 |                 |                 | on              |
|                 |                 |                 | ads.twitter.com |
|                 |                 |                 | that have a [   |
|                 |                 |                 | \"sou           |
|                 |                 |                 | rce\":\"Twitter |
|                 |                 |                 | for Advertisers |
|                 |                 |                 | (legacy)\"      |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | or [            |
|                 |                 |                 | \"sou           |
|                 |                 |                 | rce\":\"Twitter |
|                 |                 |                 | for             |
|                 |                 |                 | Advertisers\".  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | This operator   |
|                 |                 |                 | must be         |
|                 |                 |                 | negated.        |
|                 |                 |                 |                 |
|                 |                 |                 | For more info   |
|                 |                 |                 | on Nullcasted   |
|                 |                 |                 | Tweets, see our |
|                 |                 |                 | page on [Tweet  |
|                 |                 |                 | availabi        |
|                 |                 |                 | lity](/content/ |
|                 |                 |                 | developer-twitt |
|                 |                 |                 | er/en/docs/twit |
|                 |                 |                 | ter-api/v1/twee |
|                 |                 |                 | ts/post-and-eng |
|                 |                 |                 | age/guides/twee |
|                 |                 |                 | t-availability) |
|                 |                 |                 | .               |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | \"mobile        |
|                 |                 |                 | games\"         |
|                 |                 |                 | -is:nullcast    |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:hashtags  | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that contain at |
|                 |                 |                 | least one       |
|                 |                 |                 | hashtag.        |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | from:twitterdev |
|                 |                 |                 | -has:hashtags   |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:cashtags  | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that contain a  |
|                 |                 |                 | cashtag symbol  |
|                 |                 |                 | (with a leading |
|                 |                 |                 | '\$' character. |
|                 |                 |                 | For example, [  |
|                 |                 |                 | \$tag           |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | ).              |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #stonks         |
|                 |                 |                 | has:cashtags    |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:links     | Conjunction     | Essential       | This operator   |
| ]{.code-inline} | required        |                 | matches Tweets  |
|                 |                 |                 | which contain   |
|                 |                 |                 | links and media |
|                 |                 |                 | in the Tweet    |
|                 |                 |                 | body.           |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | from:twitterdev |
|                 |                 |                 | announcement    |
|                 |                 |                 | has:links       |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:mentions  | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that mention    |
|                 |                 |                 | another Twitter |
|                 |                 |                 | user.           |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #nowplaying     |
|                 |                 |                 | has:mentions    |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:media     | Conjunction     | Essential       | *Available      |
| ]{.code-inline} | required        |                 | alias:* [       |
|                 |                 |                 | has:media_link  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | that contain a  |
|                 |                 |                 | media object,   |
|                 |                 |                 | such as a       |
|                 |                 |                 | photo, GIF, or  |
|                 |                 |                 | video, as       |
|                 |                 |                 | determined by   |
|                 |                 |                 | Twitter. This   |
|                 |                 |                 | will not match  |
|                 |                 |                 | on media        |
|                 |                 |                 | created with    |
|                 |                 |                 | Periscope, or   |
|                 |                 |                 | Tweets with     |
|                 |                 |                 | links to other  |
|                 |                 |                 | media hosting   |
|                 |                 |                 | sites.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | (kittens OR     |
|                 |                 |                 | puppies)        |
|                 |                 |                 | has:media       |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:images    | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that contain a  |
|                 |                 |                 | recognized URL  |
|                 |                 |                 | to an image.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #meme           |
|                 |                 |                 | has:images      |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [               | Conjunction     | Essential       | *Available      |
| has:video_link  | required        |                 | alias:* [       |
| ]{.code-inline} |                 |                 | has:videos      |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | that contain    |
|                 |                 |                 | native Twitter  |
|                 |                 |                 | videos,         |
|                 |                 |                 | uploaded        |
|                 |                 |                 | directly to     |
|                 |                 |                 | Twitter. This   |
|                 |                 |                 | will not match  |
|                 |                 |                 | on videos       |
|                 |                 |                 | created with    |
|                 |                 |                 | Periscope, or   |
|                 |                 |                 | Tweets with     |
|                 |                 |                 | links to other  |
|                 |                 |                 | video hosting   |
|                 |                 |                 | sites.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #ice            |
|                 |                 |                 | bucketchallenge |
|                 |                 |                 | has:video_link  |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ has:geo       | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that have       |
|                 |                 |                 | Tweet-specific  |
|                 |                 |                 | geolocation     |
|                 |                 |                 | data provided   |
|                 |                 |                 | by the Twitter  |
|                 |                 |                 | user. This can  |
|                 |                 |                 | be either a     |
|                 |                 |                 | location in the |
|                 |                 |                 | form of a       |
|                 |                 |                 | Twitter place,  |
|                 |                 |                 | with the        |
|                 |                 |                 | corresponding   |
|                 |                 |                 | display name,   |
|                 |                 |                 | geo polygon,    |
|                 |                 |                 | and other       |
|                 |                 |                 | fields, or in   |
|                 |                 |                 | rare cases, a   |
|                 |                 |                 | geo lat-long    |
|                 |                 |                 | coordinate.     |
|                 |                 |                 | Note: Operators |
|                 |                 |                 | matching on     |
|                 |                 |                 | place (Tweet    |
|                 |                 |                 | geo) will only  |
|                 |                 |                 | include matches |
|                 |                 |                 | from original   |
|                 |                 |                 | tweets.         |
|                 |                 |                 | Retweets do not |
|                 |                 |                 | contain any     |
|                 |                 |                 | place data.     |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | recommend       |
|                 |                 |                 | #paris has:geo  |
|                 |                 |                 | -bakery         |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ sample:       | Conjunction     | Essential       | Returns a       |
| ]{.code-inline} | required        |                 | random percent  |
|                 |                 |                 | sample of       |
|                 |                 |                 | Tweets that     |
|                 |                 |                 | match a rule    |
|                 |                 |                 | rather than the |
|                 |                 |                 | entire set of   |
|                 |                 |                 | Tweets. The     |
|                 |                 |                 | percent value   |
|                 |                 |                 | must be         |
|                 |                 |                 | represented by  |
|                 |                 |                 | an integer      |
|                 |                 |                 | between 1 and   |
|                 |                 |                 | 100 (for        |
|                 |                 |                 | example, [      |
|                 |                 |                 | sample:10       |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | will return a   |
|                 |                 |                 | random 10%      |
|                 |                 |                 | sample).        |
|                 |                 |                 |                 |
|                 |                 |                 | This operator   |
|                 |                 |                 | first reduces   |
|                 |                 |                 | the scope of    |
|                 |                 |                 | the stream to   |
|                 |                 |                 | the percentage  |
|                 |                 |                 | you specified,  |
|                 |                 |                 | then the        |
|                 |                 |                 | rule/filter is  |
|                 |                 |                 | applied to that |
|                 |                 |                 | sampled subset. |
|                 |                 |                 | In other words, |
|                 |                 |                 | if you are      |
|                 |                 |                 | using, for      |
|                 |                 |                 | example, [      |
|                 |                 |                 | sample:10       |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | , each Tweet    |
|                 |                 |                 | will have a 10% |
|                 |                 |                 | chance of being |
|                 |                 |                 | in the sample.  |
|                 |                 |                 |                 |
|                 |                 |                 | This operator   |
|                 |                 |                 | applies to the  |
|                 |                 |                 | entire rule and |
|                 |                 |                 | requires all    |
|                 |                 |                 | OR\'d terms to  |
|                 |                 |                 | be grouped.     |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | #nowplaying     |
|                 |                 |                 | \@spotify       |
|                 |                 |                 | sample:15       |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ lang:         | Conjunction     | Essential       | Matches Tweets  |
| ]{.code-inline} | required        |                 | that have been  |
|                 |                 |                 | classified by   |
|                 |                 |                 | Twitter as      |
|                 |                 |                 | being of a      |
|                 |                 |                 | particular      |
|                 |                 |                 | language (if,   |
|                 |                 |                 | and only if,    |
|                 |                 |                 | the tweet has   |
|                 |                 |                 | been            |
|                 |                 |                 | classified). It |
|                 |                 |                 | is important to |
|                 |                 |                 | note that each  |
|                 |                 |                 | Tweet is        |
|                 |                 |                 | currently only  |
|                 |                 |                 | classified as   |
|                 |                 |                 | being of one    |
|                 |                 |                 | language, so    |
|                 |                 |                 | AND'ing         |
|                 |                 |                 | together        |
|                 |                 |                 | multiple        |
|                 |                 |                 | languages will  |
|                 |                 |                 | yield no        |
|                 |                 |                 | results.        |
|                 |                 |                 |                 |
|                 |                 |                 | You can only    |
|                 |                 |                 | pass a single   |
|                 |                 |                 | BCP 47 language |
|                 |                 |                 | identifier per  |
|                 |                 |                 | [ lang:         |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 | operator.       |
|                 |                 |                 |                 |
|                 |                 |                 | Note: if no     |
|                 |                 |                 | language        |
|                 |                 |                 | classification  |
|                 |                 |                 | can be made the |
|                 |                 |                 | provided result |
|                 |                 |                 | is 'und' (for   |
|                 |                 |                 | undefined).     |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | recommend       |
|                 |                 |                 | #paris lang:en  |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | The list below  |
|                 |                 |                 | represents the  |
|                 |                 |                 | currently       |
|                 |                 |                 | supported       |
|                 |                 |                 | languages and   |
|                 |                 |                 | their           |
|                 |                 |                 | corresponding   |
|                 |                 |                 | BCP 47 language |
|                 |                 |                 | identifier:     |
|                 |                 |                 |                 |
|                 |                 |                 |   ------------  |
|                 |                 |                 | ----- --------- |
|                 |                 |                 | -------- ------ |
|                 |                 |                 | ----------- --- |
|                 |                 |                 | --------------- |
|                 |                 |                 |   Amhari        |
|                 |                 |                 | c: [ am     Ger |
|                 |                 |                 | man: [ de       |
|                 |                 |                 | Malayalam: [ ml |
|                 |                 |                 |    Slovak: [ sk |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Arabic: [     |
|                 |                 |                 |  ar      Greek: |
|                 |                 |                 |  [ el       Mal |
|                 |                 |                 | divian: [ dv    |
|                 |                 |                 | Slovenian: [ sl |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Armenian: [   |
|                 |                 |                 |  hy    Gujarati |
|                 |                 |                 | : [ gu    Marat |
|                 |                 |                 | hi: [ mr     So |
|                 |                 |                 | rani Kurdish: [ |
|                 |                 |                 |   ]{.code-inli  |
|                 |                 |                 | ne}   ]{.code-i |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ckb |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |               ] |
|                 |                 |                 | {.code-inline}\ |
|                 |                 |                 |                 |
|                 |                 |                 |   Basque:       |
|                 |                 |                 |  [ eu      Hait |
|                 |                 |                 | ian Creole: [ N |
|                 |                 |                 | epali: [ ne     |
|                 |                 |                 |   Spanish: [ es |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ht     |
|                 |                 |                 |             ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |          ]{.cod |
|                 |                 |                 | e-inline}       |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |   Bengali       |
|                 |                 |                 | : [ bn     Hebr |
|                 |                 |                 | ew: [ iw      N |
|                 |                 |                 | orwegian: [ no  |
|                 |                 |                 |   Swedish: [ sv |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Bosnian       |
|                 |                 |                 | : [ bs     Hind |
|                 |                 |                 | i: [ hi       O |
|                 |                 |                 | riya: [ or      |
|                 |                 |                 |   Tagalog: [ tl |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Bulga         |
|                 |                 |                 | rian: [ bg   La |
|                 |                 |                 | tinized Hindi:  |
|                 |                 |                 |  Panjabi: [ pa  |
|                 |                 |                 |     Tamil: [ ta |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   [ hi-L |
|                 |                 |                 | atn         ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |          ]{.cod |
|                 |                 |                 | e-inline}       |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |   Burmes        |
|                 |                 |                 | e: [ my     Hun |
|                 |                 |                 | garian: [ hu    |
|                 |                 |                 | Pashto: [ ps    |
|                 |                 |                 |    Telugu: [ te |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Croa          |
|                 |                 |                 | tian: [ hr    I |
|                 |                 |                 | celandic: [ is  |
|                 |                 |                 |   Persian: [ fa |
|                 |                 |                 |      Thai: [ th |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Catalan       |
|                 |                 |                 | : [ ca     Indo |
|                 |                 |                 | nesian: [ in  P |
|                 |                 |                 | olish: [ pl     |
|                 |                 |                 |   Tibetan: [ bo |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Czech         |
|                 |                 |                 | : [ cs       It |
|                 |                 |                 | alian: [ it     |
|                 |                 |                 |  Portuguese: [  |
|                 |                 |                 | pt  Traditional |
|                 |                 |                 |   ]{.code-in    |
|                 |                 |                 | line}   ]{.code |
|                 |                 |                 | -inline}   ]{.c |
|                 |                 |                 | ode-inline}   C |
|                 |                 |                 | hinese: [ zh-TW |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Danish:       |
|                 |                 |                 |  [ da      Japa |
|                 |                 |                 | nese: [ ja    R |
|                 |                 |                 | omanian: [ ro   |
|                 |                 |                 |   Turkish: [ tr |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Dutch: [      |
|                 |                 |                 | nl       Kannad |
|                 |                 |                 | a: [ kn     Rus |
|                 |                 |                 | sian: [ ru      |
|                 |                 |                 | Ukrainian: [ uk |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Engl          |
|                 |                 |                 | ish: [ en     K |
|                 |                 |                 | hmer: [ km      |
|                 |                 |                 |   Serbian: [ sr |
|                 |                 |                 |      Urdu: [ ur |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Estoni        |
|                 |                 |                 | an: [ et    Kor |
|                 |                 |                 | ean: [ ko       |
|                 |                 |                 | Simplified      |
|                 |                 |                 |    Uyghur: [ ug |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   Chi |
|                 |                 |                 | nese: [ zh-CN   |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |             ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 |                 |
|                 |                 |                 |   Finnish: [    |
|                 |                 |                 |  fi     Lao: [  |
|                 |                 |                 | lo         Sind |
|                 |                 |                 | hi: [ sd      V |
|                 |                 |                 | ietnamese: [ vi |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Frenc         |
|                 |                 |                 | h: [ fr      La |
|                 |                 |                 | tvian: [ lv     |
|                 |                 |                 |  Sinhala: [ si  |
|                 |                 |                 |     Welsh: [ cy |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}   ]{. |
|                 |                 |                 | code-inline}    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 |   Georgian:     |
|                 |                 |                 |  [ ka    Lithua |
|                 |                 |                 | nian: [ lt      |
|                 |                 |                 |                 |
|                 |                 |                 |   ]{.code-i     |
|                 |                 |                 | nline}   ]{.cod |
|                 |                 |                 | e-inline}       |
|                 |                 |                 |                 |
|                 |                 |                 |   ------------  |
|                 |                 |                 | ----- --------- |
|                 |                 |                 | -------- ------ |
|                 |                 |                 | ----------- --- |
|                 |                 |                 | --------------- |
+-----------------+-----------------+-----------------+-----------------+
| [               |                 | Essential       | Matches Tweets  |
| f               |                 |                 | when the author |
| ollowers_count: |                 |                 | has a followers |
| ]{.code-inline} |                 |                 | count within    |
|                 |                 |                 | the given       |
|                 |                 |                 | range.          |
|                 |                 |                 |                 |
|                 |                 |                 | If a single     |
|                 |                 |                 | number is       |
|                 |                 |                 | specified, any  |
|                 |                 |                 | number equal to |
|                 |                 |                 | or higher will  |
|                 |                 |                 | match.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | foll            |
|                 |                 |                 | owers_count:500 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Additionally, a |
|                 |                 |                 | range can be    |
|                 |                 |                 | specified to    |
|                 |                 |                 | match any       |
|                 |                 |                 | number in the   |
|                 |                 |                 | given range.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | followers_co    |
|                 |                 |                 | unt:1000..10000 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ tweets_count: |                 | Essential       | [ *Available    |
| ]{.code-inline} |                 |                 | alias:*         |
|                 |                 |                 | statuses_count: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | when the author |
|                 |                 |                 | has posted a    |
|                 |                 |                 | number of       |
|                 |                 |                 | Tweets that     |
|                 |                 |                 | falls within    |
|                 |                 |                 | the given       |
|                 |                 |                 | range.          |
|                 |                 |                 |                 |
|                 |                 |                 | If a single     |
|                 |                 |                 | number is       |
|                 |                 |                 | specified, any  |
|                 |                 |                 | number equal to |
|                 |                 |                 | or higher will  |
|                 |                 |                 | match.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | tw              |
|                 |                 |                 | eets_count:1000 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Additionally, a |
|                 |                 |                 | range can be    |
|                 |                 |                 | specified to    |
|                 |                 |                 | match any       |
|                 |                 |                 | number in the   |
|                 |                 |                 | given range.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | tweets_co       |
|                 |                 |                 | unt:1000..10000 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [               |                 | Essential       | [ *Available    |
| f               |                 |                 | alias:*         |
| ollowing_count: |                 |                 | friends_count:  |
| ]{.code-inline} |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | when the author |
|                 |                 |                 | has a friends   |
|                 |                 |                 | count (the      |
|                 |                 |                 | number of users |
|                 |                 |                 | they follow)    |
|                 |                 |                 | that falls      |
|                 |                 |                 | within the      |
|                 |                 |                 | given range.    |
|                 |                 |                 |                 |
|                 |                 |                 | If a single     |
|                 |                 |                 | number is       |
|                 |                 |                 | specified, any  |
|                 |                 |                 | number equal to |
|                 |                 |                 | or higher will  |
|                 |                 |                 | match.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | foll            |
|                 |                 |                 | owing_count:500 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Additionally, a |
|                 |                 |                 | range can be    |
|                 |                 |                 | specified to    |
|                 |                 |                 | match any       |
|                 |                 |                 | number in the   |
|                 |                 |                 | given range.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | following_co    |
|                 |                 |                 | unt:1000..10000 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ listed_count: |                 | Essential       | [ *Available    |
| ]{.code-inline} |                 |                 | alias:*         |
|                 |                 |                 | user_           |
|                 |                 |                 | in_lists_count: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Matches Tweets  |
|                 |                 |                 | when the author |
|                 |                 |                 | is included in  |
|                 |                 |                 | the specified   |
|                 |                 |                 | number of       |
|                 |                 |                 | Lists.          |
|                 |                 |                 |                 |
|                 |                 |                 | If a single     |
|                 |                 |                 | number is       |
|                 |                 |                 | specified, any  |
|                 |                 |                 | number equal to |
|                 |                 |                 | or higher will  |
|                 |                 |                 | match.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | listed_count:10 |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Additionally, a |
|                 |                 |                 | range can be    |
|                 |                 |                 | specified to    |
|                 |                 |                 | match any       |
|                 |                 |                 | number in the   |
|                 |                 |                 | given range.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | liste           |
|                 |                 |                 | d_count:10..100 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ url_title:    |                 | Essential       | [ *Available    |
| ]{.code-inline} |                 |                 | alias:*         |
|                 |                 |                 | wi              |
|                 |                 |                 | thin_url_title: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Performs a      |
|                 |                 |                 | keyword/phrase  |
|                 |                 |                 | match on the    |
|                 |                 |                 | expanded URL    |
|                 |                 |                 | HTML title      |
|                 |                 |                 | metadata.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | url_title:snow  |
|                 |                 |                 | ]               |
|                 |                 |                 | {.code-inline}\ |
+-----------------+-----------------+-----------------+-----------------+
| [               |                 | Essential       | [ *Available    |
| u               |                 |                 | alias:*         |
| rl_description: |                 |                 | within_u        |
| ]{.code-inline} |                 |                 | rl_description: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Performs a      |
|                 |                 |                 | keyword/phrase  |
|                 |                 |                 | match on the    |
|                 |                 |                 | expanded page   |
|                 |                 |                 | description     |
|                 |                 |                 | metadata.       |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | url_desc        |
|                 |                 |                 | ription:weather |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ url_contains: |                 | Essential       | Matches Tweets  |
| ]{.code-inline} |                 |                 | with URLs that  |
|                 |                 |                 | literally       |
|                 |                 |                 | contain the     |
|                 |                 |                 | given phrase or |
|                 |                 |                 | keyword. To     |
|                 |                 |                 | search for      |
|                 |                 |                 | patterns with   |
|                 |                 |                 | punctuation in  |
|                 |                 |                 | them (i.e.      |
|                 |                 |                 | google.com)     |
|                 |                 |                 | enclose the     |
|                 |                 |                 | search term in  |
|                 |                 |                 | quotes.         |
|                 |                 |                 |                 |
|                 |                 |                 | NOTE: This will |
|                 |                 |                 | match against   |
|                 |                 |                 | the expanded    |
|                 |                 |                 | URL as well.    |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | url_            |
|                 |                 |                 | contains:photos |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [ source:       |                 | Essential       | Matches any     |
| ]{.code-inline} |                 |                 | Tweet generated |
|                 |                 |                 | by the given    |
|                 |                 |                 | source          |
|                 |                 |                 | application.    |
|                 |                 |                 | The value must  |
|                 |                 |                 | be either the   |
|                 |                 |                 | name of the     |
|                 |                 |                 | application or  |
|                 |                 |                 | the             |
|                 |                 |                 | application's   |
|                 |                 |                 | URL. Cannot be  |
|                 |                 |                 | used alone.     |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | s               |
|                 |                 |                 | ource:\"Twitter |
|                 |                 |                 | for iPhone\"    |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Note: As a      |
|                 |                 |                 | Twitter app     |
|                 |                 |                 | developer,      |
|                 |                 |                 | Tweets created  |
|                 |                 |                 | p               |
|                 |                 |                 | rogrammatically |
|                 |                 |                 | by your         |
|                 |                 |                 | application     |
|                 |                 |                 | will have the   |
|                 |                 |                 | source of your  |
|                 |                 |                 | application     |
|                 |                 |                 | Name and        |
|                 |                 |                 | Website URL set |
|                 |                 |                 | in your [app    |
|                 |                 |                 | settings](htt   |
|                 |                 |                 | ps://developer. |
|                 |                 |                 | twitter.com/en/ |
|                 |                 |                 | docs/apps/app-m |
|                 |                 |                 | anagement.html) |
|                 |                 |                 | .               |
+-----------------+-----------------+-----------------+-----------------+
| [               |                 | Essential       | [ *Available    |
| in_rep          |                 |                 | alias:*         |
| ly_to_tweet_id: |                 |                 | in_repl         |
| ]{.code-inline} |                 |                 | y_to_status_id: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Deliver only    |
|                 |                 |                 | explicit        |
|                 |                 |                 | Replies to the  |
|                 |                 |                 | specified       |
|                 |                 |                 | Tweet.          |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | in_reply_t      |
|                 |                 |                 | o_tweet_id:1539 |
|                 |                 |                 | 382664746020864 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+
| [               |                 | Essential       | [ *Available    |
| retwee          |                 |                 | alias:*         |
| ts_of_tweet_id: |                 |                 | retweet         |
| ]{.code-inline} |                 |                 | s_of_status_id: |
|                 |                 |                 | ]{.code-inline} |
|                 |                 |                 |                 |
|                 |                 |                 | Deliver only    |
|                 |                 |                 | explicit (or    |
|                 |                 |                 | native)         |
|                 |                 |                 | Retweets of the |
|                 |                 |                 | specified       |
|                 |                 |                 | Tweet. Note     |
|                 |                 |                 | that the status |
|                 |                 |                 | ID used should  |
|                 |                 |                 | be the ID of an |
|                 |                 |                 | original Tweet  |
|                 |                 |                 | and not a       |
|                 |                 |                 | Retweet.        |
|                 |                 |                 |                 |
|                 |                 |                 | Example: [      |
|                 |                 |                 | retweets_o      |
|                 |                 |                 | f_tweet_id:1539 |
|                 |                 |                 | 382664746020864 |
|                 |                 |                 | ]{.code-inline} |
+-----------------+-----------------+-----------------+-----------------+

</div>
:::
:::
