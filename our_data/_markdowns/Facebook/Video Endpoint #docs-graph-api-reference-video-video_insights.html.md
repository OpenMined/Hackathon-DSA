Total Video Insights Metrics /video-id/video\_insights - Documentation - Meta for Developers

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
Graph API Versionv19.0Video Insights
==============
Reading
-------
Get aggregated insight metrics for videos on a Page. You can get metrics for Videos, Reels, and Ad Breaks. For the full list of metrics, see Available Metrics.

### Requirements

* The pages\_manage\_engagement Permission.
* The read\_insights Permission.
* A Page access token requested by a person who is able to perform `ANALYZE` Tasks on a Page.
* Only Page admins can query earnings insights by using the API. Learn about setting up user roles for a Page.

### Limitations

* Insights for Videos on Users or Groups are not available.
* Data is only available for the past 2 years.
* A crossposted Video will have a unique video ID for each Page it was posted to.

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{video-id}/video_insights HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{video-id}/video_insights',
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
    "/{video-id}/video_insights",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{video-id}/video_insights",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{video-id}/video_insights"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `metric`list<A valid metric for an insights endpoint> | A list of available metrics that you want to receive.
 |
| `period`enum{day, week, days\_28, month, lifetime, total\_over\_range} | The aggregation period.
 |
| `since`datetime/timestamp | Lower bound of the time range to consider.
 |
| `until`datetime/timestamp | Upper bound of the time range to consider.
 |
### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {}
}

```
#### `data`
A list of InsightsResult nodes.#### `paging`
For more details about pagination, see the Graph API guide.### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.Available Metrics
-----------------

### Ad Breaks Metrics

The following metrics are available for the `metric` parameter when you read aggregated insights for ad breaks.

 Name
  | 
 Description
  | 
 Values for `period` || `total_video_ad_break_ad_cpm` | The average amount paid by advertisers for 1,000 impressions of their ads in your video, in U.S. cents. This number also includes the amount paid to Facebook. | day, lifetime |
| `total_video_ad_break_ad_impressions` | Number of times an ad was shown during your video's ad breaks. | day, lifetime |
| `total_video_ad_break_earnings` | An estimate of the amount you earned from ad breaks in your video, in U.S. cents, based on the number of impressions and CPM of ads shown. Actual payments may differ if there are content ownership claims or other adjustments. | day, lifetime |
### Reels Metrics

The following metrics are available for the `metric` parameter when you read aggregated insights for a reel. For more information about Reels, see Reels Developer Documentation.

 Name
  | 
 Description
  | 
 Values for `period` || `blue_reels_play_count` | The number of times your reel starts to play after an impression is already counted. This metric counts reels sessions with 1 millisecond or more of playback. This metric excludes replays. | lifetime |
| `fb_reels_replay_count` | The number of times your reel starts to play again after an initial play of your reel by the same account for at least 1ms in the same session. | lifetime |
| `fb_reels_total_plays` | The number of times your reel starts to play after an impression is already counted.This is defined as reel sessions with 1ms or more and includes replays. Replays are counted after the initial play of the reel in the same session. | lifetime |
| `post_impressions_unique` | The number of people who saw your reel at least once, whether or not the person played your reel. This metric is different from impressions, which includes multiple views of your reel by the same person. This metric is estimated. | lifetime |
| `post_video_avg_time_watched` | The average number of milliseconds your reel was played during a single instance of playing it, including time spent replaying your reel. Because this metric includes replays, the value can be greater than the total length of the reel. | lifetime |
| `post_video_followers` | The number of follows for your reel. | lifetime |
| `post_video_likes_by_reaction_type` | The number of likes on your reel. | lifetime |
| `post_video_retention_graph` | The percentage of times your reel was played at various timestamp segments out of the total number of plays. Most reels will start out at 100% retention and curve downward as plays begin to drop off. If someone skipped the beginning of the reel, your curve will start at the timestamp where the reel started playing. | lifetime |
| `post_video_social_actions` | The number of comments on your reel and the number of times your reel was shared. | lifetime |
| `post_video_view_time` | The total number of milliseconds your reel played, including time spent replaying your reel. | lifetime |
### Video Metrics

The following metrics are available for the `metric` parameter when you read aggregated insights for a video.

 Name
  | 
 Description
  | 
 Values for `period` || `total_video_views` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_autoplayed` | The number of times your videos automatically played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_clicked_to_play` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid` | The number of times your promoted videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid_unique` | The number of people who viewed your promoted videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_sound_on` | The number of times your videos played with sound on for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views` | The number of times your videos played for 97%, or more, or its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_unique` | The number of people who viewed your videos for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_auto_played` | The number of times your videos automatically played for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_clicked_to_play` | The number of times your videos played for 97%, or more, of its length, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic` | The number of times your videos played for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic_unique` | The number of people who viewed your videos for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid` | The number of times your promoted videos played for 97%, or more, of its length. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid_unique` | The number of people who viewed your promoted videos for 97%, or more, of its length. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views` | The number of times your videos played for 10 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_unique` | The number of people who viewed your videos for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_auto_played` | The number of times your videos automatically played for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_clicked_to_play` | The number of times your videos played for 10 seconds or more, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_organic` | The number of times your videos played for 10 seconds or more, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_paid` | The number of times your promoted videos played for 10 seconds or more. For each impression of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_sound_on` | The number of times your videos played with sound on for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_15s_views` | The number of times your videos played for 15 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_60s_excludes_shorter_views` | The number of times your videos played for 60 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_retention_graph` | The number of times your videos played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more impressions later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors | lifetime |
| `total_video_retention_graph_autoplayed` | The number of times your videos automatically played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more impressions later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_retention_graph_clicked_to_play` | The number of times your videos played at each interval as a percentage of all views, after people clicked play. Videos are divided into 40 equal intervals. Retention graphs may show more impressions later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_avg_time_watched` | The average time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time` | The total time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time_organic` | The total time, in milliseconds, people viewed your videos, by organic reach. | lifetime |
| `total_video_view_total_time_paid` | The total time, in milliseconds, people viewed your promoted videos. | lifetime |
| `total_video_impressions` | The total number of impressions of your videos. | lifetime |
| `total_video_impressions_unique` | The total number of unique impressions of your videos. | lifetime |
| `total_video_impressions_paid_unique` | The total number of unique impressions or your promoted videos. | lifetime |
| `total_video_impressions_paid` | The total number of impressions of your promoted videos. | lifetime |
| `total_video_impressions_organic_unique` | The total number of unique impressions of your videos, by organic reach. | lifetime |
| `total_video_impressions_organic` | The total number of impressions of your videos, by organic reach. | lifetime |
| `total_video_impressions_viral_unique` | The total number of unique impressions of your videos in a friend's story. | lifetime |
| `total_video_impressions_viral` | The total number of impressions of your videos in a story generated by a friend. | lifetime |
| `total_video_impressions_fan_unique` | The total number of unique impressions of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan` | The total number of impressions of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid_unique` | The total number of unique impressions of your promoted videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid` | The total number of impressions of your promoted video for people who liked your Page. | lifetime |
| `total_video_stories_by_action_type` | The total number of stories created about your Page's video, by action type; liking, commenting, sharing, etc. | lifetime |
| `total_video_reactions_by_type_total` | The total number of reactions to your Page's video, by type. | lifetime |
| `total_video_view_time_by_age_bucket_and_gender` | The total time, in milliseconds, your video has been viewed by Top Audiences; age and gender. | lifetime |
| `total_video_view_time_by_region_id` | The total time, in milliseconds, your Page's videos played for your Top 45 Locations; Region - Country. | lifetime |
| `total_video_views_by_distribution_type` | The number of times your videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_time_by_distribution_type` | The total time, in milliseconds, your Page's videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_total_time_live` | Total time (in ms) video has been viewed when it was broadcasted live. (Total Count). | lifetime |
| `total_video_views_by_country_id` | Lifetime video views by country. | lifetime |
| `total_video_views_live` | Number of people who viewed your video for 3 seconds or viewed to the end, when it was streamed live. | lifetime |
| `total_video_views_by_age_bucket_and_gender` | Lifetime video views by age bucket and gender. | lifetime |
| `total_video_views_gender_male` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by male viewers. | lifetime |
| `total_video_views_gender_female` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by female viewers. | lifetime |
| `total_video_views_live_clicked_to_play` | Lifetime total number of times people clicked to play your video and viewed it more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_male_live` | Lifetime total number of times males viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `total_video_views_live_autoplayed` | Lifetime total number of times your video started automatically playing and people viewed it for more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_female_live` | Lifetime total number of times females viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `has_total_video_views_by_publisher_platform_type` | Whether the video played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds broken down by publisher platform type. | lifetime |
| `total_video_30s_views` | Total number of times your video was viewed for 30 seconds or 97% of the video if video is less than 30 seconds. (Total Count) | lifetime |