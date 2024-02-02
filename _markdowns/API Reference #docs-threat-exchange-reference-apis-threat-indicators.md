::: {._4-u3 ._588p}
The following query parameters are available (bold parameters are
required):

-   **` access_token `** - The key for authenticating to the API. It is
    a concatenation of &lt;your-app-id&gt;\|&lt;your-app-secret&gt;. For
    example, if our app ID was 555 and our app secret aSdF123GhK, our
    access_token would be \"555\|aSdF123GhK\".

-   ` limit ` - Defines the maximum size of a page of results. The
    maximum is 1,000.

-   ` text ` - Freeform text field with a value to search for. This can
    be a file hash or a string found in other fields of the objects.

-   ::: fcb
    ` sort_order ` - A given
    [SortOrderType](/docs/threat-exchange/reference/apis/sort-order-type)
    :::

-   ` sort_by ` - Sort results by RELEVANCE or by CREATE_TIME. When
    sorting by RELEVANCE, your query will return results sorted by
    similarity against your text query.

-   ` strict_text ` - When set to \'true\', the API will not do
    approximate matching on the value in text

-   ::: fcb
    ` threat_type ` - The broad threat type the indicator is associated
    with (see
    [ThreatTypes](/docs/threat-exchange/reference/apis/threat-type/) )
    :::

-   ::: fcb
    ` type ` - The type of indicators to search for (see
    [IndicatorTypes](/docs/threat-exchange/reference/apis/indicator-type/)
    )
    :::

-   ` since ` - Returns indicators collected after a timestamp

-   ` until ` - Returns indicators collected before a timestamp

-   ` fields ` - A list of fields to return in the response

Example query for all malicious IP addresses that are proxies:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.7/threat_indicators?access_token=555|aSdF123GhK&amp;type=IP_ADDRESS&amp;text=proxy
```

The data returned by this API call changed in Platform version 2.4. Data
returned in Platform v2.3:

``` {._5s-8 .prettyprint .lang-code}
{
  "data": [
    {
      "added_on": "2015-02-25T14:46:37+0000", 
      "confidence": 50, 
      "description": "Localhost IP", 
      "indicator": "127.0.0.1", 
      "severity": "INFO", 
      "share_level": "GREEN", 
      "status": "NON_MALICIOUS", 
      "type": "IP_ADDRESS", 
      "threat_types": [
        "MALICIOUS_IP"
      ], 
      "id": "804745332940593"
    }
  ], 
  "paging": {
    "cursors": {
      "before": "MA==", 
      "after": "MA=="
    }
  }
}
```

Data returned in Platforms v2.4 and above:

``` {._5s-8 .prettyprint .lang-code}
{
  "data": [
    {
      "indicator": "77.2.132.202",
      "type": "IP_ADDRESS",
      "id": "675010235935327"
    },
    ...
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.7/threat_indicators?access_token=555|1234&amp;pretty=0&amp;text=proxy&amp;type=IP_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}
```

The same query using a cURL:

``` {._5s-8 .prettyprint .lang-code}
curl -i -X GET \
 "https://graph.facebook.com/v2.7/threat_indicators?type=IP_ADDRESS&amp;text=proxy&amp;access_token=555%7C1234"
```

The same query in Python:

``` {._5s-8 .prettyprint .lang-code}
import requests
import json
import ast
import urllib

app_id = '555' # Replace this with your app ID
app_secret = '1234' # Replace this with your app secret
type_ = 'IP_ADDRESS'
text = 'proxy'

query_params = urllib.urlencode({
    'access_token' : app_id + '|' + app_secret,
    'type' : type_,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v2.7/threat_indicators?' + query_params)

print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```

The same query in Java:

``` {._5s-8 .prettyprint .lang-code}
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

    public final static void main(String[] args) throws Exception {
        String url = "https://graph.facebook.com/v2.7/threat_indicators?";
        String appID = "5555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP_ADDRESS";
        String text = "proxy";
        
        String query = String.format("access_token=%s&amp;type=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
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

``` {._5s-8 .prettyprint .lang-code}
<?php
  $appID = "555"; // Replace this with your AppID
  $appSecret = "1234"; // Replace this with your App Secret
  $type = 'IP_ADDRESS';
  $text = 'proxy';
  $access_token = $appID . "|" . $appSecret;

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL,
    "https://graph.facebook.com/v2.7/threat_indicators?" .
    "access_token=" . $access_token .
    "&amp;type=" . $type .
    "&amp;text=" . $text);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $response = curl_exec($ch);
  $json = json_encode(json_decode($response), JSON_PRETTY_PRINT);
  print($json . PHP_EOL);
  curl_close($ch);
?>
```
:::
