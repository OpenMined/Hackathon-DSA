
Updates and differences in the datasets - Ad Targeting dataset - Documentation - Meta for Developers










Ad Targeting dataset* Overview
* Get started
* Sample queries
* Table schema
* Support
Updates and differences in the datasets
=======================================


The Ad Targeting February 2021 dataset consists of targeting data on social issue, electoral, and political ads from August 3 - November 1, 2020 (U.S. data only).


The Ad Targeting May 2022 dataset consists of targeting data on social issue, electoral, and political ads beginning August 3, 2020 through the present. The May 2022 dataset includes ads from all countries in which we currently have our ad authorizations and disclaimer tools available.


Both datasets include data from August 3 - November 1, 2020.


Understanding the differences between the two datasets
------------------------------------------------------


Since you might be using one or both datasets in your research, and since you might want to transfer your research from the old dataset to the new one, it is important to understand the differences:




 Feature | February 2021 dataset | May 2022 dataset || Table name | `ad_targeting_dataset` | `ad_targeting_dataset_siep_aug_2020`
There are three additional columns in this table: `exclude_audience_data_missing`, 
`include_audience_data_missing`, and `language`.
See Table schema for details. |
| Coverage area | USA data only. | All countries in which we currently have our ad authorizations and disclaimer tools available.
 More information about the countries this includes is available here. |
| Minimum number of impressions for the ad to be included | 100 | 1 |
| Ongoing data collected and published | No | Yes
On the 1st of each month beginning June 2022, an update to the table is published so that it includes all data through the 21st of the previous month. A delta table is also published, listing ads that were reclassified as non-political (and therefore removed) since the previous publication. |
| Indicates where custom audience data is known to be missing.
See How to manage issues found in the datasets for more information. | No | Yes
`include_audience_data_missing` and `exclude_audience_data_missing` columns are new in this dataset.
 |
| Preserves custom audience information for audiences that were removed.
See How to manage issues found in the datasets for more information. | No | Yes, after November 1, 2021. |

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


* Issue #1: incorrect calculations
* Issue #2: deleted custom audiences


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



```

old_targeting_dataset = execute("SELECT * FROM fbri_prod_atp.ad_library_targeting")
new_targeting_dataset = execute("SELECT * FROM fbri_prod_atp.ad_targeting_dataset_siep_aug_2020")
data = old_targeting_dataset.join(new_targeting_dataset.set_index('archive_id'), 'archive_id', rsuffix='_new')

data[(data['include_custom_audience'] != data['include_custom_audience_new'])] # Checking the new data against the old data

data[(data['include_custom_audience'] != data['include_custom_audience_new']) and (data['include_audience_data_missing'] == False)] # Checking the new data against the old data where there are no instances of missing data
          
          


```
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



```

old_targeting_dataset = execute("SELECT * FROM fbri_prod_atp.ad_library_targeting")
# use the subset of old ads on which you were doing research
new_targeting_dataset = execute("SELECT * FROM fbri_prod_atp.ad_targeting_dataset_siep_aug_2020")
data = old_targeting_dataset.join(new_targeting_dataset.set_index('archive_id'), 'archive_id', rsuffix='_new')
data[(data['include_audience_data_missing'] == True) | (data['exclude_audience_data_missing'] == True)] # Get rows where there is missing data
data[((data['include_custom_audience'] != data['include_custom_audience_new']) | (data['include_data_file_custom_audience_new'] != data['include_data_file_custom_audience']) | (data['include_lookalike'] != data['include_lookalike_new'])) & (data['include_audience_data_missing'] == True)] # Find places where differences in include columns could be due to missing data


```
Transferring your research to the new dataset
---------------------------------------------


Here we present two examples of transferring your research from the original dataset to the new dataset.


To transfer to the new dataset for the exact set of ads visible in the February 2021 dataset:



```

data = execute("SELECT * FROM fbri_prod_atp.ad_targeting_dataset_siep_aug_2020 WHERE archive_id IN (SELECT archive_id FROM fbri_prod_atp.ad_library_targeting)")

```
To do analysis on all ads in the new dataset from approximately the same timeframe as the original February 2021 dataset (to capture the ads with less than 100 impressions):



```

data = execute("SELECT b.* FROM fbri_prod_atp.ad_archive_api AS a, fbri_prod_atp.ad_targeting_dataset_siep_aug_2020 AS b WHERE a.ds = b.ds AND a.fbid = b.archive_id AND (ad_delivery_start_time BETWEEN 1596427200 AND 1604476800 OR ad_delivery_stop_time BETWEEN 1596427200 AND 1604476800) AND reached_countries LIKE '%US%'")

```
### Learn more


* Table schema






































 
