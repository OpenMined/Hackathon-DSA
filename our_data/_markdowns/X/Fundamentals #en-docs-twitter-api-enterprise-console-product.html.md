
Products tab | Docs | Twitter Developer Platform 

Products tab

Products tab
------------

Upon logging into your account at console.gnip.com, you will land on the products tab of the dashboard.  This page includes an overview of the enterprise products currently available on your account.

For products using streaming delivery like PowerTrack or Decahose, this page lists the product name, and stream label,  the number of current active connections, the number of rules currently active for each (where applicable), and the raw count of activities (for example, Tweets) delivered in the most recent 24 hours.

For products with REST delivery, like Search API, this page lists the product name,labels (also shown as "streams"), current activities (for example, Tweets) returned through these endpoints, and a few different request counts per endpoint.

Note that the Usage API delivers much of this data programatically.

Specific details per stream are available by clicking the name, or the settings button.

### Overview

Clicking on one of the streams in the main dashboard will take you to an overview page for that stream.

For streaming delivery products, this page includes the following:

1. A volume chart of the number of activities being delivered to you through each specific stream connection
2. Details (connection ID and IP address) on currently active connections on the stream
3. A log of recent connection, disconnection, and rule-update events for your stream

Note that the scale of the chart may be adjusted with the links in the top-right corner. The visibility of individual connections and disconnections can be toggled by clicking the appropriate key in the legend directly below the chart.

### Connections

The Connections page provides details on recent connection events on your stream. This includes the start and end times for each connection (in 24 hour UTC), the duration of each connection, the IP of the server that made the connection, a unique connection ID for reference purposes, and the current connection status. The status corresponds to the most recent event for the specified connection – i.e. Client Connected, or a disconnect, with the type of disconnect specified.   For more details on connection debugging, visit the disconnections explained guide.

### API Help

The API Help page provides the API endpoint URLs for your stream, as well as the Rules API endpoint for the stream, where applicable. In addition, it includes sample curl commands and instructions on how to connect to the stream endpoint, and how to programmatically add, delete, and list rules from your stream's Rules API endpoint.

### Rules

The Rules tab is available for PowerTrack streams, and provides a quick way to get started by manually entering plain text rules via a user interface. Note that the interface only supports adding up to 1000 rules via this manual method, and should be only used for initial testing. We recommend managing your rules programmatically via the Rules API in any production setting.

### Settings

The Settings tab allows you to switch the output format of the data in your stream, where multiple format options are supported. To switch the format, just use the radio buttons indicating the different options. The change will take effect upon reconnecting to the stream.  Note that updating this setting will take place immediately on the next request or connection and may break your parser with the new format. 

**Please note:** The recommended setting for getting the most data is "Leave data in the original format" which will return data in the enriched native format here.  Activity streams format is described here.

### Next Steps:

* Review usage tab
* Review account tab

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies