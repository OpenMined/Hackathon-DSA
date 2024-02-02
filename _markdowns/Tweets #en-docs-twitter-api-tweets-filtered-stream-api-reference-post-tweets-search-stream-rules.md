::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Add or delete rules to your stream.

Once you\'ve added a rule or rules to your stream, you can retrieve all
of the Tweets that match these rules by using the [GET
/tweets/search/stream](/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream)
endpoint.

To learn how to build a rule, please read our guide on [building a
rule](/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule)
.

To create one or more rules, submit an ` add ` JSON body with an array
of rules and operators. Similarly, to delete one or more rules, submit a
` delete ` JSON body with an array of list of existing rule IDs.

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

  ` delete_all `\         boolean                 Set to true to delete
  [Optional]{.small}                              all existing rules.

  ` dry_run `\            boolean                 Set to true to test the
  [Optional]{.small}                              syntax of your rule
                                                  without submitting it.
                                                  This is useful if you
                                                  want to check the
                                                  syntax of a rule before
                                                  removing one or more of
                                                  your existing rules.
  ----------------------- ----------------------- -----------------------

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` add `\              | array                 | Specifies the         |
| [Required]{.small}    |                       | operation you want to |
|                       |                       | perform on the rules. |
+-----------------------+-----------------------+-----------------------+
| ` add.value `\        | string                | The rule text. You    |
| [Required]{.small}    |                       | can learn how to      |
|                       |                       | build a rule by       |
|                       |                       | following our guide   |
|                       |                       | on [how to build a    |
|                       |                       | rule](/en/            |
|                       |                       | docs/twitter-api/twee |
|                       |                       | ts/filtered-stream/in |
|                       |                       | tegrate/build-a-rule) |
|                       |                       | . If you have         |
|                       |                       | Essential access, you |
|                       |                       | can use basic         |
|                       |                       | operators to build    |
|                       |                       | your rule, can add up |
|                       |                       | to 5 rules to your    |
|                       |                       | stream concurrently,  |
|                       |                       | and each rule can be  |
|                       |                       | 512 characters long.  |
|                       |                       | If you have Elevated  |
|                       |                       | access, you can use   |
|                       |                       | basic operators, can  |
|                       |                       | add up to 25 rules to |
|                       |                       | your stream, and each |
|                       |                       | rule can be 512       |
|                       |                       | characters long If    |
|                       |                       | you have Academic     |
|                       |                       | Research access, you  |
|                       |                       | can use all           |
|                       |                       | operators, can add up |
|                       |                       | to 1000 rules to your |
|                       |                       | stream, and each rule |
|                       |                       | can be 1024           |
|                       |                       | characters long.      |
|                       |                       |                       |
|                       |                       | To learn more about   |
|                       |                       | Twitter API access    |
|                       |                       | levels, please visit  |
|                       |                       | our [about Twitter    |
|                       |                       | API                   |
|                       |                       | page](/en/docs        |
|                       |                       | /twitter-api/getting- |
|                       |                       | started/about-twitter |
|                       |                       | -api#v2-access-level) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| ` delete `\           | object                | Specifies the         |
| [Required]{.small}    |                       | operation you want to |
|                       |                       | perform on the rules. |
+-----------------------+-----------------------+-----------------------+
| ` delete.ids `\       | array                 | Array of rule IDs,    |
| [Required]{.small}    |                       | each one representing |
|                       |                       | a rule already active |
|                       |                       | in your stream. IDs   |
|                       |                       | must be submitted as  |
|                       |                       | strings. You can find |
|                       |                       | a rule ID by using    |
|                       |                       | the [GET              |
|                       |                       | /tweets/searc         |
|                       |                       | h/stream/rules](/en/d |
|                       |                       | ocs/twitter-api/tweet |
|                       |                       | s/filtered-stream/api |
|                       |                       | -reference/get-tweets |
|                       |                       | -search-stream-rules) |
|                       |                       | endpoint.             |
+-----------------------+-----------------------+-----------------------+
| ` add.tag `\          | string                | The tag label. This   |
| [Optional]{.small}    |                       | is a free-form text   |
|                       |                       | you can use to        |
|                       |                       | identify the rules    |
|                       |                       | that matched a        |
|                       |                       | specific Tweet in the |
|                       |                       | streaming response.   |
|                       |                       | Tags can be the same  |
|                       |                       | across rules.         |
|                       |                       |                       |
|                       |                       | Learn more about tags |
|                       |                       | from our [matching    |
|                       |                       | returned Tweets       |
|                       |                       | gu                    |
|                       |                       | ide](/en/docs/twitter |
|                       |                       | -api/tweets/filtered- |
|                       |                       | stream/integrate/matc |
|                       |                       | hing-returned-tweets) |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ----------------------- ----------------------- ----------------------------------------------------------
  Name                    Type                    Description

  ` id `                  string                  Unique identifier of this rule. This is returned as a
                                                  string in order to avoid complications with languages and
                                                  tools that cannot handle large integers.

  ` value `               string                  The rule text as submitted when creating the rule.

  ` tag `                 string                  The tag label as defined when creating the rule.

  ` meta `\               object                  Contains information about when the rule was created, and
  [Default]{.small}                               whether the rule was either created or not created, or
                                                  deleted or not deleted.

  ` meta.sent `\          number                  The time when the request body was returned.
  [Default]{.small}                               

  ` meta.summary `\       object                  Contains fields that describe whether you were successful
  [Default]{.small}                               or unsuccessful in creating or deleting the different
                                                  rules that you passed in your request.

  ` errors `              object                  Contains details about errors that affected any of the
                                                  requested Tweets. See [Status codes and error
                                                  messages](/en/support/twitter-api/error-troubleshooting)
                                                  for more details.
  ----------------------- ----------------------- ----------------------------------------------------------
:::
:::
:::
