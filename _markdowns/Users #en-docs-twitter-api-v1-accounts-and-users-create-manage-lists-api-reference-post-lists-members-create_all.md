::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Adds multiple members to a list, by specifying a comma-separated list of
member ids or screen names. The authenticated user must own the list to
be able to add members to it. Note that lists can\'t have more than
5,000 members, and you are limited to adding up to 100 members to a list
at a time with this method.

Please note that there can be issues with lists that rapidly remove and
add memberships. Take care when using these methods such that you are
not too rapidly switching between removals and adds on the same list.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/members/create_all.json `

  -------------------------- ------
  Response formats           JSON
  Requires authentication?   Yes
  Rate limited?              Yes
  -------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name                Required   Description                                                                                                                                                                                              Default Value   Example
  list_id             required   The numerical *id* of the list.                                                                                                                                                                                          
  slug                required   You can identify a list by its slug instead of its numerical id. If you decide to do so, note that you\'ll also have to specify the list owner using the *owner_id* or *owner_screen_name* parameters.                   
  user_id             optional   A comma separated list of user IDs, up to 100 are allowed in a single request.                                                                                                                                           
  screen_name         optional   A comma separated list of screen names, up to 100 are allowed in a single request.                                                                                                                                       
  owner_screen_name   optional   The screen name of the user who owns the list being requested by a *slug* .                                                                                                                                              
  owner_id            optional   The user ID of the user who owns the list being requested by a *slug* .                                                                                                                                                  
  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/lists/members/create_all.json?screen_name=rsarver,episod,jasoncosta,theseancook,kurrik,froginthevalley&list_id=23 `

## Example Response [¶](#example-response){.headerlink}
:::
:::
:::
:::
:::
:::
:::
