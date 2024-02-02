
Sample Application - LinkedIn | Microsoft Learn

Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge

Table of contents 

Exit focus mode

Read in English

Save

Table of contents
Read in English

Save
Edit

Print

Twitter
LinkedIn
Facebook
Email

Table of contents

OAuth Sample Application
========================

* Article
* 05/08/2023
* 3 contributors

Feedback

In this article
---------------

Overview
--------

The OAuth Sample Application is a ready-to-use code example that you can readily use to try out RESTful OAuth calls to the LinkedIn Authentication server. This version of the sample application is based on Java. The OAuth sample application shown below provides scalable and customizable code for your requirements as you begin API development with LinkedIn.

The sample application contains the client and server components you can use to manage your request calls to LinkedIn's APIs. The server creates and stores your access token and invokes APIs upon request from the client application.You can download or clone the OAuth sample application and try out these APIs as shown in the demo.

The OAuth sample application uses the following development tools:

* Spring Boot: provides the web server framework [https://spring.io/projects/spring-boot]
* LinkedIn OAuth 2.0: user authorization and API authentication
* Maven: app building and management
* Java: requires SE 7 or later versions for development

Prerequisites
-------------

* Register your application in the LinkedIn Developer Portal.
After registration of the application, note down the Client ID and Client Secret for your future reference
* Add http://localhost:8080/login to the Authorized Redirect URLs under the **Authentication** section
* Configure your application build by installing and using Apache Maven
* Download the OAuth sample application from Sample Application Repository

Configure the OAuth sample application
--------------------------------------

**Configure the client app:**

1. Access the `application.properties` file. This file is located at `/client/src/main/resources/application.properties`
2. Enter the `server.port` and `SERVER_URL` in the noted fields:

```
server.port = <replace_with_required_port_no>
SERVER_URL = <replace_with_required_server_url>
```
3. Save your changes.

**Configure the server app:**

1. Access the `config.properties` file. This file is located at `/server/src/main/resources/config.properties`
2. Enter your client credential values in the noted fields:

```
clientId = <replace_with_client_id>
clientSecret = <replace_with_client_secret>
redirectUri = <replace_with_redirect_url_set_in_developer_portal>
scope = <replace_with_api_scope> 
client_url = <replace_with_client_url>
```
3. Save your changes.

Start the OAuth sample application
----------------------------------

**To start the server:**

1. Access the server folder.
2. Open the terminal/command prompt and run the following command to install dependencies:
`mvn install`
3. Execute the following command to run the spring-boot server:
`mvn spring-boot:run`

Note

The server runs on `http://localhost:8080/`

**To start the client:**

1. Access the client folder.
2. Open the terminal/command prompt and run the following command to install dependencies:
`mvn install`
3. Execute the following command to run the spring-boot server:
`mvn spring-boot:run`

> 
> **Note**: The client runs on `http://localhost:8989/`
> 
> 
> 

Sample Application Demo
-----------------------

This demo shows an overall execution of the LinkedIn OAuth Sample Application. The demo contains clickable areas on the screen, which you can use to navigate.

Note

You can reset the demo by refreshing the page.

### Next Steps

If you are interested in exploring the sample application for Marketing, see Marketing Sample Application.

### List of dependencies

| Component Name | License | Linked | Modified |
| --- | --- | --- | --- |
| boot:spring-boot-starter-parent:2.5.2 | Apache 2.0 | Static | No |
| boot:spring-boot-starter-parent:2.5.2 | Apache 2.0 | Static | No |
| org.springframework.boot:spring-boot-starter-thymeleaf:2.2.2.RELEASE | Apache 2.0 | Static | No |
| org.springframework.boot:spring-boot-devtools:2.6.0 | Apache 2.0 | Static | No |
| com.fasterxml.jackson.core:jackson-databind:2.13.0 | Apache 2.0 | Static | No |
| com.fasterxml.jackson.core:jackson-core:2.13.0 | Apache 2.0 | Static | No |
| org.springframework.boot:spring-boot-starter-web:2.5.2 | Apache 2.0 | Static | No |
| org.springframework.boot:spring-boot-starter-test:2.6.0 | Apache 2.0 | Static | No |
| org.springframework:spring-core:5.3.13 | Apache 2.0 | Static | No |

---

Feedback
--------

Was this page helpful?

Yes

No

Provide product feedback

Feedback
--------

Submit and view feedback for

This product
This page

View all page feedback

---

Additional resources
--------------------

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024

Additional resources
--------------------

### In this article

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024