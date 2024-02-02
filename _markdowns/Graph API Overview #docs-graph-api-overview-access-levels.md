::: {._4-u3 ._588p}
::: {._57yz ._57z1 ._3-8p}
::: _57y-
This document is only applicable to apps created using an App Type.
:::
:::

Access levels are an additional layer of Graph API authorization that
apply to [permissions](/docs/permissions/reference) and
[features](/docs/apps/features-reference) for
[Business](/docs/development/create-an-app/app-dashboard/app-types#business)
,
[Consumer](/docs/development/create-an-app/app-dashboard/app-types#consumer)
, and
[Gaming](/docs/development/create-an-app/app-dashboard/app-types#gaming-services)
apps.

<div>

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/130946061_668701493796906_1998528720072373367_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=8r2dyotWRwsAX_dseAb&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAhG_4UzPZPf_uMQ1XI-6nA5AF9byS9ZOcqS_Y83C1spw&oe=65CA0BA0){._254
.img width="729"
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/130946061_668701493796906_1998528720072373367_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=8r2dyotWRwsAX_dseAb&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAhG_4UzPZPf_uMQ1XI-6nA5AF9byS9ZOcqS_Y83C1spw&oe=65CA0BA0"}

</div>

There are two access levels: [Standard](#standard-access) and
[Advanced](#advanced-access) . Apps can request permissions with
Advanced Access from any app user, and features with Advanced Access are
active for all app users. Permissions with Standard Access, however, can
only be requested from app users who have a role on the requesting app,
and features with Standard Access are only active for app users who have
a role on the app.

If your app will only be used by people who have a role on it, the
permissions and features your app requires will only need Standard
Access. If your app will be used by people who do not have a role on it,
the permissions and features that your app requires will need Advanced
Access.

All Business, Consumer, and Gaming apps are automatically approved for
Standard Access for all permissions and features. Advanced Access,
however, must be approved on an individual permission and feature basis
through the [App Review](/docs/app-review) process.
:::
