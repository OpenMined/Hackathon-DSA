<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This guide explains how to get started with receiving data from the
Facebook Social Graph.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
[Open the Graph API Explorer in a new browser
window.](https://developers.facebook.com/tools/explorer) This allows you
to execute the examples as you read this tutorial.

The explorer loads with a default query with the ` GET ` method, the
lastest version of the Graph API, the ` /me ` node and the ` id ` and
` name ` fields in the [Query String
Field](https://developers.facebook.com/docs/graph-api/guides/explorer#query-string-field)
, and your Facebook App.

<div>

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232068365_563091814813799_6070357364579520404_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=Jb0X_FjdtXMAX_lx8OB&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDcXmBaXCzJaLkQrjTEqC_Pzy282lrE0XR4m6CAeQK_9g&oe=65CA33E4){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232068365_563091814813799_6070357364579520404_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=Jb0X_FjdtXMAX_lx8OB&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDcXmBaXCzJaLkQrjTEqC_Pzy282lrE0XR4m6CAeQK_9g&oe=65CA33E4"}

</div>

### Step 2. Generate an Access Token {#step-2--generate-an-access-token}

Click the **Generate Access Token** button. A **Log in With Facebook**
window will pop up. This popup is your app asking for your permission to
get your name and profile picture from Facebook.

+-----------------------------------+-----------------------------------+
| This flow is our [Facebook        | !                                 |
| Login](/docs/facebook-login)      | [](https://scontent-cdg4-3.xx.fbc |
| product that allows a person to   | dn.net/v/t39.2365-6/231956490_308 |
| log into an app using their       | 313234407833_1605768375436620205_ |
| Facebook credentials. Facebook    | n.png?_nc_cat=106&ccb=1-7&_nc_sid |
| Login allows an app to ask a      | =e280be&_nc_ohc=H78Z8HX0lowAX-2lr |
| person to access the person\'s    | h4&_nc_ht=scontent-cdg4-3.xx&oh=0 |
| Facebook data, and for the person | 0_AfCcEVCId2_KiCorvd-1lgmyZ_a_PN1 |
| to accept or decline access. Your | 3TK3dDbqXrJ7ovg&oe=65CA18AE){.img |
| name and profile picture are      | width="300px"                     |
| public, to allow people to find   | s                                 |
| you on Facebook, so no additional | rcset="https://scontent-cdg4-3.xx |
| requirements are needed to run    | .fbcdn.net/v/t39.2365-6/231956490 |
| this request.                     | _308313234407833_1605768375436620 |
|                                   | 205_n.png?_nc_cat=106&ccb=1-7&_nc |
| Click **Continue as\...**         | _sid=e280be&_nc_ohc=H78Z8HX0lowAX |
|                                   | -2lrh4&_nc_ht=scontent-cdg4-3.xx& |
| A User Access Token is created.   | oh=00_AfCcEVCId2_KiCorvd-1lgmyZ_a |
| This token contains information   | _PN13TK3dDbqXrJ7ovg&oe=65CA18AE"} |
| such as the app making the        |                                   |
| request, the person using the app |                                   |
| to make a request, if the access  |                                   |
| token is still valid (it expires  |                                   |
| in about an hour), the expiration |                                   |
| time, and the scope of data the   |                                   |
| app can request. In this request  |                                   |
| the scope is ` public_profile `   |                                   |
| which includes your name and      |                                   |
| profile picture.                  |                                   |
+-----------------------------------+-----------------------------------+

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232991718_592378688435455_3147910228443606263_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=XOaDXvshUrQAX85c1c1&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBikv7WdelGSDzKdXlytSaL4ArPPAciM4EtrUt01PxdqQ&oe=65CA1D34){.img width="500px" srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232991718_592378688435455_3147910228443606263_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=XOaDXvshUrQAX85c1c1&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBikv7WdelGSDzKdXlytSaL4ArPPAciM4EtrUt01PxdqQ&oe=65CA1D34"}   Click the information circle icon next to the acces token to view the token\'s information.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

Click the **Submit** button in the upper right corner.

#### What You Should See

In the [Response
Window](https://developers.facebook.com/docs/graph-api/guides/explorer#response-window)
, you will see a JSON response with your Facebook User ID and your name.

<div>

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/232902382_904467853476103_7217229934737479641_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=qaKGbtV383YAX9NR_jP&_nc_oc=AQlrv7X5tLdtKcm_RDT-b3lLC602uyQqOHDHJ9O5i2xtLgcIWzxid1Ym85wQhnGOdJU&_nc_ht=scontent-cdg4-1.xx&oh=00_AfD94oqz2Xj2w23lhOzdDwOaEy-2VGvUvo7HT-42XDZufg&oe=65CA1063){.img
srcset="https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/232902382_904467853476103_7217229934737479641_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=qaKGbtV383YAX9NR_jP&_nc_oc=AQlrv7X5tLdtKcm_RDT-b3lLC602uyQqOHDHJ9O5i2xtLgcIWzxid1Ym85wQhnGOdJU&_nc_ht=scontent-cdg4-1.xx&oh=00_AfD94oqz2Xj2w23lhOzdDwOaEy-2VGvUvo7HT-42XDZufg&oe=65CA1063"}

</div>

If you remove ` ?fields=id,name ` from the query string field and click
**Submit** , you will see the same result since ` name ` and ` id ` are
the User node fields returned by default.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Let\'s make the First Request a little more complex by adding another
field, ` email ` . There are two ways to add fields:

-   Click the search dropdown menu in the [Node Field
    Viewer](https://developers.facebook.com/docs/graph-api/guides/explorer#node-field-viewer)
    to the left of the response window
-   Start typing in the query string field.

Let\'s add the ` email ` field and click **Submit** .

#### What You Should See

While the call did not fail, only the ` name ` and ` id ` fields were
returned along with a debug message. Click the (Show) link to debug the
request.

<div>

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/233410295_959323958245691_7180707304587023135_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=9blxrTg0eRsAX-fjOiW&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCbZuTf86yXE9qKzprBUju7J-ic5o2CMFyhLPIXBAbb7Q&oe=65CA0E56){.img
width="600px"
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/233410295_959323958245691_7180707304587023135_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=9blxrTg0eRsAX-fjOiW&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCbZuTf86yXE9qKzprBUju7J-ic5o2CMFyhLPIXBAbb7Q&oe=65CA0E56"}

</div>

Almost all nodes and fields need a specific permission to access them.
The debug message is telling you that you need to give your app
permission to access the email address that you have associated with
your Facebook account.

### Step 2. Add a Permission {#step-2--add-a-permission}

+-----------------------------------+-----------------------------------+
| In the right side panel, under    | ![](https://scontent-cdg4-3.xx.fb |
| **Permissions** , click the **Add | cdn.net/v/t39.2365-6/234580746_36 |
| a Permission** dropdown menu.     | 7949518031866_340317674627083357_ |
| Click **User Data Permissions**   | n.png?_nc_cat=104&ccb=1-7&_nc_sid |
| and select **email** .            | =e280be&_nc_ohc=GGMp-Li8JUwAX84Im |
|                                   | ei&_nc_ht=scontent-cdg4-3.xx&oh=0 |
| ####                              | 0_AfDAkH2KxoG191VRZuS3zcVgUIa04kw |
|  Generate A New User Access Token | Om8RzPkEm2EWrKQ&oe=65CA2EDE){.img |
|                                   | width="350px"                     |
| Because you are changing the      | srcset="https://scontent-cdg4-3.x |
| scope of the access token, you    | x.fbcdn.net/v/t39.2365-6/23458074 |
| need to create a new one. Click   | 6_367949518031866_340317674627083 |
| **Generate Access Token** . Just  | 357_n.png?_nc_cat=104&ccb=1-7&_nc |
| like your first request, you must | _sid=e280be&_nc_ohc=GGMp-Li8JUwAX |
| give your app permission to       | 84Imei&_nc_ht=scontent-cdg4-3.xx& |
| access your email in the Facebook | oh=00_AfDAkH2KxoG191VRZuS3zcVgUIa |
| Login dialog.                     | 04kwOm8RzPkEm2EWrKQ&oe=65CA2EDE"} |
|                                   |                                   |
| Once the new token has been       |                                   |
| created, click **Submit** . Now   |                                   |
| all fields in your request will   |                                   |
| be returned.                      |                                   |
+-----------------------------------+-----------------------------------+

::: _7ab
Try getting your Facebook posts.

[See the steps.](#)
:::

Notice that ` id ` values returned in the response window are links.
These links can represent nodes, such as User, Page, or Post. If you
click on a link, the ID will replace the contents of the query string
field. Now you can run requests on that node. Because this node is
connected to the parent node, a Post of a User, you may not need to add
permissions. You can click on a Post ID now since we will be using it in
the next example.

Notice: Some IDs are a combination of the parent ID and a new ID string.
For example, a User\'s Post will have a Post ID that looks something
like this: ` 1028223264288_102224043055529 ` where ` 1028223264288 ` is
the User ID.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
The User node does not have many edges that can return data. Access to
User objects can only be given by the User who owns the object. In most
cases, a User owns an object if they created it.

For example, if you publish a post you can see information about the
post such as when it was created, text, photos, and links shared in the
post, and the number of reactions the post received. If you comment on
your post, you will be able to get that comment, but if another person
publishes a comment on your post, you will not be able to see the
comment or who published it.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
The explorer tool lets you test requests and once you have a successful
response, you can get the code to insert into your app code. At the
bottom of the response window, click **Get Code** . The explorer offers
Android, iOS, JavaScript, PHP, and cURL code. The code is pre-selected
so you can just copy and paste.

<div>

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/231948896_1065545040645743_5920314088559660186_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=RwigMkJPRiEAX9cZF-8&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBI50RlJHHI8xsJjdgCgNqEDzLCqEFYTEgqPD7jMia_sw&oe=65CA346C){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/231948896_1065545040645743_5920314088559660186_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=RwigMkJPRiEAX9cZF-8&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBI50RlJHHI8xsJjdgCgNqEDzLCqEFYTEgqPD7jMia_sw&oe=65CA346C"}

</div>

We recommend that you implement the Facebook SDK for your app. This SDK
will include Facebook Login which allows your app to ask for permissions
and get access tokens.
:::
:::

</div>
