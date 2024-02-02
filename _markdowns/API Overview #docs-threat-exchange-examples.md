
API Examples - ThreatExchange - Documentation - Meta for Developers









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
API Examples
============

This page has various API examples in Python, Java, PHP, and using cURL.

Python
------

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.


```
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

r = requests.get('https://graph.facebook.com/v2.4/threat_indicators?' + query_params)

print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```
Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.


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

r = requests.get('https://graph.facebook.com/v2.4/threat_descriptors?' + query_params)

print json.dumps(ast.literal_eval(r.text), sort_keys=True,indent=4,separators=(',', ': '))
```
Java
----

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.


```
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

public final static void main(String[] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat_indicators?";
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
Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.


```
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatDescriptors {

public final static void main(String[] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat_descriptors?";
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
PHP
---

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.


```
<?php
$appID = "555"; // Replace this with your AppID
$appSecret = "1234"; // Replace this with your App Secret
$type = 'IP_ADDRESS';
$text = 'proxy';
$access_token = $appID . "|" . $appSecret;

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL,
"https://graph.facebook.com/v2.5/threat_indicators?" .
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
Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.


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
"https://graph.facebook.com/v2.5/threat_descriptors?" .
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
cURL
----

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.


```
curl -i -X GET \
"https://graph.facebook.com/v2.4/threat_indicators"\
"?type=IP_ADDRESS&text=proxy&access_token=555%7C1234"
```
Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.


```
curl -i -X GET \
"https://graph.facebook.com/v2.4/threat_descriptors"\
"?type=IP_ADDRESS&owner=820763734618599&text=proxy&access_token=555%7C1234"
```
































 
