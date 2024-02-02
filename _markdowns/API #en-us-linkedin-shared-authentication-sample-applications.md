::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

The OAuth Sample Application is a ready-to-use code example that you can
readily use to try out RESTful OAuth calls to the LinkedIn
Authentication server. This version of the sample application is based
on Java. The OAuth sample application shown below provides scalable and
customizable code for your requirements as you begin API development
with LinkedIn.

![OAuth sample app](../../media/oauth-sample-app.png)

The sample application contains the client and server components you can
use to manage your request calls to LinkedIn\'s APIs. The server creates
and stores your access token and invokes APIs upon request from the
client application.You can download or clone the OAuth sample
application and try out these APIs as shown in the demo.

The OAuth sample application uses the following development tools:

-   Spring Boot: provides the web server framework \[
    <https://spring.io/projects/spring-boot> \]
-   LinkedIn OAuth 2.0: user authorization and API authentication
-   Maven: app building and management
-   Java: requires SE 7 or later versions for development

## Prerequisites

## Configure the OAuth sample application

**Configure the client app:**

1.  Access the ` application.properties ` file. This file is located at
    ` /client/src/main/resources/application.properties `

2.  Enter the ` server.port ` and ` SERVER_URL ` in the noted fields:

    ``` lang-javascript
    server.port = <replace_with_required_port_no>
    SERVER_URL = <replace_with_required_server_url>
    ```

3.  Save your changes.

**Configure the server app:**

1.  Access the ` config.properties ` file. This file is located at
    ` /server/src/main/resources/config.properties `

2.  Enter your client credential values in the noted fields:

    ``` lang-javascript
    clientId = <replace_with_client_id>
    clientSecret = <replace_with_client_secret>
    redirectUri = <replace_with_redirect_url_set_in_developer_portal>
    scope = <replace_with_api_scope> 
    client_url = <replace_with_client_url>
    ```

3.  Save your changes.

## Start the OAuth sample application

**To start the server:**

1.  Access the server folder.
2.  Open the terminal/command prompt and run the following command to
    install dependencies: ` mvn install `
3.  Execute the following command to run the spring-boot server:
    ` mvn spring-boot:run `

::: NOTE
Note

The server runs on ` http://localhost:8080/ `
:::

**To start the client:**

1.  Access the client folder.
2.  Open the terminal/command prompt and run the following command to
    install dependencies: ` mvn install `
3.  Execute the following command to run the spring-boot server:
    ` mvn spring-boot:run `

> **Note** : The client runs on ` http://localhost:8989/ `

## Sample Application Demo

This demo shows an overall execution of the LinkedIn OAuth Sample
Application. The demo contains clickable areas on the screen, which you
can use to navigate.

::: NOTE
Note

You can reset the demo by refreshing the page.
:::

If you are interested in exploring the sample application for Marketing,
see [Marketing Sample Application](../../marketing/sample-apps-lms) .

### List of dependencies
:::
