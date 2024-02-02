Overview - Ad Targeting dataset - Documentation - Meta for Developers

Ad Targeting dataset* Get access
* Overview
* Get started
* Sample queries
* Table schema
* Support
Overview
========

The Ad Targeting Dataset contains the ad targeting logic of all of the Social Issue, Electoral, and Political (SIEP) ads run beginning August 3, 2020 on the Facebook and Instagram platforms.

This document provides an overview of the dataset and its usage requirements.

**Get access**

To query the dataset, you must be an approved Meta Research Partner. See Onboarding to get access.

Dataset
-------

The dataset comprises a single table containing targeting data of social issue, electoral, and political ads. All data used to build the dataset has been processed to remove any personally identifiable user information.

Only ads concerning social issues, elections, and politics that were run on or after August 3, 2020 are included in the data. Ads included are from all countries in which we currently have our ad authorizations and disclaimer tools available. More information about the included countries is available here.
Publication of this data began in May of 2022.

On the 1st of each month, an update to the table is published so that it includes all data through the 21st of the previous month. Beginning with the second month of published data (June 2022), there is also a delta table that describes ads that were reclassified as non-political since the previous update. The first three months of data (August 3 - November 1, 2020) were originally published as the Ad Targeting February 2021 Dataset (with U.S. data only).

**Ads are retained for seven years**

We store all social issue, electoral and political ads in our Ad Library for seven years. In line with this, data in the Ad Targeting dataset is not accessible after seven years.

Issues with inclusions and exclusions of custom and lookalike audiences
-----------------------------------------------------------------------

For the dataset of targeting data on social issue, electoral and political ads for the 90-day period leading up to the US 2020 election, released in February 2021, there were some issues with inclusions and exclusions of custom and lookalike audiences.

Also, for ads created before November 1, 2021, data may be missing from some ads where advertisers initially used a custom or lookalike audience, but later deleted that audience.

We are addressing the issues we’ve discovered by providing updated documentation on how to proceed.

See Updates and differences in the datasets for a comparison of the original and new datasets and more information about these issues.

Important dates
---------------

It might be helpful to know these important dates as you work with the dataset:

 Significance | Date || Beginning date of both the original February 2021 dataset and the new May 2022 dataset. | August 3, 2020 |
| Last date included in the original February 2021 dataset. | November 1, 2020 |
| Dates included in both the original and new datasets. | August 3 - November 1, 2020 |
| First publication of the new dataset. | May 31, 2022
Includes data from August 3, 2020 - April 21, 2022 |
| First monthly update to the new dataset. | June 1, 2022
Updates the dataset to include data from August 3, 2020 - May 21, 2022 |
| First publication of the delta table. | June 1, 2022 |
| Date we began to preserve custom audience information for audiences that were initially used and later removed by advertisers. | November 1, 2021
See Updates and Differences in the Datasets for more information. |
| Date the `fbid` column name in the `ad_archive_api` table changed from `ad_archive_id` to `fbid`. | April 21, 2021
See Joining Ads Targeting Dataset Data with Ad Library Data in the Table Schema section for more information.
 |
| Date changes were made to the table schema to more clearly and accurately represent included and excluded targeting criteria. | September 1, 2022
See Changelog for details.
 |
| Date as of which researchers could apply for access to the Ad Targeting Dataset by submitting a data access request and completing the required, self-serve onboarding process. | September 7, 2022
See Meta for Developers Onboarding for more information.
 |
Researcher Platform
-------------------

You must use our Researcher Platform web app to access the dataset. The app runs on JupyterHub, which allows you to import our Python3 SQL query module into a Jupyter Notebook and run SQL queries against the dataset. You can access Researcher Platform user documentation here.

The Researcher Platform URL is emailed to you once you have completed the onboarding process.

VPN
---

You must access the Researcher Platform through our virtual private network (VPN) using OpenVPN. Follow our OpenVPN Setup document to learn how to install and configure the OpenVPN client correctly.

How it works
------------

Once you have completed onboarding, this is the general flow for querying the dataset:

1. Connect to our VPN.
2. Visit the Researcher Platform URL that was emailed to you and sign in with your Facebook account.
3. Create a Python3 Jupyter notebook.
4. Import our query module.
5. Use the module to create and execute SQL queries.
6. Examine the results returned to your Jupyter notebook.

Next steps
----------

Read our Get started guide to learn how to use the Researcher Platform and perform a basic SQL query.

Learn more
----------

 For the dataset's codebook, see Ad Targeting Dataset Codebook.
Additional resources:

* Updates and differences in the datasets
* Onboarding for access to the Ad Targeting dataset
* OpenVPN setup