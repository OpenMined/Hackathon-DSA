Secure Requests - Graph API - Documentation - Meta for Developers

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
Secure Graph API Calls
======================

Almost every Graph API call requires an access token. Malicious developers can steal access tokens and use them to send spam from your app. Meta has automated systems to detect this, but you can help us secure your app. This document covers some of the ways you can improve security in your app.

Meta Crawler
------------

A number of platform services such as Social Plugins and Open Graph require our systems to be able to reach your web pages. We recognize that there are situations where you might not want these pages on the public web, during testing or for other security reasons.

We've provided information on IP allow lists and User Agent strings for Meta's crawlers in our Meta Crawler guide.

Login Security
--------------

There are a large number of settings you can change to improve the security of your app. Please see our Login Security documentation for a checklist of things you can do.

It's also worth looking at our access token documentation which covers various architectures and the security trade-offs that you should consider.

Server Allow List
-----------------

We also enable you to restrict some of your API calls to come from a list of servers that you have allowed to make calls. Learn more in our login security documentation.

Social Plugin Confirmation Steps
--------------------------------

In order to protect users from unintentionally liking content around the web, our systems will occasionally require them to confirm that they intended to interact with one of our Social Plugins via a "confirm" dialog. This is expected behavior and once the system has verified your site as a good actor, the step will be removed automatically.

Encryption
----------

When connecting to our servers your client must use TLS and be able to verify a certificate signed using `sha256WithRSAEncryption`.

Graph API supports TLS 1.2 and 1.3 and non-static RSA cipher suites. We are currently deprecating support for older TLS versions and static RSA cipher suites. Version 16.0 no longer supports TLS versions older than 1.1 or static RSA cipher suites. This change will apply to all API versions on May 3, 2023.

Verify Graph API Calls with `appsecret_proof`
---------------------------------------------

Access tokens are portable. It's possible to take an access token generated on a client by Meta's SDK, send it to a server and then make calls from that server on behalf of the client. An access token can also be stolen by malicious software on a person's computer or a man in the middle attack. Then that access token can be used from an entirely different system that's not the client and not your server, generating spam or stealing data.

Calls from a server can be better secured by adding a parameter called `appsecret_proof`. The app secret proof is a sha256 hash of your access token, using your app secret as the key. The app secret can be found in your app dashboard in **Settings > Basic**.

If you're using the official PHP SDK, the `appsecret_proof` parameter is automatically added.

### Generate the Proof

The following code example is what the call looks like in PHP:

```
$appsecret_proof= hash_hmac('sha256', $access_token, $app_secret); 
```
### Add the Proof

You add the result as an `appsecret_proof` parameter to each call you make:

```
curl \
  -F 'access_token=<access_token>' \
  -F 'appsecret_proof=<app secret proof>' \
  -F 'batch=[{"method":"GET", "relative_url":"me"},{"method":"GET", "relative_url":"me/friends?limit=50"}]' \
  https://graph.facebook.com
```
### Require the Proof

In the **Settings > Advanced** section of your app dashboard in the **Security** section, you enable **Require App Secret**. When this is enabled, we will only allow API calls that include the `appsecret_proof`.