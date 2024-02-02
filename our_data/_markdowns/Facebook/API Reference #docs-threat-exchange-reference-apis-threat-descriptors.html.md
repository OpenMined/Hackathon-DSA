/threat\_descriptors - ThreatExchange - Documentation - Meta for Developers

ThreatExchange* Get Started
* Get Access
* Best Practices
* UI Overview
* UI Reference
* API Overview
* API Examples
* API Structure
* API Reference
* Privacy Controls
* Submitting Data
* Editing Existing Data
* Delete Data
* Re-sharing
* React to Data
* Submit Connections
* Integrations
* Webhooks
* FAQ
* Webinar
* Changelog
/threat\_descriptors
====================
NOTE: Queries using this call are not guaranteed to be comprehensive and may only return partial results. See how to do bulk download in Best Practices.The API call enables searching for subjective opinions on indicators stored in ThreatExchange. With this call you can search by free text, type, submitter, or all in a specific time window. Combinations of these query types are also allowed. This call is only permitted on Platform versions 2.4 and later.  
This query may only return partial results and should only be used to find examples of ThreatDescriptors matching the query parameters. To get a comprehensive list of ThreatDescriptors you should use the `\threat_tags` endpoint and do any necessary post-process filtering 
Parameters
----------
The following query parameters are available (bold params are required):
* **`access_token`** - The key for authenticating to the API, in the format <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
* `include_expired` - When set to true, the API can return data which has expired. Expired data is denoted by having the expire\_time field as non-zero and less than the current time.
* `limit` - Defines the maximum size of a page of results. The maximum is 1,000.
* `max_confidence` - Define the maximum allowed confidence value for the data returned.
* `min_confidence` - Define the minimum allowed confidence value for the data returned.
* `owner` - Comma-separated list of AppIDs of the person who submitted the data.
* `text` - Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects.
* `review_status` - A given ReviewStatusType
* `share_level` - A given ShareLevelType
* `sort_by` - Sort search results by RELEVANCE or by CREATE\_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query.
* `status` - A given StatusType
* `strict_text` - When set to 'true', the API will not do approximate matching on the value in text
* `tags` - Comma-separated list of tags to filter results
* `tags_are_anded` - If omitted or set to `false`, with `tags=a,b` shows descriptors having tags `a` or `b`. If set to `true`, shows descriptors having tags `a` and `b`.
* `type` - The type of descriptor to search for (see IndicatorTypes)
* `since` - Returns descriptors collected after a timestamp
* `until` - Returns descriptors collected before a timestamp
* `fields` - A list of fields to return in the response
Optional parameters for POST -- documented with examples here:
* `related_ids_for_upload`
* `related_triples_for_upload`
Example query for all IP addresses submitted by Facebook Administrator which contain the word "proxy":

```
https://graph.facebook.com/v2.8/threat_descriptors?access_token=555|asDF&amp;type=IP_ADDRESS&amp;owner=820763734618599&amp;text=proxy
```
Data returned:

```
{
  "data": [
    {
      "id": "600399050063019",
      "indicator": {
        "indicator": "52.68.54.232",
        "type": "IP_ADDRESS",
        "id": "1117440484937537"
      },
      "owner": {
        "id": "820763734618599",
        "email": "threatexchange@support.facebook.com",
        "name": "Facebook Administrator"
      },
      "type": "IP_ADDRESS",
      "raw_indicator": "52.68.54.232",
      "description": "TOR Proxy IP Address",
      "status": "UNKNOWN"
    },
    ...
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.8/threat_descriptors?access_token=555|1234&amp;pretty=0&amp;owner=820763734618599&amp;text=proxy&amp;type=IP_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}
```
The same query using a cURL:

```
curl -i -X GET \
 "https://graph.facebook.com/v2.8/threat_descriptors?type=IP_ADDRESS&amp;owner=820763734618599&amp;text=proxy&amp;access_token=555%7C1234"
```
The same query in Python:

```
import requests
import json
import ast
import urllib
app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
type_ = 'IP_ADDRESS'
owner_app_id = 820763734618599
text = 'proxy'
query_params = urllib.urlencode({
    'access_token' : app_id + '|' + app_secret,
    'type' : type_,
    'owner' : owner_app_id,
    'text' : text
    })
r = requests.get('https://graph.facebook.com/v2.8/threat_descriptors?' + query_params)
print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```
The same query in Java:

```
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;
public class ThreatDescriptors {
    public final static void main(String[] args) throws Exception {
        String url = "https://graph.facebook.com/v2.8/threat_descriptors?";
        String appID = "555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP_ADDRESS";
        String ownerAppID = "820763734618599";
        String text = "proxy";
        String query = String.format("access_token=%s&amp;type=%s&amp;owner=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
                ownerAppID,
                text
                );
        URLConnection connection = new URL(url + query).openConnection();
        InputStream response = connection.getInputStream();
        System.out.print(convertStreamToString(response));
        response.close();
    }
    static String convertStreamToString(InputStream inputStream){
        Scanner scanner = new Scanner(inputStream).useDelimiter("\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }
}
```
The same query in PHP:

```
<?php
  $appID = "555"; // Replace this with your AppID
  $appSecret = "1234"; // Replace this with your App Secret
  $type = 'IP_ADDRESS';
  $text = 'proxy';
  $ownerAppID = "820763734618599";
  $access_token = $appID . "|" . $appSecret;
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,
    "https://graph.facebook.com/v2.8/threat_descriptors?" .
    "access_token=" . $access_token .
    "&amp;type=" . $type .
    "&amp;owner=" . $ownerAppID .
    "&amp;text=" . $text);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $response = curl_exec($ch);
  $json = json_encode(json_decode($response), JSON_PRETTY_PRINT);
  print($json . PHP_EOL);
  curl_close($ch);
?>
```