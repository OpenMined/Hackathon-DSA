::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The v2 filtered stream endpoints group is replacing the [standard
v1.1 statuses/filter](/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter)
and [PowerTrack API](/en/docs/twitter-api/enterprise/powertrack-api)
. If you have code, apps, or tools that use an older version of the
filtered stream endpoint, and are considering migrating to the newer
Twitter API v2 endpoint, then this comparison can help you get started.

See our more in depth migration guides for:

[Migrating from Standard v1.1 compared to Twitter API
v2](/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2)

[Migrating from PowerTrack API migration to Twitter API
v2](/en/docs/twitter-api/tweets/filtered-stream/migrate/powertrack-api-migration-to-twitter-api-v2)

The following table compares the filtered streaming endpoints Twitter
offers:\

+-----------------+-----------------+-----------------+-----------------+
| **Description** | **Standard      | **PowerTrack    | **Twitter API   |
|                 | v1.1**          | API**           | v2**            |
+=================+=================+=================+=================+
| Access          | Twitter App     | Requires an     | Requires a      |
|                 |                 | enterprise      | developer       |
|                 |                 | contract and    | account ( [sign |
|                 |                 | account         | up](https://de  |
|                 |                 |                 | veloper.twitter |
|                 |                 |                 | .com/en/portal/ |
|                 |                 |                 | petition/essent |
|                 |                 |                 | ial/basic-info) |
|                 |                 |                 | ), and [Twitter |
|                 |                 |                 | App]            |
|                 |                 |                 | (/en/docs/apps) |
|                 |                 |                 | within a        |
|                 |                 |                 | [Project](/en   |
|                 |                 |                 | /docs/projects) |
+-----------------+-----------------+-----------------+-----------------+
| Host domain     | ******[         | ******[         | ******[         |
|                 | https://str     | h               | https://        |
|                 | eam.twitter.com | ttps://gnip-str | api.twitter.com |
|                 | ]{.cod          | eam.twitter.com | ]{.cod          |
|                 | e-inline}****** | ]{.cod          | e-inline}****** |
|                 |                 | e-inline}****** |                 |
+-----------------+-----------------+-----------------+-----------------+
| Endpoint path   | ******[         | ******[         | ******[         |
|                 | 1.1/statu       | /stream/pow     | /2/tweet        |
|                 | ses/filter.json | ertrack/account | s/search/stream |
|                 | ]{.cod          | s/{gnip_account | ]{.cod          |
|                 | e-inline}****** | _name}/publishe | e-inline}****** |
|                 |                 | rs/twitter/{str |                 |
|                 |                 | eam_label}.json | ******[         |
|                 |                 | ]{.cod          | /2/tweets/sear  |
|                 |                 | e-inline}****** | ch/stream/rules |
|                 |                 |                 | ]{.cod          |
|                 |                 | ******[         | e-inline}****** |
|                 |                 | /rules/pow      |                 |
|                 |                 | ertrack/account |                 |
|                 |                 | s/{gnip_account |                 |
|                 |                 | _name}/publishe |                 |
|                 |                 | rs/twitter/{str |                 |
|                 |                 | eam_label}.json |                 |
|                 |                 | ]{.cod          |                 |
|                 |                 | e-inline}****** |                 |
|                 |                 |                 |                 |
|                 |                 | ******[         |                 |
|                 |                 | /rules          |                 |
|                 |                 | /powertrack/acc |                 |
|                 |                 | ounts/{gnip_acc |                 |
|                 |                 | ount_name}/publ |                 |
|                 |                 | ishers/twitter/ |                 |
|                 |                 | {stream_label}/ |                 |
|                 |                 | validation.json |                 |
|                 |                 | ]{.cod          |                 |
|                 |                 | e-inline}****** |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Authentica     | OAuth 1.0a User | HTTP Basic      | OAuth 2.0       |
| tion](/en/docs/ | Context         | Authentication  | App-Only        |
| authentication) |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| HTTP methods    | POST            | GET\            | GET\            |
| supported       |                 | POST            | POST            |
+-----------------+-----------------+-----------------+-----------------+
| Required        | Rule defined on | No required     | No required     |
| parameters      | connection as   | parameters for  | parameters for  |
|                 | parameter, at   | streaming       | streaming       |
|                 | least one of:   | connection,     | connection,     |
|                 |                 | optional        | optional        |
|                 |                 | backfill        | parameters to   |
|                 |                 | parameter.      | define response |
|                 |                 |                 | format and add  |
|                 |                 | Rules managed   | [backfill       |
|                 |                 | separately      | recovery        |
|                 |                 |                 | feature](/en    |
|                 |                 |                 | /docs/twitter-a |
|                 |                 |                 | pi/tweets/filte |
|                 |                 |                 | red-stream/inte |
|                 |                 |                 | grate/recoverin |
|                 |                 |                 | g-missing-data) |
|                 |                 |                 | for Academic    |
|                 |                 |                 | Research        |
|                 |                 |                 | access.         |
|                 |                 |                 |                 |
|                 |                 |                 | Rules managed   |
|                 |                 |                 | separately      |
+-----------------+-----------------+-----------------+-----------------+
| Delivery type   | Streaming       | Streaming       | Streaming       |
|                 |                 |                 |                 |
|                 |                 | REST (for rules | REST (for rules |
|                 |                 | management)     | management)     |
+-----------------+-----------------+-----------------+-----------------+
| Default request | 5 connection    | 60 requests per | Depends on the  |
| rate limits     | attempts per 5  | min aggregated  | endpoint and    |
|                 | min             | for both POST   | the [access     |
|                 |                 | and GET         | lev             |
|                 |                 | requests        | el](/en/docs/tw |
|                 |                 |                 | itter-api/getti |
|                 |                 | /rules:  60     | ng-started/abou |
|                 |                 | requests per    | t-twitter-api#v |
|                 |                 | minute,         | 2-access-level) |
|                 |                 | aggregated      | .               |
|                 |                 | across all      |                 |
|                 |                 | requests to     | [GET            |
|                 |                 | /rules endpoint | /2/             |
|                 |                 | for the         | tweets/search/s |
|                 |                 | specific        | tream](/en/docs |
|                 |                 | stream's API    | /twitter-api/tw |
|                 |                 | (POST and GET). | eets/filtered-s |
|                 |                 |                 | tream/api-refer |
|                 |                 |                 | ence/get-tweets |
|                 |                 |                 | -search-stream) |
|                 |                 |                 | :\              |
|                 |                 |                 | Pro - 50        |
|                 |                 |                 | requests per    |
|                 |                 |                 | 15-minutes per  |
|                 |                 |                 | App             |
|                 |                 |                 |                 |
|                 |                 |                 | [GET            |
|                 |                 |                 | /2/tweets/searc |
|                 |                 |                 | h/stream/rules] |
|                 |                 |                 | (/en/docs/twitt |
|                 |                 |                 | er-api/tweets/f |
|                 |                 |                 | iltered-stream/ |
|                 |                 |                 | api-reference/g |
|                 |                 |                 | et-tweets-searc |
|                 |                 |                 | h-stream-rules) |
|                 |                 |                 | :\              |
|                 |                 |                 | Pro - 450       |
|                 |                 |                 | requests per    |
|                 |                 |                 | 15-minutes per  |
|                 |                 |                 | App             |
|                 |                 |                 |                 |
|                 |                 |                 | \-\--           |
|                 |                 |                 |                 |
|                 |                 |                 | [POST           |
|                 |                 |                 | /2/tweet        |
|                 |                 |                 | s/search/stream |
|                 |                 |                 | /rules](https:/ |
|                 |                 |                 | /developer-stag |
|                 |                 |                 | ing.twitter.com |
|                 |                 |                 | /en/docs/twitte |
|                 |                 |                 | r-api/tweets/fi |
|                 |                 |                 | ltered-stream/a |
|                 |                 |                 | pi-reference/po |
|                 |                 |                 | st-tweets-searc |
|                 |                 |                 | h-stream-rules) |
|                 |                 |                 | : Pro - 100     |
|                 |                 |                 | requests per 15 |
|                 |                 |                 | minutes per App |
+-----------------+-----------------+-----------------+-----------------+
| Maximum allowed | 2 concurrent    | Supports        | Pro access:\    |
| connections     | per authorized  | mul             | 1               |
|                 | user            | tiple/redundant |                 |
|                 |                 | connections,    |                 |
|                 |                 | determined by   |                 |
|                 |                 | contract        |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Recovery and   | None            | Backfill,       |                 |
| redundancy      |                 | redundant       |                 |
| feature         |                 | connections,    |                 |
| s](/en/docs/twi |                 | and the Replay  |                 |
| tter-api/tweets |                 | API             |                 |
| /filtered-strea |                 |                 |                 |
| m/integrate/rec |                 |                 |                 |
| overy-and-redun |                 |                 |                 |
| dancy-features) |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| [Tweet          | Limited to 1%   | Determined by   | There is a      |
| caps](/e        | of firehose     | contract        | monthly,        |
| n/docs/twitter- |                 |                 | Project-level   |
| api/tweet-caps) |                 |                 | Tweet cap       |
|                 |                 |                 | applied to all  |
|                 |                 |                 | Tweets received |
|                 |                 |                 | from this       |
|                 |                 |                 | endpoint:       |
|                 |                 |                 |                 |
|                 |                 |                 | Basic:\         |
|                 |                 |                 | 10,000 Tweets   |
|                 |                 |                 |                 |
|                 |                 |                 | Pro:\           |
|                 |                 |                 | 1 million       |
|                 |                 |                 | Tweets          |
+-----------------+-----------------+-----------------+-----------------+
| Keep-alive      | blank lines     | blank lines     | blank lines     |
| si              | (\\r\\n or      | (\\r\\n or      | (\\r\\n or      |
| gnal/heartbeats | similar) at     | similar) every  | similar) at     |
|                 | least every 20  | 10 seconds      | least every 20  |
|                 | seconds         |                 | seconds         |
+-----------------+-----------------+-----------------+-----------------+
| Latency         | 10 seconds      | 2 seconds       | 10 seconds \    |
|                 |                 |                 |                 |
|                 |                 | At least 10     |                 |
|                 |                 | seconds for URL |                 |
|                 |                 | unwinding       |                 |
|                 |                 | enrichment      |                 |
+-----------------+-----------------+-----------------+-----------------+
| Maximum allowed | 1 rule (within  | Determined by   | Pro access:\    |
| rules           | the endpoint    | contract up to  | 1000 rules      |
|                 | connection      | 250,000         |                 |
|                 | request)        |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Rule filter     | One query per   | Up to 2,048     | Pro Access:\    |
| limitations     | connection, up  | characters per  | 1,024           |
|                 | to either:      | rule            | characters per  |
|                 |                 |                 | rule            |
|                 | \- 400 track    |                 |                 |
|                 | keywords        |                 |                 |
|                 |                 |                 |                 |
|                 | \- 5000 follow  |                 |                 |
|                 | user IDs        |                 |                 |
|                 |                 |                 |                 |
|                 | \- 25 location  |                 |                 |
|                 | boxes           |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Tweet [JSON     | Standard v1.1   | [Native         | [Twitter API v2 |
| format](/en/d   | format          | Enr             | format](/co     |
| ocs/twitter-api |                 | iched](/en/docs | ntent/developer |
| /data-dictionar |                 | /twitter-api/en | -twitter/en/doc |
| y/introduction) |                 | terprise/data-d | s/twitter-api/d |
|                 |                 | ictionary/nativ | ata-dictionary) |
|                 |                 | e-enriched-obje | (determined by  |
|                 |                 | cts/tweet.html) | ******[ fields  |
|                 |                 | or [Activity    | ]{.cod          |
|                 |                 | Stream          | e-inline}****** |
|                 |                 | s](/en/docs/twi | and ******[     |
|                 |                 | tter-api/enterp | expansions      |
|                 |                 | rise/data-dicti | ]{.cod          |
|                 |                 | onary/activity- | e-inline}****** |
|                 |                 | streams-objects | request         |
|                 |                 | /activity.html) | parameters, not |
|                 |                 | (selected       | back            |
|                 |                 | within the      | ward-compatible |
|                 |                 | [con            | with v1.1       |
|                 |                 | sole](/en/docs/ | formats)        |
|                 |                 | twitter-api/ent |                 |
|                 |                 | erprise/console | To learn more   |
|                 |                 | /overview.html) | about how to    |
|                 |                 | )               | migrate from    |
|                 |                 |                 | the Standard    |
|                 |                 |                 | v1.1 format to  |
|                 |                 |                 | the Twitter API |
|                 |                 |                 | v2 format,      |
|                 |                 |                 | please visit    |
|                 |                 |                 | our [data       |
|                 |                 |                 | formats         |
|                 |                 |                 | migration       |
|                 |                 |                 | guid            |
|                 |                 |                 | e](/en/docs/twi |
|                 |                 |                 | tter-api/migrat |
|                 |                 |                 | e/data-formats) |
|                 |                 |                 | . We will be    |
|                 |                 |                 | releasing       |
|                 |                 |                 | additional data |
|                 |                 |                 | format          |
|                 |                 |                 | migration       |
|                 |                 |                 | guides for      |
|                 |                 |                 | Native Enriched |
|                 |                 |                 | and Activity    |
|                 |                 |                 | Streams soon.   |
+-----------------+-----------------+-----------------+-----------------+
| Provides Tweet  | ✔               | ✔               | ✔               |
| edit history    |                 |                 |                 |
| and metadata    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Unique Features | Filtering done  | Filtering done  | Filtering done  |
|                 | via query       | via rules       | via             |
|                 | parameters on   | created through | [rule           |
|                 | connection      | an independent  | s](/en/docs/twi |
|                 | request         | endpoint        | tter-api/tweets |
|                 |                 |                 | /filtered-strea |
|                 | No              | [Enri           | m/build-a-rule) |
|                 | configuration   | chment](https:/ | created through |
|                 | UI              | /developer.twit | an independent  |
|                 |                 | ter.com/en/docs | endpoint        |
|                 |                 | /twitter-api/en |                 |
|                 |                 | terprise/enrich | [Metrics        |
|                 |                 | ments/overview) | ](https://devel |
|                 |                 | features        | oper.twitter.co |
|                 |                 | available in    | m/en/docs/twitt |
|                 |                 | contract        | er-api/metrics) |
|                 |                 |                 | and URL         |
|                 |                 | Configuration   | enrichment      |
|                 |                 | on              | features        |
|                 |                 | c               | included        |
|                 |                 | onsole.gnip.com |                 |
|                 |                 | UI              | Object          |
|                 |                 |                 | [field          |
|                 |                 |                 | s](https://deve |
|                 |                 |                 | loper.twitter.c |
|                 |                 |                 | om/en/docs/twit |
|                 |                 |                 | ter-api/fields) |
|                 |                 |                 | and             |
|                 |                 |                 | [expansions](h  |
|                 |                 |                 | ttps://develope |
|                 |                 |                 | r.twitter.com/e |
|                 |                 |                 | n/docs/twitter- |
|                 |                 |                 | api/expansions) |
|                 |                 |                 | specified with  |
|                 |                 |                 | request         |
|                 |                 |                 | parameters      |
|                 |                 |                 |                 |
|                 |                 |                 | Tweet           |
|                 |                 |                 | [               |
|                 |                 |                 | Annotations](ht |
|                 |                 |                 | tps://developer |
|                 |                 |                 | .twitter.com/en |
|                 |                 |                 | /docs/twitter-a |
|                 |                 |                 | pi/annotations) |
|                 |                 |                 |                 |
|                 |                 |                 | [Conversation   |
|                 |                 |                 | ID](/en/doc     |
|                 |                 |                 | s/twitter-api/c |
|                 |                 |                 | onversation-id) |
|                 |                 |                 | operator and    |
|                 |                 |                 | field           |
|                 |                 |                 |                 |
|                 |                 |                 | Configuration   |
|                 |                 |                 | through         |
|                 |                 |                 | [developer      |
|                 |                 |                 | port            |
|                 |                 |                 | al](/en/docs/de |
|                 |                 |                 | veloper-portal) |
+-----------------+-----------------+-----------------+-----------------+
:::
:::
:::
:::
:::
:::
:::
:::
