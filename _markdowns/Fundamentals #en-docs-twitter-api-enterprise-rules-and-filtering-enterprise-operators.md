::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Below are the operators available with PowerTrack and Historical
PowerTrack. A subset of these are available with the 30-Day and
Full-Archive search APIs. See [this
table](/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product)
for a product-by-product list of available operators.
:::
:::

::: c01-rich-text-editor
<div>

+-----------------------------------+-----------------------------------+
| **Operator**\                     | Description                       |
+-----------------------------------+-----------------------------------+
| keyword\                          | Matches a keyword within the text |
|                                   | body or URL of a Tweet. Keywords  |
|                                   | must start with either a digit    |
|                                   | (0-9) or any non-puncutation      |
|                                   | character.  Keyword matching is a |
|                                   | tokenized match, meaning that     |
|                                   | your keyword will be matched      |
|                                   | against the tokenized text of the |
|                                   | Tweet body -- tokenization is     |
|                                   | based on punctuation, symbol, and |
|                                   | separator Unicode basic plane     |
|                                   | characters.  To match strings     |
|                                   | containing punctuation (for       |
|                                   | example, coca-cola), symbol, or   |
|                                   | separator characters, you must    |
|                                   | use a quoted \"exact phrase       |
|                                   | match\". Example:                 |
|                                   |                                   |
|                                   | [ (social OR pizza OR wildfire)   |
|                                   | -planet\                          |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | \                                 |
|                                   | **Note:** With the Search         |
|                                   | API, accented and special         |
|                                   | characters are normalized to      |
|                                   | standard latin characters, which  |
|                                   | can change meanings in foreign    |
|                                   | languages or return unexpected    |
|                                   | results:\                         |
|                                   | For example, \"músic\" will match |
|                                   | "music" and vice versa.\          |
|                                   | For example, common phrases like  |
|                                   | \"Feliz Año Nuevo!\" in Spanish,  |
|                                   | would be indexed as \"Feliz Ano   |
|                                   | Nuevo\", which changes the        |
|                                   | meaning of the phrase.            |
|                                   |                                   |
|                                   | **Note:** This operator will      |
|                                   | match on both URLs and unwound    |
|                                   | URLs within a Tweet. \            |
+-----------------------------------+-----------------------------------+
| emoji\                            | Matches an emoji within the body  |
|                                   | of a Tweet. Emojis are a          |
|                                   | tokenized match, meaning that     |
|                                   | your emoji will be matched        |
|                                   | against the tokenized text of the |
|                                   | Tweet body -- tokenization is     |
|                                   | based on punctuation,             |
|                                   | symbol/emoji, and separator       |
|                                   | Unicode basic plane characters.   |
|                                   | For example, a Tweet with the     |
|                                   | text "I like 🍕" would be split   |
|                                   | into the following tokens: I,     |
|                                   | like, 🍕. These tokens would then |
|                                   | be compared to the emoji used in  |
|                                   | your rule. Note that if an emoji  |
|                                   | has a variant, you must use       |
|                                   | "quotations" to add to a rule.    |
|                                   | Example:                          |
|                                   |                                   |
|                                   | [ (🍕 OR 💜 OR 🐢) -🤖            |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | \                                 |
+-----------------------------------+-----------------------------------+
| \"exact phrase match\"\           | Matches an exact phrase within    |
|                                   | the body of a Tweet.              |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (\"social media\" OR            |
|                                   | \"developer.twitter.com\" OR      |
|                                   | \"wildfire911\" OR \"coca-cola\") |
|                                   | -\"planet earth\" ]{.code-inline} |
|                                   |                                   |
|                                   | **Note:** In 30 Day Search and    |
|                                   | Full Archive Search, punctuation  |
|                                   | is not tokenized and is instead   |
|                                   | treated as whitespace. For        |
|                                   | example, quoted "#hashtag" will   |
|                                   | match "hashtag" but not #hashtag  |
|                                   | (use the hashtag \# operator      |
|                                   | without quotes to match on actual |
|                                   | hashtags)                         |
|                                   |                                   |
|                                   | For example, quoted "\$cashtag"   |
|                                   | will match "cashtag" but not      |
|                                   | \$cashtag (use the cashtag \$     |
|                                   | operator without quotes to match  |
|                                   | on actual cashtags)               |
|                                   |                                   |
|                                   | **Note:** This operator will      |
|                                   | match on both URLs and unwound    |
|                                   | URLs within a Tweet.              |
+-----------------------------------+-----------------------------------+
| \#\                               | Matches any Tweet with the given  |
|                                   | hashtag.                          |
|                                   |                                   |
|                                   | This operator performs an exact   |
|                                   | match, NOT a tokenized match,     |
|                                   | meaning the rule "2016" will      |
|                                   | match posts with the exact        |
|                                   | hashtag "2016", but not those     |
|                                   | with the hashtag "2016election"   |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (#social OR #pizza OR           |
|                                   | #2016election) -#planet           |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note** : that the hashtag       |
|                                   | operator relies on Twitter's      |
|                                   | entity extraction to match        |
|                                   | hashtags, rather than extracting  |
|                                   | the hashtag from the body         |
|                                   | itself. See                       |
|                                   | [HERE](/content                   |
|                                   | /developer-twitter/en/docs/twitte |
|                                   | r-api/enterprise/data-dictionary/ |
|                                   | native-enriched-objects/entities) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.         |
+-----------------------------------+-----------------------------------+
| @\                                | Matches any Tweet that mentions   |
|                                   | the given username.               |
|                                   |                                   |
|                                   | The to: operator returns a subset |
|                                   | match of the \@mention operator.  |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (@twitterdev OR \@twitterapi OR |
|                                   | \@twittereng) -@jack              |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note** : that the mention       |
|                                   | operator relies on Twitter's      |
|                                   | entity extraction to match        |
|                                   | mentioned users, rather than      |
|                                   | extracting the mention from the   |
|                                   | body itself. See                  |
|                                   | [HERE](/content                   |
|                                   | /developer-twitter/en/docs/twitte |
|                                   | r-api/enterprise/data-dictionary/ |
|                                   | native-enriched-objects/entities) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.\        |
+-----------------------------------+-----------------------------------+
| \"keyword1 keyword2\"\~N\         | Commonly referred to as a         |
|                                   | proximity operator, this matches  |
|                                   | a Tweet where the keywords are no |
|                                   | more than N tokens from each      |
|                                   | other.                            |
|                                   |                                   |
|                                   | If the keywords are in the        |
|                                   | opposite order, they can not be   |
|                                   | more than N-2 tokens from each    |
|                                   | other.                            |
|                                   |                                   |
|                                   | Can have any number of keywords   |
|                                   | in quotes.                        |
|                                   |                                   |
|                                   | N cannot be greater than 6.       |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ \"social media\"\~5 OR          |
|                                   | \"twitter API\"\~3                |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | [\                                |
|                                   | ]{.code-inline} **Note** : Only   |
|                                   | available with PowerTrack and     |
|                                   | Historical PowerTrack.            |
+-----------------------------------+-----------------------------------+
| contains:                         | Substring match for Tweets that   |
|                                   | have the given substring in the   |
|                                   | body, regardless of tokenization. |
|                                   | In other words, this does a pure  |
|                                   | substring match, and does not     |
|                                   | consider word boundaries.         |
|                                   |                                   |
|                                   | Use double quotes to match        |
|                                   | substrings that contain           |
|                                   | whitespace or punctuation.        |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (contains:social OR             |
|                                   | contains:\"wikipedia.com\")       |
|                                   | -contains:\"buy now\"             |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note** : Only available with    |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| from:\                            | Matches any Tweet from a specific |
|                                   | user.                             |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (from:2244994945 OR             |
|                                   | from:twitterapi OR                |
|                                   | from:twittereng) -from:jack       |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | The value must be the user's      |
|                                   | Twitter numeric Account ID or     |
|                                   | username (excluding the @         |
|                                   | character). See                   |
|                                   | [HERE](/en/docs/accounts          |
|                                   | -and-users/follow-search-get-user |
|                                   | s/api-reference/get-users-lookup) |
|                                   | for looking up numeric Twitter    |
|                                   | Account IDs.                      |
+-----------------------------------+-----------------------------------+
| to:\                              | Matches any Tweet that is in      |
|                                   | reply to a particular user.       |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (to:2244994945 OR to:twitterapi |
|                                   | OR to:twittereng) -to:jack        |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | The value must be the user's      |
|                                   | numeric Account ID or username    |
|                                   | (excluding the @ character). See  |
|                                   | [HERE](/en/docs/accounts          |
|                                   | -and-users/follow-search-get-user |
|                                   | s/api-reference/get-users-lookup) |
|                                   | for looking up numeric Twitter    |
|                                   | Account IDs.\                     |
+-----------------------------------+-----------------------------------+
| url:\                             | Performs a tokenized              |
|                                   | (keyword/phrase) match on the     |
|                                   | expanded URLs of a Tweet (similar |
|                                   | to url_contains). Example:        |
|                                   |                                   |
|                                   | [ \@twitterdev                    |
|                                   | url:\"developer.twitter.com\"\    |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | \                                 |
|                                   | **Note:** When using PowerTrack   |
|                                   | or Historical PowerTrack, this    |
|                                   | operator will match on URLs       |
|                                   | contained within the original     |
|                                   | Tweet of a Quote Tweet. For       |
|                                   | example, if your rule includes    |
|                                   | url:\"developer.twitter.com\",    |
|                                   | and a Tweet contains that URL,    |
|                                   | any Quote Tweets of that Tweet    |
|                                   | will be included in the results.  |
|                                   | This is not the case when using   |
|                                   | the Search API.\                  |
+-----------------------------------+-----------------------------------+
| url_title:\                       | *Available alias* :               |
|                                   | within_url_title:                 |
|                                   |                                   |
|                                   | Performs a keyword/phrase match   |
|                                   | on the (new) expanded URL HTML    |
|                                   | title metadata. See               |
|                                   | [HERE](/en/docs/twitt             |
|                                   | er-api/enterprise/enrichments/ove |
|                                   | rview/expanded-and-enhanced-urls) |
|                                   | for more information on expanded  |
|                                   | URL enrichment.                   |
|                                   |                                   |
|                                   | **Note** : Only available with    |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| url_description:\                 | *Available alias* :               |
|                                   | within_url_description:           |
|                                   |                                   |
|                                   | Performs a keyword/phrase match   |
|                                   | on the (new) expanded page        |
|                                   | description metadata. See         |
|                                   | [HERE](/en/docs/twitt             |
|                                   | er-api/enterprise/enrichments/ove |
|                                   | rview/expanded-and-enhanced-urls) |
|                                   | for more information on expanded  |
|                                   | URL enrichment.                   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| url_contains:\                    | Matches Tweets with URLs that     |
|                                   | literally contain the given       |
|                                   | phrase or keyword. To search for  |
|                                   | patterns with punctuation in them |
|                                   | (for example, google.com) enclose |
|                                   | the search term in quotes.        |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [                                 |
|                                   | (url_c                            |
|                                   | ontains:\"developer.twitter.com\" |
|                                   | OR url_contains:wildfire)         |
|                                   | -url_contains:reddit              |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note** : If you're using the    |
|                                   | [Expanded                         |
|                                   | URL](/en/docs/twitt               |
|                                   | er-api/enterprise/enrichments/ove |
|                                   | rview/expanded-and-enhanced-urls) |
|                                   | output format, we will match      |
|                                   | against the expanded URL as well. |
+-----------------------------------+-----------------------------------+
| bio:\                             | *Available alias* : user_bio:     |
|                                   |                                   |
|                                   | Matches a keyword or phrase       |
|                                   | within the user bio of a Tweet.   |
|                                   | This is a tokenized match within  |
|                                   | the contents of the               |
|                                   | \'description\' field within the  |
|                                   | [User                             |
|                                   | object](/con                      |
|                                   | tent/developer-twitter/en/docs/tw |
|                                   | itter-api/enterprise/data-diction |
|                                   | ary/native-enriched-objects/user) |
|                                   | . Example:                        |
|                                   |                                   |
|                                   | [ (bio:engineer OR                |
|                                   | bio:\"wordpress.com\" OR bio:🚀)  |
|                                   | -bio:troll ]{.code-inline}        |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| bio_name:\                        | Matches a keyword within the user |
|                                   | bio name of a Tweet. This is a    |
|                                   | tokenized match within the        |
|                                   | contents of a user's "name" field |
|                                   | within the [User                  |
|                                   | object](/con                      |
|                                   | tent/developer-twitter/en/docs/tw |
|                                   | itter-api/enterprise/data-diction |
|                                   | ary/native-enriched-objects/user) |
|                                   | .                                 |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| bio_location:\                    | *Available alias* :               |
|                                   | user_bio_location:                |
|                                   |                                   |
|                                   | Matches tweets where the User     |
|                                   | object\'s location contains the   |
|                                   | specified keyword or phrase. This |
|                                   | operator performs a tokenized     |
|                                   | match, similar to the normal      |
|                                   | keyword rules on the message      |
|                                   | body.                             |
|                                   |                                   |
|                                   | This location is part of the      |
|                                   | [User                             |
|                                   | object](/con                      |
|                                   | tent/developer-twitter/en/docs/tw |
|                                   | itter-api/enterprise/data-diction |
|                                   | ary/native-enriched-objects/user) |
|                                   | , and is the account\'s \'home\'  |
|                                   | lcoation, is a non-normalized,    |
|                                   | user-generated, free-form string, |
|                                   | and is different from a Tweet\'s  |
|                                   | location (when available).        |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| statuses_count:\                  | *Available alias* : tweets_count: |
|                                   |                                   |
|                                   | Matches Tweets when the author    |
|                                   | has posted a number of statuses   |
|                                   | that falls within the given       |
|                                   | range.                            |
|                                   |                                   |
|                                   | If a single number is specified,  |
|                                   | any number equal to or higher     |
|                                   | will match.                       |
|                                   |                                   |
|                                   | Additionally, a range can be      |
|                                   | specified to match any number in  |
|                                   | the given range  (for example,    |
|                                   | statuses_count:1000..10000).\     |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ to:twitterapi statuses_count:10 |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | [ \@twitterdev                    |
|                                   | statuses_count:1..10              |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| followers_count:\                 | Matches Tweets when the author    |
|                                   | has a followers count within the  |
|                                   | given range.                      |
|                                   |                                   |
|                                   | If a single number is specified,  |
|                                   | any number equal to or higher     |
|                                   | will match.                       |
|                                   |                                   |
|                                   | Additionally, a range can be      |
|                                   | specified to match any number in  |
|                                   | the given range (for example,     |
|                                   | followers_count:1000..10000).\'   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| friends_count:\                   | *Available alias* :               |
|                                   | following_count:                  |
|                                   |                                   |
|                                   | Matches Tweets when the author    |
|                                   | has a friends count (the number   |
|                                   | of users they follow) that falls  |
|                                   | within the given range.           |
|                                   |                                   |
|                                   | If a single number is specified,  |
|                                   | any number equal to or higher     |
|                                   | will match.                       |
|                                   |                                   |
|                                   | Additionally, a range can be      |
|                                   | specified to match any number in  |
|                                   | the given range (for example,     |
|                                   | friends_count:1000..10000).       |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| listed_count:\                    | *Available alias* :               |
|                                   | user_in_lists_count:              |
|                                   |                                   |
|                                   | Matches Tweets when the author    |
|                                   | has been listed within Twitter a  |
|                                   | number of times falls within the  |
|                                   | given range.                      |
|                                   |                                   |
|                                   | If a single number is specified,  |
|                                   | any number equal to or higher     |
|                                   | will match.                       |
|                                   |                                   |
|                                   | Additionally, a range can be      |
|                                   | specified to match any number in  |
|                                   | the given range (for example,     |
|                                   | listed_count:10..100).            |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.\                      |
+-----------------------------------+-----------------------------------+
| \$                                | Matches any Tweet that contains   |
|                                   | the specified 'cashtag' entity.   |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (\$TWTR OR \$TSLA OR \$BRK.A)   |
|                                   | -\$F ]{.code-inline}              |
|                                   |                                   |
|                                   | **Note** : The cashtag operator   |
|                                   | relies on Twitter's 'symbols'     |
|                                   | entity extraction to match        |
|                                   | cashtags, rather than trying to   |
|                                   | extract the cashtag from the body |
|                                   | itself. See                       |
|                                   | [HERE](/content                   |
|                                   | /developer-twitter/en/docs/twitte |
|                                   | r-api/enterprise/data-dictionary/ |
|                                   | native-enriched-objects/entities) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.         |
+-----------------------------------+-----------------------------------+
| retweets_of:\                     | *Available alias* :               |
|                                   | retweets_of_user:                 |
|                                   |                                   |
|                                   | Matches Tweets that are Retweets  |
|                                   | of a specified user. Accepts both |
|                                   | usernames and numeric Twitter     |
|                                   | Account IDs (NOT Tweet status     |
|                                   | IDs). Example:                    |
|                                   |                                   |
|                                   | [ (retweets_of:2244994945 OR      |
|                                   | retweets_of:twitterapi OR         |
|                                   | retweets_of:twittereng)           |
|                                   | -retweets_of:jack ]{.code-inline} |
|                                   |                                   |
|                                   | See                               |
|                                   | [HERE](https://dev.twitter.com    |
|                                   | /rest/reference/get/users/lookup) |
|                                   | for looking up numeric Twitter    |
|                                   | Account IDs.                      |
|                                   |                                   |
|                                   | \                                 |
+-----------------------------------+-----------------------------------+
| retweets_of_status_id:\           | *Available alias* :               |
|                                   | retweets_of_tweet_id:             |
|                                   |                                   |
|                                   | Deliver only explicit Retweets of |
|                                   | the specified Tweet. Note that    |
|                                   | the status ID used should be the  |
|                                   | ID of an original Tweet and not a |
|                                   | Retweet. Example:                 |
|                                   |                                   |
|                                   | [                                 |
|                                   | retweets                          |
|                                   | _of_status_id:1293593516040269825 |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| in_reply_to_status_id:\           | *Available alias* :               |
|                                   | in_reply_to_tweet_id:             |
|                                   |                                   |
|                                   | Deliver only explicit replies to  |
|                                   | the specified Tweet. Example:     |
|                                   |                                   |
|                                   | [                                 |
|                                   | in_reply                          |
|                                   | _to_status_id:1293593516040269825 |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| sample:                           | Returns a random sample of Tweets |
|                                   | that match a rule rather than the |
|                                   | entire set of Tweets. Sample      |
|                                   | percent must be represented by an |
|                                   | integer value between 1 and 100.  |
|                                   | This operator applies to the      |
|                                   | entire rule and requires any      |
|                                   | "OR'd" terms be grouped.          |
|                                   |                                   |
|                                   | **Important Note:** The sample    |
|                                   | operator first reduces the scope  |
|                                   | of the firehose to X%, then the   |
|                                   | rule/filter is applied tio that   |
|                                   | sampled subset. If you are using, |
|                                   | for example, **sample:10** , each |
|                                   | Tweet has a 10% chance of being   |
|                                   | in the sample.                    |
|                                   |                                   |
|                                   | The sampling is deterministic,    |
|                                   | and you will get the same data    |
|                                   | sample in realtime as you would   |
|                                   | if you pulled the data            |
|                                   | historically.                     |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ #happybirthday sample:5         |
|                                   | ]{.code-inline}\                  |
|                                   | [ \"happy birthday\"\~5 sample:80 |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** Only available with     |
|                                   | PowerTrack and Historical         |
|                                   | PowerTrack.                       |
+-----------------------------------+-----------------------------------+
| source:                           | Matches any Tweet generated by    |
|                                   | the given source application. The |
|                                   | value must be either the name of  |
|                                   | the application, or the           |
|                                   | application's URL. **Cannot be    |
|                                   | used alone.\                      |
|                                   | ** Example:                       |
|                                   |                                   |
|                                   | [ #happybirthday source:\"Twitter |
|                                   | for iPhone\" ]{.code-inline}      |
|                                   |                                   |
|                                   | \                                 |
|                                   | [ \"This is a test Tweet from my  |
|                                   | TestingApp\"                      |
|                                   | source:MyTestAppName\             |
|                                   | ]{.code-inline}\                  |
|                                   | **Note** : As a Twitter app       |
|                                   | developer, Tweets created         |
|                                   | programattically by your          |
|                                   | application will have the source  |
|                                   | of your application Name and      |
|                                   | Website URL set in your [app      |
|                                   | settings](/                       |
|                                   | en/docs/apps/app-management.html) |
|                                   | . The source operator seraches on |
|                                   | the Tweet source attribute.  See  |
|                                   | [HERE](/content                   |
|                                   | /developer-twitter/en/docs/twitte |
|                                   | r-api/enterprise/data-dictionary/ |
|                                   | native-enriched-objects/entities) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.\        |
+-----------------------------------+-----------------------------------+
| lang:\                            | Matches Tweets that have been     |
|                                   | classified by Twitter as being of |
|                                   | a particular language (if, and    |
|                                   | only if, the tweet has been       |
|                                   | classified). It is important to   |
|                                   | note that each Tweet is currently |
|                                   | only classified as being of one   |
|                                   | language, so AND'ing together     |
|                                   | multiple languages will yield no  |
|                                   | results. This operator is not     |
|                                   | recommended to be used alone,     |
|                                   | matching volume will be very      |
|                                   | high.                             |
|                                   |                                   |
|                                   | The list below represents the     |
|                                   | current supported languages and   |
|                                   | their corresponding BCP 47        |
|                                   | language indentifier:             |
|                                   |                                   |
|                                   |   ------------ --------           |
|                                   | ----- ------------- ------------- |
|                                   |   Amharic: am  Germa              |
|                                   | n: de    Malayalam: ml Slovak: sk |
|                                   |                                   |
|                                   |   Arabic: ar   Greek: e           |
|                                   | l     Maldivian: dv Slovenian: sl |
|                                   |                                   |
|                                   |   Armenian: hy G                  |
|                                   | ujarati: gu  Marathi: mr   Sorani |
|                                   |                                   |
|                                   |                     Kurdish: ckb\ |
|                                   |                                   |
|                                   |   Basque: eu   Haitia             |
|                                   | n       Nepali: ne    Spanish: es |
|                                   |                                   |
|                                   |      Creole: ht                   |
|                                   |                                   |
|                                   |   Bengali: bn  Hebrew             |
|                                   | : iw    Norwegian: no Swedish: sv |
|                                   |                                   |
|                                   |   Bosnian: bs  Hindi:             |
|                                   |  hi     Oriya: or     Tagalog: tl |
|                                   |                                   |
|                                   |   Bulgarian:   Lati               |
|                                   | nized     Panjabi: pa   Tamil: ta |
|                                   |   bg                              |
|                                   |      Hindi:                       |
|                                   |                                   |
|                                   |      hi-Latn                      |
|                                   |                                   |
|                                   |   Burmese: my  Hunga              |
|                                   | rian: hu Pashto: ps    Telugu: te |
|                                   |                                   |
|                                   |   Croatian: hr Ice                |
|                                   | landic: is Persian: fa   Thai: th |
|                                   |                                   |
|                                   |   Catalan: ca  Indone             |
|                                   | sian:   Polish: pl    Tibetan: bo |
|                                   |                                   |
|                                   |      in                           |
|                                   |                                   |
|                                   |   Czech: cs    Italia             |
|                                   | n: it   Portuguese:   Traditional |
|                                   |                                   |
|                                   |            pt            Chinese: |
|                                   |                                   |
|                                   |                             zh-TW |
|                                   |                                   |
|                                   |   Danish: da   Japane             |
|                                   | se: ja  Romanian: ro  Turkish: tr |
|                                   |                                   |
|                                   |   Dutch: nl    Kannada:           |
|                                   |  kn   Russian: ru   Ukrainian: uk |
|                                   |                                   |
|                                   |   English: en  Khm                |
|                                   | er: km     Serbian: sr   Urdu: ur |
|                                   |                                   |
|                                   |   Estonian: et Korea              |
|                                   | n: ko    Simplified    Uyghur: ug |
|                                   |                                   |
|                                   |                    Chinese:       |
|                                   |                                   |
|                                   |                    zh-CN          |
|                                   |                                   |
|                                   |   Finnish: fi  Lao: l             |
|                                   | o       Sindhi: sd    Vietnamese: |
|                                   |                                   |
|                                   |                                vi |
|                                   |                                   |
|                                   |   French: fr   Latv               |
|                                   | ian: lv   Sinhala: si   Welsh: cy |
|                                   |                                   |
|                                   |   Georgian                        |
|                                   | : ka Lithuanian:                  |
|                                   |                                   |
|                                   |      lt                           |
|                                   |   ------------ --------           |
|                                   | ----- ------------- ------------- |
|                                   |                                   |
|                                   | Example: \                        |
|                                   |                                   |
|                                   | [ (@twitterdev OR to:twitterdev)  |
|                                   | lang:es ]{.code-inline}\          |
|                                   |                                   |
|                                   | **Note:** The language operator   |
|                                   | matches on the specific Tweet     |
|                                   | language determined by Twitter    |
|                                   | and set as the lang Tweet         |
|                                   | attribute.  See                   |
|                                   | [HERE](/content                   |
|                                   | /developer-twitter/en/docs/twitte |
|                                   | r-api/enterprise/data-dictionary/ |
|                                   | native-enriched-objects/entities) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.  If no  |
|                                   | language classification can be    |
|                                   | made for a Tweet, the Tweet lang  |
|                                   | will be set as 'und' (for         |
|                                   | undefined).                       |
+-----------------------------------+-----------------------------------+
| place:\                           | Matches Tweets tagged with the    |
|                                   | specified location *or* Twitter   |
|                                   | place ID (see examples).          |
|                                   | Multi-word place names ("New York |
|                                   | City", "Palo Alto") should be     |
|                                   | enclosed in quotes.               |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ (place:London OR place:\"Great  |
|                                   | Britain\") -place:USA             |
|                                   | ]{.code-inline}\                  |
|                                   | [ place:fd70c22040963ac7          |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** See the [GET            |
|                                   | geo/searc                         |
|                                   | h](/en/docs/geo/places-near-locat |
|                                   | ion/api-reference/get-geo-search) |
|                                   | public API endpoint for how to    |
|                                   | obtain Twitter place IDs.         |
|                                   |                                   |
|                                   | **Note:** This operator will not  |
|                                   | match on Retweets, since          |
|                                   | Retweet\'s places are attached to |
|                                   | the original Tweet. It will also  |
|                                   | not match on places attached to   |
|                                   | the original Tweet of a Quote     |
|                                   | Tweet.                            |
+-----------------------------------+-----------------------------------+
| place_country:\                   | Matches Tweets where the country  |
|                                   | code associated with a tagged     |
|                                   | [place/location](/co              |
|                                   | ntent/developer-twitter/en/docs/t |
|                                   | witter-api/enterprise/data-dictio |
|                                   | nary/native-enriched-objects/geo) |
|                                   | matches the given ISO alpha-2     |
|                                   | character code.                   |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ place_country:GB OR             |
|                                   | place_country:AU OR               |
|                                   | place_country:CA ]{.code-inline}\ |
|                                   |                                   |
|                                   | Valid ISO codes can be found      |
|                                   | here:                             |
|                                   | <http://en.wikip                  |
|                                   | edia.org/wiki/ISO_3166-1_alpha-2> |
|                                   |                                   |
|                                   | **Note:** This operator will not  |
|                                   | match on Retweets, since          |
|                                   | Retweet\'s places are attached to |
|                                   | the original Tweet. It will also  |
|                                   | not match on places attached to   |
|                                   | the original Tweet of a Quote     |
|                                   | Tweet.                            |
+-----------------------------------+-----------------------------------+
| point_radius:\[lon lat radius\]\  | Matches against the Exact         |
|                                   | Location (x,y) of the Tweet when  |
|                                   | present, and in Twitter, against  |
|                                   | a "Place" geo polygon, where the  |
|                                   | Place is fully contained within   |
|                                   | the defined region.               |
|                                   |                                   |
|                                   | -   Radius must be less than      |
|                                   |     25mi.                         |
|                                   | -   Units of radius supported are |
|                                   |     miles (mi) and kilometers     |
|                                   |     (km).                         |
|                                   | -   Longitude is in the range of  |
|                                   |     ±180                          |
|                                   | -   Latitude is in the range of   |
|                                   |     ±90                           |
|                                   | -   All coordinates are in        |
|                                   |     decimal degrees.              |
|                                   | -   Rule arguments are contained  |
|                                   |     with brackets, space          |
|                                   |     delimited.                    |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ point_radius:\[-105.27346517    |
|                                   | 40.01924738 0.5mi\]               |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | [ point_radius:\[2.355128         |
|                                   | 48.861118 16km\] ]{.code-inline}  |
|                                   |                                   |
|                                   | **Note:** This operator will not  |
|                                   | match on Retweets, since          |
|                                   | Retweet\'s places are attached to |
|                                   | the original Tweet. It will also  |
|                                   | not match on places attached to   |
|                                   | the original Tweet of a Quote     |
|                                   | Tweet.                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| bounding_box:\[west_long          | *Available alias* :               |
| south_lat east_long north_lat\]\  | geo_bounding_box:                 |
|                                   |                                   |
|                                   | Matches against the Exact         |
|                                   | Location (long, lat) of the Tweet |
|                                   | when present, and in Twitter,     |
|                                   | against a "Place" geo polygon,    |
|                                   | where the Place is fully          |
|                                   | contained within the defined      |
|                                   | region.                           |
|                                   |                                   |
|                                   | -   west_long south_lat represent |
|                                   |     the southwest corner of the   |
|                                   |     bounding box where west-long  |
|                                   |     is the longitude of that      |
|                                   |     point, and south_lat is the   |
|                                   |     latitude.                     |
|                                   | -   east_long and north_lat       |
|                                   |     represent the northeast       |
|                                   |     corner of the bounding box,   |
|                                   |     where east_long is the        |
|                                   |     longitude of that point, and  |
|                                   |     north_lat is the latitude.    |
|                                   |     -   Width and height of the   |
|                                   |         bounding box must be less |
|                                   |         than 25mi                 |
|                                   |     -   Longitude is in the range |
|                                   |         of ±180                   |
|                                   |     -   Latitude is in the range  |
|                                   |         of ±90                    |
|                                   | -   All coordinates are in        |
|                                   |     decimal degrees.              |
|                                   | -   Rule arguments are contained  |
|                                   |     with brackets, space          |
|                                   |     delimited.                    |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ bounding_box:\[-105.301758      |
|                                   | 39.964069 -105.178505 40.09455\]  |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** This operator will not  |
|                                   | match on Retweets, since          |
|                                   | Retweet\'s places are attached to |
|                                   | the original Tweet. It will also  |
|                                   | not match on places attached to   |
|                                   | the original Tweet of a Quote     |
|                                   | Tweet.                            |
+-----------------------------------+-----------------------------------+
| profile_country:\                 | Exact match on the "countryCode"  |
|                                   | field from the "address" object   |
|                                   | in the Profile Geo enrichment.    |
|                                   |                                   |
|                                   | Uses a normalized set of          |
|                                   | two-letter country codes, based   |
|                                   | on ISO-3166-1-alpha-2             |
|                                   | specification. This operator is   |
|                                   | provided in lieu of an operator   |
|                                   | for "country" field from the      |
|                                   | "address" object to be concise.   |
+-----------------------------------+-----------------------------------+
| profile_region:\                  | Matches on the "region" field     |
|                                   | from the "address" object in the  |
|                                   | Profile Geo enrichment.           |
|                                   |                                   |
|                                   | This is an exact full string      |
|                                   | match. It is not necessary to     |
|                                   | escape characters with a          |
|                                   | backslash. For example, if        |
|                                   | matching something with a slash,  |
|                                   | use "one/two", not "one\\/two".   |
|                                   | Use double quotes to match        |
|                                   | substrings that contain           |
|                                   | whitespace or punctuation.        |
+-----------------------------------+-----------------------------------+
| profile_locality:\                | Matches on the "locality" field   |
|                                   | from the "address" object in the  |
|                                   | Profile Geo enrichment.           |
|                                   |                                   |
|                                   | This is an exact full string      |
|                                   | match. It is not necessary to     |
|                                   | escape characters with a          |
|                                   | backslash. For example, if        |
|                                   | matching something with a slash,  |
|                                   | use "one/two", not "one\\/two".   |
|                                   | Use double quotes to match        |
|                                   | substrings that contain           |
|                                   | whitespace or punctuation.        |
+-----------------------------------+-----------------------------------+
| profile_subregion:\               | Matches on the "subRegion" field  |
|                                   | from the "address" object in the  |
|                                   | [Profile                          |
|                                   | Geo]                              |
|                                   | (/en/docs/twitter-api/enterprise/ |
|                                   | enrichments/overview/profile-geo) |
|                                   | enrichment. In addition to        |
|                                   | targeting specific counties,      |
|                                   | these operators can be helpful to |
|                                   | filter on a metro area without    |
|                                   | defining filters for every city   |
|                                   | and town within the region.       |
|                                   |                                   |
|                                   | This is an exact full string      |
|                                   | match. It is not necessary to     |
|                                   | escape characters with a          |
|                                   | backslash. For example, if        |
|                                   | matching something with a slash,  |
|                                   | use "one/two", not "one\\/two".   |
|                                   | Use double quotes to match        |
|                                   | substrings that contain           |
|                                   | whitespace or punctuation.        |
+-----------------------------------+-----------------------------------+
| has:geo\                          | Matches Tweets that have          |
|                                   | Tweet-specific geo location data  |
|                                   | provided from Twitter. This can   |
|                                   | be either "geo" lat-long          |
|                                   | coordinate, or a "location" in    |
|                                   | the form of a Twitter             |
|                                   | ["Place"](https://dev             |
|                                   | .twitter.com/overview/api/places) |
|                                   | , with corresponding display      |
|                                   | name, geo polygon, and other      |
|                                   | fields.                           |
|                                   |                                   |
|                                   | **Note** : When using the Search  |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:profile_geo\                  | *Available alias* :               |
|                                   | has:derived_user_geo              |
|                                   |                                   |
|                                   | Matches Tweets that have any      |
|                                   | [Profile                          |
|                                   | Geo]                              |
|                                   | (/en/docs/twitter-api/enterprise/ |
|                                   | enrichments/overview/profile-geo) |
|                                   | metadata, regardless of the       |
|                                   | actual value.                     |
|                                   |                                   |
|                                   | **Note** : When using the Search  |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:links                         | This operator matches Tweets that |
|                                   | contain a link or referenced      |
|                                   | media in the \"text\" object of   |
|                                   | the payload.\                     |
|                                   |                                   |
|                                   | **Note:** In addition to this     |
|                                   | operator matching Tweets with a   |
|                                   | link in their text, it also       |
|                                   | matches Tweets with media (image, |
|                                   | video, gif), and Quote Tweets.    |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| is:retweet\                       | Deliver only explicit retweets    |
|                                   | that match a rule. Can also be    |
|                                   | negated to exclude retweets that  |
|                                   | match a rule from delivery and    |
|                                   | only original content is          |
|                                   | delivered.                        |
|                                   |                                   |
|                                   | This operator looks only for true |
|                                   | Retweets. Quoted Tweets which do  |
|                                   | not use Twitter's Retweet         |
|                                   | functionality will not be matched |
|                                   | by this operator.                 |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| is:reply\                         | Delivers only explicit replies    |
|                                   | that match a rule. Can also be    |
|                                   | negated to exclude replies that   |
|                                   | match a rule from delivery (see   |
|                                   | example request below). When used |
|                                   | with PowerTrack, this operator    |
|                                   | matches on replies to an original |
|                                   | Tweet, replies in quoted Tweets   |
|                                   | and replies in Retweets. When     |
|                                   | used with the Search API, this    |
|                                   | operator only matches on replies  |
|                                   | to an original Tweet and excludes |
|                                   | replies in quoted Tweets and      |
|                                   | replies in Retweets. Example:     |
|                                   |                                   |
|                                   | [ #contest123 is:reply            |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | \                                 |
|                                   | [ \@twitterdev -is:reply          |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note** : When using the Search  |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| is:quote                          | Delivers only Quote Tweets, or    |
|                                   | Tweets that reference another     |
|                                   | Tweet, as identified by the       |
|                                   | \"is_quote_status\":true in Tweet |
|                                   | payloads. Can also be negated to  |
|                                   | exclude Quote Tweets.             |
|                                   |                                   |
|                                   | Example:\                         |
|                                   | [ \@twitterdev is:quote           |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| is:verified\                      | Deliver only Tweets where the     |
|                                   | author is "verified" by Twitter.  |
|                                   | Can also be negated to exclude    |
|                                   | Tweets where the author is        |
|                                   | verified. Example:                |
|                                   |                                   |
|                                   | [ \@twitterdev is:verified        |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:mentions\                     | Matches Tweets that mention       |
|                                   | another Twitter user.             |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:hashtags\                     | Matches Tweets that contain a     |
|                                   | hashtag.                          |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:media\                        | *Available alias* :               |
|                                   | has:media_link                    |
|                                   |                                   |
|                                   | Matches Tweets that contain a     |
|                                   | media url classified by Twitter.  |
|                                   | For example, pic.twitter.com.     |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:images\                       | Matches Tweets that contain a     |
|                                   | media url classified by Twitter.  |
|                                   | For example, pic.twitter.com.     |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:videos\                       | *Available alias* :               |
|                                   | has:video_link                    |
|                                   |                                   |
|                                   | Matches Tweets that contain       |
|                                   | native Twitter videos, uploaded   |
|                                   | directly to Twitter. This will    |
|                                   | not match on videos created with  |
|                                   | YouTube, Periscope, or Tweets     |
|                                   | with links to other video hosting |
|                                   | sites.                            |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+
| has:symbols\                      | Matches Tweets that contain a     |
|                                   | cashtag symbol (with a leading    |
|                                   | '\$' character. For example,      |
|                                   | \$tag).                           |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` . You can     |
|                                   | include this as a standalone      |
|                                   | operator when using PowerTrack    |
|                                   | and Historical PowerTrack.        |
+-----------------------------------+-----------------------------------+

</div>
:::
:::
:::
:::
:::
:::
:::
