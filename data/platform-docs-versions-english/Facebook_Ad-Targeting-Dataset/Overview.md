Overview
========

The Ad Targeting Dataset contains the ad targeting logic of all of the Social Issue, Electoral, and Political (SIEP) ads run beginning August 3, 2020 on the Facebook and Instagram platforms.

This document provides an overview of the dataset and its usage requirements.

**Get access**

To query the dataset, you must be an approved Meta Research Partner. See [Onboarding](https://developers.facebook.com/docs/fort/get-access) to get access.

Dataset
-------

The dataset comprises a single table containing targeting data of social issue, electoral, and political ads. All data used to build the dataset has been processed to remove any personally identifiable user information.

Only ads concerning social issues, elections, and politics that were run on or after August 3, 2020 are included in the data. Ads included are from all countries in which we currently have our ad authorizations and disclaimer tools available. More information about the included countries is available [here.](https://www.facebook.com/business/help/2150157295276323?id=288762101909005)

Publication of this data began in May of 2022.

On the 1st of each month, an update to the table is published so that it includes all data through the 21st of the previous month. Beginning with the second month of published data (June 2022), there is also a delta table that describes ads that were reclassified as non-political since the previous update. The first three months of data (August 3 - November 1, 2020) were originally published as the Ad Targeting February 2021 Dataset (with U.S. data only).

**Ads are retained for seven years**

We store all social issue, electoral and political ads in our Ad Library for seven years. In line with this, data in the Ad Targeting dataset is not accessible after seven years.

Issues with inclusions and exclusions of custom and lookalike audiences
-----------------------------------------------------------------------

For the dataset of targeting data on social issue, electoral and political ads for the 90-day period leading up to the US 2020 election, released in February 2021, there were some issues with inclusions and exclusions of custom and lookalike audiences.

Also, for ads created before November 1, 2021, data may be missing from some ads where advertisers initially used a custom or lookalike audience, but later deleted that audience.

We are addressing the issues we’ve discovered by providing updated documentation on how to proceed.

See [Updates and differences in the datasets](https://developers.facebook.com/docs/fort-ads-targeting-dataset/january-2021-dataset) for a comparison of the original and new datasets and more information about these issues.

Important dates
---------------

It might be helpful to know these important dates as you work with the dataset:

| Significance | Date |
| --- | --- |
| Beginning date of both the original February 2021 dataset and the new May 2022 dataset. | August 3, 2020 |
| Last date included in the original February 2021 dataset. | November 1, 2020 |
| Dates included in both the original and new datasets. | August 3 - November 1, 2020 |
| First publication of the new dataset. | May 31, 2022<br><br>  <br><br>Includes data from August 3, 2020 - April 21, 2022 |
| First monthly update to the new dataset. | June 1, 2022<br><br>  <br><br>Updates the dataset to include data from August 3, 2020 - May 21, 2022 |
| First publication of the [delta table](https://developers.facebook.com/docs/fort-ads-targeting-dataset/table-schema#delta-schema). | June 1, 2022 |
| Date we began to preserve custom audience information for audiences that were initially used and later removed by advertisers. | November 1, 2021<br><br>  <br><br>See [Updates and Differences in the Datasets](https://developers.facebook.com/docs/fort-ads-targeting-dataset/january-2021-dataset) for more information. |
| Date the `fbid` column name in the `ad_archive_api` table changed from `ad_archive_id` to `fbid`. | April 21, 2021<br><br>  <br><br>See [Joining Ads Targeting Dataset Data with Ad Library Data](https://developers.facebook.com/docs/fort-ads-targeting-dataset/table-schema#joining-ad-library) in the Table Schema section for more information. |
| Date changes were made to the table schema to more clearly and accurately represent included and excluded targeting criteria. | September 1, 2022<br><br>  <br><br>See [Changelog](https://developers.facebook.com/docs/fort-ads-targeting-dataset/support/changelog) for details. |
| Date as of which researchers could apply for access to the Ad Targeting Dataset by submitting a data access request and completing the required, self-serve onboarding process. | September 7, 2022<br><br>  <br><br>See [Meta for Developers Onboarding](https://developers.facebook.com/docs/fort/get-access) for more information. |

Researcher Platform
-------------------

You must use our Researcher Platform web app to access the dataset. The app runs on JupyterHub, which allows you to import our Python3 SQL query module into a Jupyter Notebook and run SQL queries against the dataset. You can access Researcher Platform [user documentation here](https://developers.facebook.com/docs/researcher-platform/).

The Researcher Platform URL is emailed to you once you have [completed the onboarding process](https://developers.facebook.com/docs/fort/get-access).

VPN
---

You must access the Researcher Platform through our virtual private network (VPN) using OpenVPN. Follow our [OpenVPN Setup](https://developers.facebook.com/docs/fort/get-access/vpn) document to learn how to install and configure the OpenVPN client correctly.

How it works
------------

Once you have [completed onboarding](https://developers.facebook.com/docs/fort/get-access), this is the general flow for querying the dataset:

1. Connect to our VPN.
2. Visit the Researcher Platform URL that was emailed to you and sign in with your Facebook account.
3. Create a Python3 Jupyter notebook.
4. Import our query module.
5. Use the module to create and execute SQL queries.
6. Examine the results returned to your Jupyter notebook.

Next steps
----------

Read our [Get started](https://developers.facebook.com/docs/fort-ads-targeting-dataset/get-started) guide to learn how to use the Researcher Platform and perform a basic SQL query.

Learn more
----------

For the dataset's codebook, see [Ad Targeting Dataset Codebook.](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/327966766_556592703070288_3426165002794598818_n.pdf?_nc_cat=102&ccb=1-7&_nc_sid=b8d81d&_nc_ohc=ooEqA2kH2gkAX9W_NgR&_nc_oc=AQlALs9OEgnGSiZ-HaODbEdbImq8cimime9l_M-NbrbTpUYNxRKfKGuTfU657LRLcVc&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCDg9z4trzJkJBFw5kqbN5K9AqZtjDDoKZ07AfUCk414g&oe=65B5A8A4)

Additional resources:

* [Updates and differences in the datasets](https://developers.facebook.com/docs/fort-ads-targeting-dataset/january-2021-dataset)
* [Onboarding for access to the Ad Targeting dataset](https://developers.facebook.com/docs/fort/get-access)
* [OpenVPN setup](https://developers.facebook.com/docs/fort/get-access/vpn)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Updates and differences in the datasets
=======================================

The Ad Targeting February 2021 dataset consists of targeting data on social issue, electoral, and political ads from August 3 - November 1, 2020 (U.S. data only).

The Ad Targeting May 2022 dataset consists of targeting data on social issue, electoral, and political ads beginning August 3, 2020 through the present. The May 2022 dataset includes ads from all countries in which we currently have our ad authorizations and disclaimer tools available.

Both datasets include data from August 3 - November 1, 2020.

Understanding the differences between the two datasets
------------------------------------------------------

Since you might be using one or both datasets in your research, and since you might want to transfer your research from the old dataset to the new one, it is important to understand the differences:

| Feature | February 2021 dataset | May 2022 dataset |
| --- | --- | --- |
| Table name | `ad_targeting_dataset` | `ad_targeting_dataset_siep_aug_2020`<br><br>  <br><br>There are three additional columns in this table: `exclude_audience_data_missing`, `include_audience_data_missing`, and `language`.<br><br>  <br><br>See [Table schema](https://developers.facebook.com/docs/fort-ads-targeting-dataset/table-schema) for details. |
| Coverage area | USA data only. | All countries in which we currently have our ad authorizations and disclaimer tools available.<br><br>  <br><br>More information about the countries this includes is available [here.](https://www.facebook.com/business/help/2150157295276323?id=288762101909005) |
| Minimum number of impressions for the ad to be included | 100 | 1   |
| Ongoing data collected and published | No  | Yes<br><br>  <br><br>On the 1st of each month beginning June 2022, an update to the table is published so that it includes all data through the 21st of the previous month. A delta table is also published, listing ads that were reclassified as non-political (and therefore removed) since the previous publication. |
| Indicates where custom audience data is known to be missing.<br><br>  <br><br>See [How to manage issues found in the datasets](#manage-issues) for more information. | No  | Yes<br><br>  <br><br>`include_audience_data_missing` and `exclude_audience_data_missing` columns are new in this dataset. |
| Preserves custom audience information for audiences that were removed.<br><br>  <br><br>See [How to manage issues found in the datasets](#manage-issues) for more information. | No  | Yes, after November 1, 2021. |

How to manage issues found in the datasets
------------------------------------------

There are two issues having to do with the inclusion or exclusion of custom and lookalike audiences that we found in the datasets.

**These issues only affected data related to custom and lookalike audiences.**

Your research was not impacted if it did not involve custom or lookalike audiences.

Here's what we have done to address these issues:

* We are providing this updated documentation explaining the issues and describing ways to interpret the data in light of them.
    
* We have corrected the issues in the May 2022 targeting dataset.
    
* We have included two new columns in the May 2022 targeting dataset called `include_audience_data_missing` and `exclude_audience_data_missing`. These columns are marked True where we know we are missing data. A value of True (data is missing) indicates that a custom or lookalike audience was used, but we’re unable to identify or report the specifics of that audience.
    

Here are the two issues and strategies for interpreting any data affected by them:

* Issue #1: [incorrect calculations](#incorrect-calculations)
    
* Issue #2: [deleted custom audiences](#deleted-CA)
    

### **Issue #1 incorrect calculations**

Due to an error in the source code for the February 2021 dataset, when calculating the `include_custom_audience` and `exclude_custom_audience` data fields, we calculated the inclusion and exclusion of custom audiences where custom audiences may not actually have been used. For less than 12% of ads within the targeting dataset, this resulted in custom audience inclusion or exclusion incorrectly reading as True.

This has been corrected in the new dataset released in 2022, so if you are only using the new dataset, this problem will not affect your research.

If you are using the 2021 dataset, comparing ads from the 2021 and 2022 datasets can help you to interpret the data. Here's how:

1. For the three months of overlap, compare the two datasets, looking specifically at these custom audience columns:
    
    * `include_custom_audience`
    * `exclude_custom_audience`
2. If there is a difference between the two datasets in the `include_custom_audience` column, and `include_audience_data_missing` (in the new dataset) is True, the discrepancy could be the result of either incorrect calculation (Issue #1) or custom audience deletion (Issue #2), and there is no way to know which. If `include_audience_data_missing` is False (no missing data), the discrepancy is the result of incorrect calculation (Issue #1).
    
3. If there is a difference between the two datasets in the `exclude_custom_audience` column, and `exclude_audience_data_missing` (in the new dataset) is True, the discrepancy could be the result of either incorrect calculation (Issue #1) or custom audience deletion (Issue #2), and there is no way to know which. If `exclude_audience_data_missing` is False (no missing data), the discrepancy is the result of incorrect calculation (Issue #1).
    

This example shows how you can use `join` to compare the old and new datasets:

old\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_library\_targeting")
new\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020")
data = old\_targeting\_dataset.join(new\_targeting\_dataset.set\_index('archive\_id'), 'archive\_id', rsuffix='\_new')

data\[(data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\])\] # Checking the new data against the old data

data\[(data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\]) and (data\['include\_audience\_data\_missing'\] == False)\] # Checking the new data against the old data where there are no instances of missing data
          
          

### Issue #2 deleted custom audiences

For ads created before November 1, 2021, data might be missing from some ads where advertisers initially used a custom or lookalike audience, but later deleted that audience. Because the data is missing, data fields for custom or lookalike audience use may read as False when they should have shown as True.

This impacted less than 15% of ads within the targeting dataset released in February 2021 and impacted less than 6% of all social issue, electoral or political ads created before November 1, 2021.

In the new dataset (May 2022), if an advertiser deleted a custom or lookalike audience associated with an ad before November 1, 2021, it is indicated by a value of True in the new `include_audience_data_missing` or `exclude_audience_data_missing` columns. If you are only looking at data in the new dataset, you can choose how to treat the data in your analysis based on those columns.

You can also use those new columns to help you interpret affected data in the February 2021 dataset. Here's how:

1. As in Issue #1, compare the two datasets, but this time, looking specifically at these columns:
    
    * `include_custom_audience`
    * `exclude_custom_audience`
    * `include_data_file_custom_audience`
    * `exclude_data_file_custom_audience`
    * `include_lookalike`
    * `exclude_lookalike`
2. If a field is True in the new dataset, then even if data is marked as missing, it doesn’t affect these columns (or there were other, non-deleted audiences that allowed us to calculate this information).
    
3. If there is a difference between the two datasets, and `include_audience_data_missing` or `exclude_audience_data_missing` is True for the respective columns, the difference could be due to an audience getting deleted in the original dataset.
    
    * For the `include_data_file_custom_audience`, `exclude_data_file_custom_audience`, `include_lookalike`, and `exclude_lookalike` columns, audience deletion is definitely the reason for the discrepancy.
    * For the `include_custom_audience` and `exclude_custom_audience` columns, the discrepancy might also be due to incorrect calculation (Issue #1).
4. If all custom audience columns are the same between datasets but either of the data missing columns have a True value, there was missing data in the original dataset.
    
5. You can filter your data on `include_audience_data_missing` and `exclude_audience_data_missing`.
    
6. In the `include_data_file_custom_audience`, `exclude_data_file_custom_audience`, `include_lookalike`, and `exclude_lookalike` columns, you can safely copy True values from the old dataset to the new dataset when there is data missing in the new dataset—those audiences were deleted between the release of the February 2021 dataset and the release of the May 2022 dataset. This is something you might do if you are transferring your research from the old dataset to the new, for example.
    

This example shows how you can use `join` to compare the old and new datasets:

old\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_library\_targeting")
# use the subset of old ads on which you were doing research
new\_targeting\_dataset = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020")
data = old\_targeting\_dataset.join(new\_targeting\_dataset.set\_index('archive\_id'), 'archive\_id', rsuffix='\_new')
data\[(data\['include\_audience\_data\_missing'\] == True) | (data\['exclude\_audience\_data\_missing'\] == True)\] # Get rows where there is missing data
data\[((data\['include\_custom\_audience'\] != data\['include\_custom\_audience\_new'\]) | (data\['include\_data\_file\_custom\_audience\_new'\] != data\['include\_data\_file\_custom\_audience'\]) | (data\['include\_lookalike'\] != data\['include\_lookalike\_new'\])) & (data\['include\_audience\_data\_missing'\] == True)\] # Find places where differences in include columns could be due to missing data

Transferring your research to the new dataset
---------------------------------------------

Here we present two examples of transferring your research from the original dataset to the new dataset.

To transfer to the new dataset for the exact set of ads visible in the February 2021 dataset:

data = execute("SELECT \* FROM fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020 WHERE archive\_id IN (SELECT archive\_id FROM fbri\_prod\_atp.ad\_library\_targeting)")

To do analysis on all ads in the new dataset from approximately the same timeframe as the original February 2021 dataset (to capture the ads with less than 100 impressions):

data = execute("SELECT b.\* FROM fbri\_prod\_atp.ad\_archive\_api AS a, fbri\_prod\_atp.ad\_targeting\_dataset\_siep\_aug\_2020 AS b WHERE a.ds = b.ds AND a.fbid = b.archive\_id AND (ad\_delivery\_start\_time BETWEEN 1596427200 AND 1604476800 OR ad\_delivery\_stop\_time BETWEEN 1596427200 AND 1604476800) AND reached\_countries LIKE '%US%'")

### Learn more

* [Table schema](https://developers.facebook.com/docs/fort-ads-targeting-dataset/table-schema)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)