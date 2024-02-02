::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

The LinkedIn Developer Portal Token Generator Tool allows a quick and
easy method for generating an access token to make authenticated API
calls.

## Generate a Token in the Developer Portal

Once a token is generated, users are redirected to the token information
page which includes details like OAuth scopes and token time to live
(TTL) for reference during development activities.

The authenticated member will receive a request for your app to access
to their profile. ![LinkedIn Authorization
Screen](../../media/token-auth-screen.png)

Once the token is generated, the \"Token Details\" will be shown along
with the token. Click \"Copy token\" to paste it into your application
code.

![Token Generation Success](../../media/token-gen-success.png)

Should you wish to verify this an existing token, the [Token Inspector
tool](https://www.linkedin.com/developers/tools/oauth/token-inspector)
is available on the same page as the token generator.

![OAuth Token Tools](../../media/oauth-token-tools.png)

## Developer Portal Token Inspector

LinkedIn\'s Developer Portal has a token inspector tool to make token
validation as simple as copy and paste. The same Token validation is
available through the API or the UI. The [OAuth 2.0 token
inspector](https://www.linkedin.com/developers/tools/oauth/token-inspector)
is accessible from the developer portal under \"Docs and Tools\" in the
navigation bar.

The tool requires you to select a developer application either from a
dropdown or by entering the client ID if you have more than 10 developer
applications. Make sure you have created at least one developer
application or have been added as an Admin team member to a developer
application before using the tool. You may only inspect tokens generated
by the selected developer application.

![Developer Portal Token
Inspector](../../media/dev_portal_token_inspector.png)

The tool can also be used to generate a curl request to the token
introspection endpoint. Simply paste a token in the text box, click
\"Inspect\", and use the \"Copy cUrl request\" button.

![Developer Portal Token Inspector
Results](../../media/dev_portal_token_inspector_results.png)
:::
