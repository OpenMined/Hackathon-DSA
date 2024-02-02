::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Below is a list of all operators supported in Twitter\'s premium and
enterprise search APIs:

-   [ Enterprise ]{.subscription-tag .subscription-tag--enterprise}
    30-day search API
-   [ Enterprise ]{.subscription-tag .subscription-tag--enterprise}
    Full-archive search API

For a side-by-side comparison of available operators by product see
[HERE](/en/docs/twitter-api/enterprise/rules-and-filtering/operators-by-product)
.

+-----------------------------------+-----------------------------------+
| Operator                          | Description                       |
+-----------------------------------+-----------------------------------+
| keyword\                          | Matches a tokenized keyword       |
|                                   | within the body or urls of a      |
|                                   | Tweet. This is a tokenized match, |
|                                   | meaning that your keyword string  |
|                                   | will be matched against the       |
|                                   | tokenized text of the Tweet body  |
|                                   | -- tokenization is based on       |
|                                   | punctuation, symbol, and          |
|                                   | separator Unicode basic plane     |
|                                   | characters. For example, a Tweet  |
|                                   | with the text "I like coca-cola"  |
|                                   | would be split into the following |
|                                   | tokens: I, like, coca, cola.      |
|                                   | These tokens would then be        |
|                                   | compared to the keyword string    |
|                                   | used in your rule. To match       |
|                                   | strings containing punctuation    |
|                                   | (for example, coca-cola), symbol, |
|                                   | or separator characters, you must |
|                                   | use a quoted exact match as       |
|                                   | described below.                  |
|                                   |                                   |
|                                   | **Note:** With the Search API,    |
|                                   | accented and special characters   |
|                                   | are normalized to standard latin  |
|                                   | characters, which can change      |
|                                   | meanings in foreign languages or  |
|                                   | return unexpected results:        |
|                                   |                                   |
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
|                                   | URLs within a Tweet.              |
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
|                                   | "quotations" to add to a rule.\   |
+-----------------------------------+-----------------------------------+
| \"exact phrase match\"\           | Matches the tokenized and ordered |
|                                   | phrase within the body or urls of |
|                                   | a Tweet. This is a tokenized      |
|                                   | match, meaning that your keyword  |
|                                   | string will be matched against    |
|                                   | the tokenized text of the Tweet   |
|                                   | body -- tokenization is based on  |
|                                   | punctuation, symbol, and          |
|                                   | separator Unicode basic plane     |
|                                   | characters.\                      |
|                                   |                                   |
|                                   | **Note:** Punctuation is not      |
|                                   | tokenized and is instead treated  |
|                                   | as whitespace. For                |
|                                   | example, quoted "#hashtag" will   |
|                                   | match "hashtag" but not #hashtag  |
|                                   | (use the hashtag \# operator      |
|                                   | without quotes to match on actual |
|                                   | hashtags. For example, quoted     |
|                                   | "\$cashtag" will match "cashtag"  |
|                                   | but not \$cashtag (use the        |
|                                   | cashtag \$ operator without       |
|                                   | quotes to match on actual         |
|                                   | cashtags.                         |
|                                   |                                   |
|                                   | For example, \"Love Snow\" will   |
|                                   | match \"#love #snow\"\            |
|                                   | For example, \"#Love #Snow\" will |
|                                   | match \"love snow\"               |
|                                   |                                   |
|                                   | **Note:** This operator will      |
|                                   | match on both URLs and unwound    |
|                                   | URLs within a Tweet.              |
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
|                                   | other. Can have any number of     |
|                                   | keywords in quotes. N cannot be   |
|                                   | greater than 6.                   |
|                                   |                                   |
|                                   | Note that this operator is only   |
|                                   | available in the [ enterprise     |
|                                   | ]{.subscription-tag               |
|                                   | .subscription-tag--enterprise}    |
|                                   | search APIs.\                     |
+-----------------------------------+-----------------------------------+
| from:\                            | Matches any Tweet from a specific |
|                                   | user.                             |
|                                   |                                   |
|                                   | The value must be the user's      |
|                                   | Twitter numeric Account ID or     |
|                                   | username (excluding the @         |
|                                   | character). See                   |
|                                   | [                                 |
|                                   | HERE](/content/developer-twitter/ |
|                                   | en/docs/twitter-api/users/lookup) |
|                                   | or                                |
|                                   | [HERE](http://gettwitterid.com/)  |
|                                   | for methods for looking up        |
|                                   | numeric Twitter Account IDs.      |
+-----------------------------------+-----------------------------------+
| to:\                              | Matches any Tweet that is in      |
|                                   | reply to a particular user.       |
|                                   |                                   |
|                                   | The value must be the user's      |
|                                   | numeric Account ID or username    |
|                                   | (excluding the @ character). See  |
|                                   | [                                 |
|                                   | HERE](/content/developer-twitter/ |
|                                   | en/docs/twitter-api/users/lookup) |
|                                   | for methods for looking up        |
|                                   | numeric Twitter Account IDs.      |
+-----------------------------------+-----------------------------------+
| url:\                             | Performs a tokenized              |
|                                   | (keyword/phrase) match on the     |
|                                   | expanded URLs of a tweet (similar |
|                                   | to url_contains). Tokens and      |
|                                   | phrases containing punctuation or |
|                                   | special characters should be      |
|                                   | double-quoted. For example,       |
|                                   | url:\"/developer\". While         |
|                                   | generally not recommended, if you |
|                                   | want to match on a specific       |
|                                   | protocol, enclose in              |
|                                   | double-quotes:                    |
|                                   | url:\                             |
|                                   | "https://developer.twitter.com\". |
|                                   |                                   |
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
|                                   | the Search API.                   |
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
|                                   | Note: that the hashtag operator   |
|                                   | relies on Twitter's entity        |
|                                   | extraction to match hashtags,     |
|                                   | rather than extracting the        |
|                                   | hashtag from the body itself. See |
|                                   | [HERE](/content/develope          |
|                                   | r-twitter/en/docs/twitter-api/ent |
|                                   | erprise/data-dictionary/native-en |
|                                   | riched-objects/entities#hashtags) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.         |
+-----------------------------------+-----------------------------------+
| @\                                | Matches any Tweet that mentions   |
|                                   | the given username.               |
|                                   |                                   |
|                                   | The to: operator returns a subset |
|                                   | match of the \@mention operator.  |
+-----------------------------------+-----------------------------------+
| \$                                | Matches any Tweet that contains   |
|                                   | the specified 'cashtag' (where    |
|                                   | the leading character of the      |
|                                   | token is the '\$' character).     |
|                                   |                                   |
|                                   | Note that the cashtag operator    |
|                                   | relies on Twitter's 'symbols'     |
|                                   | entity extraction to match        |
|                                   | cashtags, rather than trying to   |
|                                   | extract the cashtag from the body |
|                                   | itself. See                       |
|                                   | [HERE](/content/develop           |
|                                   | er-twitter/en/docs/twitter-api/en |
|                                   | terprise/data-dictionary/native-e |
|                                   | nriched-objects/entities#symbols) |
|                                   | for more information on Twitter   |
|                                   | Entities JSON attributes.         |
|                                   |                                   |
|                                   | Note that this operator is only   |
|                                   | available in the [ enterprise     |
|                                   | ]{.subscription-tag               |
|                                   | .subscription-tag--enterprise}    |
|                                   | search APIs.                      |
+-----------------------------------+-----------------------------------+
| retweets_of:\                     | *Available alias* :               |
|                                   | retweets_of_user:                 |
|                                   |                                   |
|                                   | Matches tweets that are retweets  |
|                                   | of a specified user. Accepts both |
|                                   | usernames and numeric Twitter     |
|                                   | Account IDs (NOT tweet status     |
|                                   | IDs).\                            |
|                                   | See                               |
|                                   | [                                 |
|                                   | HERE](/content/developer-twitter/ |
|                                   | en/docs/twitter-api/users/lookup) |
|                                   | for methods for looking up        |
|                                   | numeric Twitter Account IDs.\     |
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
|                                   | results.                          |
|                                   |                                   |
|                                   | **Note:** if no language          |
|                                   | classification can be made the    |
|                                   | provided result is 'und' (for     |
|                                   | undefined).                       |
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
+-----------------------------------+-----------------------------------+
| place:\                           | Matches Tweets tagged with the    |
|                                   | specified location *or* Twitter   |
|                                   | place ID (see examples).          |
|                                   | Multi-word place names ("New York |
|                                   | City", "Palo Alto") should be     |
|                                   | enclosed in quotes.               |
|                                   |                                   |
|                                   | **Note:** See the [GET            |
|                                   | geo/search](/content/develo       |
|                                   | per-twitter/en/docs/twitter-api/v |
|                                   | 1/geo/place-information/overview) |
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
|                                   | [place](/content/develo           |
|                                   | per-twitter/en/docs/twitter-api/v |
|                                   | 1/geo/place-information/overview) |
|                                   | matches the given ISO alpha-2     |
|                                   | character code.                   |
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
|                                   | -   Units of radius supported are |
|                                   |     miles (mi) and kilometers     |
|                                   |     (km).                         |
|                                   | -   Radius must be less than      |
|                                   |     25mi.                         |
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
|                                   | **Note:** This operator will not  |
|                                   | match on Retweets, since          |
|                                   | Retweet\'s places are attached to |
|                                   | the original Tweet. It will also  |
|                                   | not match on places attached to   |
|                                   | the original Tweet of a Quote     |
|                                   | Tweet.                            |
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
|                                   | -   Width and height of the       |
|                                   |     bounding box must be less     |
|                                   |     than 25mi                     |
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
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**NOTE:** All [ is: ]{.code-inline} and [ has: ]{.code-inline} operators
cannot be used as standalone operators when using the Search API, and
must be combined with another clause.

For example, [ \@TwitterDev has:links ]{.code-inline}
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
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
|                                   | \                                 |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:profile_geo\                  | *Available alias* :               |
|                                   | has:derived_user_geo              |
|                                   |                                   |
|                                   | Matches Tweets that have any      |
|                                   | [Profile                          |
|                                   | Geo](http://support.gnip.         |
|                                   | com/enrichments/profile_geo.html) |
|                                   | metadata, regardless of the       |
|                                   | actual value.                     |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:links                         | This operators matches Tweets     |
|                                   | which contain links in the        |
|                                   | message body.                     |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| is:retweet\                       | Deliver only explicit retweets    |
|                                   | that match a rule. Can also be    |
|                                   | negated to exclude retweets that  |
|                                   | match a rule from delivery and    |
|                                   | only original content is          |
|                                   | delivered.                        |
|                                   |                                   |
|                                   | This operator looks only for true |
|                                   | Retweets, which use Twitter's     |
|                                   | retweet functionality. Quoted     |
|                                   | Tweets and Modified Tweets which  |
|                                   | do not use Twitter's retweet      |
|                                   | functionality will not be matched |
|                                   | by this operator.                 |
|                                   |                                   |
|                                   | \                                 |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| is:reply\                         | An operator to filter Tweets      |
|                                   | based on whether they are or are  |
|                                   | not replies to Tweets. Deliver    |
|                                   | only explicit replies that match  |
|                                   | a rule. Can also be negated to    |
|                                   | exclude replies that match a rule |
|                                   | from delivery.                    |
|                                   |                                   |
|                                   | Note that this operator is        |
|                                   | available for paid premium and    |
|                                   | enterprise search and is not      |
|                                   | available in Sandbox dev          |
|                                   | environments.                     |
|                                   |                                   |
|                                   | \                                 |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| is:quote                          | Delivers only Quote Tweets, or    |
|                                   | Tweets that reference another     |
|                                   | Tweet, as identified by the       |
|                                   | \"is_quote_status\":true in Tweet |
|                                   | payloads. Can also be negated to  |
|                                   | exclude Quote Tweets.\            |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| is:verified\                      | Deliver only Tweets where the     |
|                                   | author is "verified" by Twitter.  |
|                                   | Can also be negated to exclude    |
|                                   | Tweets where the author is        |
|                                   | verified.                         |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:mentions\                     | Matches Tweets that mention       |
|                                   | another Twitter user.             |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:hashtags\                     | Matches Tweets that contain a     |
|                                   | hashtag.                          |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
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
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:images\                       | Matches Tweets that contain a     |
|                                   | media url classified by           |
|                                   | Twitter. For example,             |
|                                   | pic.twitter.com.                  |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:videos\                       | *Available alias* :               |
|                                   | has:video_link                    |
|                                   |                                   |
|                                   | Matches Tweets that contain       |
|                                   | native Twitter videos, uploaded   |
|                                   | directly to Twitter. This will    |
|                                   | not match on videos created with  |
|                                   | Vine, Periscope, or Tweets with   |
|                                   | links to other video hosting      |
|                                   | sites.                            |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
| has:symbols\                      | Matches Tweets that contain a     |
|                                   | cashtag symbol (with a leading    |
|                                   | '\$' character. For example,      |
|                                   | \$tag).  Note that this operator  |
|                                   | is only available in the [        |
|                                   | enterprise ]{.subscription-tag    |
|                                   | .subscription-tag--enterprise}    |
|                                   | search APIs.                      |
|                                   |                                   |
|                                   | **Note:** When using the Search   |
|                                   | API, this operator must be used   |
|                                   | in conjunction with other         |
|                                   | operators that don\'t include     |
|                                   | ` is: ` or ` has: ` .             |
+-----------------------------------+-----------------------------------+
:::
:::
:::
:::
:::
:::
:::
:::
