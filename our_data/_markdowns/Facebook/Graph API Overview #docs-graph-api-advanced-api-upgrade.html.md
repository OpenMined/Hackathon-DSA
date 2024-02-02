Upgrade - Graph API - Documentation - Meta for Developers

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
Upgrade to the Latest Graph API Version
=======================================

This guide describes how to prepare your app to test different versions of the Graph API and to upgrade to the latest version.

The API Upgrade Tool shows the API calls from your app that may be affected by changes in newer versions of the API. You will be able to quickly see which changes you need to make to upgrade from your current version to a newer version.

Learn How a Change Affects Your App
-----------------------------------

The API Upgrade Tool displays a customized list of changes that impact an app when upgrading to a specified target version. This allows you to view all relevant changes between the source and target versions.

Step 1. In the Upgrade tool, select your app from the dropdown menu or type in the name of the app.

The dropdown menu only lists up to ten apps. To view more apps than those listed, use the search bar in the dropdown menu.

Step 2. Use the dropdown menus to the right to select the version you would like to **Upgrade from** and the version you would like to **Upgrade to**.

### Read the Results

The tool displays the number of changes that need to be made to update your app to the selected version. If your app makes API calls that will not be affected by a newer version no data will be returned.

Methods are color coded by the version affecting the call. Hover over the bar chart to see how many changes are in each version. The dates associated with each version are when the changes will be enforced for all apps.

The table shows the type of change (deprecation, new feature or change), which methods are affected, the number of calls made in the last 7 days, and the percentage of API calls affected by that specific change.

### Limitations

* You must be an admin or developer of the app to view the app in the tool.
* No data will be returned if your app has not made any, or too few, API calls from the **Update from** version.
* Call volumes may appear incorrect. API call logging is sampled and aggregated over the previous week. It is compared with the call volume to estimate how many of your calls could be affected by a given version change.

**Note:** Not all changes may affect each API call. Use your best judgment on whether a particular change needs to be handled by your app. Be sure to test your API calls in the newer version to ensure it works properly.

Implement a New Version
-----------------------

In the App Dashboard **Settings > Advanced**, scroll to the **Upgrade API Version** section.

#### Upgrading Developers and Admins

This upgrades all developers and admins of an app to the next available version. This allows you to test changes with a small subset of real users before releasing the new version to the public.

#### Upgrading All Calls

This upgrades all calls made by an app to the next available version. Upgrading early is useful since it preserves the option of going back to the original version in case of unforeseen bugs or issues.

Learn More
----------

* Graph API Changelog – Learn about the latest version changes.
* Versioning – Learn all about Graph API versioning, requests to different versions, and more.
* Test Apps – Learn how to create test apps to test changes to your app before public release.
* Test Users – Learn how to create test users to test changes to your app before public release.