<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This data dictionary describes the data names displayed in the Meta
Content Library web UI (the Name column) if applicable, and the
corresponding API fields returned in Meta Content Library API search
responses (the API field column). In the API field column, some fields
have nested fields indicated by a dot notation. These are referred to as
*expanded fields* . See [Field
expansion](https://developers.facebook.com/docs/content-library-api/field-expansion)
for information about how to include some or all of a parent field\'s
expanded fields in your queries.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

</div>

</div>

API field

Description

Products

Name

name

The name of the Facebook Page.

Content Library

\

Content Library API

About

about

The short paragraph in the About section of the Facebook Page.

Content Library

\

Content Library API

Website

website

The external URL from the Facebook Page's About section.

Content Library API

Description

description

The long paragraph in the About section of the Facebook Page.

Content Library

\

Content Library API

Verification status

verification_status

The verification status of the Facebook Page. A Facebook Page with a
verified badge indicates that Facebook has confirmed that it is the
authentic presence for that person or brand. [Learn
more.](https://www.facebook.com/help/196050490547892)

Content Library

\

Content Library API

Page categories

page_categories

The list of up to three categories of the Facebook Page, selected by the
Page manager.

Content Library

\

Content Library API

Location city

location.city

The self-reported, publicly available city location associated with the
Facebook Page.

Content Library API

Location country

location.country

The self-reported, publicly available country location associated with
the Facebook Page.

Content Library API

Location country code

location.country_code

The self-reported, publicly available country code location associated
with the Facebook Page.

Content Library API

Location name

location.name

The self-reported, publicly available location name associated with the
Facebook Page.

Content Library API

Location region

location.region

The self-reported, publicly available region location associated with
the Facebook Page.

Content Library API

Location zip

location.zip

The self-reported, publicly available location zip associated with the
Facebook Page.

Content Library API

Location street

location.street

The self-reported, publicly available street location associated with
the Facebook Page.

Content Library API

Location state

location.state

The self-reported, publicly available state location associated with the
Facebook Page.

Content Library API

Page name change date

page_transparency.page_name_changes.data.date

The date the Facebook Page's name changed.

Content Library API

Page name old

page_transparency.page_name_changes.data.old_name

The old name of the Facebook Page prior to the name change.

Content Library API

Page name new

page_transparency.page_name_changes.data.new_name

The new name of the Facebook Page, following the name change.

Content Library API

Page merged date

page_transparency.page_merges.data.date

The date another Facebook Page merged with this Page.

Content Library API

Page merged

page_transparency.page_merges.data.page_merged

The name of the Facebook Page that merged with this Page.

Content Library API

Creation date

creation_date

The date the Facebook Page was created.

Content Library

\

Content Library API

Page manager countries

page_transparency.admin_countries.data.country

The predicted primary country locations of people who manage this
Facebook Page.

Content Library

\

Content Library API

Count of Page managers by countries

page_transparency.admin_countries.data.count

The number of people who manage this Facebook Page predicted to be from
the associated country.

Content Library

\

Content Library API

Page owner

page_transparency.confirmed_page_owner

The confirmed owner associated with the Facebook Page.

Content Library API

Has active ads

page_transparency.has_active_ads

Whether the Facebook Page has active ads or not.

Content Library API

Has run political ads

page_transparency.has_run_political_ads

Whether the Facebook Page has run political ads or not.

Content Library API

Followers

follower_count

The number of followers of the Facebook Page.

Content Library

\

Content Library API

Page likes

like_count

The number of likes of the Facebook Page.

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

API field

Description

Products

Name

name

The name of the Facebook group.

Content Library

\

Content Library API

Description

description

The description of the Facebook group.

Content Library

\

Content Library API

Creation date

creation_date

The date the Facebook group was created.

Content Library

\

Content Library API

Group original name

group_transparency.original_name

The original name of the Facebook group.

Content Library API

Group name change date

group_transparency.name_changes.data.date

The date the name of the Facebook group changed.

Content Library

\

Content Library API

Group name new

group_transparency.name_changes.data.new_name

The new name of the Facebook group.

Content Library API

Group admin and moderator Page IDs

group_transparency.admin_and_moderator_page_ids

The list of encrypted IDs of Facebook Pages that are admins or
moderators of the Facebook group.

Content Library API

Group owner type

group_owners.data.type

The type of the group owner associated with the Facebook group.This
field will display if the group owner is a professional profile or Page.
Only the encrypted Page ID will be shared.

Content Library API

Group owner ID

group_owners.data.id

The encrypted ID of the Facebook group owners.This field will display if
the group owner is a professional profile or Page. Only the encrypted
Page ID will be shared.

Content Library API

Picture URL

picture_url

The photo URL of the Facebook group.

Content Library API

Group members

member_count

The number of members of the Facebook group.

Content Library

\

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

API field

Description

Products

Name

name

The name of the Facebook event.

Content Library

\

Content Library API

Description

description

The description of the Facebook event.

Content Library

\

Content Library API

Creation time

creation_time

The time the Facebook event was created.

Content Library API

Event start time

event_start_time

The start time of the Facebook event. Not available if the event is the
parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library

\

Content Library API

Event end time

event_end_time

The end time of the Facebook event. Not available if the event is the
parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library API

Going responses

going_count

The number of Going responses on a Facebook event. Not available if the
event is the parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library

\

Content Library API

Not going responses

not_going_count

The number of Not Going responses on a Facebook event. Not available if
the event is the parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library API

Interested responses

interested_count

The number of Interested responses on a Facebook event. Not available if
the event is the parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library

\

Content Library API

Event type

event_type

The type of Facebook event. Event types include single instance,
recurring or instance of recurring.

Content Library API

Recurring event IDs

recurring_event_ids

The list of encrypted IDs of the recurring instances of the Facebook
event, if the event is recurring. Only available if the event is the
parent of recurring event instances. [Learn
more](/docs/content-library-api/guide-fb-events#recurring) .

Content Library API

Parent event ID

parent_event_id

The encrypted ID of the parent event of the Facebook event, if the event
is recurring. Only available if the event is an instance of a recurring
event. [Learn more](/docs/content-library-api/guide-fb-events#recurring)
.

Content Library API

Event owners type

event_owners.data.type

The type of the event owner associated with the Facebook event.

Content Library API

Event owners ID

event_owners.data.id

The encrypted ID of the event owner associated with the Facebook event.
This field will display if the event owner is a group, professional
profile or Page. For events owned by professional profiles or Pages,
only the encrypted Page ID will be shared.

Content Library API

Place name

place.name

The self-reported, publicly available name of the place where the
Facebook event is located.

Content Library API

Place location city

place.location.city

The self-reported, publicly available city where the Facebook event is
located.

Content Library API

Place location country

place.location.country

The self-reported, publicly available country where the Facebook event
is located.

Content Library API

Place location country code

place.location.country_code

The self-reported, publicly available country code of the Facebook
event's location.

Content Library API

Place location name

place.location.name

The self-reported, publicly available name of the Facebook event's
location.

Content Library API

Place location region

place.location.region

The self-reported, publicly available region where the Facebook event is
located.

Content Library API

Place location state

place.location.state

The self-reported, publicly available state where the Facebook event is
located.

Content Library API

Place location street

place.location.street

The self-reported, publicly available street where the Facebook event is
located.

Content Library API

Place location zip

place.location.zip

The self-reported, publicly available zip of the Facebook event's
location.

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

API field

Description

Products

Text

text

The text of the Facebook post. Tags are excluded.

Content Library

\

Content Library API

Creation time

creation_time

The time the Facebook post was created.

Content Library

\

Content Library API

Modified time

modified_time

The time the Facebook post was most recently modified.

Content Library API

Language

lang

The content language of the Facebook post. Returns ISO 639-1 language
code in 2-letter lowercase format.

Content Library (Filter only)

\

Content Library API

Likes

statistics.like_count

The number of like reactions on the post or reel.

Content Library

\

Content Library API

Love reactions

statistics.love_count

The number of love reactions on the post or reel.

Content Library

\

Content Library API

Wow reactions

statistics.wow_count

The number of wow reactions on the post or reel.

Content Library

\

Content Library API

Haha reactions

statistics.haha_count

The number of haha reactions on the post or reel.

Content Library

\

Content Library API

Sad reactions

statistics.sad_count

The number of sad reactions on the post or reel.

Content Library

\

Content Library API

Angry reactions

statistics.angry_count

The number of angry reactions on the post or reel.

Content Library

\

Content Library API

Comments

statistics.comment_count

The number of comments on the post or reel.

Content Library

\

Content Library API

Reactions

statistics.reaction_count

The total number of reactions on the post. Reactions include: Like,
Love, Care, Haha, Wow, Sad or Angry.

Content Library

\

Content Library API

Shares

statistics.share_count

The number of times the post was shared.

Content Library

\

Content Library API

Care reactions

statistics.care_count

The number of care reactions on the post.

Content Library

\

Content Library API

Views

statistics.views

The number of times the post or reel was on screen, not including times
it appeared on the post owner's screen. For video posts, views are
counted whether the video was played or not. Only posts with more than
100 views display the view count. A post displays no view count value if
there were fewer than 100 views as of the last refresh. View counts for
Facebook posts or reels made before January 1, 2017 are not available.
View counts are not available for Facebook posts created in the last 5-7
days due to the refresh cycle.

Content Library

\

Content Library API

View counts last refreshed date

view_date_last_refreshed

The date the view count was last refreshed. View counts are refreshed
every 7 days for all Facebook posts.

Content Library

\

Content Library API

Post owner type

post_owner.data.type

The type of post owner associated with the Facebook post. Post owner
types include: Pages, groups and events.

Content Library

\

Content Library API

Post owner ID

post_owner.data.id

The encrypted ID of the owner associated with the Facebook post.

Content Library API

Post owner name

post_owner.data.name

The name of the post owner associated with the Facebook post.

Content Library

\

Content Library API

Media type

media_type

The media type included in the Facebook Post. Media types include
photos, videos and reels, and miscellaneous (including links, reshares,
and text-only posts).

Content Library

Branded content Page ID

branded_content_page_id

The encrypted ID of the Page associated with the Facebook post. Included
if the post has branded content. [Learn
more.](https://www.facebook.com/business/help/788160621327601?id=1912903575666924)

Content Library API

Link attachment fields description

link_attachment_fields.description

The description of the link attachment included in the Facebook post.

Content Library API

Link attachment fields link

link_attachment_fields.link

The URL of the link attachment included in the Facebook post.

Content Library API

Link attachment fields name

link_attachment_fields.name

The name of the link attachment included in the Facebook post.

Content Library API

Link attachment fields caption

link_attachment_fields.caption

The caption of the link attachment included in the Facebook post.

Content Library API

Shared post ID

shared_post_id

The encrypted ID of the reshared post included in the Facebook post.

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

API field

Description

Products

Account type

account_type

The type of Instagram account. Only creator and business accounts are
included.

Content Library API

Is verified

is_verified

Whether the Instagram account is verified. An Instagram account with a
verified badge means that Instagram has confirmed that it is the
authentic presence for that person or brand. [Learn
more.](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F854227311295302&h=AT3J81mQ_zxTfvsj5F27g3M9tdNAGhxO4RlNSPP6SH1dYHoOEAu0S5tCIZxN-2lOcR0q8P25IiseJ1lbeXKyyaw5HyaexE0k60ipkyoGe2AtSgkxMkvgamiTroKkmsXiWPnqZi-BtaVK0mT5)

Content Library

\

Content Library API

Followers

follower_count

The number of followers of the Instagram account.

Content Library

\

Content Library API

Following

following_count

The number of accounts the Instagram account is following.

Content Library API

Website

website

The external website URL of the Instagram account.

Content Library API

Name

name

The name of the Instagram account.

Content Library

\

Content Library API

Biography

biography

The description of the Instagram account.

Content Library

\

Content Library API

Creation date

creation_date

The date the Instagram account was created.

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: _57-c
Name
:::
:::
:::

API field

Description

Products

Text

text

The text of the Instagram post. Tags are excluded.

Content Library

\

Content Library API

Creation time

creation_time

The time the Instagram post was created.

Content Library

\

Content Library API

Modified time

modified_time

The time the Instagram post was most recently modified.

Content Library API

Language

lang

The content language of the Instagram post. Returns ISO 639-1 language
code in 2-letter lowercase format.

Content Library API

Comments

statistics.comment_count

The number of comments on the post or reel.

Content Library

\

Content Library API

Likes

statistics.like_count

The number of like reactions on the post or reel.

Content Library

\

Content Library API

Views

statistics.views

The number of times the post or reel was on screen, not including times
it appeared on the post owner's screen. For video posts, views are
counted whether the video was played or not. Only posts with more than
100 views display the view count. A post displays no view count value if
there were fewer than 100 views as of the last refresh. View counts for
Instagram posts or reels made before October 1, 2022 are not available.
View counts are not available for Instagram posts created in the last
3-5 days due to the refresh cycle.

Content Library

\

Content Library API

View counts last refreshed date

view_date_last_refreshed

The date the view count was last refreshed. View counts are refreshed
every 3 days for all Instagram posts and reels.

Content Library

\

Content Library API

Post owner account type

post_owner.type

The account type of the post owner associated with the Instagram post.
Post owner types include business or creator.

Content Library API

Post owner ID

post_owner.id

The encrypted ID of the owner associated with the Instagram post.

Content Library API

Is branded content

is_branded_content

Whether the Instagram post has branded content or not. [Learn
more.](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F&h=AT2YLKT10TVjmNj1NoRZkmGm12JbCN4KaK-NjjN12qZZVVblTp2KQCKyI4IONt29HW1mqaxTm7XE9Xc5K-SQidgARJVJNyuCO9vM3EvOaR1o5L-48Vt7aErBA27ivbLk3L8cLDTCzhmbR9fB)

Content Library API

Media type

media_type

The media type included in the Instagram post. Media types include
albums, photos, and videos and reels.

Content Library

\

Content Library API

Hashtags

hashtags

The list of hashtags included in the Instagram post.

Content Library

\

Content Library API

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
## Learn more
:::
