Data deletion - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Data deletion
=============

Researcher Platform JupyterHub environment programmatically deletes all Meta Content Library API research output data and generated local files from JupyterHub environments every 30 days. This ensures that updates made to the visibility of content on Facebook or Instagram are carried over to Researcher Platform in accordance with Meta data deletion policies.

The data deletion is carried out during a 24-hour maintenance window the first day of every month beginning at 12:00 AM PST and ending at 11:59 PM PST on the same day, during which you cannot log in to your JupyterHub environment.

What is and is not deleted
--------------------------

The following forms of data are deleted:

* All output cells in notebook files
* All non-notebook files on researchers' persistent storage
* All S3 bucket files including uploads carried out from within the JupyterHub environment, asynchronous query output, and all query results

The following forms of data are *not* deleted:

* Notebook files (.ipyhb files)
* Notebook input cells (code and markdown)
* Graphics in notebook cells

The maintenance window
----------------------

The maintenance window, during which you will be unable to log into your JupyterHub environment, begins on the first day of every month at 12:00 AM PST. It lasts for 24 hours and ends at 11:59 PM PST on the same day.

When the maintenance window begins, this message is displayed in JupyterHub and remains until the window ends:

Managing your data to avoid research disruption
-----------------------------------------------

To minimize the disruption to your research, consider taking the following measures:

* Since your input query cells are not affected by the data deletion, you can plan to rerun your queries and regenerate new outputs every 30 days. The output will not match exactly what you had previously because it will not include any user data that no longer meets visibility requirements for Content Library API.
* You can plan ahead to accommodate the maintenance window each month, so you are not caught by surprise, unable to work.
* You can plan to perform analysis on query results before a maintenance window occurs. Although the raw data is affected by the data deletion, your code, figures, tables, graphs and statistics from your analyses are not.