::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Add a member to a list. The authenticated user must own the list to be
able to add members to it. Note that lists cannot have more than 5,000
members.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/members/create.json `

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
  user_id             required   The ID of the user for whom to return results. Helpful for disambiguating when a valid user ID is also a valid screen name.                                                                                              
  screen_name         required   The screen name of the user for whom to return results. Helpful for disambiguating when a valid screen name is also a user ID.                                                                                           
  owner_screen_name   optional   The screen name of the user who owns the list being requested by a *slug* .                                                                                                                                              
  owner_id            optional   The user ID of the user who owns the list being requested by a *slug* .                                                                                                                                                  
  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/lists/members/create.json?slug=team&owner_screen_name=twitter&screen_name=kurrik `

## Example Response [¶](#example-response){.headerlink}
:::
:::
:::
:::
:::
:::
:::
