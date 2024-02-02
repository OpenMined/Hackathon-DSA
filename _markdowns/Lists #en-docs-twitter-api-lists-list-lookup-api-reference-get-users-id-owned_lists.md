::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Returns all Lists owned by the specified user.

### Endpoint URL

` https://api.twitter.com/2/users/:id/owned_lists `

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` id `\                 string                  The user ID whose owned
  [Required]{.small}                              Lists you would like to
                                                  retrieve.
  ----------------------- ----------------------- -----------------------

  ----------------------- -------------------------- ------------------------------------------------------------------
  Name                    Type                       Description

  ` expansions `\         enum ( ` owner_id ` )      [Expansions](/en/docs/twitter-api/expansions) enable you to
  [Optional]{.small}                                 request additional data objects that relate to the originally
                                                     returned List. The ID that represents the expanded data object
                                                     will be included directly in the List data object, but the
                                                     expanded object metadata will be returned within the ` includes `
                                                     response object, and will also include the ID so that you can
                                                     match this data object to the original user object. At this time,
                                                     the only expansion available to endpoints that primarily return
                                                     List objects is ` expansions=owner_id ` . You will find the
                                                     expanded user data object living in the ` includes ` response
                                                     object.

  ` list.fields `\        enum ( ` created_at ` ,    This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` follower_count ` ,       to select which specific [List
                          ` member_count ` ,         fields](/en/docs/twitter-api/data-dictionary/object-model/lists)
                          ` private ` ,              will deliver with each returned List objects. Specify the desired
                          ` description ` ,          fields in a comma-separated list without spaces between commas and
                          ` owner_id ` )             fields. These specified List fields will display directly in the
                                                     List data objects.

  ` max_results `\        integer                    The maximum number of results to be returned per page. This can be
  [Optional]{.small}                                 a number between 1 and 100. By default, each page will return 100
                                                     results.

  ` pagination_token `\   string                     Used to request the next page of results if all results weren\'t
  [Optional]{.small}                                 returned with the latest request, or to go back to the previous
                                                     page of results. To return the next page, pass the next_token
                                                     returned in your previous response. To go back one page, pass the
                                                     previous_token returned in your previous response.

  ` user.fields `\        enum ( ` created_at ` ,    This [fields](/en/docs/twitter-api/fields) parameter enables you
  [Optional]{.small}      ` description ` ,          to select which specific [user
                          ` entities ` , ` id ` ,    fields](/en/docs/twitter-api/data-dictionary/object-model/user)
                          ` location ` ,             will deliver with the users object. Specify the desired fields in
                          ` most_recent_tweet_id ` , a comma-separated list without spaces between commas and fields.
                          ` name ` ,                 The user fields will only be returned if you have included
                          ` pinned_tweet_id ` ,      ` expansions=owner_id ` query parameter in your request. You will
                          ` profile_image_url ` ,    find this ID and all additional user fields in the ` included `
                          ` protected ` ,            data object.
                          ` public_metrics ` ,       
                          ` url ` , ` username ` ,   
                          ` verified ` ,             
                          ` withheld ` )             
  ----------------------- -------------------------- ------------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` id `\               | string                | Unique identifier of  |
| [Default]{.small}     |                       | this List. This is    |
|                       |                       | returned as a string  |
|                       |                       | in order to avoid     |
|                       |                       | complications with    |
|                       |                       | languages and tools   |
|                       |                       | that cannot handle    |
|                       |                       | large integers.       |
+-----------------------+-----------------------+-----------------------+
| ` name `\             | string                | The name of this      |
| [Default]{.small}     |                       | List.                 |
+-----------------------+-----------------------+-----------------------+
| ` created_at `        | date (ISO 8601)       | Creation time of this |
|                       |                       | List.                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` lis                 |
|                       |                       | t.fields=created_at ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` private `           | boolean               | Indicates if this     |
|                       |                       | List has been set to  |
|                       |                       | private. The List (in |
|                       |                       | other words, if this  |
|                       |                       | is publicly viewed or |
|                       |                       | not).                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | `                     |
|                       |                       | list.fields=private ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` follower_count `    | integer               | Number of users who   |
|                       |                       | follow this List.     |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` list.fi             |
|                       |                       | elds=follower_count ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` member_count `      | integer               | Number of users who   |
|                       |                       | are a member of this  |
|                       |                       | List.                 |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` list.               |
|                       |                       | fields=member_count ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` owner_id `          | string                | Unique identifier of  |
|                       |                       | this List\'s owner.   |
|                       |                       | This is returned as a |
|                       |                       | string in order to    |
|                       |                       | avoid complications   |
|                       |                       | with languages and    |
|                       |                       | tools that cannot     |
|                       |                       | handle large          |
|                       |                       | integers.             |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` l                   |
|                       |                       | ist.fields=owner_id ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` description `       | string                | A brief description   |
|                       |                       | of this List, if the  |
|                       |                       | owner provided one.   |
|                       |                       |                       |
|                       |                       | To return this field, |
|                       |                       | add                   |
|                       |                       | ` list                |
|                       |                       | .fields=description ` |
|                       |                       | in the request\'s     |
|                       |                       | query parameter.      |
+-----------------------+-----------------------+-----------------------+
| ` includes.users `    | array                 | When including the    |
|                       |                       | `                     |
|                       |                       | expansions=owner_id ` |
|                       |                       | parameter, this       |
|                       |                       | includes the          |
|                       |                       | referenced List owner |
|                       |                       | in the form of a      |
|                       |                       | [user                 |
|                       |                       | object](/en/docs/twit |
|                       |                       | ter-api/data-dictiona |
|                       |                       | ry/object-model/user) |
|                       |                       | with their default    |
|                       |                       | fields and any        |
|                       |                       | additional fields     |
|                       |                       | requested using the   |
|                       |                       | ` user.fields `       |
|                       |                       | parameter.            |
+-----------------------+-----------------------+-----------------------+
| ` meta `\             | object                | This object contains  |
| [Default]{.small}     |                       | information about the |
|                       |                       | number of users       |
|                       |                       | returned in the       |
|                       |                       | current request, and  |
|                       |                       | pagination details.   |
+-----------------------+-----------------------+-----------------------+
| `                     | integer               | The number of users   |
|  meta.result_count `\ |                       | returned in this      |
| [Default]{.small}     |                       | request. Note that    |
|                       |                       | this number may be    |
|                       |                       | lower than what was   |
|                       |                       | specified in the      |
|                       |                       | ` max_results ` query |
|                       |                       | parameter.            |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | Pagination token for  |
| meta.previous_token ` |                       | the previous page of  |
|                       |                       | results. This value   |
|                       |                       | is returned when      |
|                       |                       | there are multiple    |
|                       |                       | pages of results, as  |
|                       |                       | the current request   |
|                       |                       | may only return a     |
|                       |                       | subset of results. To |
|                       |                       | go back to the        |
|                       |                       | previous page,        |
|                       |                       | passing the value     |
|                       |                       | from this field in    |
|                       |                       | the                   |
|                       |                       | ` pagination_token `  |
|                       |                       | query parameter. When |
|                       |                       | this field is not     |
|                       |                       | returned in the       |
|                       |                       | response, it means    |
|                       |                       | you are on the first  |
|                       |                       | page of results.      |
+-----------------------+-----------------------+-----------------------+
| ` meta.next_token `   | string                | Pagination token for  |
|                       |                       | the next page of      |
|                       |                       | results. This value   |
|                       |                       | is returned when      |
|                       |                       | there are multiple    |
|                       |                       | pages of results, as  |
|                       |                       | the current request   |
|                       |                       | may only return a     |
|                       |                       | subset of results. To |
|                       |                       | retrieve the full     |
|                       |                       | list, keep passing    |
|                       |                       | the value from this   |
|                       |                       | field in the          |
|                       |                       | ` pagination_token `  |
|                       |                       | query parameter. When |
|                       |                       | this field is not     |
|                       |                       | returned in the       |
|                       |                       | response, it means    |
|                       |                       | you\'ve reached the   |
|                       |                       | last page of results, |
|                       |                       | and that there are no |
|                       |                       | further pages.        |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
