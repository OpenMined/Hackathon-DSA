Get Started - Graph API - Documentation - Meta for Developers

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
Get Started
===========

This guide explains how to get started with receiving data from the Facebook Social Graph.

Before You Start
----------------

You will need:

* Register as a Meta Developer
* A Meta App – This app will be for testing so there is no need to involve your app code when creating this Meta App.
* The Graph API Explorer tool open in a separate browser window
* A brief understanding of the structure of the Meta's social graph from our Graph API Overview guide
Your First Request
------------------

### Step 1: Open the Graph API Explorer tool

Open the Graph API Explorer in a new browser window. This allows you to execute the examples as you read this tutorial.
The explorer loads with a default query with the `GET` method, the lastest version of the Graph API, the `/me` node and the `id` and `name` fields in the Query String Field, and your Facebook App.

### Step 2. Generate an Access Token

Click the **Generate Access Token** button. A **Log in With Facebook** window will pop up. This popup is your app asking for your permission to get your name and profile picture from Facebook.

|  |  |
| --- | --- |
| This flow is our Facebook Login product that allows a person to log into an app using their Facebook credentials. Facebook Login allows an app to ask a person to access the person's Facebook data, and for the person to accept or decline access. Your name and profile picture are public, to allow people to find you on Facebook, so no additional requirements are needed to run this request.
Click **Continue as...**
A User Access Token is created. This token contains information such as the app making the request, the person using the app to make a request, if the access token is still valid (it expires in about an hour), the expiration time, and the scope of data the app can request. In this request the scope is `public_profile` which includes your name and profile picture. |  |

|  |  |
| --- | --- |
|  | Click the information circle icon next to the acces token to view the token's information. |
### Step 3. Submit the Request

Click the **Submit** button in the upper right corner.

#### What You Should See

In the Response Window, you will see a JSON response with your Facebook User ID and your name.

If you remove `?fields=id,name` from the query string field and click **Submit**, you will see the same result since `name` and `id` are the User node fields returned by default.

Your Second Request
-------------------

### Step 1. Let's Add a Field

Let's make the First Request a little more complex by adding another field, `email`. There are two ways to add fields:

* Click the search dropdown menu in the Node Field Viewer to the left of the response window
* Start typing in the query string field.

Let's add the `email` field and click **Submit**.

#### What You Should See

While the call did not fail, only the `name` and `id` fields were returned along with a debug message. Click the (Show) link to debug the request.

Almost all nodes and fields need a specific permission to access them. The debug message is telling you that you need to give your app permission to access the email address that you have associated with your Facebook account.

### Step 2. Add a Permission

|  |  |
| --- | --- |
| In the right side panel, under **Permissions**, click the **Add a Permission** dropdown menu. Click **User Data Permissions** and select **email**.
Generate A New User Access Token
Because you are changing the scope of the access token, you need to create a new one. Click **Generate Access Token**. Just like your first request, you must give your app permission to access your email in the Facebook Login dialog.
Once the new token has been created, click **Submit**. Now all fields in your request will be returned. |  |
Try getting your Facebook posts.

See the steps.
#### Links in the Response

Notice that `id` values returned in the response window are links. These links can represent nodes, such as User, Page, or Post. If you click on a link, the ID will replace the contents of the query string field. Now you can run requests on that node. Because this node is connected to the parent node, a Post of a User, you may not need to add permissions. You can click on a Post ID now since we will be using it in the next example.

Notice: Some IDs are a combination of the parent ID and a new ID string. For example, a User's Post will have a Post ID that looks something like this: `1028223264288_102224043055529` where `1028223264288` is the User ID.

Let's Look at an Edge
---------------------

The User node does not have many edges that can return data. Access to User objects can only be given by the User who owns the object. In most cases, a User owns an object if they created it.

For example, if you publish a post you can see information about the post such as when it was created, text, photos, and links shared in the post, and the number of reactions the post received. If you comment on your post, you will be able to get that comment, but if another person publishes a comment on your post, you will not be able to see the comment or who published it.

Try getting the number of reactions for one of your posts. You will want to take a look at the

Object Reactions reference.See the steps.
Get the Code for your Request
-----------------------------

The explorer tool lets you test requests and once you have a successful response, you can get the code to insert into your app code. At the bottom of the response window, click **Get Code**. The explorer offers Android, iOS, JavaScript, PHP, and cURL code. The code is pre-selected so you can just copy and paste.

We recommend that you implement the Facebook SDK for your app. This SDK will include Facebook Login which allows your app to ask for permissions and get access tokens.

Learn More
----------

You can use the Graph API Explorer to test any request for Users, Pages, Groups, and more. Visit the reference for each node or edge to determine the permission and access token type required.

|  |  |
| --- | --- |
| * Access Token
* Facebook Login
* Facebook SDKs
 | * Graph API References
* Graph API Explorer Guide
* Login Security
* Permissions Reference
 |