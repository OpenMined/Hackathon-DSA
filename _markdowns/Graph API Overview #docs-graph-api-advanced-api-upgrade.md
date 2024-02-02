::: {._4-u3 ._588p}
The API Upgrade Tool displays a customized list of changes that impact
an app when upgrading to a specified target version. This allows you to
view all relevant changes between the source and target versions.

Step 1. In the [Upgrade
tool](https://developers.facebook.com/tools/api_versioning/) , select
your app from the dropdown menu or type in the name of the app.

The dropdown menu only lists up to ten apps. To view more apps than
those listed, use the search bar in the dropdown menu.

Step 2. Use the dropdown menus to the right to select the version you
would like to **Upgrade from** and the version you would like to
**Upgrade to** .

### Read the Results

The tool displays the number of changes that need to be made to update
your app to the selected version. If your app makes API calls that will
not be affected by a newer version no data will be returned.

Methods are color coded by the version affecting the call. Hover over
the bar chart to see how many changes are in each version. The dates
associated with each version are when the changes will be enforced for
all apps.

The table shows the type of change (deprecation, new feature or change),
which methods are affected, the number of calls made in the last 7 days,
and the percentage of API calls affected by that specific change.

### Limitations

-   You must be an admin or developer of the app to view the app in the
    tool.
-   No data will be returned if your app has not made any, or too few,
    API calls from the **Update from** version.
-   Call volumes may appear incorrect. API call logging is sampled and
    aggregated over the previous week. It is compared with the call
    volume to estimate how many of your calls could be affected by a
    given version change.

**Note:** Not all changes may affect each API call. Use your best
judgment on whether a particular change needs to be handled by your app.
Be sure to test your API calls in the newer version to ensure it works
properly.
:::
