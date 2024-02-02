<div>

<div>

Get [metrics](#availmetrics) for Pages or Page posts.

</div>

This endpoint is supported for [New Page
Experience](/docs/pages/new-pages-experience/) .

-   ::: fcb
    Page Insights data is only available on Pages with 100 or more
    likes.
    :::

-   ::: fcb
    Most metrics will update once every 24 hours.
    :::

-   ::: fcb
    Only the last two years of insights data is available.
    :::

-   ::: fcb
    The values for ` period ` are calculated from the initial collection
    of the data point.
    :::

-   ::: fcb
    \"Period\" in the tables below only refers to the time frame for
    which the metric can be accessed in an aggregated form.
    :::

-   ::: fcb
    The value \"lifetime\" means the time period for which the insights
    data is available. By default, this time period is 2 years or
    shorter.
    :::

-   ::: fcb
    Only 90 days of insights can be viewed at one time when using the
    ` since ` and ` until ` parameters.
    :::

-   ::: fcb
    When using ` since ` and ` until ` , the ` since ` date data will be
    included in the first ` value ` returned.
    :::

-   ::: fcb
    Unique impression insights values are calculated independently.
    -   ::: fcb
        Total page reach may not always be exactly equal to the sum of
        paid and non-paid unique values.
        :::

    -   ::: fcb
        Total page reach may not always be exactly equal to the sum of
        ` viral_unique ` and ` organic_unique ` .
        :::
    :::

-   ::: fcb
    When an organic post is boosted, metrics for paid post impressions
    will include both organic and paid reach.
    :::

-   ::: fcb
    Demographic metrics, such as age, gender, and location, are only
    returned if there is data for 100 or more people.
    :::

-   ::: fcb
    Breakdown metrics for Page post and Page view insights will only
    return non-zero values.
    :::

-   ::: fcb
    Several video related metrics only return accurate values if the
    person requesting the metric is the Page video post creator.
    :::

-   ::: fcb
    If you reshare a video post of another Page and retrieve its
    insights, the metrics return a value of 0. Metrics that return 0 for
    resharers are denoted with \"Returns 0 for reshared videos\" in
    their description.
    :::

-   ::: fcb
    If you neglect to indicate a specific metric or metrics for the
    endpoint, you will receive an error response with code ` 3001 ` ,
    with subcode ` 1504028 ` and an error message that states: \"No
    metric was specified to be fetched. Please specify one or more
    metrics to be fetched and try again.\"
    :::

-   ::: fcb
    Interactions on Reels are not included.
    :::

<div>

<div>

::: _5z09
::: {#u_0_6_2C ._51xa ._5gt2 ._51xb}
[Graph API Explorer
](/tools/explorer/?method=GET&path=%7Bobject-id%7D%2Finsights%2F%7Bmetric%7D&version=v19.0){._42ft
._51tl .selected}
:::

::: _xmu
``` {#u_0_c_dx ._5gt1 .prettyprint}
GET v19.0/{object-id}/insights/{metric} HTTP/1.1
Host: graph.facebook.com
```

``` {#u_0_d_+c ._5gt1 .prettyprint}
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '{object-id}/insights/{metric}',
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

``` {#u_0_e_28 ._5gt1 .prettyprint}
/* make the API call */
FB.api(
    "{object-id}/insights/{metric}",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

``` {#u_0_f_Ho ._5gt1 .prettyprint}
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "{object-id}/insights/{metric}",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

``` {#u_0_g_aD ._5gt1 .prettyprint}
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"{object-id}/insights/{metric}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
:::
:::

If you want to learn how to use the Graph API, read our [Using Graph API
guide](/docs/graph-api/using-graph-api/) .

</div>

<div>

::: _5z09
::: {#u_0_h_qA ._51xa ._5gt2 ._51xb}
[Graph API Explorer
](/tools/explorer/?method=GET&path=%7Bobject-id%7D%2Finsights%3Fmetric%3D%257Bmetric-1%257D%252C%257Bmetric-2%257D%252C%257Bmetric-3%257D%252C...&version=v19.0){._42ft
._51tl .selected}
:::

::: _xmu
``` {#u_0_n_7s ._5gt1 .prettyprint}
GET v19.0/{object-id}/insights?metric={metric-1},{metric-2},{metric-3},... HTTP/1.1
Host: graph.facebook.com
```

``` {#u_0_o_2T ._5gt1 .prettyprint}
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '{object-id}/insights?metric={metric-1},{metric-2},{metric-3},...',
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

``` {#u_0_p_gv ._5gt1 .prettyprint}
/* make the API call */
FB.api(
    "{object-id}/insights?metric={metric-1},{metric-2},{metric-3},...",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

``` {#u_0_q_0Z ._5gt1 .prettyprint}
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "{object-id}/insights?metric={metric-1},{metric-2},{metric-3},...",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

``` {#u_0_r_x5 ._5gt1 .prettyprint}
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"{object-id}/insights?metric={metric-1},{metric-2},{metric-3},..."
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
:::
:::

If you want to learn how to use the Graph API, read our [Using Graph API
guide](/docs/graph-api/using-graph-api/) .

</div>

Metric names indicate whether a metric is for a Page or a Page post.

::: _57-c
Suffix
:::

</div>

</div>

Description

` _unique `

Indicates that the metric shows the number of unique users who performed
a specific action, for example ` page_impressions_unique ` . **Metrics
generated with the ` _unique ` suffix are approximate and may not be
100% accurate.**

` _login `

Indicates whether a person was logged into Facebook, for example,
` page_tab_views_login_top ` .

` _logout `

Indicates whether a person is logged out of Facebook, for example
` page_views_logout ` .

` _source `

Indicates that the metric will be broken down into a list of referral
sources, for example ` page_fans_by_like_source ` . External referrals
are broken down by domain. Internal referrals are broken down by
Facebook-specific features such as **Profile** , **Search** ,
**Requests** , **Suggestions** , **Stream** , etc. In these cases the
` value ` returned will be an object containing a series of key-value
pairs where the key is the source name and the value is the metric for
that source.

` * `

Indicates that a metric is refreshed several times during the day, for
example ` page_impressions_unique* ` .

### Page Content

Most of the metrics below can be retrieved using
` post_activity_by_action_type ` , ` post_clicks_by_type ` , and
` page_consumptions_by_consumption_type ` .

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page_tab_vie        | <div>                 |                       |
| ws_login_top_unique ` |                       |                       |
|                       | The number of users   |                       |
|                       | logged in to Facebook |                       |
|                       | who saw tabs on your  |                       |
|                       | Page. (See [possible  |                       |
|                       | types](#tab-types) )  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| tab_views_login_top ` |                       |                       |
|                       | The number of times   |                       |
|                       | users logged into     |                       |
|                       | Facebook saw tabs on  |                       |
|                       | your Page. (See       |                       |
|                       | [possible             |                       |
|                       | types](#tab-types) )  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_t              | <div>                 |                       |
| ab_views_logout_top ` |                       |                       |
|                       | The number of times   |                       |
|                       | users not logged in   |                       |
|                       | to Facebook saw tabs  |                       |
|                       | on your Page. (See    |                       |
|                       | [possible             |                       |
|                       | types](#tab-types) )  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

#### Tab Types

Tab types for Page content metrics.

::: _57-c

  Name                 Description
  -------------------- -------------
  ` allactivity `      
  ` app `              
  ` info `             
  ` insights `         
  ` likes `            
  ` locations `        
  ` photos `           
  ` photos_albums `    
  ` photos_stream `    
  ` profile `          
  ` profile_info `     
  ` profile_likes `    
  ` profile_photos `   
  ` timeline `         
  ` events `           
  ` videos `           
  ` wall `             
:::

### Page CTA Clicks

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| `                     | <div>                 |                       |
|  page_total_actions ` |                       |                       |
|                       | The number of clicks  |                       |
|                       | on your Page\'s       |                       |
|                       | contact info and      |                       |
|                       | call-to-action        |                       |
|                       | button.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_cta_cli        | <div>                 |                       |
| cks_logged_in_total ` |                       |                       |
|                       | Total number of       |                       |
|                       | clicks on the Page    |                       |
|                       | CTA button by people  |                       |
|                       | who are logged in to  |                       |
|                       | Facebook.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_cta_clic       | <div>                 |                       |
| ks_logged_in_unique ` |                       |                       |
|                       | Unique number of      |                       |
|                       | clicks on the Page    |                       |
|                       | CTA button by people  |                       |
|                       | who are logged in to  |                       |
|                       | Facebook.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_cta_clicks_by_si |                       |                       |
| te_logged_in_unique ` | Number of people who  |                       |
|                       | are logged in to      |                       |
|                       | Facebook and clicked  |                       |
|                       | on the CTA button,    |                       |
|                       | broken down by www,   |                       |
|                       | mobile, api or other. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_c              | <div>                 |                       |
| ta_clicks_by_age_gend |                       |                       |
| er_logged_in_unique ` | Number of people who  |                       |
|                       | are logged in to      |                       |
|                       | Facebook and clicked  |                       |
|                       | the Page CTA button,  |                       |
|                       | broken down by age    |                       |
|                       | and gender group.     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_cta_clicks_logged_i |                       |                       |
| n_by_country_unique ` | Number of people who  |                       |
|                       | are logged in to      |                       |
|                       | Facebook and clicked  |                       |
|                       | the Page CTA button,  |                       |
|                       | broken down by        |                       |
|                       | country.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_cta_clicks_logge |                       |                       |
| d_in_by_city_unique ` | Number of people who  |                       |
|                       | are logged in to      |                       |
|                       | Facebook and clicked  |                       |
|                       | the Page CTA button,  |                       |
|                       | broken down by city.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_call_phone_clic |                       |                       |
| ks_logged_in_unique ` | Number of people who  |                       |
|                       | logged into Facebook  |                       |
|                       | and clicked the Call  |                       |
|                       | Now button.           |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_call_pho       | <div>                 |                       |
| ne_clicks_by_age_gend |                       |                       |
| er_logged_in_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Call  |                       |
|                       | Now button, broken    |                       |
|                       | down by age and       |                       |
|                       | gender group.         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_call_          | <div>                 |                       |
| phone_clicks_logged_i |                       |                       |
| n_by_country_unique ` | Number of people who  |                       |
|                       | logged into Facebook  |                       |
|                       | and clicked the Call  |                       |
|                       | Now button, broken    |                       |
|                       | down by countries.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_ca             | <div>                 |                       |
| ll_phone_clicks_logge |                       |                       |
| d_in_by_city_unique ` | Number of people who  |                       |
|                       | logged into Facebook  |                       |
|                       | and clicked the Call  |                       |
|                       | Now button, broken    |                       |
|                       | down by city.         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_ca             | <div>                 |                       |
| ll_phone_clicks_by_si |                       |                       |
| te_logged_in_unique ` | The number of people  |                       |
|                       | who clicked your      |                       |
|                       | Page\'s phone number  |                       |
|                       | or Call now button    |                       |
|                       | while they were       |                       |
|                       | logged into Facebook, |                       |
|                       | broken down by the    |                       |
|                       | type of device they   |                       |
|                       | used.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_get_directions_clic |                       |                       |
| ks_logged_in_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Get   |                       |
|                       | Directions button.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_get_directio   | <div>                 |                       |
| ns_clicks_by_age_gend |                       |                       |
| er_logged_in_unique ` | Number of people who  |                       |
|                       | logged into Facebook  |                       |
|                       | and clicked the Get   |                       |
|                       | Directions button,    |                       |
|                       | broken down by age    |                       |
|                       | and gender group.     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_get_direc      | <div>                 |                       |
| tions_clicks_logged_i |                       |                       |
| n_by_country_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Get   |                       |
|                       | Directions button,    |                       |
|                       | broken down by        |                       |
|                       | country.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_get_di         | <div>                 |                       |
| rections_clicks_logge |                       |                       |
| d_in_by_city_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Get   |                       |
|                       | Directions button,    |                       |
|                       | broken down by city.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_get_di         | <div>                 |                       |
| rections_clicks_by_si |                       |                       |
| te_logged_in_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Get   |                       |
|                       | Directions button,    |                       |
|                       | broken down by www,   |                       |
|                       | mobile, api or other. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_website_click  | <div>                 |                       |
| s_logged_in_unique* ` |                       |                       |
|                       | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the goto  |                       |
|                       | website CTA button.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_websi          | <div>                 |                       |
| te_clicks_by_age_gend |                       |                       |
| er_logged_in_unique ` | Number of people who  |                       |
|                       | logged into Facebook  |                       |
|                       | and clicked the goto  |                       |
|                       | website CTA button,   |                       |
|                       | broken down by age    |                       |
|                       | and gender group.     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_we             | <div>                 |                       |
| bsite_clicks_logged_i |                       |                       |
| n_by_country_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the goto  |                       |
|                       | website CTA button,   |                       |
|                       | broken down by        |                       |
|                       | country.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _website_clicks_logge |                       |                       |
| d_in_by_city_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the goto  |                       |
|                       | website CTA button,   |                       |
|                       | broken down by city.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _website_clicks_by_si |                       |                       |
| te_logged_in_unique ` | Number of people who  |                       |
|                       | logged in to Facebook |                       |
|                       | and clicked the Page  |                       |
|                       | CTA button, broken    |                       |
|                       | down by www, mobile,  |                       |
|                       | api and other.        |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Engagement

::: {._57yz ._57z1 ._3-8p}
::: _57y-
The \"like\" reaction counts include both \"like\" and \"care\"
reactions.
:::
:::

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| `                     | <div>                 |                       |
| page_engaged_users* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who engaged with your |                       |
|                       | Page. Engagement      |                       |
|                       | includes any click.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_post_engagements* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people have engaged   |                       |
|                       | with your posts       |                       |
|                       | through reactions,    |                       |
|                       | comments, shares and  |                       |
|                       | more.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_consumptions* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people clicked on any |                       |
|                       | of your content.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_c              | <div>                 |                       |
| onsumptions_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who clicked on any of |                       |
|                       | your content.         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_consumptions_  |                       |                       |
| by_consumption_type ` |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _consumptions_by_cons |                       |                       |
| umption_type_unique ` | The number of people  |                       |
|                       | who clicked on any of |                       |
|                       | your content, by      |                       |
|                       | type.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_pl             | <div>                 |                       |
| aces_checkin_total* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people checked into a |                       |
|                       | place.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_places_ch      | <div>                 |                       |
| eckin_total_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who checked into a    |                       |
|                       | place.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_pl             | <div>                 |                       |
| aces_checkin_mobile ` |                       |                       |
|                       | The number of times   |                       |
|                       | people checked into a |                       |
|                       | place using mobile    |                       |
|                       | phones.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_places_ch      | <div>                 |                       |
| eckin_mobile_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who checked into a    |                       |
|                       | place using mobile    |                       |
|                       | phones.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_places_che     | <div>                 |                       |
| ckins_by_age_gender ` |                       |                       |
|                       | gender and age of     |                       |
|                       | people who checked in |                       |
|                       | at your Place.        |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_places         | <div>                 |                       |
| _checkins_by_locale ` |                       |                       |
|                       | top locales of people |                       |
|                       | who checked into your |                       |
|                       | Place.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_places_        | <div>                 |                       |
| checkins_by_country ` |                       |                       |
|                       | top countries of      |                       |
|                       | people who checked    |                       |
|                       | into your Place.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_negative_feedback ` |                       |                       |
|                       | The number of times   |                       |
|                       | people took a         |                       |
|                       | negative action       |                       |
|                       | (e.g., un-liked or    |                       |
|                       | hid a post).          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_negat          | <div>                 |                       |
| ive_feedback_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who took a negative   |                       |
|                       | action (e.g.,         |                       |
|                       | un-liked or hid a     |                       |
|                       | post).                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_negati         | <div>                 |                       |
| ve_feedback_by_type ` |                       |                       |
|                       | The number of times   |                       |
|                       | people took a         |                       |
|                       | negative action       |                       |
|                       | broken down by type.  |                       |
|                       | (See [possible        |                       |
|                       | types](#ne            |                       |
|                       | gative-feedback-type) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_negative_feed  | <div>                 |                       |
| back_by_type_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who took a negative   |                       |
|                       | action broken down by |                       |
|                       | type. (See [possible  |                       |
|                       | types](#ne            |                       |
|                       | gative-feedback-type) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_positi         | <div>                 |                       |
| ve_feedback_by_type ` |                       |                       |
|                       | The number of times   |                       |
|                       | people took a         |                       |
|                       | positive action       |                       |
|                       | broken down by type.  |                       |
|                       | (See [possible        |                       |
|                       | types](#pos           |                       |
|                       | itive-feedback-types) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_positive_feed  | <div>                 |                       |
| back_by_type_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who took a positive   |                       |
|                       | action broken down by |                       |
|                       | type. (See [possible  |                       |
|                       | types](#pos           |                       |
|                       | itive-feedback-types) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_online `  | <div>                 |                       |
|                       |                       |                       |
|                       | The number of your    |                       |
|                       | fans who saw any      |                       |
|                       | posts on Facebook on  |                       |
|                       | a given day, broken   |                       |
|                       | down by hour of day   |                       |
|                       | in PST/PDT.           |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| fans_online_per_day ` |                       |                       |
|                       | The number of your    |                       |
|                       | fans who saw any      |                       |
|                       | posts on Facebook on  |                       |
|                       | a given day.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fan_adds_by_p  | <div>                 |                       |
| aid_non_paid_unique ` |                       |                       |
|                       | The number of new     |                       |
|                       | people who have liked |                       |
|                       | your Page broken down |                       |
|                       | by paid and non-paid. |                       |
|                       | This metric is        |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Impressions

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page_impressions* ` | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times   |                       |
|                       | any content from your |                       |
|                       | Page or about your    |                       |
|                       | Page entered a        |                       |
|                       | person\'s screen.     |                       |
|                       | This includes posts,  |                       |
|                       | stories, ads, as well |                       |
|                       | other content or      |                       |
|                       | information on your   |                       |
|                       | Page.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| impressions_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any content   |                       |
|                       | from your Page or     |                       |
|                       | about your Page enter |                       |
|                       | their screen. This    |                       |
|                       | includes posts,       |                       |
|                       | check-ins, ads,       |                       |
|                       | social information    |                       |
|                       | from people who       |                       |
|                       | interact with your    |                       |
|                       | Page and more. This   |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_impressions_paid* ` |                       |                       |
|                       | The number of times   |                       |
|                       | any post or story     |                       |
|                       | content from your     |                       |
|                       | Page or about your    |                       |
|                       | Page entered a        |                       |
|                       | person\'s screen      |                       |
|                       | through paid          |                       |
|                       | distribution such as  |                       |
|                       | an ad.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impre          | <div>                 |                       |
| ssions_paid_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any content   |                       |
|                       | from your Page or     |                       |
|                       | about your Page enter |                       |
|                       | their screen through  |                       |
|                       | paid distribution     |                       |
|                       | such as an ad. This   |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impr           | <div>                 |                       |
| essions_organic_v2* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Facebook Page    |                       |
|                       | and Page content was  |                       |
|                       | on screen through     |                       |
|                       | organic distribution. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impressions    | <div>                 |                       |
| _organic_unique_v2* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any content   |                       |
|                       | from your Page or     |                       |
|                       | about your Page enter |                       |
|                       | their screen through  |                       |
|                       | unpaid distribution.  |                       |
|                       | This includes posts,  |                       |
|                       | stories, check-ins,   |                       |
|                       | social information    |                       |
|                       | from people who       |                       |
|                       | interact with your    |                       |
|                       | Page and more. This   |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _impressions_viral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | any content from your |                       |
|                       | Page or about your    |                       |
|                       | Page entered a        |                       |
|                       | person\'s screen with |                       |
|                       | social information    |                       |
|                       | attached. Social      |                       |
|                       | information displays  |                       |
|                       | when a person\'s      |                       |
|                       | friend interacted     |                       |
|                       | with your Page, post  |                       |
|                       | or story. This        |                       |
|                       | includes when         |                       |
|                       | someone\'s friend     |                       |
|                       | likes or follows your |                       |
|                       | Page, engages with a  |                       |
|                       | post, shares a photo  |                       |
|                       | of your Page and      |                       |
|                       | checks into your      |                       |
|                       | Page. This metric is  |                       |
|                       | [in                   |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impres         | <div>                 |                       |
| sions_viral_unique* ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content when     |                       |
|                       | they were shown with  |                       |
|                       | social information    |                       |
|                       | attached. Social      |                       |
|                       | information is shown  |                       |
|                       | on Feed after someone |                       |
|                       | interacts with your   |                       |
|                       | Page, post or story.  |                       |
|                       | Reach is only counted |                       |
|                       | once if it occurs     |                       |
|                       | from both organic and |                       |
|                       | paid distribution.    |                       |
|                       | This metric is        |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | and [in               |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_im             | <div>                 |                       |
| pressions_nonviral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Facebook Page    |                       |
|                       | and Page content was  |                       |
|                       | on screen, excluding  |                       |
|                       | when they were shown  |                       |
|                       | with social           |                       |
|                       | information attached. |                       |
|                       | Social information is |                       |
|                       | shown on Feed after   |                       |
|                       | someone interacts     |                       |
|                       | with your Page, post  |                       |
|                       | or story. This metric |                       |
|                       | is [in                |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impressio      | <div>                 |                       |
| ns_nonviral_unique* ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content,         |                       |
|                       | excluding when they   |                       |
|                       | were shown with       |                       |
|                       | social information    |                       |
|                       | attached. Social      |                       |
|                       | information is shown  |                       |
|                       | on Feed after someone |                       |
|                       | interacts with your   |                       |
|                       | Page, post or story.  |                       |
|                       | Reach is only counted |                       |
|                       | once if it occurs     |                       |
|                       | from both organic and |                       |
|                       | paid distribution.    |                       |
|                       | This metric is        |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | and [in               |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impres         | <div>                 |                       |
| sions_by_story_type ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Facebook Page    |                       |
|                       | and Page content was  |                       |
|                       | on screen, grouped by |                       |
|                       | [Page Story           |                       |
|                       | type](https           |                       |
|                       | ://developers.faceboo |                       |
|                       | k.com/docs/graph-api/ |                       |
|                       | reference/v18.0/insig |                       |
|                       | hts#page-story-types) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impressions_b  | <div>                 |                       |
| y_story_type_unique ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by [Page Story        |                       |
|                       | type](https           |                       |
|                       | ://developers.faceboo |                       |
|                       | k.com/docs/graph-api/ |                       |
|                       | reference/v18.0/insig |                       |
|                       | hts#page-story-types) |                       |
|                       | . Reach is only       |                       |
|                       | counted once if it    |                       |
|                       | occurs from both      |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impress        | <div>                 |                       |
| ions_by_city_unique ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by city. Reach is     |                       |
|                       | only counted once if  |                       |
|                       | it occurs from both   |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impression     | <div>                 |                       |
| s_by_country_unique ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by country. Reach is  |                       |
|                       | only counted once if  |                       |
|                       | it occurs from both   |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impressio      | <div>                 |                       |
| ns_by_locale_unique ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by language. Reach is |                       |
|                       | only counted once if  |                       |
|                       | it occurs from both   |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_impressions_b  | <div>                 |                       |
| y_age_gender_unique ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by age and gender.    |                       |
|                       | Reach is only counted |                       |
|                       | once if it occurs     |                       |
|                       | from both organic and |                       |
|                       | paid distribution.    |                       |
|                       | This metric is        |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_impressions_fre |                       |                       |
| quency_distribution ` | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content, grouped |                       |
|                       | by the number of      |                       |
|                       | times your content    |                       |
|                       | was on screen. Reach  |                       |
|                       | is only counted once  |                       |
|                       | if it occurs from     |                       |
|                       | both organic and paid |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| impressions_viral_fre |                       |                       |
| quency_distribution ` | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Facebook Page and     |                       |
|                       | Page content when     |                       |
|                       | they were shown with  |                       |
|                       | social information    |                       |
|                       | attached. This metric |                       |
|                       | is also grouped by    |                       |
|                       | the number of times   |                       |
|                       | your content was on   |                       |
|                       | screen. Social        |                       |
|                       | information is shown  |                       |
|                       | on Feed after someone |                       |
|                       | interacts with your   |                       |
|                       | Page, post or story.  |                       |
|                       | Reach is only counted |                       |
|                       | once if it occurs     |                       |
|                       | from both organic and |                       |
|                       | paid distribution.    |                       |
|                       | This metric is        |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | and [in               |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Posts

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page                | <div>                 |                       |
| _posts_impressions* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s posts    |                       |
|                       | entered a person\'s   |                       |
|                       | screen. Posts include |                       |
|                       | statuses, photos,     |                       |
|                       | links, videos and     |                       |
|                       | more.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_         | <div>                 |                       |
| impressions_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any of your   |                       |
|                       | Page\'s posts enter   |                       |
|                       | their screen. Posts   |                       |
|                       | include statuses,     |                       |
|                       | photos, links, videos |                       |
|                       | and more.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_post           | <div>                 |                       |
| s_impressions_paid* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Facebook Page    |                       |
|                       | and Page content was  |                       |
|                       | on screen, attributed |                       |
|                       | to your ads.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_impre    | <div>                 |                       |
| ssions_paid_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any of your   |                       |
|                       | Page\'s posts enter   |                       |
|                       | their screen through  |                       |
|                       | paid distribution     |                       |
|                       | such as an ad. This   |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_i        | <div>                 |                       |
| mpressions_organic* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen through     |                       |
|                       | organic distribution. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_impressi | <div>                 |                       |
| ons_organic_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any of your   |                       |
|                       | Page\'s posts enter   |                       |
|                       | their screen through  |                       |
|                       | unpaid distribution.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _posts_served_impress |                       |                       |
| ions_organic_unique ` | The number of people  |                       |
|                       | who were served your  |                       |
|                       | Page\'s posts in      |                       |
|                       | their Feed whether it |                       |
|                       | entered their screen  |                       |
|                       | or not. Posts include |                       |
|                       | statuses, photos,     |                       |
|                       | links, videos and     |                       |
|                       | more.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts          | <div>                 |                       |
| _impressions_viral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s posts    |                       |
|                       | entered a person\'s   |                       |
|                       | screen with social    |                       |
|                       | information attached. |                       |
|                       | Social information    |                       |
|                       | displays when a       |                       |
|                       | person\'s friend      |                       |
|                       | interacted with you   |                       |
|                       | Page or post. This    |                       |
|                       | includes when         |                       |
|                       | someone\'s friend     |                       |
|                       | likes or follows your |                       |
|                       | Page, engages with a  |                       |
|                       | post, shares a photo  |                       |
|                       | of your Page and      |                       |
|                       | checks into your      |                       |
|                       | Page.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_impres   | <div>                 |                       |
| sions_viral_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had any of your   |                       |
|                       | Page\'s posts enter   |                       |
|                       | their screen with     |                       |
|                       | social information    |                       |
|                       | attached. As a form   |                       |
|                       | of organic            |                       |
|                       | distribution, social  |                       |
|                       | information displays  |                       |
|                       | when a person\'s      |                       |
|                       | friend interacted     |                       |
|                       | with you Page or      |                       |
|                       | post. This includes   |                       |
|                       | when someone\'s       |                       |
|                       | friend likes or       |                       |
|                       | follows your Page,    |                       |
|                       | engages with a post,  |                       |
|                       | shares a photo of     |                       |
|                       | your Page and checks  |                       |
|                       | into your Page.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_posts_im       | <div>                 |                       |
| pressions_nonviral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s posts    |                       |
|                       | entered a person\'s   |                       |
|                       | screen. This does not |                       |
|                       | include content       |                       |
|                       | created about your    |                       |
|                       | Page with social      |                       |
|                       | information attached. |                       |
|                       | Social information    |                       |
|                       | displays when a       |                       |
|                       | person\'s friend      |                       |
|                       | interacted with you   |                       |
|                       | Page or post. This    |                       |
|                       | includes when         |                       |
|                       | someone\'s friend     |                       |
|                       | likes or follows your |                       |
|                       | Page, engages with a  |                       |
|                       | post, shares a photo  |                       |
|                       | of your Page and      |                       |
|                       | checks into your      |                       |
|                       | Page.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_posts_impressio |                       |                       |
| ns_nonviral_unique* ` | The number of people  |                       |
|                       | who had any posts by  |                       |
|                       | your Page enter their |                       |
|                       | screen. This does not |                       |
|                       | include content       |                       |
|                       | created about your    |                       |
|                       | Page with social      |                       |
|                       | information attached. |                       |
|                       | As a form of organic  |                       |
|                       | distribution, social  |                       |
|                       | information displays  |                       |
|                       | when a person\'s      |                       |
|                       | friend interacted     |                       |
|                       | with you Page or      |                       |
|                       | post. This includes   |                       |
|                       | when someone\'s       |                       |
|                       | friend likes or       |                       |
|                       | follows your Page,    |                       |
|                       | engages with a post,  |                       |
|                       | shares a photo of     |                       |
|                       | your Page and checks  |                       |
|                       | into your Page.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| posts_impressions_fre |                       |                       |
| quency_distribution ` | The number of people  |                       |
|                       | who saw your Page     |                       |
|                       | posts, broken down by |                       |
|                       | how many times people |                       |
|                       | saw your posts.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Post Engagement

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| `                     | <div>                 |                       |
| post_engaged_users* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who clicked anywhere  |                       |
|                       | in your posts.        |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post                | <div>                 |                       |
| _negative_feedback* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people took a         |                       |
|                       | negative action in    |                       |
|                       | your post (e.g. hid   |                       |
|                       | it).                  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_negati         | <div>                 |                       |
| ve_feedback_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who took a negative   |                       |
|                       | action in your post   |                       |
|                       | (e.g., hid it).       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_negativ        | <div>                 |                       |
| e_feedback_by_type* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people took a         |                       |
|                       | negative action in    |                       |
|                       | your post broken down |                       |
|                       | by type.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_negative_feedb | <div>                 |                       |
| ack_by_type_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who took a negative   |                       |
|                       | action in your post   |                       |
|                       | broken down by type.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_engaged_fan `  | <div>                 |                       |
|                       |                       |                       |
|                       | People who have liked |                       |
|                       | your Page and engaged |                       |
|                       | with your post.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_clicks* `      | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times   |                       |
|                       | people clicked on     |                       |
|                       | anywhere in your      |                       |
|                       | posts without         |                       |
|                       | generating a story.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| post_clicks_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who clicked anywhere  |                       |
|                       | in your post without  |                       |
|                       | generating a story.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| ost_clicks_by_type* ` |                       |                       |
|                       | The number of times   |                       |
|                       | people clicked on     |                       |
|                       | anywhere in your      |                       |
|                       | posts without         |                       |
|                       | generating a story,   |                       |
|                       | by consumption type.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_cli            | <div>                 |                       |
| cks_by_type_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who clicked anywhere  |                       |
|                       | in your post without  |                       |
|                       | generating a story,   |                       |
|                       | by consumption type.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

#### Negative Feedback Types

Negative feedback types for ` page_negative_feedback_by_type ` metrics.

::: _57-c

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` hide_clicks `                   |                                   |
+-----------------------------------+-----------------------------------+
| ` hide_all_clicks `               | <div>                             |
|                                   |                                   |
|                                   | Hide all posts from this page     |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` report_spam_clicks `            | <div>                             |
|                                   |                                   |
|                                   | Report an object as a spam        |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` unlike_page_clicks `            |                                   |
+-----------------------------------+-----------------------------------+
:::

#### Positive Feedback Types

Positive feedback types for ` page_positive_feedback_by_type ` metrics.

::: _57-c

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` answer `                        |                                   |
+-----------------------------------+-----------------------------------+
| ` claim `                         |                                   |
+-----------------------------------+-----------------------------------+
| ` comment `                       |                                   |
+-----------------------------------+-----------------------------------+
| ` like `                          |                                   |
+-----------------------------------+-----------------------------------+
| ` link `                          |                                   |
+-----------------------------------+-----------------------------------+
| ` other `                         | <div>                             |
|                                   |                                   |
|                                   | Other types, such as checkins     |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` rsvp `                          |                                   |
+-----------------------------------+-----------------------------------+
:::

### Page Post Impressions

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` post_impressions* ` | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s post     |                       |
|                       | entered a person\'s   |                       |
|                       | screen. Posts include |                       |
|                       | statuses, photos,     |                       |
|                       | links, videos and     |                       |
|                       | more.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_               | <div>                 |                       |
| impressions_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had your Page\'s  |                       |
|                       | post enter their      |                       |
|                       | screen. Posts include |                       |
|                       | statuses, photos,     |                       |
|                       | links, videos and     |                       |
|                       | more. This metric is  |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pos                 | <div>                 |                       |
| t_impressions_paid* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen, attributed |                       |
|                       | to your ads.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impre          | <div>                 |                       |
| ssions_paid_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had your Page\'s  |                       |
|                       | post enter their      |                       |
|                       | screen through paid   |                       |
|                       | distribution such as  |                       |
|                       | an ad. This metric is |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` po                  | <div>                 |                       |
| st_impressions_fan* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen for         |                       |
|                       | accounts that         |                       |
|                       | followed or liked     |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impr           |                       |                       |
| essions_fan_unique* ` |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_im             | <div>                 |                       |
| pressions_fan_paid* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen, for        |                       |
|                       | accounts that         |                       |
|                       | followed or liked     |                       |
|                       | your Page through an  |                       |
|                       | ad.                   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impressio      |                       |                       |
| ns_fan_paid_unique* ` |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_i              | <div>                 |                       |
| mpressions_organic* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen through     |                       |
|                       | organic distribution. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impressi       | <div>                 |                       |
| ons_organic_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had your Page\'s  |                       |
|                       | post enter their      |                       |
|                       | screen through unpaid |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post                | <div>                 |                       |
| _impressions_viral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen with social |                       |
|                       | information attached. |                       |
|                       | Social information is |                       |
|                       | shown on Feed after   |                       |
|                       | someone interacts     |                       |
|                       | with your Page, post  |                       |
|                       | or story. This metric |                       |
|                       | is [in                |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impres         | <div>                 |                       |
| sions_viral_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who had your Page\'s  |                       |
|                       | post enter their      |                       |
|                       | screen with social    |                       |
|                       | information attached. |                       |
|                       | As a form of organic  |                       |
|                       | distribution, social  |                       |
|                       | information displays  |                       |
|                       | when a person\'s      |                       |
|                       | friend interacted     |                       |
|                       | with you Page or      |                       |
|                       | post. This includes   |                       |
|                       | when someone\'s       |                       |
|                       | friend likes or       |                       |
|                       | follows your Page,    |                       |
|                       | engages with a post,  |                       |
|                       | shares a photo of     |                       |
|                       | your Page and checks  |                       |
|                       | into your Page. This  |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | and [in               |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_im             | <div>                 |                       |
| pressions_nonviral* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen, excluding  |                       |
|                       | when your content was |                       |
|                       | shown with social     |                       |
|                       | information attached. |                       |
|                       | Social information is |                       |
|                       | shown on Feed after   |                       |
|                       | someone interacts     |                       |
|                       | with your Page, post  |                       |
|                       | or story. This metric |                       |
|                       | is [in                |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impressio      | <div>                 |                       |
| ns_nonviral_unique* ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Page content,         |                       |
|                       | excluding when your   |                       |
|                       | content was shown     |                       |
|                       | with social           |                       |
|                       | information attached. |                       |
|                       | Social information is |                       |
|                       | shown on Feed after   |                       |
|                       | someone interacts     |                       |
|                       | with your Page, post  |                       |
|                       | or story. Reach is    |                       |
|                       | only counted once if  |                       |
|                       | it occurs from both   |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | and [in               |                       |
|                       | develo                |                       |
|                       | pment](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impress        | <div>                 |                       |
| ions_by_story_type* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page content was |                       |
|                       | on screen, grouped by |                       |
|                       | [Page Story           |                       |
|                       | type](https           |                       |
|                       | ://developers.faceboo |                       |
|                       | k.com/docs/graph-api/ |                       |
|                       | reference/v18.0/insig |                       |
|                       | hts#page-story-types) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_impressions_by | <div>                 |                       |
| _story_type_unique* ` |                       |                       |
|                       | This metric counts    |                       |
|                       | reach from the        |                       |
|                       | organic or paid       |                       |
|                       | distribution of your  |                       |
|                       | Page content, grouped |                       |
|                       | by [Page Story        |                       |
|                       | type](https           |                       |
|                       | ://developers.faceboo |                       |
|                       | k.com/docs/graph-api/ |                       |
|                       | reference/v18.0/insig |                       |
|                       | hts#page-story-types) |                       |
|                       | . Reach is only       |                       |
|                       | counted once if it    |                       |
|                       | occurs from both      |                       |
|                       | organic and paid      |                       |
|                       | distribution. This    |                       |
|                       | metric is             |                       |
|                       | [esti                 |                       |
|                       | mated](https://www.fa |                       |
|                       | cebook.com/business/h |                       |
|                       | elp/metrics-labeling) |                       |
|                       | .                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Post Reactions

::: {._57yz ._57z1 ._3-8p}
::: _57y-
The \"like\" reaction counts include both \"like\" and \"care\"
reactions.
:::
:::

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` post_r              | <div>                 |                       |
| eactions_like_total ` |                       |                       |
|                       | Total \"like\"        |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_r              | <div>                 |                       |
| eactions_love_total ` |                       |                       |
|                       | Total \"love\"        |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_               | <div>                 |                       |
| reactions_wow_total ` |                       |                       |
|                       | Total \"wow\"         |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_r              | <div>                 |                       |
| eactions_haha_total ` |                       |                       |
|                       | Total \"haha\"        |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_re             | <div>                 |                       |
| actions_sorry_total ` |                       |                       |
|                       | Total \"sad\"         |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_re             | <div>                 |                       |
| actions_anger_total ` |                       |                       |
|                       | Total \"anger\"       |                       |
|                       | reactions of a post.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_reac           | <div>                 |                       |
| tions_by_type_total ` |                       |                       |
|                       | Total post reactions  |                       |
|                       | by type.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Reactions

::: {._57yz ._57z1 ._3-8p}
::: _57y-
The \"like\" reaction counts include both \"like\" and \"care\"
reactions.
:::
:::

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| `                     | <div>                 |                       |
|  page_actions_post_re |                       |                       |
| actions_like_total* ` | Daily total post      |                       |
|                       | \"like\" reactions of |                       |
|                       | a page.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_actions_post_re |                       |                       |
| actions_love_total* ` | Daily total post      |                       |
|                       | \"love\" reactions of |                       |
|                       | a page.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_actions_post_r | <div>                 |                       |
| eactions_wow_total* ` |                       |                       |
|                       | Daily total post      |                       |
|                       | \"wow\" reactions of  |                       |
|                       | a page.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_actions_post_re |                       |                       |
| actions_haha_total* ` | Daily total post      |                       |
|                       | \"haha\" reactions of |                       |
|                       | a page.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_actions_post_rea |                       |                       |
| ctions_sorry_total* ` | Daily total post      |                       |
|                       | \"sorry\" reactions   |                       |
|                       | of a page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_actions_post_rea |                       |                       |
| ctions_anger_total* ` | Daily total post      |                       |
|                       | \"anger\" reactions   |                       |
|                       | of a page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_actions_p      | <div>                 |                       |
| ost_reactions_total ` |                       |                       |
|                       | Daily total post      |                       |
|                       | reactions of a page   |                       |
|                       | by type.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page User Demographics {#page-fans}

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page_fans `         | <div>                 |                       |
|                       |                       |                       |
|                       | The total number of   |                       |
|                       | people who have liked |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_locale `  | <div>                 |                       |
|                       |                       |                       |
|                       | Aggregated language   |                       |
|                       | data about the people |                       |
|                       | who like your Page    |                       |
|                       | based on the default  |                       |
|                       | language setting      |                       |
|                       | selected when         |                       |
|                       | accessing Facebook.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_city `    | <div>                 |                       |
|                       |                       |                       |
|                       | Aggregated Facebook   |                       |
|                       | location data, sorted |                       |
|                       | by city, about the    |                       |
|                       | people who like your  |                       |
|                       | Page.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_country ` | <div>                 |                       |
|                       |                       |                       |
|                       | The number of people, |                       |
|                       | aggregated per        |                       |
|                       | country, that like    |                       |
|                       | your Page. Only the   |                       |
|                       | 45 countries with the |                       |
|                       | most people that like |                       |
|                       | your Page are         |                       |
|                       | included.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| age_fans_gender_age ` |                       |                       |
|                       | The number of likes   |                       |
|                       | of your Facebook      |                       |
|                       | Page.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fan_adds `     | <div>                 |                       |
|                       |                       |                       |
|                       | The number of new     |                       |
|                       | people who have liked |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| age_fan_adds_unique ` |                       |                       |
|                       | The number of new     |                       |
|                       | people who have liked |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| fans_by_like_source ` |                       |                       |
|                       | This is a breakdown   |                       |
|                       | of the number of Page |                       |
|                       | likes from the most   |                       |
|                       | common places where   |                       |
|                       | people can like your  |                       |
|                       | Page. (See [possible  |                       |
|                       | types                 |                       |
|                       | ](#page-like-sources) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_by        | <div>                 |                       |
| _like_source_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who liked your Page,  |                       |
|                       | broken down by the    |                       |
|                       | most common places    |                       |
|                       | where people can like |                       |
|                       | your Page. (See       |                       |
|                       | [possible             |                       |
|                       | types                 |                       |
|                       | ](#page-like-sources) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fan_removes `  |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               |                       |                       |
| fan_removes_unique* ` |                       |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_fans_by_u      | <div>                 |                       |
| nlike_source_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who unliked your      |                       |
|                       | Page, broken down by  |                       |
|                       | the most common ways  |                       |
|                       | people can unlike     |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

#### Page Like Sources

Source types for ` page_fans_by_like_source ` and
` page_fans_by_like_source_unique ` metrics.

::: _57-c

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` Ads `                           | <div>                             |
|                                   |                                   |
|                                   | Page likes that came from people  |
|                                   | who saw your Page or post in an   |
|                                   | ad.                               |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` News Feed `                     | <div>                             |
|                                   |                                   |
|                                   | Page likes that came from people  |
|                                   | who saw content posted by your    |
|                                   | Page or about your Page in News   |
|                                   | Feed.                             |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` Page Suggestions `              | <div>                             |
|                                   |                                   |
|                                   | Page likes that came from people  |
|                                   | saw your Page in a list of        |
|                                   | suggested Pages.                  |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` Restored                        | <div>                             |
| Likes from Reactivated Accounts ` |                                   |
|                                   | Page likes that came from people  |
|                                   | who reactivated their Facebook    |
|                                   | profile.                          |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` Search `                        | <div>                             |
|                                   |                                   |
|                                   | Page likes that came from people  |
|                                   | who saw you Page or post in       |
|                                   | search.                           |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` Your Page `                     | <div>                             |
|                                   |                                   |
|                                   | Page likes that came from people  |
|                                   | who visited your Page.            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

#### Page Unlike Sources

Source types for ` page_fans_by_unlike_source_unique ` and
` page_fans_by_unlike_source ` metrics.

::: _57-c
Source Type Name
:::

Description

` Deactivated or Memorialized Account Removals `

The Page likes that were removed due to deactivated or memorialized
accounts.

` Other `

The Page likes that were removed due to reasons other than deactivated
or memorialized accounts, suspicious accounts, unlikes from Page, Posts,
or NewsFeed, or unlikes from search.

` Suspicious Account Removals `

The Page likes that were removed due to suspicious account activity.

` Unlikes from Page, Posts, or News Feed `

The Page likes that were removed from people who saw content posted by
your Page or about your Page in News Feed.

` Unlikes from Search `

The Page likes that were removed from people who saw your Page or post
in search.

### Page Video Views {#videoviews}

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page_video_views `  | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_views_   | <div>                 |                       |
| by_uploaded_hosted* ` |                       |                       |
|                       | Daily video views on  |                       |
|                       | a page-level broken   |                       |
|                       | down by all variants  |                       |
|                       | of page-uploaded and  |                       |
|                       | page-hosted variants. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pa                  | <div>                 |                       |
| ge_video_views_paid ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s promoted |                       |
|                       | videos played for at  |                       |
|                       | least 3 seconds, or   |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 3 seconds. For each   |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| video_views_organic ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_view     | <div>                 |                       |
| s_by_paid_non_paid* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, broken down  |                       |
|                       | by total, paid, and   |                       |
|                       | non-paid. During a    |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vid            | <div>                 |                       |
| eo_views_autoplayed ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | automatically played  |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_         | <div>                 |                       |
| views_click_to_play ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, after people |                       |
|                       | clicked play. During  |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _video_views_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | Page\'s videos for at |                       |
|                       | least 3 seconds, or   |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 3 seconds. During a   |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _video_repeat_views ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | were replayed for at  |                       |
|                       | least 3 seconds, or   |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 3 seconds.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video          | <div>                 |                       |
| _complete_views_30s ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least   |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_comp     | <div>                 |                       |
| lete_views_30s_paid ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s promoted |                       |
|                       | videos played for at  |                       |
|                       | least 30 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 30 seconds. For each  |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_complet  | <div>                 |                       |
| e_views_30s_organic ` |                       |                       |
|                       | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least   |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_video_complete_v |                       |                       |
| iews_30s_autoplayed ` | The number of times   |                       |
|                       | your Page\'s          |                       |
|                       | automatically played  |                       |
|                       | videos played for at  |                       |
|                       | least 30 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 30 seconds. During a  |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pag                 | <div>                 |                       |
| e_video_complete_view |                       |                       |
| s_30s_click_to_play ` | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | played for at least   |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds, after people |                       |
|                       | clicked play. During  |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_comple   | <div>                 |                       |
| te_views_30s_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | Page\'s videos for at |                       |
|                       | least 30 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 30 seconds. During a  |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pa                  | <div>                 |                       |
| ge_video_complete_vie |                       |                       |
| ws_30s_repeat_views ` | The number of times   |                       |
|                       | your Page\'s videos   |                       |
|                       | replayed for at least |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| post_video_complete_v |                       |                       |
| iews_30s_autoplayed ` | The number of times   |                       |
|                       | your videos           |                       |
|                       | automatically played  |                       |
|                       | for at least 30       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_               | <div>                 |                       |
| video_complete_views_ |                       |                       |
| 30s_clicked_to_play ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 30       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds, after people |                       |
|                       | clicked play. During  |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video. Returns 0  |                       |
|                       | for reshared videos.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_complet  | <div>                 |                       |
| e_views_30s_organic ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 30       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_comp     | <div>                 |                       |
| lete_views_30s_paid ` |                       |                       |
|                       | The number of times   |                       |
|                       | your promoted videos  |                       |
|                       | played for at least   |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds. For each     |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_comple   | <div>                 |                       |
| te_views_30s_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | videos for at least   |                       |
|                       | 30 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 30       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| age_video_views_10s ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s videos played |                       |
|                       | for at least 10       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_v              | <div>                 |                       |
| ideo_views_10s_paid ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s promoted      |                       |
|                       | videos played for at  |                       |
|                       | least 10 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 10 seconds. For each  |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vide           | <div>                 |                       |
| o_views_10s_organic ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s videos played |                       |
|                       | for at least 10       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_v        | <div>                 |                       |
| iews_10s_autoplayed ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s videos        |                       |
|                       | automatically played  |                       |
|                       | for at least 10       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_video_view     | <div>                 |                       |
| s_10s_click_to_play ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s videos played |                       |
|                       | for at least 10       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds, after people |                       |
|                       | clicked play. During  |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vid            | <div>                 |                       |
| eo_views_10s_unique ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of people who  |                       |
|                       | viewed your Page\'s   |                       |
|                       | videos for at least   |                       |
|                       | 10 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vid            | <div>                 |                       |
| eo_views_10s_repeat ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | Page\'s videos        |                       |
|                       | replayed for at least |                       |
|                       | 10 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| age_video_view_time ` |                       |                       |
|                       | The total time, in    |                       |
|                       | milliseconds, people  |                       |
|                       | viewed your Page\'s   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_upl            | <div>                 |                       |
| oaded_video_play_coun |                       |                       |
| t_by_paid_non_paid* ` | The total number of   |                       |
|                       | times any of the      |                       |
|                       | videos on the page    |                       |
|                       | started playing,      |                       |
|                       | broken down by paid   |                       |
|                       | or non paid.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_uplo           | <div>                 |                       |
| aded_social_actions_c |                       |                       |
| ount_by_video_type* ` | Total amount of       |                       |
|                       | reactions, comments   |                       |
|                       | and shares on Page    |                       |
|                       | Uploaded Videos.      |                       |
|                       | Measured across all   |                       |
|                       | uploaded video        |                       |
|                       | assets, broken down   |                       |
|                       | by video type         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page                | <div>                 |                       |
| _top_hosted_crosspost |                       |                       |
| ed_by_views_60s_es* ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 1        |                       |
|                       | minute. Time spent    |                       |
|                       | replaying a video     |                       |
|                       | during a single       |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Crossposted Videos    |                       |
|                       | contains only the     |                       |
|                       | Videos from other     |                       |
|                       | Pages that you        |                       |
|                       | crossposted.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_hosted_cr  | <div>                 |                       |
| ossposted_by_views* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for 97%   |                       |
|                       | of their total length |                       |
|                       | if they\'re shorter   |                       |
|                       | than 3 seconds. Time  |                       |
|                       | spent replaying a     |                       |
|                       | video during a single |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | seconds a video was   |                       |
|                       | played, instead of    |                       |
|                       | the amount of time    |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Crossposted Videos    |                       |
|                       | contains only the     |                       |
|                       | Videos from other     |                       |
|                       | Pages that you        |                       |
|                       | crossposted.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| top_hosted_crossposte |                       |                       |
| d_by_time_spent_ms* ` | The total number of   |                       |
|                       | minutes your video    |                       |
|                       | was played or         |                       |
|                       | replayed within this  |                       |
|                       | post. This metric     |                       |
|                       | counts how many       |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Crossposted Videos    |                       |
|                       | contains only the     |                       |
|                       | Videos from other     |                       |
|                       | Pages that you        |                       |
|                       | crossposted.          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_host       | <div>                 |                       |
| ed_non_uploaded_share |                       |                       |
| d_by_time_spent_ms* ` | The total number of   |                       |
|                       | minutes your video    |                       |
|                       | was played or         |                       |
|                       | replayed within this  |                       |
|                       | post. This metric     |                       |
|                       | counts how many       |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Shared Videos are     |                       |
|                       | videos from other     |                       |
|                       | pages that you        |                       |
|                       | shared.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_to             | <div>                 |                       |
| p_uploaded_video_asse |                       |                       |
| ts_by_views_60s_es* ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 1        |                       |
|                       | minute, or for nearly |                       |
|                       | their total length if |                       |
|                       | they\'re shorter than |                       |
|                       | 1 minute. During a    |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Uploaded video |                       |
|                       | assets only include   |                       |
|                       | the Videos which are  |                       |
|                       | uploaded by the Page. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_hos        | <div>                 |                       |
| ted_non_uploaded_shar |                       |                       |
| ed_by_views_60s_es* ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 1        |                       |
|                       | minute. Time spent    |                       |
|                       | replaying a video     |                       |
|                       | during a single       |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Shared Videos are     |                       |
|                       | videos from other     |                       |
|                       | pages that you        |                       |
|                       | shared.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_videos     | <div>                 |                       |
| _by_minutes_viewed* ` |                       |                       |
|                       | The total number of   |                       |
|                       | minutes your video    |                       |
|                       | was played or         |                       |
|                       | replayed within this  |                       |
|                       | post. This metric     |                       |
|                       | counts how many       |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Top Videos represent  |                       |
|                       | all the Videos posted |                       |
|                       | on the Page           |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_video      | <div>                 |                       |
| _assets_by_revenue* ` |                       |                       |
|                       | The amount of money   |                       |
|                       | you earned from ads   |                       |
|                       | in your videos. Your  |                       |
|                       | actual earnings may   |                       |
|                       | be higher or lower    |                       |
|                       | due to pending        |                       |
|                       | reviews, content      |                       |
|                       | ownership claims or   |                       |
|                       | other adjustments.    |                       |
|                       | Top Videos represent  |                       |
|                       | all the Videos posted |                       |
|                       | on the Page           |                       |
|                       | (including Shared /   |                       |
|                       | Crossposted /         |                       |
|                       | Uploaded)             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_               | <div>                 |                       |
| top_hosted_non_upload |                       |                       |
| ed_shared_by_views* ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for 97%   |                       |
|                       | of their total length |                       |
|                       | if they\'re shorter   |                       |
|                       | than 3 seconds. Time  |                       |
|                       | spent replaying a     |                       |
|                       | video during a single |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | seconds a video was   |                       |
|                       | played, instead of    |                       |
|                       | the amount of time    |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Shared Videos are     |                       |
|                       | videos from other     |                       |
|                       | pages that you        |                       |
|                       | shared.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top_           | <div>                 |                       |
| uploaded_video_assets |                       |                       |
| _by_social_actions* ` | The number of         |                       |
|                       | reactions, comments   |                       |
|                       | and shares on your    |                       |
|                       | posts. This metric    |                       |
|                       | counts all reactions  |                       |
|                       | and comments,         |                       |
|                       | including ones that   |                       |
|                       | were removed or       |                       |
|                       | deleted.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_t              | <div>                 |                       |
| op_videos_by_views* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for 97%   |                       |
|                       | of their total length |                       |
|                       | if they\'re shorter   |                       |
|                       | than 3 seconds. Time  |                       |
|                       | spent replaying a     |                       |
|                       | video during a single |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | seconds a video was   |                       |
|                       | played, instead of    |                       |
|                       | the amount of time    |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Top Videos represent  |                       |
|                       | all the Videos posted |                       |
|                       | on the Page           |                       |
|                       | (including Shared /   |                       |
|                       | Crossposted /         |                       |
|                       | Uploaded).            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_top            | <div>                 |                       |
| _uploaded_video_asset |                       |                       |
| s_by_time_spent_ms* ` | The total number of   |                       |
|                       | minutes your video    |                       |
|                       | was played or         |                       |
|                       | replayed within this  |                       |
|                       | post. This metric     |                       |
|                       | counts how many       |                       |
|                       | minutes of a video    |                       |
|                       | were played, instead  |                       |
|                       | of the amount of time |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Uploaded video assets |                       |
|                       | only include the      |                       |
|                       | Videos which are      |                       |
|                       | uploaded by the Page. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_top_uploaded_vid |                       |                       |
| eo_assets_by_views* ` | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for 97%   |                       |
|                       | of their total length |                       |
|                       | if they\'re shorter   |                       |
|                       | than 3 seconds. Time  |                       |
|                       | spent replaying a     |                       |
|                       | video during a single |                       |
|                       | instance of the video |                       |
|                       | playing won\'t be     |                       |
|                       | included. This metric |                       |
|                       | is based on how many  |                       |
|                       | seconds a video was   |                       |
|                       | played, instead of    |                       |
|                       | the amount of time    |                       |
|                       | that passed while the |                       |
|                       | video was playing.    |                       |
|                       | Uploaded video assets |                       |
|                       | only include the      |                       |
|                       | Videos which are      |                       |
|                       | uploaded by the Page. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| page_top_video_assets |                       |                       |
| _by_ad_impressions* ` | The number of times   |                       |
|                       | an ad was shown       |                       |
|                       | during your video\'s  |                       |
|                       | in-stream ads. Top    |                       |
|                       | Videos represent all  |                       |
|                       | the Videos posted on  |                       |
|                       | the Page (including   |                       |
|                       | Shared / Crossposted  |                       |
|                       | / Uploaded).          |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Views

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` page_views_total* ` | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times a |                       |
|                       | Page\'s profile has   |                       |
|                       | been viewed by logged |                       |
|                       | in and logged out     |                       |
|                       | people.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_views_logout ` | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times a |                       |
|                       | Page has been viewed  |                       |
|                       | by people not logged  |                       |
|                       | into Facebook.        |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vie            | <div>                 |                       |
| ws_logged_in_total* ` |                       |                       |
|                       | The number of times a |                       |
|                       | Page\'s profile has   |                       |
|                       | been viewed by people |                       |
|                       | logged in to          |                       |
|                       | Facebook.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_view           | <div>                 |                       |
| s_logged_in_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | logged in to Facebook |                       |
|                       | who have viewed the   |                       |
|                       | Page profile.         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_views          | <div>                 |                       |
| _external_referrals ` |                       |                       |
|                       | Top referrering       |                       |
|                       | external domains      |                       |
|                       | sending traffic to    |                       |
|                       | your Page.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_views_b        | <div>                 |                       |
| y_profile_tab_total ` |                       |                       |
|                       | The number of people  |                       |
|                       | who have viewed each  |                       |
|                       | Page profile tab.     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pa                  | <div>                 |                       |
| ge_views_by_profile_t |                       |                       |
| ab_logged_in_unique ` | The number of people  |                       |
|                       | logged into Facebook  |                       |
|                       | who have viewed your  |                       |
|                       | Page, broken down by  |                       |
|                       | each tab.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_vi             | <div>                 |                       |
| ews_by_internal_refer |                       |                       |
| er_logged_in_unique ` | The number of people  |                       |
|                       | logged into Facebook  |                       |
|                       | who have viewed your  |                       |
|                       | Page, broken down by  |                       |
|                       | the internal referer  |                       |
|                       | within Facebook.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_views_by_si    | <div>                 |                       |
| te_logged_in_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | logged into Facebook  |                       |
|                       | who have viewed your  |                       |
|                       | Page, broken down by  |                       |
|                       | the type of device.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| age_views_by_age_gend |                       |                       |
| er_logged_in_unique ` | The number of people  |                       |
|                       | logged into Facebook  |                       |
|                       | who have viewed your  |                       |
|                       | Page, broken down by  |                       |
|                       | gender group.         |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_views_by_refere |                       |                       |
| rs_logged_in_unique ` | Logged-in Page visit  |                       |
|                       | counts (unique users) |                       |
|                       | by referral source.   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Page Video Posts

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` post_vid            | <div>                 |                       |
| eo_avg_time_watched ` |                       |                       |
|                       | The average time, in  |                       |
|                       | milliseconds, people  |                       |
|                       | viewed your videos.   |                       |
|                       | Only available for    |                       |
|                       | videos created after  |                       |
|                       | August 25th 2016.     |                       |
|                       | Returns 0 for         |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_com      | <div>                 |                       |
| plete_views_organic ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | from the beginning to |                       |
|                       | 97%, or more, of its  |                       |
|                       | length, by organic    |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
| post_video_complete_v |                       |                       |
| iews_organic_unique ` | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | videos from the       |                       |
|                       | beginning to 97%, or  |                       |
|                       | more, of its length,  |                       |
|                       | by organic reach.     |                       |
|                       | During a single       |                       |
|                       | instance of a video   |                       |
|                       | playing, we\'ll       |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_         | <div>                 |                       |
| complete_views_paid ` |                       |                       |
|                       | The number of times   |                       |
|                       | your promoted videos  |                       |
|                       | played from the       |                       |
|                       | beginning to 97%, or  |                       |
|                       | more, of its length.  |                       |
|                       | For each impression   |                       |
|                       | of a video, we\'ll    |                       |
|                       | count video views     |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. Returns 0 for  |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_complet  | <div>                 |                       |
| e_views_paid_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | promoted videos from  |                       |
|                       | the beginning to 97%, |                       |
|                       | or more, of its       |                       |
|                       | length. For each      |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vid            | <div>                 |                       |
| eo_retention_graph* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played at |                       |
|                       | each interval as a    |                       |
|                       | percentage of all     |                       |
|                       | views. Videos are     |                       |
|                       | divided into 40 equal |                       |
|                       | intervals. This       |                       |
|                       | metric does not count |                       |
|                       | impressions while the |                       |
|                       | video was live.       |                       |
|                       | Retention graphs may  |                       |
|                       | show more impressions |                       |
|                       | later in the video    |                       |
|                       | than at the           |                       |
|                       | beginning. People     |                       |
|                       | might start the video |                       |
|                       | in the middle, skip   |                       |
|                       | ahead, save, and      |                       |
|                       | rewatch it from that  |                       |
|                       | point, or other       |                       |
|                       | similar behaviors.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` po                  | <div>                 |                       |
| st_video_retention_gr |                       |                       |
| aph_clicked_to_play ` | The number of times   |                       |
|                       | your videos played at |                       |
|                       | each interval as a    |                       |
|                       | percentage of all     |                       |
|                       | views, after people   |                       |
|                       | clicked play. Videos  |                       |
|                       | are divided into 40   |                       |
|                       | equal intervals. This |                       |
|                       | metric does not count |                       |
|                       | impressions while the |                       |
|                       | video was live.       |                       |
|                       | Retention graphs may  |                       |
|                       | show more impressions |                       |
|                       | later in the video    |                       |
|                       | than at the           |                       |
|                       | beginning. People     |                       |
|                       | might start the video |                       |
|                       | in the middle, skip   |                       |
|                       | ahead, save, and      |                       |
|                       | rewatch it from that  |                       |
|                       | point, or other       |                       |
|                       | similar behaviors.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_retenti  | <div>                 |                       |
| on_graph_autoplayed ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos           |                       |
|                       | automatically played  |                       |
|                       | at each interval as a |                       |
|                       | percentage of all     |                       |
|                       | automatic views.      |                       |
|                       | Videos are divided    |                       |
|                       | into 40 equal         |                       |
|                       | intervals.This metric |                       |
|                       | does not count        |                       |
|                       | impressions while the |                       |
|                       | video was live.       |                       |
|                       | Retention graphs may  |                       |
|                       | show more impressions |                       |
|                       | later in the video    |                       |
|                       | than at the           |                       |
|                       | beginning. People     |                       |
|                       | might start the video |                       |
|                       | in the middle, skip   |                       |
|                       | ahead, save, and      |                       |
|                       | rewatch it from that  |                       |
|                       | point, or other       |                       |
|                       | similar behaviors.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_               | <div>                 |                       |
| video_views_organic ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_v        | <div>                 |                       |
| iews_organic_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | videos for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, by organic   |                       |
|                       | reach. During a       |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` po                  | <div>                 |                       |
| st_video_views_paid ` |                       |                       |
|                       | The number of times   |                       |
|                       | your promoted videos  |                       |
|                       | played for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. For each     |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vide           | <div>                 |                       |
| o_views_paid_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | promoted videos for   |                       |
|                       | at least 3 seconds,   |                       |
|                       | or for nearly their   |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 3 seconds. For each   |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_length ` | <div>                 |                       |
|                       |                       |                       |
|                       | The length, in        |                       |
|                       | milliseconds, of a    |                       |
|                       | video post.           |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_views `  | <div>                 |                       |
|                       |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video. This includes  |                       |
|                       | live views.           |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post                | <div>                 |                       |
| _video_views_unique ` |                       |                       |
|                       | The number of people  |                       |
|                       | who viewed your       |                       |
|                       | videos for at least 3 |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vid            | <div>                 |                       |
| eo_views_autoplayed ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos           |                       |
|                       | automatically played  |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_vi       | <div>                 |                       |
| ews_clicked_to_play ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 3        |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 3        |                       |
|                       | seconds, after people |                       |
|                       | clicked play. During  |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` po                  | <div>                 |                       |
| st_video_views_15s* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 15       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 15       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_views_60 | <div>                 |                       |
| s_excludes_shorter* ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | for at least 60       |                       |
|                       | seconds. This metric  |                       |
|                       | is counted only for   |                       |
|                       | videos that are 60    |                       |
|                       | seconds or longer.    |                       |
|                       | During a single       |                       |
|                       | instance of a video   |                       |
|                       | playing, we\'ll       |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| ost_video_views_10s ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | videos played for at  |                       |
|                       | least 10 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 10 seconds. During a  |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vid            | <div>                 |                       |
| eo_views_10s_unique ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of people who  |                       |
|                       | viewed your videos    |                       |
|                       | for at least 10       |                       |
|                       | seconds, or for       |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. For each     |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_v        | <div>                 |                       |
| iews_10s_autoplayed ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | videos played         |                       |
|                       | automatically for at  |                       |
|                       | least 10 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 10 seconds. During a  |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_views_   | <div>                 |                       |
| 10s_clicked_to_play ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | videos played for at  |                       |
|                       | least 10 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 10 seconds, after     |                       |
|                       | people clicked play.  |                       |
|                       | During a single       |                       |
|                       | instance of a video   |                       |
|                       | playing, we\'ll       |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vide           | <div>                 |                       |
| o_views_10s_organic ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | videos played for at  |                       |
|                       | least 10 seconds, or  |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 10 seconds, by        |                       |
|                       | organic reach. During |                       |
|                       | a single instance of  |                       |
|                       | a video playing,      |                       |
|                       | we\'ll exclude any    |                       |
|                       | time spent replaying  |                       |
|                       | the video.            |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_v              | <div>                 |                       |
| ideo_views_10s_paid ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | promoted videos       |                       |
|                       | played for at least   |                       |
|                       | 10 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. For each     |                       |
|                       | impression of a       |                       |
|                       | video, we\'ll count   |                       |
|                       | video views           |                       |
|                       | separately and        |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video          | <div>                 |                       |
| _views_10s_sound_on ` |                       |                       |
|                       | Deprecated above      |                       |
|                       | Graph API v18: The    |                       |
|                       | number of times your  |                       |
|                       | videos played with    |                       |
|                       | sound on for at least |                       |
|                       | 10 seconds, or for    |                       |
|                       | nearly their total    |                       |
|                       | length if they\'re    |                       |
|                       | shorter than 10       |                       |
|                       | seconds. During a     |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_v              | <div>                 |                       |
| ideo_views_sound_on ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played    |                       |
|                       | with sound on for at  |                       |
|                       | least 3 seconds, or   |                       |
|                       | for nearly their      |                       |
|                       | total length if       |                       |
|                       | they\'re shorter than |                       |
|                       | 3 seconds. During a   |                       |
|                       | single instance of a  |                       |
|                       | video playing, we\'ll |                       |
|                       | exclude any time      |                       |
|                       | spent replaying the   |                       |
|                       | video.                |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| ost_video_view_time ` |                       |                       |
|                       | The total time, in    |                       |
|                       | milliseconds, your    |                       |
|                       | videos played,        |                       |
|                       | including videos      |                       |
|                       | played for less than  |                       |
|                       | 3 seconds and         |                       |
|                       | replays. Returns 0    |                       |
|                       | for reshared videos.  |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_vide           | <div>                 |                       |
| o_view_time_organic ` |                       |                       |
|                       | The total time, in    |                       |
|                       | milliseconds, your    |                       |
|                       | videos played by      |                       |
|                       | organic reach.        |                       |
|                       | Returns 0 for         |                       |
|                       | reshared videos.      |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_               | <div>                 |                       |
| video_view_time_by_ag |                       |                       |
| e_bucket_and_gender ` | The total time, in    |                       |
|                       | milliseconds, your    |                       |
|                       | videos played for     |                       |
|                       | your Top Audiences,   |                       |
|                       | age and gender.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_vie      | <div>                 |                       |
| w_time_by_region_id ` |                       |                       |
|                       | The total time, in    |                       |
|                       | milliseconds, your    |                       |
|                       | videos played for     |                       |
|                       | your Top 45           |                       |
|                       | Locations, Region -   |                       |
|                       | Country.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_views_b  | <div>                 |                       |
| y_distribution_type ` |                       |                       |
|                       | The number of times   |                       |
|                       | your videos played by |                       |
|                       | distribution type;    |                       |
|                       | page_owned and        |                       |
|                       | shared.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` p                   | <div>                 |                       |
| ost_video_view_time_b |                       |                       |
| y_distribution_type ` | The total time, in    |                       |
|                       | milliseconds, your    |                       |
|                       | videos played by      |                       |
|                       | distribution type;    |                       |
|                       | page_owned and        |                       |
|                       | shared.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_view     | <div>                 |                       |
| _time_by_country_id ` |                       |                       |
|                       | The total number of   |                       |
|                       | minutes your videos   |                       |
|                       | played for your Top   |                       |
|                       | 45 Locations;         |                       |
|                       | Country.              |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pos                 | <div>                 |                       |
| t_video_views_live* ` |                       |                       |
|                       | Lifetime number of    |                       |
|                       | people who viewed     |                       |
|                       | your video for more   |                       |
|                       | than 3 seconds when   |                       |
|                       | it was streamed live. |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  post_video_social_ac |                       |                       |
| tions_count_unique* ` | The unique count of   |                       |
|                       | the social actions    |                       |
|                       | (reactions, comments, |                       |
|                       | shares) on a video    |                       |
|                       | post.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pos                 | <div>                 |                       |
| t_video_play_count* ` |                       |                       |
|                       | The number of times   |                       |
|                       | the video has been    |                       |
|                       | played.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_li       | <div>                 |                       |
| ve_current_viewers* ` |                       |                       |
|                       | The number of viewers |                       |
|                       | currently watching a  |                       |
|                       | live video. This      |                       |
|                       | metric is only        |                       |
|                       | returned for live     |                       |
|                       | posts. Returns 0 for  |                       |
|                       | was live posts.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video          | <div>                 |                       |
| _15s_to_60s_excludes_ |                       |                       |
| shorter_views_rate* ` | 15s to 60s Views Rate |                       |
|                       | for a video. This 60s |                       |
|                       | metric is counted     |                       |
|                       | only for videos that  |                       |
|                       | are 60 seconds or     |                       |
|                       | longer.               |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_video_vi       | <div>                 |                       |
| ews_by_live_status* ` |                       |                       |
|                       | Lifetime 3S Video     |                       |
|                       | Views broken down by  |                       |
|                       | live status: live or  |                       |
|                       | VOD                   |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

### Stories

Page and Post Stories and \"People talking about this\".

::: _57-c
+-----------------------+-----------------------+-----------------------+
| Metric Name           | Description           | Values for \`period\` |
+=======================+=======================+=======================+
| ` pag                 | <div>                 |                       |
| e_content_activity_by |                       |                       |
| _action_type_unique ` | The number of people  |                       |
|                       | talking about your    |                       |
|                       | Page\'s stories, by   |                       |
|                       | Page story type. (See |                       |
|                       | [possible             |                       |
|                       | type                  |                       |
|                       | s](#page-story-types) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pa                  | <div>                 |                       |
| ge_content_activity_b |                       |                       |
| y_age_gender_unique ` | The number of People  |                       |
|                       | Talking About the     |                       |
|                       | Page by user age and  |                       |
|                       | gender. This number   |                       |
|                       | is an estimate.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_content_acti   | <div>                 |                       |
| vity_by_city_unique ` |                       |                       |
|                       | The number of People  |                       |
|                       | Talking About the     |                       |
|                       | Page by user city.    |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| `                     | <div>                 |                       |
|  page_content_activit |                       |                       |
| y_by_country_unique ` | The number of people, |                       |
|                       | aggregated per        |                       |
|                       | country, that are     |                       |
|                       | talking about your    |                       |
|                       | Page. Only the 45     |                       |
|                       | countries with the    |                       |
|                       | most people talking   |                       |
|                       | about your page are   |                       |
|                       | included.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_content_activi | <div>                 |                       |
| ty_by_locale_unique ` |                       |                       |
|                       | The number of People  |                       |
|                       | Talking About the     |                       |
|                       | Page by user          |                       |
|                       | language.             |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` pa                  | <div>                 |                       |
| ge_content_activity ` |                       |                       |
|                       | The number of stories |                       |
|                       | created about your    |                       |
|                       | Page (Stories).       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` page_content_acti   | <div>                 |                       |
| vity_by_action_type ` |                       |                       |
|                       | The number of stories |                       |
|                       | about your Page\'s    |                       |
|                       | stories, by Page      |                       |
|                       | story type. (See      |                       |
|                       | [possible             |                       |
|                       | type                  |                       |
|                       | s](#page-story-types) |                       |
|                       | )                     |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_activity* `    | <div>                 |                       |
|                       |                       |                       |
|                       | The number of stories |                       |
|                       | generated about your  |                       |
|                       | Page post             |                       |
|                       | (\'Stories\').        |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` po                  | <div>                 |                       |
| st_activity_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who created a story   |                       |
|                       | about your Page post  |                       |
|                       | (\'People Talking     |                       |
|                       | About This\' / PTAT). |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_activ          | <div>                 |                       |
| ity_by_action_type* ` |                       |                       |
|                       | The number of stories |                       |
|                       | created about your    |                       |
|                       | Page post, by action  |                       |
|                       | type.                 |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
| ` post_activity_by_   | <div>                 |                       |
| action_type_unique* ` |                       |                       |
|                       | The number of people  |                       |
|                       | who created a story   |                       |
|                       | about your Page post, |                       |
|                       | by action type.       |                       |
|                       |                       |                       |
|                       | </div>                |                       |
+-----------------------+-----------------------+-----------------------+
:::

#### Page Story Types

Page story types for ` page_content_activity_by_action_type_unique ` and
` page_content_activity_by_action_type ` .

::: _57-c

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` checkin `                       |                                   |
+-----------------------------------+-----------------------------------+
| ` coupon `                        |                                   |
+-----------------------------------+-----------------------------------+
| ` event `                         |                                   |
+-----------------------------------+-----------------------------------+
| ` fan `                           |                                   |
+-----------------------------------+-----------------------------------+
| ` mention `                       |                                   |
+-----------------------------------+-----------------------------------+
| ` page post `                     |                                   |
+-----------------------------------+-----------------------------------+
| ` question `                      |                                   |
+-----------------------------------+-----------------------------------+
| ` user post `                     | <div>                             |
|                                   |                                   |
|                                   | Posts by people on a Page         |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` other `                         |                                   |
+-----------------------------------+-----------------------------------+
:::

### Video Ad Breaks

::: _57-c
Metric Name
:::

Description

Values for period

` page_daily_video_ad_break_ad_impressions_by_crosspost_status `

The total number of times an ad was shown during ad breaks in
crossposted videos.

day

` page_daily_video_ad_break_cpm_by_crosspost_status `

The average amount paid by advertisers for 1,000 of impressions of their
ads in a crossposted videos. This is a gross number and includes the
amount paid to Facebook.

day

` page_daily_video_ad_break_earnings_by_crosspost_status `

An estimate of the amount you earned from ad breaks in a crossposted
videos, based on the number of impressions and CPM of ads shown. Actual
payments may differ if there are content ownership claims or other
adjustments.

day

` post_video_ad_break_ad_impressions `

The total number of times an ad was shown during ad breaks in your
videos.

day, lifetime

` post_video_ad_break_earnings `

An estimate of the amount you earned from ad breaks in your videos,
based on the number of impressions and CPM of ads shown. Actual payments
may differ if there are content ownership claims or other adjustments.

day, lifetime

` post_video_ad_break_ad_cpm `

The average amount paid by advertisers for 1,000 impressions of their
ads in your videos. This number also includes the amount paid to
Facebook.

day, lifetime

<div>

::: _57-c
Parameter
:::

</div>

Description

` breakdown `

list\<A valid breakdown for an insights endpoint\>

<div>

<div>

breakdown for marketing messages metrics. This is currently in
development.

</div>

</div>

` date_preset `

enum{today, yesterday, this_month, last_month, this_quarter, maximum,
data_maximum, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d,
last_week_mon_sun, last_week_sun_sat, last_quarter, last_year,
this_week_mon_today, this_week_sun_today, this_year}

<div>

<div>

Preset a date range, like lastweek, yesterday. If since or until
presents, it does not work.

</div>

</div>

` metric `

list\<A valid metric for an insights endpoint\>

<div>

<div>

The list of metrics that needs to be fetched

</div>

</div>

` period `

enum {day, week, days_28, month, lifetime, total_over_range}

` show_description_from_api_doc `

boolean

Default value: ` false `

<div>

<div>

If set to true, then an additional description of the metric, retrieved
from the API
doc(https://developers.facebook.com/docs/graph-api/reference/insights)
will be included in the returned data

</div>

</div>

` since `

datetime

<div>

<div>

Lower bound of the time range to consider

</div>

</div>

` until `

datetime

<div>

<div>

Upper bound of the time range to consider

</div>

</div>

<div>

Reading from this edge will return a JSON formatted result:

``` _3hux
{ "data": [], "paging": {}
}
```

::: _3-8o
A list of [InsightsResult](/docs/graph-api/reference/insights-result/)
nodes.
:::

::: _3-8o
For more details about pagination, see the [Graph API
guide](/docs/graph-api/using-graph-api/#paging) .
:::

</div>

::: _57-c
  Error   Description
  ------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  80001   There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.
  200     Permissions error
  100     Invalid parameter
  190     Invalid OAuth 2.0 Access Token
  3001    Invalid query
:::
