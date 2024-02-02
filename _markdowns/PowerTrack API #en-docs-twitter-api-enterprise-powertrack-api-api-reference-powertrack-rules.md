All requests to the PowerTrack rules API must use HTTP Basic
Authentication, constructed from a valid email address and password
combination used to log into your account at console.gnip.com.
Credentials must be passed as the Authorization header for each request.
Make sure your client is adding the \"Authentication: Basic\" HTTP
header (with encoded credentials over HTTPS) to all API requests.

## POST /rules []{#AddRules .tall} [¶](#post-rules-){.headerlink} {#post-rules-}

Adds one or many rules to your PowerTrack stream\'s ruleset.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP POST                         |
+-----------------------------------+-----------------------------------+
| **Content Type**                  | \"application/json\". The request |
|                                   | should specify this as the        |
|                                   | \"Content-type\".                 |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the [Console - Products  |
|                                   | API Help                          |
|                                   | tab](/en/docs/twitte              |
|                                   | r-api/enterprise/console/product) |
|                                   | , and uses the following          |
|                                   | structure:                        |
|                                   |                                   |
|                                   | ` https://data-api                |
|                                   | .twitter.com/rules/powertrack/acc |
|                                   | ounts/{gnip_account_name}/publish |
|                                   | ers/twitter/{stream_label}.json ` |
+-----------------------------------+-----------------------------------+
| **Character Encoding**            | UTF-8                             |
+-----------------------------------+-----------------------------------+
| **Request Body Format**           | JSON                              |
+-----------------------------------+-----------------------------------+
| **Request Body Size Limit**       | 5 MB                              |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
|                                   | Rule addition requests will be    |
|                                   | processed serially and will be    |
|                                   | rejected if you have more than    |
|                                   | one rule request happening at the |
|                                   | same time.                        |
+-----------------------------------+-----------------------------------+

\

#### Request Body Content

Your request should provide rule data in the following format with the
defined Content-type: \"application/json\":

    {
        "rules":
        [
            {"value":"rule1","tag":"tag1"},
            {"value":"rule2","tag":"tag2"}
        ]
    }

\

**Example curl Request**

The following example requests demonstrate how to add rules using cURL
on the command line, using JSON rules.

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d '{"rules":[{"value":"rule1","tag":"tag1"},{"value":"rule2","tag":"tag2"}]}'

\

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json" -d @arrayofrulesfile_max5mb.json

\

    curl -v -X POST -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod.json" -d '{"rules":[{"value":"(#snow OR snowday OR "snow day" OR from:noaa) lang:en","tag":"4581245"},{"value":"(skiing OR boarding OR "hitting the slopes" OR from:OnTheSnow) lang:en","tag":"4581267"}]}'

\

#### Responses

The following responses may be returned by the API for these requests.
Non-200 responses should be retried after making any necessary
modifications in the rules.

  ----- ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  201   Created                The rule or rules were successfully added to your PowerTrack ruleset.
  400   Bad Request            Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized           HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  422   Unprocessable Entity   Generally occurs due to an invalid rule, based on the PowerTrack rule restrictions. Requests fail or succeed as a batch. For these errors, each invalid rule and the reason for rejection is included in a JSON message in the response. Catch the associated exception to expose this message.
  429   Rate Limited           Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable    Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support or contact emergency if still unable to connect after 10 minutes.
  ----- ---------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Responses**

This response indicates that all rules (two in this case) were
successfully created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 2,
            "not_created": 0
        },
        "detail": [{
            "rule": {
                "value": "(#snow OR snowday OR \"snow day\" OR from:noaa) lang:en",
                "tag": "4581245",
                "id": 734938587381145604
            },
            "created": true
        }, {
            "rule": {
                "value": "(skiing OR boarding OR \"hitting the slopes\" OR from:OnTheSnow) lang:en",
                "tag": "4581267",
                "id": 734938587381174273
            },
            "created": true
        }],
        "sent": "2016-05-24T02:46:28.402Z"
    }

This response indicates that one rule was successfully created, and two
were not created because they already exist. Rules are indexed by rule
value (syntax). For rules not created there is a \'message\' field
explaining why the rule could not be created.

    HTTP/1.1 201 Created
    {
        "summary": {
            "created": 1,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "robot OR 🤖",
                "tag": "botrule123",
                "id": 734861971116285952
            },
            "created": true
        }, {
            "rule": {
                "value": "fish OR 🐟",
                "tag": "fishrule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }, {
            "rule": {
                "value": "Pizza OR 🍕",
                "tag": "pizzarule123"
            },
            "created": false,
            "message": "A rule with this value already exists"
        }],
        "sent": "2016-05-23T21:42:01.661Z"
    }

The following responses indicate that no rules were created. In each
case there is a \'message\' field explaining why the rule could not be
created. Note that when one or more rules are invalid, no rules are
added (even rules with valid syntax).

\

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 2
        },
        "detail": [{
            "rule": {
                "value": "streaming gnip contains:$twtr",
                "tag": null
            },
            "created": false,
            "message": "no viable alternative at input '$twtr' (at position 25)\n"
        }, {
            "rule": {
                "value": "streaming gnip contains:\"$twtr\"",
                "tag": null
            },
            "created": false
        }],
        "sent": "2016-06-01T15:41:27.451Z"
    }

\

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "-follow",
                "tag": null
            },
            "created": false,
            "message": "Rules must contain a non-negation term (at position 1)\nRules must contain at least one positive, non-stopword clause (at position 1)\n"
        }],
        "sent": "2016-05-23T18:34:25.218Z"
    }

\

    HTTP/1.1 422 Unprocessable Entity
    {
        "summary": {
            "created": 0,
            "not_created": 1
        },
        "detail": [{
            "rule": {
                "value": "streaming AND lang:en",
                "tag": null
            },
            "created": false,
            "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 11)\n"
        }],
        "sent": "2016-05-23T21:39:49.612Z"
    }

\

## GET /rules []{#ListRules .tall} [¶](#get-rules-){.headerlink} {#get-rules-}

Retrieve all rules currently in place on the stream

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP GET                          |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the [Console - Products  |
|                                   | API Help                          |
|                                   | tab](/en/docs/twitte              |
|                                   | r-api/enterprise/console/product) |
|                                   | , and uses the following          |
|                                   | structure:                        |
|                                   |                                   |
|                                   | ` https://d                       |
|                                   | ata-api.twitter.com/rules/powertr |
|                                   | ack/accounts/:account_name/publis |
|                                   | hers/twitter/:stream_label.json ` |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
+-----------------------------------+-----------------------------------+

\

**Example cURL Request**

The following example request demonstrates how to retrieve rules using
cURL on the command line.

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json"

#### Response

The following responses may be returned by the API for these requests.
Non-200 responses should be retried, utilizing an exponential backoff
for subsequent requests.

  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  200   OK                    The request was successful, and the current ruleset is returned in JSON format.
  400   Bad Request           Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized          HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  429   Rate Limited          Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable   Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support.
  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:twitterdev",
            "tag": "tweetsfromtwitterdev123",
            "id": 735163830813134848
        }, {
            "value": "fish OR 🐟",
            "tag": "fishrule123",
            "id": 738034522583769088
        }, {
            "value": "Pizza OR 🍕",
            "tag": "pizzarule123",
            "id": 738034522579554304
        }, {
            "value": "robot OR 🤖",
            "tag": "botrule123",
            "id": 738034522579570689
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

\

## GET /rules/:rule_id []{#GetRule .tall} [¶](#get-rules-rule-id-){.headerlink} {#get-rules-rule-id-}

Retrieve an existing rule on the stream by rule ID. Note that all rules
are assigned a unique ID by Twitter at the time of creation, rules that
are deleted and recreated will receive a different unique rule ID.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP GET                          |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the [Console - Products  |
|                                   | API Help                          |
|                                   | tab](/en/docs/twitte              |
|                                   | r-api/enterprise/console/product) |
|                                   | , and uses the following          |
|                                   | structure:                        |
|                                   |                                   |
|                                   | ` https://data-api.twitter        |
|                                   | .com/rules/powertrack/accounts/:a |
|                                   | ccount_name/publishers/twitter/:s |
|                                   | tream_label/rules/:rule_id.json ` |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
+-----------------------------------+-----------------------------------+

\

**Example cURL Request**

The following example request demonstrates how to retrieve a rule by
rule_id using cURL on the command line.

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/rules/:rule_id.json"

\

    curl -v -uexample@customer.com "https://data-api.twitter.com/rules/powertrack/accounts/companyname/publishers/twitter/prod/rules/735163830813134848.json"

#### Response

The following responses may be returned by the API for these requests.
Non-200 responses should be retried, utilizing an exponential backoff
for subsequent requests.

  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  200   OK                    The request was successful, and the current rule is returned in JSON format.
  400   Bad Request           Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized          HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  429   Rate Limited          Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable   Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support.
  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:twitterdev",
            "tag": "tweetsfromtwitterdev123",
            "id": 735163830813134848
            "id_str":"735163830813134848"
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

\

## POST /rules \_method=get []{#GetRules .tall} [¶](#post-rules--method-get-){.headerlink} {#post-rules--method-get-}

Retrieves requested existing rules by list of rule IDs currently on a
stream.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP POST                         |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the API Help page, and   |
|                                   | uses the following structure:     |
|                                   |                                   |
|                                   | ` https://data-api.twitter.com    |
|                                   | /rules/powertrack/accounts/{gnip_ |
|                                   | account_name}/publishers/twitter/ |
|                                   | {stream_label}.json?_method=get ` |
+-----------------------------------+-----------------------------------+
| **Character Encoding**            | UTF-8                             |
+-----------------------------------+-----------------------------------+
| **Request Body Format**           | JSON                              |
+-----------------------------------+-----------------------------------+
| **Request Body Size Limit**       | 5 MB                              |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
+-----------------------------------+-----------------------------------+
| **Compression**                   | Gzip compression is supported,    |
|                                   | but not required for these        |
|                                   | requests.                         |
+-----------------------------------+-----------------------------------+

\

**Example curl Request**

The following example request demonstrates how to add rules using cURL
on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=get" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

\

#### Response

The following responses may be returned by the API for these requests.
Non-200 responses should be retried, utilizing an exponential backoff
for subsequent requests.

  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  200   OK                    The request was successful, and the current ruleset is returned in JSON format.
  400   Bad Request           Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized          HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  429   Rate Limited          Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable   Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) contact support.
  ----- --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Response**

    HTTP/1.1 200 OK
    {
        "rules": [{
            "value": "from:furiouscamper",
            "tag": null,
            "id": 734938587381145604
        }, {
            "value": "fish 🐟",
            "tag": null,
            "id": 734938587381174273
        }],
        "sent": "2016-06-01T15:52:37.341Z"
    }

\

        {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }

\

## POST /rules \_method=delete []{#DeleteRules .tall} [¶](#post-rules--method-delete-){.headerlink} {#post-rules--method-delete-}

Deletes requested existing rules by list of rule values or rule IDs
currently on a stream.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP POST                         |
+-----------------------------------+-----------------------------------+
| **Authentication**                | Basic Authentication. Your login  |
|                                   | credentials must be included in   |
|                                   | the header of the request.        |
+-----------------------------------+-----------------------------------+
| **Content Type**                  | \"application/json\". The request |
|                                   | should specify this as the        |
|                                   | \"Content-type\".                 |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the API Help page, and   |
|                                   | uses the following structure:     |
|                                   |                                   |
|                                   | ` https://data-api.twitter.com/ru |
|                                   | les/powertrack/accounts/{gnip_acc |
|                                   | ount_name}/publishers/twitter/{st |
|                                   | ream_label}.json?_method=delete ` |
+-----------------------------------+-----------------------------------+
| **Character Encoding**            | UTF-8                             |
+-----------------------------------+-----------------------------------+
| **Request Body Format**           | JSON                              |
+-----------------------------------+-----------------------------------+
| **Request Body Size Limit**       | 5 MB                              |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
+-----------------------------------+-----------------------------------+

\

#### Request Body Content

Your request should provide rule data in the following formats:

    Content-type: "application/json"
    {
        "rules":
        [
            {"value":"rule1"},
            {"value":"rule2"}
        ]
    }

    Content-type: "application/json"
    {
        "rule_ids":
        [
            734938587381145604,
            734938587381174273
        ]
    }

**Example curl Request**

The following example request demonstrates how to add rules using cURL
on the command line.

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rules":[{"value":"testrule"}]}"

    curl -v -X POST -uexample@customer.com \
    "https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json?_method=delete" \
    -d '{"rule_ids":[734938587381145604,734938587381174273]}"

\

#### Responses

The following responses may be returned by the API for these requests.
Non-200 responses should be retried following any necessary
modifications to the rules being deleted.

  ----- --------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  200   OK                    Indicates that the rule data supplied with the request consisted of valid JSON. However, note that if no rules are found in the ruleset for the PowerTrack stream based on a case-sensitive search, no rules will be deleted.
  400   Bad Request           Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized          HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  429   Rate Limited          Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable   Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) , contact support.
  ----- --------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Responses**

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 3,
            "not_deleted": 0
        },
        "detail": [],
        "sent": "2016-06-01T15:46:48.654Z"
    }

\

    HTTP/1.1 200 OK
    {
        "summary": {
            "deleted": 0,
            "not_deleted": 3
        },
        "detail": [{
            "rule": {
                "value": "Pizza",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "eggplant",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }, {
            "rule": {
                "value": "fish",
                "tag": null
            },
            "deleted": false,
            "message": "Rule does not exist"
        }],
        "sent": "2016-06-01T15:49:15.951Z"
    }

\

    HTTP/1.1 400 Bad Request
    {
        "error": {
            "message": "Invalid JSON. The body must be in the format {\"rules\":[{\"value\":\"rule1\", \"tag\":\"tag1\"}, {\"value\":\"rule2\"}]} or {\"rule_ids\": [rule_id1, rule_id2, rule_id3, rule_id4, rule_id5]}",
            "sent": "2013-08-16T00:50:00+00:00"
        }
    }

**Important note on rule management:** Rule sets are indexed by the
value or ruleID, not the tag; therefore, all rule additions must
reference the rule value or ruleID. In order to to make a tag update to
an existing rule, you must first delete it and then add it back with the
new tag value.

Rules must be unique per stream based on rule value, see below for a
rule management example scenario:

**CREATE RULE**

Action: POST rule {\"value\":\"#TwitterData\",\"tag\":\"tagtextA\"}
{\"summary\":{\"created\":1,\"not_created\":0},\"detail\":\[{\"rule\":{\"value\":\"#TwitterData\",\"tag\":\"tagtextA\",\"id\":961664522481119232,\"id_str\":\"961664522481119232\"},\"created\":true}\],\"sent\":\"2018-02-08T18:14:23.691Z\"}
System:
{\"value\":\"#TwitterData\",\"tag\":\"tagtextA\",\"id\":961664522481119232,\"id_str\":\"961664522481119232\"}

**FAILED ATTEMPT TO UPDATE TAG**

Action: POST rule {\"value\":\"#TwitterData\",\"tag\":\"tagtextB\"}
\*\*Rule tags cannot be \"updated\" - This request is ignored because
rule value ` #TwitterData ` already exists.
{\"summary\":{\"created\":0,\"not_created\":1},\"detail\":\[{\"rule\":{\"value\":\"#TwitterData\",\"tag\":\"tagtextB\",\"id\":961664522481119232,\"id_str\":\"961664522481119232\"},\"created\":false,\"message\":\"A
rule with this value already exists\"} System:
{\"value\":\"#TwitterData\",\"tag\":\"tagtextA\",\"id\":961664522481119232,\"id_str\":\"961664522481119232\"}

**FAILED ATTEMPT TO DELETE BY TAG**

Action: POST method=delete rule {\"tag\":\"tagtextA\"} \*\*Rules cannot
be deleted by tag.
{\"summary\":{\"deleted\":0,\"not_deleted\":1},\"detail\":\[{\"rule\":{\"value\":\"\",\"tag\":null},\"deleted\":false,\"message\":\"Rule
does not exist\"}\],\"sent\":\"2018-02-08T18:42:37.004Z\"} System:
{\"value\":\"#TwitterData\",\"tag\":\"tagtextA\",\"id\":961664522481119232,\"id_str\":\"961664522481119232\"}

**DELETE BY ID**

Action: POST method=delete rule {\"rule_ids\":\[961664522481119232\]}
{\"summary\":{\"deleted\":1,\"not_deleted\":0},\"detail\":\[\],\"sent\":\"2018-02-08T18:53:54.185Z\"}

**DELETE BY VALUE**

Action: POST method=delete rule {\"value\":\"#TwitterData\"}
{\"summary\":{\"deleted\":1,\"not_deleted\":0},\"detail\":\[\],\"sent\":\"2018-02-08T18:53:54.185Z\"}

**RECREATE RULE- NOW WITH NEW ID**

Action: POST rule {\"value\":\"#TwitterData\",\"tag\":\"tagtextB\"}
{\"summary\":{\"created\":1,\"not_created\":0},\"detail\":\[{\"rule\":{\"value\":\"#TwitterData\",\"tag\":\"tagtextB\",\"id\":961675641140609025,\"id_str\":\"961675641140609025\"},\"created\":true}\],\"sent\":\"2018-02-08T18:58:34.586Z\"}
System:
{\"value\":\"#TwitterData\",\"tag\":\"tagtextB\",\"id\":961675641140609025,\"id_str\":\"961675641140609025\"}

## POST /validation []{#ValidateRules .tall} [¶](#post-validation-){.headerlink} {#post-validation-}

Validates PowerTrack rules.

**Note:** Using this endpoint will not impact your PowerTrack streams.

#### Request Specifications

+-----------------------------------+-----------------------------------+
| **Request Method**                | HTTP POST                         |
+-----------------------------------+-----------------------------------+
| **URL**                           | Found on the API Help page in     |
|                                   | console, and uses the following   |
|                                   | structure:                        |
|                                   |                                   |
|                                   | ` https://data-api.twi            |
|                                   | tter.com/rules/powertrack/account |
|                                   | s/:account_name/publishers/twitte |
|                                   | r/:stream_label/validation.json ` |
+-----------------------------------+-----------------------------------+
| **Character Encoding**            | UTF-8                             |
+-----------------------------------+-----------------------------------+
| **Request Body Format**           | JSON                              |
+-----------------------------------+-----------------------------------+
| **Request Body Size Limit**       | 5 MB                              |
+-----------------------------------+-----------------------------------+
| **Rate Limit**                    | 60 requests per minute,           |
|                                   | aggregated across all requests to |
|                                   | /rules endpoint for the specific  |
|                                   | stream\'s API (POST and GET).     |
+-----------------------------------+-----------------------------------+

\

**Example curl Request**

The following example request demonstrates how to add rules using cURL
on the command line.

``` json
curl --compressed -v -uexample@customer.com \
"https://data-api.twitter.com/rules/powertrack/accounts/:account_name/publishers/twitter/:stream_label/validation.json" \
-d '{
    "rules": [{
        "value": "Pizza OR 🍕 OR \"🍕\" sample:100"
    }, {
        "value": "from:contains:heart"
    }, {
        "value": "fish AND bird"
    }, {
        "value": "(((\"#quotedhashtag\""
    }, {
        "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]"
    }, {
        "value": "from:jack"
    }]
}'
```

#### Response

The following responses may be returned by the API for these requests.
Non-200 responses should be retried, utilizing an exponential backoff
for subsequent requests.

  ----- --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  200   OK                    The request was successful, and the rule validation result is returned.
  400   Bad Request           Generally relates to poorly formatted JSON, and includes an \"Invalid JSON\" message in the response.
  401   Unauthorized          HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request.
  429   Rate Limited          Your app has exceeded the limit on requests to add, delete, or list rules for this stream.
  503   Service Unavailable   Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/) , contact support.
  ----- --------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\

**Example Response**

This response indicates that one rule is valid and five are not valid.
For rules that are not valid, there is a \'message\' field explaining
why the rule is not valid.

``` json
HTTP/1.1 200 OK
{
    "summary": {
        "valid": 1,
        "not_valid": 5
    },
    "detail": [{
        "rule": {
            "value": "from:jack",
            "tag": null
        },
        "valid": true
    }, {
        "rule": {
            "value": "Pizza OR 🍕 OR \"🍕\" sample:100",
            "tag": null
        },
        "valid": false,
        "message": "The sample operator cannot be used with an OR. To use the sample operator with an OR in the rule, the ORed clauses must be grouped together with parenthesis.  For example, to get 10% of activites that have term1 or term2, the rule should be (excluding the single quotes) '(term1 OR term2) sample:10' (at position 21)\n"
    }, {
        "rule": {
            "value": "from:contains:heart",
            "tag": null
        },
        "valid": false,
        "message": "Cannot parse rule at ':' (position 14)\n"
    }, {
        "rule": {
            "value": "fish AND bird",
            "tag": null
        },
        "valid": false,
        "message": "Ambiguous use of and as a keyword. Use a space to logically join two clauses, or \"and\" to find occurrences of and in text (at position 6)\n"
    }, {
        "rule": {
            "value": "(((\"#quotedhashtag\"",
            "tag": null
        },
        "valid": false,
        "message": "mismatched input 'EOF' expecting ')' (at position 20)\n\n"
    }, {
        "rule": {
            "value": "bounding_box:[-71.199636,42.230046,-70.979909,42.398619]",
            "tag": null
        },
        "valid": false,
        "message": "Cannot parse rule at '71.199636,42.230046,-70.979909,42.398619' (position 16)\n"
    }],
    "sent": "2017-03-16T02:33:01.827Z"
}
```
