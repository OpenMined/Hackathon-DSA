Page - Graph API Reference - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Page
====
Represents a Facebook Page.
Over the coming months, all classic Pages will be migrated to the New Pages Experience. Use the `has_transitioned_to_new_page_experience` Page field to determine if a Page has been migrated. After all Pages have been migrated, the classic Pages experience will no longer be available.
Refer to our Pages API Guides for additional usage information.
Reading
-------

 Get information about a Facebook Page.

 ### Requirements
* For apps that have been granted the

`pages_read_engagement`
and

`pages_read_user_content`
permissions, only data owned by the Page is accessible.
* For apps that have been approved for either the

Page Public Content Access (PPCA)
or

Page Public Metadata Access (PPMA)
feature, only public data is accessible.

Learn more.
* The `instagram_business_account` field requires a User access token from a User who is able to perform appropriate tasks on the Page. Refer to the Instagram Graph API's Page reference for more information.
* If using a business system user in your request, the `business_management` permission may be required.
#### Limitations
* A Page access token is required for any fields that may include User information.
* All users requesting access to a Page using permissions must be able to perform the

`MODERATE` task
on the Page being queried.
* When using the Page Public Content Access feature, use a system user access token to avoid rate limiting issues.
* If the page url is being used as the query input, ensure the page url is set up the following way: facebook.com/<pageusername>. More information on the page username.
#### Public Page Data
Requirements vary based on the Page's status, unpublished or published, and unrestricted or restricted. Restrictions include any visibility restrictions such as by age or region. Note that for restricted Pages, the app user must also satisfy any restrictions in order for data to be returned.

 Page Status | Access Token | Feature, to retrieve public data | Permissions, to retrieve Page owned data || Unpublished | Page Access Token or User Access Token | None | None |
| Published, Unrestricted | App Access Token or 
User Access Token | PPCA or PPMA | `pages_read_engagement`
`pages_read_user_content`
`pages_show_list` |
| Published, Restricted | Page Access Token or User Access Token. | PPCA or PPMA | `pages_read_engagement`
`pages_read_user_content`
`pages_show_list` |
### Example

```
curl -i -X GET "https://graph.facebook.com/PAGE-ID?access_token=ACCESS-TOKEN"
```
### Parameters

| Parameter | Description |
| --- | --- |
| `account_linking_token`UTF-8 encoded string | Short lived account linking token (5 mins expiry) to get the PSID for a user-page pair
 |
### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The ID representing a Facebook Page.
 |
| `about`string | Information about the Page. Can be read with Page Public Content Access or Page Public Metadata Access. This value maps to the **Description** setting in the **Edit Page Info** user interface. Limit of 100 characters.
 |
| `access_token`string | The Page's access token. Only returned if the User making the request has a role (other than Live Contributor) on the Page. If your business requires two-factor authentication, the User must also be authenticated
 |
| `ad_campaign`AdSet | The Page's currently running promotion campaign
 |
| `affiliation`string | Affiliation of this person. Applicable to Pages representing people. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `app_id`id | App ID for app-owned Pages and app Pages
 |
| `artists_we_like`string | Artists the band likes. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `attire`string | Dress code of the business. Applicable to Restaurants or Nightlife. Can be one of Casual, Dressy or Unspecified. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `awards`string | The awards information of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `band_interests`string | Band interests. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `band_members`string | Members of the band. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `best_page`Page | The best available Page on Facebook for the concept represented by this Page. The best available Page takes into account authenticity and the number of likes
 |
| `bio`string | Biography of the band. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access. Limit of 100 characters.
 |
| `birthday`string | Birthday of this person. Applicable to Pages representing people. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `booking_agent`string | Booking agent of the band. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `built`string | Year vehicle was built. Applicable to Vehicles. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `business` | The Business associated with this Page. Requires business\_management permissions, and a page or user access token. The person requesting the access token must be an admin of the page.
 |
| `can_checkin`bool | Whether the Page has checkin functionality enabled. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `can_post`bool | Indicates whether the current app user can post on this Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `category`string | The Page's category. e.g. Product/Service, Computers/Technology. Can be read with Page Public Content Access or Page Public Metadata Access.
Core |
| `category_list`list<PageCategory> | The Page's sub-categories. This field will not return the parent category.
 |
| `checkins`unsigned int32 | Number of checkins at a place represented by a Page
Core |
| `company_overview`string | The company overview. Applicable to Companies. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `connected_instagram_account`IGUser | Instagram account connected to page via page settings
 |
| `contact_address`MailingAddress | The mailing or contact address for this page. This field will be blank if the contact address is the same as the physical address
 |
| `copyright_attribution_insights`CopyrightAttributionInsights | Insight metrics that measures performance of copyright attribution. An example metric would be number of incremental followers from attribution
 |
| `copyright_whitelisted_ig_partners`list<string> | Instagram usernames who will not be reported in copyright match systems
 |
| `country_page_likes`unsigned int32 | If this is a Page in a Global Pages hierarchy, the number of people who are being directed to this Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `cover`CoverPhoto | Information about the page's cover photo
 |
| `culinary_team`string | Culinary team of the business. Applicable to Restaurants or Nightlife. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `current_location`string | Current location of the Page. Can be read with Page Public Content Access or Page Public Metadata Access. To manage a child Page's location use the `/{page-id}/locations` endpoint.
 |
| `delivery_and_pickup_option_info`list<string> | A Vector of url strings for delivery\_and\_pickup\_option\_info of the Page.
 |
| `description`string | The description of the Page. Can be read with Page Public Content Access or Page Public Metadata Access. Note that this value is mapped to the **Additional Information** setting in the **Edit Page Info** user interface.
Core |
| `description_html`string | The description of the Page in raw HTML. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `differently_open_offerings`list<KeyValue:enum,bool> | To be used when `temporary_status` is set to `differently_open` to indicate how the business is operating differently than usual, such as a restaurant offering takeout. Enum keys can be one or more of the following: ONLINE\_SERVICES, DELIVERY, PICKUP, OTHER with the value set to `true` or `false`. For example, a business offering food pick up but pausing delivery would be `differently_open_offerings:{"DELIVERY":"false", "PICKUP":"true"}`
 |
| `directed_by`string | The director of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `display_subtext`string | Subtext about the Page being viewed. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `displayed_message_response_time`string | Page estimated message response time displayed to user. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `does_viewer_have_page_permission_link_ig`bool | does\_viewer\_have\_page\_permission\_link\_ig
 |
| `emails`list<string> | The emails listed in the About section of a Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `engagement`Engagement | The social sentence and like count information for this Page. This is the same info used for the like button
 |
| `fan_count`unsigned int32 | The number of users who like the Page. For Global Pages this is the count for all Pages across the brand. Can be read with Page Public Content Access or Page Public Metadata Access. For New Page Experience Pages, this field will return `followers_count`.
 |
| `featured_video`Video | Video featured by the Page
 |
| `features`string | Features of the vehicle. Applicable to Vehicles. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `followers_count`unsigned int32 | Number of page followers
 |
| `food_styles`list<string> | The restaurant's food styles. Applicable to Restaurants
 |
| `founded`string | When the company was founded. Applicable to Pages in the Company category. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `general_info`string | General information provided by the Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `general_manager`string | General manager of the business. Applicable to Restaurants or Nightlife. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `genre`string | The genre of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `global_brand_page_name`string | The name of the Page with country codes appended for Global Pages. Only visible to the Page admin. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `global_brand_root_id`numeric string | This brand's global Root ID
 |
| `has_added_app`bool | Indicates whether this Page has added the app making the query in a Page tab. Can be read with Page Public Content Access.
 |
| `has_lead_access`HasLeadAccess | Checks that a user and/or app has the permissions needed to download leads
 |
| `has_transitioned_to_new_page_experience`bool | indicates whether a page has transitioned to new page experience or not
 |
| `has_whatsapp_business_number`bool | Indicates whether WhatsApp number connected to this page is a WhatsApp business number. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `has_whatsapp_number`bool | Indicates whether WhatsApp number connected to this page is a WhatsApp number. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `hometown`string | Hometown of the band. Applicable to Bands
 |
| `hours`map<string, string> | Indicates a single range of opening hours for a day. Each day can have 2 different `hours` ranges. The keys in the map are in the form of `{day}_{number}_{status}`. `{day}` should be the first 3 characters of the day of the week, `{number}` should be either 1 or 2 to allow for the two different hours ranges per day. `{status}` should be either `open` or `close` to delineate the start or end of a time range. 
An example with: 
`{
 "hours": {
 "mon_1_open": "09:00", //open at 9am on Monday
 "mon_1_close": "12:00", //close at 12pm
 "mon_2_open": "13:15", //open at 1:15pm
 "mon_2_close": "18:00". //close at 6pm
 }`
 If one specific day is open 24 hours, the range should be specified as `00:00` to `24:00`. If the place is open 24/7, use the `is_always_open` field instead.
**Note:** If a business is open during the night, the closing time can not pass 6:00am. For example, `"mon_2_open":"13:15"` and `"mon_2_close":"5:59"` will work however `"mon_close_close":"6:00"` will not.
 |
| `impressum`string | Legal information about the Page publishers. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `influences`string | Influences on the band. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `instagram_business_account`IGUser | Instagram account linked to page during Instagram business conversion flow
 |
| `is_always_open`bool | Indicates whether this location is always open. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_chain`bool | Indicates whether location is part of a chain. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_community_page`bool | Indicates whether the Page is a community Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_eligible_for_branded_content`bool | Indicates whether the page is eligible for the branded content tool
 |
| `is_eligible_for_disable_connect_ig_btn_for_non_page_admin_am_web`bool | is\_eligible\_for\_disable\_connect\_ig\_btn\_for\_non\_page\_admin\_am\_web
 |
| `is_messenger_bot_get_started_enabled`bool | Indicates whether the page is a Messenger Platform Bot with Get Started button enabled
 |
| `is_messenger_platform_bot`bool | Indicates whether the page is a Messenger Platform Bot. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_owned`bool | Indicates whether Page is owned. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_permanently_closed`bool | Whether the business corresponding to this Page is permanently closed. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `is_published`bool | Indicates whether the Page is published and visible to non-admins
 |
| `is_unclaimed`bool | Indicates whether the Page is unclaimed
 |
| `is_verified`bool | Deprecated, use "verification\_status". Pages with a large number of followers can be manually verified by Facebook as [having an authentic identity] (https://www.facebook.com/help/196050490547892). This field indicates whether the Page is verified by this process. Can be read with Page Public Content Access or Page Public Metadata Access.
Deprecated |
| `is_webhooks_subscribed`bool | Indicates whether the application is subscribed for real time updates from this page
 |
| `keywords`null | Deprecated. Returns null
Deprecated |
| `leadgen_tos_acceptance_time`datetime | Indicates the time when the TOS for running LeadGen Ads on the page was accepted
 |
| `leadgen_tos_accepted`bool | Indicates whether a user has accepted the TOS for running LeadGen Ads on the Page
 |
| `leadgen_tos_accepting_user`User | Indicates the user who accepted the TOS for running LeadGen Ads on the page
 |
| `link`string | The Page's Facebook URL
Core |
| `location`Location | The location of this place. Applicable to all Places
 |
| `members`string | Members of this org. Applicable to Pages representing Team Orgs. Can be read with Page Public Content Access.
 |
| `merchant_id`string | The instant workflow merchant ID associated with the Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `merchant_review_status`enum | Review status of the Page against FB commerce policies, this status decides whether the Page can use component flow
 |
| `messaging_feature_status`MessagingFeatureStatus | messaging\_feature\_status
 |
| `messenger_ads_default_icebreakers`list<string> | The default ice breakers for a certain page
 |
| `messenger_ads_default_quick_replies`list<string> | The default quick replies for a certain page
 |
| `messenger_ads_quick_replies_type`enum | Indicates what type this page is and we will generate different sets of quick replies based on it. Values include `UNKNOWN`, `PAGE_SHOP`, or `RETAIL`.
 |
| `mission`string | The company mission. Applicable to Companies
 |
| `mpg`string | MPG of the vehicle. Applicable to Vehicles. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `name`string | The name of the Page
CoreDefault |
| `name_with_location_descriptor`string | The name of the Page with its location and/or global brand descriptor. Only visible to a page admin. Non-page admins will get the same value as `name`.
 |
| `network`string | The TV network for the TV show. Applicable to TV Shows. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `new_like_count`unsigned int32 | The number of people who have liked the Page, since the last login. Only visible to a Page admin. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `offer_eligible`bool | Offer eligibility status. Only visible to a page admin
 |
| `overall_star_rating`float | Overall page rating based on rating survey from users on a scale of 1-5. This value is normalized and is not guaranteed to be a strict average of user ratings. If there are 0 or a small number of ratings, this field will not be returned.
 |
| `page_token`string | SELF\_EXPLANATORY
 |
| `parent_page`Page | Parent Page of this Page. If the Page is part of a Global Root Structure and you have permission to the Global Root, the Global Root Parent Page is returned. If you do not have Global Root permission, the Market Page for your current region is returned as the Parent Page. If your Page is not part of a Global Root Structure, the Parent Page is returned.
 |
| `parking`PageParking | Parking information. Applicable to Businesses and Places
 |
| `payment_options`PagePaymentOptions | Payment options accepted by the business. Applicable to Restaurants or Nightlife
 |
| `personal_info`string | Personal information. Applicable to Pages representing People. Can be read with Page Public Content Access.
 |
| `personal_interests`string | Personal interests. Applicable to Pages representing People. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `pharma_safety_info`string | Pharmacy safety information. Applicable to Pharmaceutical companies. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `phone`string | Phone number provided by a Page. Can be read with Page Public Content Access.
 |
| `pickup_options`list<enum> | List of pickup options available at this Page's store location. Values can include `CURBSIDE`, `IN_STORE`, and `OTHER`.
 |
| `place_type`enum | For places, the category of the place. Value can be `CITY`, `COUNTRY`, `EVENT`, `GEO_ENTITY`, `PLACE`, `RESIDENCE`, `STATE_PROVINCE`, or `TEXT`.
 |
| `plot_outline`string | The plot outline of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `preferred_audience`Targeting | Group of tags describing the preferred audienceof ads created for the Page
 |
| `press_contact`string | Press contact information of the band. Applicable to Bands
 |
| `price_range`string | Price range of the business, such as a restaurant or salon. Values can be one of `$`, `$$`, `$$$`, `$$$$`, `Not Applicable`, or `null` if no value is set.. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `privacy_info_url`string | Privacy url in page info section
 |
| `produced_by`string | The productor of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `products`string | The products of this company. Applicable to Companies
 |
| `promotion_eligible`bool | Boosted posts eligibility status. Only visible to a page admin
 |
| `promotion_ineligible_reason`string | Reason for which boosted posts are not eligible. Only visible to a page admin
 |
| `public_transit`string | Public transit to the business. Applicable to Restaurants or Nightlife. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `rating_count`unsigned int32 | Number of ratings for the Page (limited to ratings that are publicly accessible). Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `recipient`numeric string | Messenger page scope id associated with page and a user using account\_linking\_token
 |
| `record_label`string | Record label of the band. Applicable to Bands. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `release_date`string | The film's release date. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `restaurant_services`PageRestaurantServices | Services the restaurant provides. Applicable to Restaurants
 |
| `restaurant_specialties`PageRestaurantSpecialties | The restaurant's specialties. Applicable to Restaurants
 |
| `schedule`string | The air schedule of the TV show. Applicable to TV Shows. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `screenplay_by`string | The screenwriter of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `season`string | The season information of the TV Show. Applicable to TV Shows. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `single_line_address`string | The Page address, if any, in a simple single line format. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `starring`string | The cast of the film. Applicable to Films. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `start_info`PageStartInfo | Information about when the entity represented by the Page was started
 |
| `store_code`string | Unique store code for this location Page. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `store_location_descriptor`string | Location Page's store location descriptor
 |
| `store_number`unsigned int32 | Unique store number for this location Page
 |
| `studio`string | The studio for the film production. Applicable to Films
 |
| `supports_donate_button_in_live_video`bool | Whether the user can add a Donate Button to their Live Videos.
 |
| `talking_about_count`unsigned int32 | The number of people talking about this Page
 |
| `temporary_status`enum | Indicates how the business corresponding to this Page is operating differently than usual. Possible values:
* `differently_open`
* `temporarily_closed`
* `operating_as_usual`
* `no_data`

If set to `differently_open` use with `differently_open_offerings` to set status.
 |
| `unread_message_count`unsigned int32 | Unread message count for the Page. Only visible to a page admin
 |
| `unread_notif_count`unsigned int32 | Number of unread notifications. Only visible to a page admin
 |
| `unseen_message_count`unsigned int32 | Unseen message count for the Page. Only visible to a page admin
 |
| `username`string | The alias of the Page. For example, for www.facebook.com/platform the username is 'platform'
Core |
| `verification_status`string | Showing whether this Page is verified. Value can be `blue_verified` or `gray_verified`, which represents that Facebook has confirmed that a Page is the authentic presence of the public figure, celebrity, or global brand it represents, or `not_verified`. This field can be read with the Page Public Metadata Access feature.
 |
| `voip_info`VoipInfo | Voip info
 |
| `website`string | The URL of the Page's website. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `were_here_count`unsigned int32 | The number of visits to this Page's location. If the Page setting *Show map, check-ins and star ratings on the Page* (under *Page Settings* > *Page Info* > *Address*) is disabled, then this value will also be disabled. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `whatsapp_number`string | The Page's WhatsApp number. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
| `written_by`string | The writer of the TV show. Applicable to TV Shows. Can be read with Page Public Content Access or Page Public Metadata Access.
 |
### Edges

| Edge | Description |
| --- | --- |
| `ab_tests` | ab\_tests
 |
| `ads_posts` | The ad posts for this Page
 |
| `agencies` | Businesses that have agency permissions on the Page
 |
| `albums` | Photo albums for this Page. Can be read with Page Public Content Access.
 |
| `ar_experience` | Page that owns a container
 |
| `assigned_users` | Users assigned to this Page. Can be read with Page Public Content Access.
 |
| `audio_media_copyrights` | The music copyrights owned by this page (using alacorn)
 |
| `blocked` | User or Page Profiles blocked from this Page
 |
| `businessprojects` | Business projects
 |
| `call_to_actions` | The call-to-action created by this Page. Can be read with Page Public Content Access.
 |
| `canvas_elements` | The canvas elements associated with this page
 |
| `canvases` | The canvas documents associated with this page
 |
| `chat_plugin` | customization configuration values of the Page's corresponding Chat Plugin
 |
| `commerce_orders` | The commerce orders of this Page
 |
| `conversations` | This Page's conversations
 |
| `crosspost_whitelisted_pages` | Pages that are allowed to crosspost
 |
| `custom_labels` | custom\_labels
 |
| `custom_user_settings` | Custom user settings for a page
 |
| `fantasy_games` | Fantasy Games sponsored by this page
 |
| `feed` | This Page's feed. Can be read with Page Public Content Access.
 |
| `global_brand_children` | Children Pages of a Global Pages root Page. Both default and root Page can return children Pages. Can be read with Page Public Content Access.
 |
| `groups` | groups
 |
| `image_copyrights` | Image copyrights from this page
 |
| `insights` | This Page's Insights data
 |
| `instagram_accounts` | Linked Instagram accounts for this Page
 |
| `leadgen_forms` | A library of lead generation forms created for this page.
 |
| `likes` | The Pages that this Page has liked. Can be read with Page Public Content Access. For New Page Experience Pages, this field will return `followers_count`.
Core |
| `live_videos` | Live videos on this Page. Can be read with Page Public Content Access.
 |
| `locations` | The location Pages that are children of this Page. Can be read with Page Public Content Access. To manage a child Page's location use the `/{page-id}/locations` endpoint.
 |
| `media_fingerprints` | Media fingerprints from this page
 |
| `messaging_feature_review` | Feature status of the page that has been granted through feature review that show up in the page settings
 |
| `messenger_lead_forms` | messenger\_lead\_forms
 |
| `messenger_profile` | SELF\_EXPLANATORY
 |
| `page_backed_instagram_accounts` | Gets the Page Backed Instagram Account (an InstagramUser) associated with this Page.
 |
| `personas` | Messenger Platform Bot personas for the Page
 |
| `photos` | This Page's Photos. Can be read with Page Public Content Access.
 |
| `picture` | This Page's profile picture
Core |
| `posts` | This Page's own Posts, a derivative of the `/feed` edge. Can be read with Page Public Content Access.
 |
| `product_catalogs` | Product catalogs owned by this page
 |
| `published_posts` | All published posts by this page
 |
| `ratings` | Open Graph ratings given to this Page
 |
| `roles` | The Page's Admins
 |
| `scheduled_posts` | All posts that are scheduled to a future date by a page
 |
| `secondary_receivers` | Secondary Receivers for a page
 |
| `settings` | Controllable settings for this page
 |
| `shop_setup_status` | Shows the shop setup status
 |
| `subscribed_apps` | Applications that have real time update subscriptions for this Page. Note that we will only return information about the current app
 |
| `tabs` | This Page's tabs and the apps in them. Can be read with Page Public Content Access.
 |
| `tagged` | The Photos, Videos, and Posts in which the Page has been tagged. A derivative of `/feeds`. Can be read with Page Public Content Access.
 |
| `thread_owner` | App which owns a thread for Handover Protocol
 |
| `threads` | Deprecated. Use conversations instead
 |
| `video_copyright_rules` | Video copyright rules from this page
 |
| `video_lists` | Video Playlists for this Page
 |
| `videos` | Videos for this Page. Can be read with Page Public Content Access.
 |
| `visitor_posts` | Shows all public Posts published by Page visitors on the Page. Can be read with Page Public Content Access.
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 110 | Invalid user id |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 9009 | Instagram user is unavailable |
| 80002 | There have been too many calls to this Instagram account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 230 | Permissions disallow message to user |
| 210 | User not visible |
Creating
--------
This is only available to select developers. Please contact your Facebook Partner for more information.
You can make a POST request to `take_thread_control` edge from the following paths: * `/{page_id}/take_thread_control`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `metadata`string | Additional information about the conversation
 |
| `recipient`Object | The PSID for the customer who sent the message to your business
Required |
| `id`numeric string |  |
| `phone_number`string |  |
| `name`Object |  |
| `first_name`string |  |
| `last_name`string |  |
| `user_ref`string |  |
| `comment_id` |  |
| `post_id`string |  |
| `player_id`player ID |  |
| `one_time_notif_token`string |  |
| `notification_messages_token`string |  |
| `login_id`string |  |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 551 | This person isn't available right now. |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 504 | Invalid reply thread id |
You can make a POST request to `personas` edge from the following paths: * `/{page_id}/personas`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `name`string | Name of a Persona
Required |
| `profile_picture_url`URI | Profile picture of a Persona
Required |
### Return Type
 Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
You can make a POST request to `nlp_configs` edge from the following paths: * `/{page_id}/nlp_configs`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `api_version`enum {} | api\_version
 |
| `custom_token`string | An optional Wit token enable custom entities
 |
| `model`enum {ARABIC, CHINESE, CROATIAN, CUSTOM, DANISH, DUTCH, ENGLISH, FRENCH\_STANDARD, GEORGIAN, GERMAN\_STANDARD, GREEK, HEBREW, HUNGARIAN, IRISH, ITALIAN\_STANDARD, KOREAN, NORWEGIAN\_BOKMAL, POLISH, PORTUGUESE, ROMANIAN, SPANISH, SWEDISH, VIETNAMESE} | An option for which model to use in production.
 |
| `n_best`int64 | The number of intents and traits to return, other than the best one.
 |
| `nlp_enabled`boolean | A boolean to enable/disable Built-In NLP.
 |
| `other_language_support`JSON object {string : JSON object} | A map of language to model type and Wit token for language identification.
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
You can make a POST request to `subscribed_apps` edge from the following paths: * `/{page_id}/subscribed_apps`
When posting to this edge, a Page will be created.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
POST /v19.0/{page-id}/subscribed_apps HTTP/1.1
Host: graph.facebook.com
subscribed_fields=leadgen
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{page-id}/subscribed_apps',
    array (
      'subscribed_fields' => 'leadgen',
    ),
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```
```
/* make the API call */
FB.api(
    "/{page-id}/subscribed_apps",
    "POST",
    {
        "subscribed_fields": "leadgen"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("subscribed_fields", "leadgen");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-id}/subscribed_apps",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"subscribed_fields": @"leadgen",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-id}/subscribed_apps"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
```
curl -X POST \
  -F 'subscribed_fields="leadgen"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{page-id}/subscribed_apps
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `subscribed_fields`array<enum {feed, mention, name, picture, category, description, conversations, feature\_access\_list, inbox\_labels, standby, message\_mention, messages, message\_reactions, messaging\_account\_linking, messaging\_checkout\_updates, messaging\_customer\_information, message\_echoes, message\_deliveries, message\_context, messaging\_game\_plays, messaging\_optins, messaging\_optouts, messaging\_payments, messaging\_postbacks, messaging\_pre\_checkouts, message\_reads, messaging\_referrals, messaging\_handovers, messaging\_policy\_enforcement, messaging\_appointments, messaging\_direct\_sends, messaging\_fblogin\_account\_linking, user\_action, messaging\_feedback, send\_cart, otp\_verification, group\_feed, messaging\_in\_thread\_lead\_form\_submit, founded, company\_overview, mission, products, general\_info, leadgen, leadgen\_fat, location, hours, parking, public\_transit, page\_about\_story, mcom\_invoice\_change, invoice\_access\_invoice\_change, invoice\_access\_invoice\_draft\_change, invoice\_access\_onboarding\_status\_active, invoice\_access\_bank\_slip\_events, local\_delivery, phone, email, website, ratings, attire, payment\_options, culinary\_team, general\_manager, price\_range, awards, hometown, current\_location, bio, affiliation, birthday, personal\_info, personal\_interests, members, checkins, page\_upcoming\_change, page\_change\_proposal, merchant\_review, product\_review, videos, live\_videos, video\_text\_question\_responses, registration, publisher\_subscriptions, invalid\_topic\_placeholder}> | Page Webhooks fields that you want to subscribe
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 210 | User not visible |
| 190 | Invalid OAuth 2.0 Access Token |
You can make a POST request to `messenger_lead_forms` edge from the following paths: * `/{page_id}/messenger_lead_forms`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `account_id`int64 | ID of the account
 |
| `block_send_api`boolean | Whether to block messages sent using Send API while user is in Lead Gen Experience
 |
| `handover_app_id`int64 | Hand over thread to specified app after leadgen is complete
 |
| `handover_summary`boolean | Opt-in to get a summary message sent to the target HOP app at the end of the automated flow
 |
| `privacy_url`URI | Privacy URL for Messenger Lead Gen Experience
 |
| `reminder_text`string | Reminder text that will be sent to user after inactivity
 |
| `step_list`array<JSON object> | List of steps in Messenger Lead Gen Experience
Required |
| `step_id`int64 | step\_id
Required |
| `message`string | message
Required |
| `step_type`enum {QUESTION, CONFIRMATION, DISCLAIMER, DISQUALIFY, INFO, INTRO, SUMMARY, POST\_LEAD\_TRANSITION} | step\_type
Required |
| `reply_type`enum {QUICK\_REPLIES, TEXT, NONE, PREFILL, ICE\_BREAKERS, APPOINTMENT, SUBSCRIBE, CALL\_PREFERENCE} | reply\_type
Required |
| `answers`array<string> | Default value: `[]`answers
 |
| `next_step_ids`array<int64> | Default value: `[]`next\_step\_ids
 |
| `prefill_type`enum {FULL\_ADDRESS, STREET\_ADDRESS, ZIP\_CODE, POST\_CODE, CITY, STATE, PROVINCE, COUNTRY, EMAIL, PHONE, PHONE\_OTP, JOB\_TITLE, COMPANY\_NAME, GENDER, DOB, DATE\_TIME, SLIDER, NONE, FIRST\_NAME, LAST\_NAME, FULL\_NAME, RELATIONSHIP\_STATUS, MARITAL\_STATUS, MILITARY\_STATUS, WORK\_EMAIL, WORK\_PHONE, NATIONAL\_ID\_BRAZIL, NATIONAL\_ID\_ARGENTINA, NATIONAL\_ID\_PERU, NATIONAL\_ID\_CHILE, NATIONAL\_ID\_COLOMBIA, NATIONAL\_ID\_ECUADOR, NATIONAL\_ID\_MEXICO} | Default value: `"NONE"`prefill\_type
 |
| `crm_field_id`string | crm\_field\_id
 |
| `answer_crm_field_ids`array<string> | Default value: `[]`answer\_crm\_field\_ids
 |
| `media_type`enum {TEXT, IMAGE, VIDEO} | media\_type
 |
| `media_content`string | media\_content
 |
| `options_format`enum {TEXT, CAROUSEL} | Default value: `"TEXT"`options\_format
 |
| `carousel_answers`array<JSON object> | Default value: `[]`carousel\_answers
 |
| `value`string | value
Required |
| `media_content`string | media\_content
Required |
| `answer_validation_enabled`boolean | answer\_validation\_enabled
 |
| `invalid_reply_text`string | invalid\_reply\_text
 |
| `cta`JSON object | cta
 |
| `cta_type`enum {VIEW\_WEBSITE, CALL\_BUSINESS, MESSAGE\_BUSINESS, DOWNLOAD, SCHEDULE\_APPOINTMENT, VIEW\_ON\_FACEBOOK, NONE} | cta\_type
Required |
| `cta_text`string | cta\_text
Required |
| `cta_content`string | cta\_content
Required |
| `allow_to_skip`boolean | allow\_to\_skip
 |
| `qualifying_answers_list`array<string> | qualifying\_answers\_list
 |
| `next_step_on_disqualification_id`int64 | next\_step\_on\_disqualification\_id
 |
| `offer_code_file_id`int64 | offer\_code\_file\_id
 |
| `offer_code`string | offer\_code
 |
| `offer_code_format`string | offer\_code\_format
 |
| `stop_question_message`string | Confirmation message after user clicks on the Stop Question option in persistent menu
 |
| `template_name`string | Name for the form
 |
| `tracking_parameters`JSON object {string : string} | Tracking Parameters of Lead Forms
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
You can make a POST request to `leadgen_forms` edge from the following paths: * `/{page_id}/leadgen_forms`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `allow_organic_lead_retrieval`boolean | Default value: `true`Previously, this flag controlled whether any leads submitted in a non-Ad context were retrievable. Now this flag will not be considered and it will be deprecated entirely. To control visibility of Lead Forms in a non-Ad context you should use 'block\_display\_for\_non\_targeted\_viewer'
 |
| `block_display_for_non_targeted_viewer`boolean | Whether to make the organic post invisible to viewers in non-Ad context
 |
| `context_card`Object | Optional context card shown as the intro page
Supports Emoji |
| `title`string |  |
| `style`enum {LIST\_STYLE, PARAGRAPH\_STYLE} |  |
| `content`array<string> |  |
| `button_text`string |  |
| `cover_photo_id`photo ID |  |
| `cover_photo`file | Custom cover photo for context card
 |
| `custom_disclaimer`Object | Customized disclaimer including title, body content with inline links, and consent checkboxes
 |
| `title`string |  |
| `body`Object |  |
| `text`string | Required |
| `url_entities`list<JSON object> |  |
| `checkboxes`list<Object> |  |
| `is_required`boolean | Default value: `true` |
| `is_checked_by_default`boolean | Default value: `false` |
| `text`string | Required |
| `key`string |  |
| `follow_up_action_url`URI | The final destination URL that user will go to when clicking view website button
 |
| `is_for_canvas`boolean | Default value: `false`Flag to indicate that the form is going to be used under a canvas
 |
| `is_optimized_for_quality`boolean | Default value: `false`Flag to indicate whether the form will be optimized for quality
 |
| `locale`enum {AR\_AR, CS\_CZ, DA\_DK, DE\_DE, EL\_GR, EN\_GB, EN\_US, ES\_ES, ES\_LA, FI\_FI, FR\_FR, HE\_IL, HI\_IN, HU\_HU, ID\_ID, IT\_IT, JA\_JP, KO\_KR, NB\_NO, NL\_NL, PL\_PL, PT\_BR, PT\_PT, RO\_RO, RU\_RU, SV\_SE, TH\_TH, TR\_TR, VI\_VN, ZH\_CN, ZH\_HK, ZH\_TW} | The locale of the form. Pre-defined questions renders in this locale
 |
| `name`string | The name that will help identity the form
Required |
| `privacy_policy`Object | The url and link\_text of the privacy policy of advertiser. link\_text is limited to a maximum of 70 characters.
 |
| `url`string |  |
| `link_text`string |  |
| `question_page_custom_headline`string | The custom headline for the question page within the form
 |
| `questions`list<Object> | An array of questions of the form
Required |
| `key`string |  |
| `label`string |  |
| `type`enum {CUSTOM, CITY, COMPANY\_NAME, COUNTRY, DOB, EMAIL, GENDER, FIRST\_NAME, FULL\_NAME, JOB\_TITLE, LAST\_NAME, MARITIAL\_STATUS, PHONE, PHONE\_OTP, POST\_CODE, PROVINCE, RELATIONSHIP\_STATUS, STATE, STREET\_ADDRESS, ZIP, WORK\_EMAIL, MILITARY\_STATUS, WORK\_PHONE\_NUMBER, SLIDER, STORE\_LOOKUP, STORE\_LOOKUP\_WITH\_TYPEAHEAD, DATE\_TIME, ID\_CPF, ID\_AR\_DNI, ID\_CL\_RUT, ID\_CO\_CC, ID\_EC\_CI, ID\_PE\_DNI, ID\_MX\_RFC, JOIN\_CODE, USER\_PROVIDED\_PHONE\_NUMBER, FACEBOOK\_LEAD\_ID, EMAIL\_ALIAS, MESSENGER} | Required |
| `inline_context`string |  |
| `options`list<JSON object> |  |
| `dependent_conditional_questions`list<JSON object> |  |
| `conditional_questions_group_id`LeadGen Conditional Questions Group ID |  |
| `thank_you_page`Object | Optional customized thank you page displayed post submission
 |
| `title`string | Required |
| `body`string | Required |
| `short_message`string |  |
| `button_text`string |  |
| `button_description`string |  |
| `business_phone_number`phone number string |  |
| `enable_messenger`boolean | Default value: `false` |
| `website_url`string |  |
| `button_type`enum {VIEW\_WEBSITE, CALL\_BUSINESS, MESSAGE\_BUSINESS, DOWNLOAD, SCHEDULE\_APPOINTMENT, VIEW\_ON\_FACEBOOK, NONE} | Required |
| `country_code`string |  |
| `tracking_parameters`JSON object {string : string} | Map for additional tracking parameters to include with the form's field data
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 192 | Invalid phone number |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
You can make a POST request to `owned_pages` edge from the following paths: * `/{business_id}/owned_pages`
When posting to this edge, a Page will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `entry_point`string | entry point of claiming BusinessClaimAssetEntryPoint
 |
| `page_id`Page ID | Page ID.
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`access_status`: string, }### Error Codes

| Error | Description |
| --- | --- |
| 413 | Invalid password |
| 200 | Permissions error |
| 3982 | You do not have sufficient permissions to import this asset into the given Business Manager. |
| 3944 | Your Business Manager already has access to this object. |
| 100 | Invalid parameter |
| 457 | The session has an invalid origin |
| 42000 | This Page can't be added because it's already linked to an Instagram business profile. To add this Page to Business Manager, go to Instagram and convert to a personal account or change the Page linked to your business profile. |
| 3977 | To claim a Page in Business Manager, you must already be an Admin of the Page. |
| 3948 | Please assign someone as a manager to this Page before removing it from your Business Manager. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
You can make a POST request to `feed` edge from the following paths: * `/{page_id}/feed`
When posting to this edge, a Page will be created.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
POST /v19.0/{page-id}/feed HTTP/1.1
Host: graph.facebook.com
message=This+is+a+test+value
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/{page-id}/feed',
    array (
      'message' => 'This is a test value',
    ),
    '{access-token}'
  );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}
$graphNode = $response->getGraphNode();
/* handle the result */
```
```
/* make the API call */
FB.api(
    "/{page-id}/feed",
    "POST",
    {
        "message": "This is a test value"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("message", "This is a test value");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-id}/feed",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"message": @"This is a test value",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-id}/feed"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
```
curl -X POST \
  -F 'message="This is a test value"' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{page-id}/feed
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `actions` | SELF\_EXPLANATORY
 |
| `adaptive_type`string | adaptive\_type
 |
| `album_id`numeric string | SELF\_EXPLANATORY
 |
| `android_key_hash`string | SELF\_EXPLANATORY
 |
| `animated_effect_id`int64 | animated\_effect\_id
 |
| `application_id`non-empty string | SELF\_EXPLANATORY
 |
| `asked_fun_fact_prompt_id`int64 | asked\_fun\_fact\_prompt\_id
 |
| `asset3d_id`int64 | asset3d\_id
 |
| `associated_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `attach_place_suggestion`boolean | Default value: `false`SELF\_EXPLANATORY
 |
| `attached_media`list<Object> | SELF\_EXPLANATORY
 |
| `media_fbid`numeric string |  |
| `message`UTF-8 string | Supports Emoji |
| `audience_exp`boolean | Default value: `false`SELF\_EXPLANATORY
 |
| `backdated_time`datetime | SELF\_EXPLANATORY
 |
| `backdated_time_granularity`enum{year, month, day, hour, min, none} | Default value: `none`SELF\_EXPLANATORY
 |
| `breaking_news`boolean | breaking\_news
 |
| `breaking_news_expiration`int64 | breaking\_news\_expiration
 |
| `call_to_action`Object | SELF\_EXPLANATORY
Supports Emoji |
| `type`enum{BOOK\_TRAVEL, CONTACT\_US, DONATE, DONATE\_NOW, DOWNLOAD, GET\_DIRECTIONS, GO\_LIVE, INTERESTED, LEARN\_MORE, LIKE\_PAGE, MESSAGE\_PAGE, RAISE\_MONEY, SAVE, SEND\_TIP, SHOP\_NOW, SIGN\_UP, VIEW\_INSTAGRAM\_PROFILE, INSTAGRAM\_MESSAGE, LOYALTY\_LEARN\_MORE, PURCHASE\_GIFT\_CARDS, PAY\_TO\_ACCESS, SEE\_MORE, TRY\_IN\_CAMERA, WHATSAPP\_LINK, BOOK\_NOW, CHECK\_AVAILABILITY, ORDER\_NOW, WHATSAPP\_MESSAGE, GET\_MOBILE\_APP, INSTALL\_MOBILE\_APP, USE\_MOBILE\_APP, INSTALL\_APP, USE\_APP, PLAY\_GAME, WATCH\_VIDEO, WATCH\_MORE, OPEN\_LINK, NO\_BUTTON, LISTEN\_MUSIC, MOBILE\_DOWNLOAD, GET\_OFFER, GET\_OFFER\_VIEW, BUY\_NOW, BUY\_TICKETS, UPDATE\_APP, BET\_NOW, ADD\_TO\_CART, SELL\_NOW, GET\_SHOWTIMES, LISTEN\_NOW, GET\_EVENT\_TICKETS, REMIND\_ME, SEARCH\_MORE, PRE\_REGISTER, SWIPE\_UP\_PRODUCT, SWIPE\_UP\_SHOP, PLAY\_GAME\_ON\_FACEBOOK, VISIT\_WORLD, OPEN\_INSTANT\_APP, JOIN\_GROUP, GET\_PROMOTIONS, SEND\_UPDATES, INQUIRE\_NOW, VISIT\_PROFILE, CHAT\_ON\_WHATSAPP, EXPLORE\_MORE, CONFIRM, JOIN\_CHANNEL, CALL, MISSED\_CALL, CALL\_NOW, CALL\_ME, APPLY\_NOW, BUY, GET\_QUOTE, SUBSCRIBE, RECORD\_NOW, VOTE\_NOW, GIVE\_FREE\_RIDES, REGISTER\_NOW, OPEN\_MESSENGER\_EXT, EVENT\_RSVP, CIVIC\_ACTION, SEND\_INVITES, REFER\_FRIENDS, REQUEST\_TIME, SEE\_MENU, SEARCH, TRY\_IT, TRY\_ON, LINK\_CARD, DIAL\_CODE, FIND\_YOUR\_GROUPS, START\_ORDER} | The type of the action. Not all types can be used for all
 ads. Check
 Ads Product Guide
 to see which type can be used for based on the `objective` of your
 campaign.
Required |
| `value`Object | Default value: `Vec`JSON containing the call to action data.
Supports Emoji |
| `link`URL |  |
| `app_link`string |  |
| `page`numeric string or integer |  |
| `link_format`enum {VIDEO\_LEAD, VIDEO\_LPP, VIDEO\_NEKO, VIDEO\_NON\_LINK, VIDEO\_SHOP, WHATSAPP\_CATALOG\_ATTACHMENT} |  |
| `application`numeric string or integer |  |
| `link_title`string | Supports Emoji |
| `link_description`string | Supports Emoji |
| `link_caption`string |  |
| `product_link`string |  |
| `get_movie_showtimes`boolean |  |
| `sponsorship`Object |  |
| `link`URL |  |
| `image`URL |  |
| `video_annotation`Object |  |
| `annotations`list<Object> |  |
| `start_time_in_sec`int64 |  |
| `end_time_in_sec`int64 |  |
| `link`URL |  |
| `link_title`string |  |
| `link_description`string |  |
| `link_caption`string |  |
| `image_url`URL |  |
| `header_color`string |  |
| `logo_url`URL |  |
| `post_click_cta_title`string |  |
| `post_click_description_title`string |  |
| `offer_id`numeric string or integer |  |
| `offer_view_id`numeric string or integer |  |
| `advanced_data`Object |  |
| `offer_id`numeric string or integer |  |
| `lead_gen_form_id`numeric string or integer |  |
| `referral_id`numeric string or integer |  |
| `fundraiser_campaign_id`numeric string or integer |  |
| `event_id`numeric string or integer |  |
| `event_tour_id`numeric string or integer |  |
| `app_destination`enum {MESSENGER, MESSENGER\_EXTENSIONS, MESSENGER\_GAMES, LINK\_CARD, MARKETPLACE, WHATSAPP, INSTAGRAM\_DIRECT} |  |
| `app_destination_page_id`numeric string or integer |  |
| `is_canvas_video_transition_enabled`boolean |  |
| `whatsapp_number`string |  |
| `preinput_text`string |  |
| `customized_message_page_cta_text`string |  |
| `external_offer_provider_id`numeric string or integer |  |
| `origins`enum {COMPOSER, CAMERA} |  |
| `object_store_urls`array<string> |  |
| `facebook_login_spec`Object |  |
| `facebook_login_app_id`numeric string or integer |  |
| `offer_type`enum {NO\_OFFER, PERCENTAGE\_BASED, AMOUNT\_BASED} |  |
| `offer_pct_call_to_action`enum {TEN} |  |
| `offer_amt_call_to_action`enum {TEN} |  |
| `product_id`numeric string or integer |  |
| `group_id`numeric string or integer |  |
| `caption`string | SELF\_EXPLANATORY
Supports Emoji |
| `child_attachments`list<Object> | SELF\_EXPLANATORY
Supports Emoji |
| `picture`URL |  |
| `name`string | Supports Emoji |
| `link`URL | Required |
| `caption`string | Supports Emoji |
| `description`string | Supports Emoji |
| `quote`UTF-8 string | Supports Emoji |
| `source`URL |  |
| `properties` |  |
| `object_attachment`numeric string or integer |  |
| `height`int64 |  |
| `width`int64 |  |
| `expanded_height`int64 |  |
| `expanded_width`int64 |  |
| `referral_id`numeric string or integer |  |
| `thumbnail`file |  |
| `image_crops`dictionary { enum{191x100, 100x72, 400x150, 600x360, 100x100, 400x500, 90x160} : <list<list<int64>>> } |  |
| `call_to_action`Object | Supports Emoji |
| `type`enum{BOOK\_TRAVEL, CONTACT\_US, DONATE, DONATE\_NOW, DOWNLOAD, GET\_DIRECTIONS, GO\_LIVE, INTERESTED, LEARN\_MORE, LIKE\_PAGE, MESSAGE\_PAGE, RAISE\_MONEY, SAVE, SEND\_TIP, SHOP\_NOW, SIGN\_UP, VIEW\_INSTAGRAM\_PROFILE, INSTAGRAM\_MESSAGE, LOYALTY\_LEARN\_MORE, PURCHASE\_GIFT\_CARDS, PAY\_TO\_ACCESS, SEE\_MORE, TRY\_IN\_CAMERA, WHATSAPP\_LINK, BOOK\_NOW, CHECK\_AVAILABILITY, ORDER\_NOW, WHATSAPP\_MESSAGE, GET\_MOBILE\_APP, INSTALL\_MOBILE\_APP, USE\_MOBILE\_APP, INSTALL\_APP, USE\_APP, PLAY\_GAME, WATCH\_VIDEO, WATCH\_MORE, OPEN\_LINK, NO\_BUTTON, LISTEN\_MUSIC, MOBILE\_DOWNLOAD, GET\_OFFER, GET\_OFFER\_VIEW, BUY\_NOW, BUY\_TICKETS, UPDATE\_APP, BET\_NOW, ADD\_TO\_CART, SELL\_NOW, GET\_SHOWTIMES, LISTEN\_NOW, GET\_EVENT\_TICKETS, REMIND\_ME, SEARCH\_MORE, PRE\_REGISTER, SWIPE\_UP\_PRODUCT, SWIPE\_UP\_SHOP, PLAY\_GAME\_ON\_FACEBOOK, VISIT\_WORLD, OPEN\_INSTANT\_APP, JOIN\_GROUP, GET\_PROMOTIONS, SEND\_UPDATES, INQUIRE\_NOW, VISIT\_PROFILE, CHAT\_ON\_WHATSAPP, EXPLORE\_MORE, CONFIRM, JOIN\_CHANNEL, CALL, MISSED\_CALL, CALL\_NOW, CALL\_ME, APPLY\_NOW, BUY, GET\_QUOTE, SUBSCRIBE, RECORD\_NOW, VOTE\_NOW, GIVE\_FREE\_RIDES, REGISTER\_NOW, OPEN\_MESSENGER\_EXT, EVENT\_RSVP, CIVIC\_ACTION, SEND\_INVITES, REFER\_FRIENDS, REQUEST\_TIME, SEE\_MENU, SEARCH, TRY\_IT, TRY\_ON, LINK\_CARD, DIAL\_CODE, FIND\_YOUR\_GROUPS, START\_ORDER} | The type of the action. Not all types can be used for all
 ads. Check
 Ads Product Guide
 to see which type can be used for based on the `objective` of your
 campaign.
Required |
| `value`Object | Default value: `Vec`JSON containing the call to action data.
Supports Emoji |
| `link`URL |  |
| `app_link`string |  |
| `page`numeric string or integer |  |
| `link_format`enum {VIDEO\_LEAD, VIDEO\_LPP, VIDEO\_NEKO, VIDEO\_NON\_LINK, VIDEO\_SHOP, WHATSAPP\_CATALOG\_ATTACHMENT} |  |
| `application`numeric string or integer |  |
| `link_title`string | Supports Emoji |
| `link_description`string | Supports Emoji |
| `link_caption`string |  |
| `product_link`string |  |
| `get_movie_showtimes`boolean |  |
| `sponsorship`Object |  |
| `link`URL |  |
| `image`URL |  |
| `video_annotation`Object |  |
| `annotations`list<Object> |  |
| `start_time_in_sec`int64 |  |
| `end_time_in_sec`int64 |  |
| `link`URL |  |
| `link_title`string |  |
| `link_description`string |  |
| `link_caption`string |  |
| `image_url`URL |  |
| `header_color`string |  |
| `logo_url`URL |  |
| `post_click_cta_title`string |  |
| `post_click_description_title`string |  |
| `offer_id`numeric string or integer |  |
| `offer_view_id`numeric string or integer |  |
| `advanced_data`Object |  |
| `offer_id`numeric string or integer |  |
| `lead_gen_form_id`numeric string or integer |  |
| `referral_id`numeric string or integer |  |
| `fundraiser_campaign_id`numeric string or integer |  |
| `event_id`numeric string or integer |  |
| `event_tour_id`numeric string or integer |  |
| `app_destination`enum {MESSENGER, MESSENGER\_EXTENSIONS, MESSENGER\_GAMES, LINK\_CARD, MARKETPLACE, WHATSAPP, INSTAGRAM\_DIRECT} |  |
| `app_destination_page_id`numeric string or integer |  |
| `is_canvas_video_transition_enabled`boolean |  |
| `whatsapp_number`string |  |
| `preinput_text`string |  |
| `customized_message_page_cta_text`string |  |
| `external_offer_provider_id`numeric string or integer |  |
| `origins`enum {COMPOSER, CAMERA} |  |
| `object_store_urls`array<string> |  |
| `facebook_login_spec`Object |  |
| `facebook_login_app_id`numeric string or integer |  |
| `offer_type`enum {NO\_OFFER, PERCENTAGE\_BASED, AMOUNT\_BASED} |  |
| `offer_pct_call_to_action`enum {TEN} |  |
| `offer_amt_call_to_action`enum {TEN} |  |
| `product_id`numeric string or integer |  |
| `group_id`numeric string or integer |  |
| `image_hash`string |  |
| `static_card`boolean |  |
| `place_data`Object |  |
| `address_string`string |  |
| `label`string |  |
| `latitude` |  |
| `location_source_id`location page/page set ID |  |
| `longitude` |  |
| `type`enum {DYNAMIC, REALTIME, SINGLE} | Required |
| `video_id`numeric string or integer |  |
| `caption_ids`list<numeric string or integer> |  |
| `offer_id`numeric string or integer |  |
| `client_mutation_id`string | SELF\_EXPLANATORY
 |
| `composer_entry_picker`string | composer\_entry\_picker
 |
| `composer_entry_point`string | composer\_entry\_point
 |
| `composer_entry_time`int64 | composer\_entry\_time
 |
| `composer_session_events_log`JSON-encoded string | composer\_session\_events\_log
 |
| `composer_session_id`string | SELF\_EXPLANATORY
 |
| `composer_source_surface`string | composer\_source\_surface
 |
| `composer_type`string | composer\_type
 |
| `connection_class`string | SELF\_EXPLANATORY
 |
| `content_attachment`numeric string | content\_attachment
 |
| `coordinates`JSON-encoded coordinate list | SELF\_EXPLANATORY
 |
| `cta_link`string | cta\_link
 |
| `cta_type`string | cta\_type
 |
| `description`string | SELF\_EXPLANATORY
Supports Emoji |
| `direct_share_status`int64 | direct\_share\_status
 |
| `enforce_link_ownership`boolean | Default value: `false`SELF\_EXPLANATORY
 |
| `expanded_height`int64 | SELF\_EXPLANATORY
 |
| `expanded_width`int64 | SELF\_EXPLANATORY
 |
| `feed_targeting`feed target | SELF\_EXPLANATORY
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> | Values for targeted locales. Use `type` of `adlocale` to find Targeting Options and use the returned key to specify.
 |
| `age_min`int64 | Must be `13` or higher. Default is 0.
 |
| `age_max`int64 | Maximum age.
 |
| `genders`list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both.
 |
| `college_years`list<int64> | Array of integers. Represent graduation years from college.
 |
| `education_statuses`list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents).
 |
| `interested_in`list<int64> | Deprecated. Please see the Graph API Changelog for more information.
Deprecated |
| `relationship_statuses`list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types.
 |
| `interests`list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as find Targeting Options and use the returned id to specify.
 |
| `formatting`enum {PLAINTEXT, MARKDOWN} | formatting
 |
| `fun_fact_prompt_id`int64 | fun\_fact\_prompt\_id
 |
| `fun_fact_toastee_id`int64 | fun\_fact\_toastee\_id
 |
| `has_nickname`boolean | has\_nickname
 |
| `height`int64 | SELF\_EXPLANATORY
 |
| `holiday_card`JSON-encoded string | holiday\_card
 |
| `home_checkin_city_id`place tag | SELF\_EXPLANATORY
 |
| `image_crops`dictionary { enum{191x100, 100x72, 400x150, 600x360, 100x100, 400x500, 90x160} : <list<list<int64>>> } | SELF\_EXPLANATORY
 |
| `implicit_with_tags`list<int> | SELF\_EXPLANATORY
 |
| `instant_game_entry_point_data`string | instant\_game\_entry\_point\_data
 |
| `ios_bundle_id`string | SELF\_EXPLANATORY
 |
| `is_backout_draft`boolean | is\_backout\_draft
 |
| `is_boost_intended`boolean | is\_boost\_intended
 |
| `is_explicit_location`boolean | SELF\_EXPLANATORY
 |
| `is_explicit_share`boolean | SELF\_EXPLANATORY
 |
| `is_group_linking_post`boolean | is\_group\_linking\_post
 |
| `is_photo_container`boolean | SELF\_EXPLANATORY
 |
| `link`URL | SELF\_EXPLANATORY
 |
| `location_source_id`numeric string or integer | location\_source\_id
 |
| `manual_privacy`boolean | Default value: `false`SELF\_EXPLANATORY
 |
| `message`UTF-8 string | SELF\_EXPLANATORY
Supports Emoji |
| `multi_share_end_card`boolean | Default value: `true`SELF\_EXPLANATORY
 |
| `multi_share_optimized`boolean | Default value: `true`SELF\_EXPLANATORY
 |
| `name`string | SELF\_EXPLANATORY
Supports Emoji |
| `nectar_module`string | SELF\_EXPLANATORY
 |
| `object_attachment`numeric string or integer | SELF\_EXPLANATORY
 |
| `offer_like_post_id`int64 | offer\_like\_post\_id
 |
| `og_action_type_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `og_hide_object_attachment`boolean | SELF\_EXPLANATORY
 |
| `og_icon_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `og_object_id`OG object ID or URL string | SELF\_EXPLANATORY
 |
| `og_phrase`UTF-8 string | SELF\_EXPLANATORY
Supports Emoji |
| `og_set_profile_badge`boolean | Default value: `false`og\_set\_profile\_badge
 |
| `og_suggestion_mechanism`string | SELF\_EXPLANATORY
 |
| `page_recommendation`JSON-encoded string | page\_recommendation
 |
| `picture`URL | SELF\_EXPLANATORY
 |
| `place`place tag | SELF\_EXPLANATORY
 |
| `place_attachment_setting`enum {1, 2} | Default value: `2`place\_attachment\_setting
 |
| `place_list`JSON-encoded string | place\_list
 |
| `place_list_data`array | place\_list\_data
 |
| `post_surfaces_blacklist`list<enum {1, 2, 3, 4, 5}> | post\_surfaces\_blacklist
 |
| `posting_to_redspace`enum {enabled, disabled} | Default value: `disabled`posting\_to\_redspace
 |
| `privacy`Privacy Parameter | SELF\_EXPLANATORY
 |
| `prompt_id`string | prompt\_id
 |
| `prompt_tracking_string`string | prompt\_tracking\_string
 |
| `properties` | SELF\_EXPLANATORY
 |
| `proxied_app_id`numeric string or integer | SELF\_EXPLANATORY
 |
| `publish_event_id`int64 | publish\_event\_id
 |
| `published`boolean | Default value: `true`SELF\_EXPLANATORY
 |
| `quote`UTF-8 string | quote
Supports Emoji |
| `react_mode_metadata`JSON-encoded string | This metadata is required for clip reacts feature
 |
| `ref`list<string> | Default value: `Default`SELF\_EXPLANATORY
 |
| `referenceable_image_ids`list<numeric string or integer> | referenceable\_image\_ids
 |
| `referral_id`numeric string or integer | referral\_id
 |
| `scheduled_publish_time`datetime | SELF\_EXPLANATORY
 |
| `source`URL | SELF\_EXPLANATORY
 |
| `sponsor_id`numeric string or integer | sponsor\_id
 |
| `sponsor_relationship`int64 | sponsor\_relationship
 |
| `suggested_place_id`place tag | SELF\_EXPLANATORY
 |
| `tags`list<int> | SELF\_EXPLANATORY
 |
| `target_surface`enum {STORY, TIMELINE} | Default value: `"TIMELINE"`target\_surface
 |
| `targeting`target | SELF\_EXPLANATORY
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> |  |
| `excluded_countries`list<string> |  |
| `excluded_regions`list<int64> |  |
| `excluded_cities`list<int64> |  |
| `excluded_zipcodes`list<string> |  |
| `timezones`list<int64> |  |
| `age_min`enum {13, 15, 18, 21, 25} |  |
| `text_format_metadata`JSON-encoded string | text\_format\_metadata
 |
| `text_format_preset_id`numeric string or integer | text\_format\_preset\_id
 |
| `text_only_place`string | SELF\_EXPLANATORY
 |
| `throwback_camera_roll_media`JSON-encoded string | throwback\_camera\_roll\_media
 |
| `thumbnail`file | SELF\_EXPLANATORY
 |
| `time_since_original_post`int64 | SELF\_EXPLANATORY
 |
| `title`UTF-8 string | SELF\_EXPLANATORY
Supports Emoji |
| `tracking_info`JSON-encoded string | tracking\_info
 |
| `unpublished_content_type`enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | SELF\_EXPLANATORY
 |
| `user_selected_tags`boolean | Default value: `false`SELF\_EXPLANATORY
 |
| `video_start_time_ms`int64 | video\_start\_time\_ms
 |
| `viewer_coordinates`JSON-encoded coordinate list | SELF\_EXPLANATORY
 |
| `width`int64 | SELF\_EXPLANATORY
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: token with structure: Post ID, `post_supports_client_mutation_id`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 197 | The post is empty. Please enter a message to share. |
| 190 | Invalid OAuth 2.0 Access Token |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 1500 | The url you supplied is invalid |
| 105 | The number of parameters exceeded the maximum for this operation |
| 5101 | Uploaded file is too large. |
Updating
--------
You can update a Page by making a POST request to `/{page_id}`.### Parameters

| Parameter | Description |
| --- | --- |
| `about`UTF-8 string | Update the `about` field. Note that this value is mapped to the **Description** setting in the **Edit Page Info** user interface.
Supports Emoji |
| `accept_crossposting_handshake`array<JSON object> | Accepts a pending crossposting request initiated by another Page
 |
| `partner_page_id`page ID | partner\_page\_id
Required |
| `allow_live`boolean | allow\_live
Required |
| `allow_spherical_photo`boolean | Default value: `false`Indicates that we should allow this photo to be treated as a spherical photo. This param will only be used when uploading a new image file. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true.
 |
| `attire`enum{Unspecified, Casual, Dressy} | Update the `attire` field
 |
| `begin_crossposting_handshake`array<JSON object> | Begins the video crossposting handshake with another page
 |
| `partner_page_id`page ID | partner\_page\_id
Required |
| `allow_live`boolean | allow\_live
Required |
| `bio`string | Update the `bio` field
 |
| `category_list`list<numeric string> | Update the `category_list` field
 |
| `company_overview`string | Update the `company_overview` field
 |
| `contact_address`Object | Update the `contact_address` field
 |
| `city_id`city id |  |
| `street1`string |  |
| `street2`string |  |
| `zip`string |  |
| `cover`numeric string or integer | Update the `cover` field. This field can only be updated by the Page Admin or Page Editor with `EDIT_PROFILE` and `business_management` permissions.
 |
| `culinary_team`string | Update the `culinary_team` field
 |
| `delivery_and_pickup_option_info`array<string> | delivery\_and\_pickup\_option\_info. Each String represent the url link to a delivery and pick up option webpage. The API filters out duplicated urls as well as invalidated urls. If empty array is input, `delivery_and_pickup_option_info` field of the page will be cleared.
 |
| `description`string | Update the `description` field. Note that this value is mapped to the **Additional Information** setting in the **Edit Page Info** user interface.
 |
| `differently_open_offerings`JSON object {enum {ONLINE\_SERVICES, DELIVERY, PICKUP, OTHER} : boolean} | Indication of services currently offered by this business. Specify "true" for all that apply. Intended to be used when `temporary_status` = 'differently\_open'.
Note to restaurants: See `restaurant_services` for how to indicate longer term or permanent aspects of your business.
 |
| `directed_by`string | Update the `directed_by` field
 |
| `displayed_message_response_time`string | Page estimated message response time displayed to user
 |
| `emails`list<string> | Update the `emails` field
 |
| `focus_x`float | Cover photo focus x
 |
| `focus_y`float | Cover photo focus y
 |
| `food_styles`list<enum{Afghani, American (New), American (Traditional), Asian fusion, Barbeque, Brazilian, Breakfast, British, Brunch, Buffets, Burgers, Burmese, Cajun/Creole, Caribbean, Chinese, Creperies, Cuban, Delis, Diners, Ethiopian, Fast food, Filipino, Fondue, Food stands, French, German, Greek and Mediterranean, Hawaiian, Himalayan/Nepalese, Hot dogs, Indian/Pakistani, Irish, Italian, Japanese, Korean, Latin American, Mexican, Middle Eastern, Moroccan, Pizza, Russian, Sandwiches, Seafood, Singaporean, Soul food, Southern, Spanish/Basque, Steakhouses, Sushi bars, Taiwanese, Tapas bars, Tex-Mex, Thai, Turkish, Vegan, Vegetarian, Vietnamese}> | Update the `food_styles` field
 |
| `general_info`string | Update the `general_info` field
 |
| `general_manager`string | Update the `general_manager` field
 |
| `genre`string | Update the `genre` field
 |
| `hours`dictionary { string : <> } | Update the `hours` field
 |
| `ignore_coordinate_warnings`boolean | Ignore coordinate warnings when updating this Page's location
 |
| `impressum`string | Update the `impressum` field
 |
| `is_always_open`boolean | Is this location always open?
 |
| `is_permanently_closed`boolean | Update the `is_permanently_closed` field
 |
| `is_published`boolean | Update the `is_published` field
 |
| `is_webhooks_subscribed`boolean | Is the application subscribed for real time updates from this page?
 |
| `location`Object | Update the `location` field
 |
| `city`string |  |
| `city_id`city id |  |
| `state`string |  |
| `country`string |  |
| `street`string |  |
| `zip`string |  |
| `latitude`float |  |
| `longitude`float |  |
| `mission`string | Update the `mission` field
 |
| `no_feed_story`boolean | Default value: `false`Don't generate a feed story for the cover photo
 |
| `no_notification`boolean | Default value: `false`Don't generate a notification for the cover photo
 |
| `offset_x`integer | Default value: `50`Cover photo offset x
 |
| `offset_y`integer | Default value: `50`Cover photo offset y
 |
| `parking`dictionary { enum{street, lot, valet} : <boolean> } | Update the `parking` field
 |
| `payment_options`dictionary { enum{visa, amex, mastercard, discover, cash\_only} : <boolean> } | Update the `payment_options` field
 |
| `phone`string | Update the `phone` field
 |
| `pickup_options`array<enum {CURBSIDE, IN\_STORE, OTHER}> | List of pickup option types available at this Page's business location
 |
| `plot_outline`string | Update the `plot_outline` field
 |
| `price_range`string | Update the `price_range` field
 |
| `public_transit`string | Update the `public_transit` field
 |
| `restaurant_services`dictionary { enum{reserve, walkins, groups, kids, takeout, delivery, catering, waiter, outdoor} : <boolean> } | Update the `restaurant_services` field
 |
| `restaurant_specialties`dictionary { enum{breakfast, lunch, dinner, coffee, drinks} : <boolean> } | Update the `restaurant_specialties` field
 |
| `scrape`boolean | Re-scrape the website associated with this Page
 |
| `spherical_metadata`JSON object | A set of params describing an uploaded spherical photo. This param will only be used when uploading a new image file. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata
 |
| `ProjectionType`string | Accepted values include equirectangular (full spherical photo),
 cylindrical (panorama), and cubestrip (also known as cubemap, e.g.
 for synthetic or rendered content; stacked vertically with 6 faces).
Required |
| `CroppedAreaImageWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to equirectangular.
 This value should be equal to the actual width of the image, and
 together with FullPanoWidthPixels, it describes the horizontal FOV
 of content of the image: HorizontalFOV = 360 \*
 CroppedAreaImageWidthPixels / FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 horizontal FOV of the content of the image.
 HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `CroppedAreaImageHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value will NOT be equal to
 the actual height of the image. Instead, together with
 FullPanoHeightPixels, it describes the vertical FOV of the image:
 VerticalFOV = 180 \* CroppedAreaImageHeightPixels /
 FullPanoHeightPixels. In other words, this value is equal to the
 CroppedAreaImageHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 vertical FOV of the content of the image.
 VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `FullPanoWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to
 equirectangular. This value defines a ratio of horizontal pixels to
 degrees in the space of the image, and in general the pixel to degree
 ratio in the scope of the metadata object. Concretely, PixelsPerDegree =
 FullPanoWidthPixels / 360. This is also equivalent to the
 circumference of the cylinder used to model this projection.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It only defines
 the pixel to degree ratio in the scope of the metadata object. It
 represents the number of pixels in 360 degrees, so pixels per degree
 is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an
 example, if FullPanoWidthPixels were chosen to be 3600, we would have
 PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of
 view of 65 degrees would then have a CroppedAreaImageHeightPixels value
 of 65 \* 10 = 650.
Required |
| `FullPanoHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the FullPanoHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is always equal to
 FullPanoWidthPixels / 2.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is a second,
 redundant representation of PixelsPerDegree.
 FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent
 with FullPanoWidthPixels:
 FullPanoHeightPixels = FullPanoWidthPixels / 2.
Required |
| `CroppedAreaLeftPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaLeftPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `CroppedAreaTopPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaTopPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `PoseHeadingDegrees`float |  |
| `PosePitchDegrees`float |  |
| `PoseRollDegrees`float |  |
| `InitialViewHeadingDegrees`float |  |
| `InitialViewPitchDegrees`float |  |
| `InitialViewRollDegrees`float | This is not currently supported
 |
| `InitialViewVerticalFOVDegrees`float | This is deprecated. Please use InitialVerticalFOVDegrees.
 |
| `InitialVerticalFOVDegrees`float | You can set the intial vertical FOV of the image. You can set either
 this field or InitialHorizontalFOVDegrees.
 |
| `InitialHorizontalFOVDegrees`float | You can set the intial horizontal FOV of the image. You can set either
 this field or InitialVerticalFOVDegrees.
 |
| `PreProcessCropLeftPixels`int64 |  |
| `PreProcessCropRightPixels`int64 |  |
| `start_info`Object | Update the `start_info` field
 |
| `type`enum{Unspecified, Born, Founded, Started, Opened, Created, Launched} | Required |
| `date`Object |  |
| `year`integer |  |
| `month`integer |  |
| `day`integer |  |
| `store_location_descriptor`string | Update the `store_location_descriptor` field
 |
| `temporary_status`enum {DIFFERENTLY\_OPEN, TEMPORARILY\_CLOSED, OPERATING\_AS\_USUAL, NO\_DATA} | Update the `temporary_status` field
 |
| `website`URL | Update the `website` field
 |
| `zoom_scale_x`float | Cover photo zoom scale x
 |
| `zoom_scale_y`float | Cover photo zoom scale y
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 370 | Invalid call to update this page |
| 371 | Invalid Page location update |
| 210 | User not visible |
| 375 | This Page doesn't have a location descriptor. Add one to continue. |
| 320 | Photo edit failure |
| 374 | Invalid store location descriptor update since this Page is not a location Page. |
| 160 | Invalid geolocation type |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
You can update a Page by making a POST request to `/{page_id}/page_whatsapp_number_verification`.### Parameters

| Parameter | Description |
| --- | --- |
| `verification_code`string | The verification code which was sent to the WhatsApp number.
 |
| `whatsapp_number`string | The WhatsApp number to be verified.
Required |
### Return Type
 Struct {`error_message`: string, `verification_status`: enum, `whatsapp_number_type`: int32, `whatsapp_display_number`: string, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
You can update a Page by making a POST request to `/{page_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`array<enum {MANAGE, CREATE\_CONTENT, MODERATE, MESSAGING, ADVERTISE, ANALYZE, MODERATE\_COMMUNITY, MANAGE\_JOBS, PAGES\_MESSAGING, PAGES\_MESSAGING\_SUBSCRIPTIONS, READ\_PAGE\_MAILBOXES, VIEW\_MONETIZATION\_INSIGHTS, MANAGE\_LEADS, PROFILE\_PLUS\_FULL\_CONTROL, PROFILE\_PLUS\_MANAGE, PROFILE\_PLUS\_FACEBOOK\_ACCESS, PROFILE\_PLUS\_CREATE\_CONTENT, PROFILE\_PLUS\_MODERATE, PROFILE\_PLUS\_MODERATE\_DELEGATE\_COMMUNITY, PROFILE\_PLUS\_MESSAGING, PROFILE\_PLUS\_ADVERTISE, PROFILE\_PLUS\_ANALYZE, PROFILE\_PLUS\_REVENUE, PROFILE\_PLUS\_MANAGE\_LEADS, CASHIER\_ROLE}> | Page permission tasks to assign this user
 |
| `user`UID | Business user id or system user id
Required |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
Deleting
--------
This is only available to select developers. Please contact your Facebook Partner for more information.
You can dissociate a Page from a Page by making a DELETE request to `/{page_id}/locations`.### Parameters

| Parameter | Description |
| --- | --- |
| `location_page_ids`array<location\_page ID> | Array of Page IDs for the pages to delete
Required |
| `store_numbers`array<int64> | Array of Store numbers for the pages to delete
Required |
### Return Type
 Struct {`status`: bool, `data`: List [ Struct {`child_id`: string, `success`: bool, }], }### Error Codes

| Error | Description |
| --- | --- |
| 371 | Invalid Page location update |
| 200 | Permissions error |
| 100 | Invalid parameter |
You can dissociate a Page from a Page by making a DELETE request to `/{page_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `user`UID | Business scoped user id
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |