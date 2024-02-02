::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Updates the specified list. The authenticated user must own the list to
be able to update it.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/lists/update.json `

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
  name                optional   The name for the list.                                                                                                                                                                                                   
  mode                optional   Whether your list is public or private. Values can be *public* or *private* . If no mode is specified the list will be public.                                                                                           
  description         optional   The description to give the list.                                                                                                                                                                                        
  owner_screen_name   optional   The screen name of the user who owns the list being requested by a *slug* .                                                                                                                                              
  owner_id            optional   The user ID of the user who owns the list being requested by a *slug* .                                                                                                                                                  
  ------------------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/lists/update.json?list_id=1234&mode=public&name=Party%20Time `

## Example Response [¶](#example-response){.headerlink}
:::
:::
:::
:::
:::
:::
:::
