::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
<div>

The following API endpoints can be used to programmatically follow
users, search for users, and get user information:

+-----------------------+-----------------------+-----------------------+
| **Friends and         | **POST friendships**  | **Get user info**     |
| followers**           |                       |                       |
+-----------------------+-----------------------+-----------------------+
| -   GET followers/ids | -   POST              | -   GET users/lookup  |
| -   GET               |                       | -   GET users/search  |
|     followers/list    |    friendships/create | -   GET users/show    |
| -   GET friends/ids   | -   POST              |                       |
| -   GET friends/list  |                       |                       |
| -   GET               |   friendships/destroy |                       |
|                       | -   POST              |                       |
|  friendships/incoming |                       |                       |
| -   GET               |    friendships/update |                       |
|                       |                       |                       |
|    friendships/lookup |                       |                       |
| -   GET               |                       |                       |
|     friend            |                       |                       |
| ships/no_retweets/ids |                       |                       |
| -   GET               |                       |                       |
|                       |                       |                       |
|  friendships/outgoing |                       |                       |
| -   GET               |                       |                       |
|     friendships/show  |                       |                       |
+-----------------------+-----------------------+-----------------------+

For more details, please see the individual endpoint information within
the [API
reference](/en/docs/accounts-and-users/follow-search-get-users/api-reference)
section.\

### Terminology

To avoid confusion around the term \"friends\" and \"followers\" with
respect to the API endpoints, below is a definition of each:

**Friends** - we refer to \"friends\" as the Twitter users that a
specific user follows (e.g., following). Therefore, the [ GET
friends/ids ]{.code-inline} endpoint returns a collection of user IDs
that the specified user follows.

**Followers** - refers to the Twitter users that follow a specific user.
Therefore, making a request to the [ GET followers/ids ]{.code-inline}
endpoint returns a collection of user IDs for every user following the
specified user.

</div>
:::
:::
:::
:::
:::
:::
:::
