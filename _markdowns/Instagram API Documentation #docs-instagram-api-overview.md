::: {._4-u3 ._588p}
In order for an app user to grant your app permissions, the app user
must be able to perform [tasks](/docs/pages/access-tokens#page-tasks) on
the Facebook Page connected to the Instagram account they are attempting
to access. App users may grant your app permissions based on tasks they
are able to perform as follows:

::: _57-c
  Permission                  ` MANAGE `   ` CREATE_CONTENT `   ` MODERATE `   ` ADVERTISE `   ` ANALYZE `
  --------------------------- ------------ -------------------- -------------- --------------- -------------
  instagram_basic             ✔            ✔                    ✔              ✔               ✔
  instagram_content_publish   ✔            ✔                                                   
  instagram_manage_comments   ✔            ✔                    ✔                              
  instagram_manage_insights   ✔            ✔                    ✔              ✔               ✔
:::

You can determine which tasks an app user is able to perform on a Page
by querying the
[` GET /me/accounts `](/docs/graph-api/reference/user/accounts#Reading)
endpoint with the app user\'s User access token. The endpoint will
return a list of Pages that the app user is able to perform tasks on,
and indicate which tasks the user can perform on each of them.

Refer to the [reference documentation](/docs/instagram-api/reference/)
to see which permissions each endpoint requires. The API does not
support [Business Manager System
Users](/docs/marketing-api/system-users) , or app users who have the
Live Contributor role.

### Referring to tasks

If you need to inform your app users about tasks (and which ones are
required to use your app properly), here\'s how tasks are referred to in
our various UIs.

#### Classic Pages

[Classic Pages](https://www.facebook.com/help/135275340210354) refer to
tasks as **roles** . App users with an Admin role on a Page can grant
your app any permission. App users with other roles can grant
permissions as follows:

::: _57-c
+-----------------------------------+-----------------------------------+
| Role                              | Grantable Permissions             |
+===================================+===================================+
| Editor                            | instagram_basic\                  |
|                                   | instagram_content_publish         |
+-----------------------------------+-----------------------------------+
| Moderator                         | instagram_basic                   |
|                                   | instagram_manage_comments         |
|                                   |                                   |
|                                   | instagram_manage_insights         |
+-----------------------------------+-----------------------------------+
| Advertiser                        | instagram_basic\                  |
|                                   | instagram_manage_insights         |
+-----------------------------------+-----------------------------------+
| Analyst                           | instagram_basic\                  |
|                                   | instagram_manage_insights         |
+-----------------------------------+-----------------------------------+
:::

#### New Experience Pages

[New Experience
Pages](https://www.facebook.com/business/help/782660422528806) refer to
tasks as either Facebook Access or Task Access. App users with Facebook
Access on a Page can grant your app any permission. App users with Task
Access can grant permissions as follows:

::: _57-c
+-----------------------------------+-----------------------------------+
| Task Access                       | Grantable Permissions             |
+===================================+===================================+
| Ads                               | instagram_basic                   |
+-----------------------------------+-----------------------------------+
| Content                           | instagram_basic\                  |
|                                   | instagram_content_publish         |
+-----------------------------------+-----------------------------------+
| Insights                          | instagram_basic\                  |
|                                   | instagram_manage_insights         |
+-----------------------------------+-----------------------------------+
| Messages & Community Activity     | instagram_basic\                  |
|                                   | instagram_manage_comments         |
+-----------------------------------+-----------------------------------+
:::

To determine if a Page is using the new experience, request its
[` has_transitioned_to_new_page_experience `](/docs/graph-api/reference/page/#Reading)
field. This value return ` true ` if the Page uses the new experience.
:::
