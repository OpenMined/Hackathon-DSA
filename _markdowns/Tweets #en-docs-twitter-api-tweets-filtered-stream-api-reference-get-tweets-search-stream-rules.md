::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Return either a single rule, or a list of rules that have been added to
the stream.

If you would like to initiate the stream to receive all Tweets that
match these rules in real-time, you will need to use the [GET
/tweets/search/stream](/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream)
endpoint.

### Endpoint URL

` https://api.twitter.com/2/tweets/search/stream/rules `

+-----------------------------------+-----------------------------------+
| Authentication methods\           | [OAuth 2.0                        |
| supported by this endpoint        | App-only](/en/docs/authentic      |
|                                   | ation/oauth-2-0/application-only) |
+-----------------------------------+-----------------------------------+
| [Rate                             | App rate limit                    |
| limit](/en/docs/rate-limits)      | (Application-only): 450 requests  |
|                                   | per 15-minute window shared among |
|                                   | all users of your app             |
+-----------------------------------+-----------------------------------+

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` ids `\                string                  Comma-separated list of
  [Optional]{.small}                              rule IDs. If omitted,
                                                  all rules are returned.
  ----------------------- ----------------------- -----------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
  --------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name            Type     Description
  ` id `          string   Unique identifier of this rule. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.
  ` value `       string   The rule text as submitted when creating the rule.
  ` tag `         string   The tag label as defined when creating the rule.
  ` meta.sent `   number   The time when the request body was returned.
  ` errors `      object   Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](/en/support/twitter-api/error-troubleshooting) for more details.
  --------------- -------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
