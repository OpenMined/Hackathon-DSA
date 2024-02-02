::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

The LinkedIn API uses [OAuth 2.0](http://oauth.net/2/) for user
authorization and API authentication. Applications must be authorized
and authenticated before they can fetch data from LinkedIn or get access
to member data. This page summarizes the available permissions and
partner programs available for accessing LinkedIn APIs. Most permissions
and partner programs require explicit approval from LinkedIn. [Open
Permissions](#open-permissions-consumer) are the only permissions that
are available to all developers without special approval.

All permissions listed below are used in either [Member Authentication
Flow](authorization-code-flow) (3-legged) or [Application Authentication
Flow](client-credentials-flow) (2-legged). More about these permission
types can be found in [Authenticating with OAuth 2.0
Overview](authentication) .

## Open Permissions (Consumer)

The following permissions are available to all developers, and may be
added via self-service through the LinkedIn [Developer
Portal](https://www.linkedin.com/developers/) , under the Products tab
on your application page. LinkedIn products can be enabled after
creating a new application.

  Product/Program                              Permission        Description
  -------------------------------------------- ----------------- --------------------------------------------------------------------------------------
  Sign in with LinkedIn using OpenID Connect   profile           **Member Auth** : Retrieve authenticated member\'s name, headline, and photo.
  Sign in with LinkedIn using OpenID Connect   email             **Member Auth** : Retrieve authenticated member\'s primary email address.
  Share on LinkedIn                            w_member_social   **Member Auth** : Post, comment and like posts on behalf of an authenticated member.

## Learning

Developers seeking to build a learning related integration should refer
to the [Request API
Access](../../learning/getting-started/request-access) page within the
LinkedIn Learning API space.

## Marketing

Developers seeking to build a marketing related integration using
Advertising APIs permissions must be approved. You can apply for access
through the [Developer Portal](https://www.linkedin.com/developers/) .
This can be done by selecting your app from [My
Apps](https://www.linkedin.com/developers/apps) , navigate to the
Products tab, and add the Marketing Developer Platform product.
Qualifications to be an Advertising APIs partner are available at
[Become a
Partner](https://business.linkedin.com/marketing-solutions/marketing-partners/become-a-partner/marketing-developer-program)
.

![MDP](../../media/marketing-dev-pgm.png)

Audiences permissions may be applied for after being an approved
Marketing Developer Platform partner. Contact support or your partner
rep for application information.

+-----------------------+-----------------------+-----------------------+
| Product/Program       | Permission            | Description           |
+=======================+=======================+=======================+
| Advertising APIs      | rw_organization_admin | **Member Auth** :     |
|                       |                       | Manage an             |
|                       |                       | authenticated         |
|                       |                       | member's company      |
|                       |                       | pages and retrieve    |
|                       |                       | reporting data.       |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r_organization_admin  | **Member Auth** :     |
|                       |                       | Retrieve an           |
|                       |                       | authenticated         |
|                       |                       | member's company      |
|                       |                       | pages and their       |
|                       |                       | reporting data.       |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | w_organization_social | **Member Auth** :     |
|                       |                       | Post, comment and     |
|                       |                       | like posts on behalf  |
|                       |                       | of an organization.   |
|                       |                       | Restricted to         |
|                       |                       | organizations in      |
|                       |                       | which the             |
|                       |                       | authenticated member  |
|                       |                       | has one of the        |
|                       |                       | following company     |
|                       |                       | page roles.           |
|                       |                       |                       |
|                       |                       | ` ADMINISTRATOR `     |
|                       |                       |                       |
|                       |                       | ` DIRECT_SPONS        |
|                       |                       | ORED_CONTENT_POSTER ` |
|                       |                       |                       |
|                       |                       | ` LEA                 |
|                       |                       | D_GEN_FORMS_MANAGER ` |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r_organization_social | **Member Auth** :     |
|                       |                       | Retrieve              |
|                       |                       | organizations\'       |
|                       |                       | posts, comments, and  |
|                       |                       | likes.                |
+-----------------------+-----------------------+-----------------------+
| Marketing Developer   | w_member_social       | **Member Auth** :     |
| Platform (MDP)        |                       | Post, comment, and    |
|                       |                       | like posts on behalf  |
|                       |                       | of an authenticated   |
|                       |                       | member.               |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | rw_ads                | **Member Auth** :     |
|                       |                       | Manage and read an    |
|                       |                       | authenticated         |
|                       |                       | member\'s ad          |
|                       |                       | accounts. Restricted  |
|                       |                       | to ad accounts in     |
|                       |                       | which the             |
|                       |                       | authenticated member  |
|                       |                       | has one of the        |
|                       |                       | following ad account  |
|                       |                       | roles.                |
|                       |                       |                       |
|                       |                       | ` AC                  |
|                       |                       | COUNT_BILLING_ADMIN ` |
|                       |                       |                       |
|                       |                       | ` ACCOUNT_MANAGER `   |
|                       |                       |                       |
|                       |                       | ` CAMPAIGN_MANAGER `  |
|                       |                       |                       |
|                       |                       | ` CREATIVE_MANAGER `  |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r_ads                 | **Member Auth** :     |
|                       |                       | Read an authenticated |
|                       |                       | member\'s ad          |
|                       |                       | accounts. Restricted  |
|                       |                       | to ad accounts in     |
|                       |                       | which the             |
|                       |                       | authenticated member  |
|                       |                       | has one of the        |
|                       |                       | following ad account  |
|                       |                       | roles:                |
|                       |                       |                       |
|                       |                       | -   ` AC              |
|                       |                       | COUNT_BILLING_ADMIN ` |
|                       |                       | -                     |
|                       |                       |   ` ACCOUNT_MANAGER ` |
|                       |                       | -                     |
|                       |                       |  ` CAMPAIGN_MANAGER ` |
|                       |                       | -                     |
|                       |                       |  ` CREATIVE_MANAGER ` |
|                       |                       | -   ` VIEWER `        |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r_ads_reporting       | **Member Auth** :     |
|                       |                       | Retrieve reporting    |
|                       |                       | for advertising       |
|                       |                       | accounts.             |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r                     | **Member Auth** :     |
|                       | _1st_connections_size | Retrieve the count of |
|                       |                       | an authenticated      |
|                       |                       | member\'s 1st-degree  |
|                       |                       | connections.          |
+-----------------------+-----------------------+-----------------------+
| Advertising APIs      | r_basicprofile        | **Member Auth** :     |
|                       |                       | Read an authenticated |
|                       |                       | member\'s basic       |
|                       |                       | profile including     |
|                       |                       | name, photo,          |
|                       |                       | headline, and public  |
|                       |                       | profile URL.          |
+-----------------------+-----------------------+-----------------------+
| Lead Sync             | r_marketi             | **Member Auth** :     |
|                       | ng_leadgen_automation | Access your lead      |
|                       |                       | generation forms and  |
|                       |                       | retrieve leads        |
|                       |                       | (including event      |
|                       |                       | leads, ad leads, and  |
|                       |                       | organization page     |
|                       |                       | leads).               |
+-----------------------+-----------------------+-----------------------+
| Audiences             | rw_dmp_segments       | **Member Auth** :     |
|                       |                       | Create and manage     |
|                       |                       | matched audiences.    |
+-----------------------+-----------------------+-----------------------+

## Sales

Developers seeking to build sales related integration using one of the
permissions below must be approved as a Sales Navigator Application
Platform (SNAP) partner. [Apply
here](https://business.linkedin.com/sales-solutions/partners/become-a-partner)
to be a SNAP partner.

  Product/Program                              Permission               Description
  -------------------------------------------- ------------------------ ------------------------------------------------------------------------------------------------------------------------------
  Sales Navigator Application Platform(SNAP)   r_sales_nav_analytics    **Member Auth** : Enables access to Sales Navigator Analytics retrieval.
  Sales Navigator Application Platform(SNAP)   r_sales_nav_display      **Member Auth** : Display Services permission for Sales Navigator.
  Sales Navigator Application Platform(SNAP)   r_sales_nav_validation   **Application Auth** : Access Sales Navigator endpoints for CRM data validation.
  Sales Navigator Application Platform(SNAP)   r_sales_nav_profiles     **Application Auth** : Access Sales Navigator endpoints that present matched, publicly available member profile information.

## Talent

Developers seeking to build talent related integrations through one of
the programs listed below can [apply
here](https://business.linkedin.com/talent-solutions/ats-partners/partner-application)
. We recommend familiarizing yourself with the types of partner
integrations available before applying by visiting
[here](https://business.linkedin.com/talent-solutions/ats-partners#all)
and
[here](https://business.linkedin.com/talent-solutions/talent-hub/integrations#all)
.

## Compliance (Closed)

The following permissions used for Compliance integrations are listed
for reference purposes only. Access is closed and may not be requested.

  Product/Program   Permission     Description
  ----------------- -------------- -------------------------------------------------------------------------------
  Compliance        r_compliance   **Member Auth** : Retrieve activities for compliance monitoring and archiving
  Compliance        w_compliance   **Member Auth** : Manage and delete data for compliance.
:::
