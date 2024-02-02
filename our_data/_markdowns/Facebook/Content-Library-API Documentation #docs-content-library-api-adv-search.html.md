Advanced search - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Advanced search guidelines
==========================

Meta Content Library and API have a search functionality that supports AND, OR, and NOT operators. Query strings are passed as the `q` parameter as in this example (select the tab for the language of your choice):

RPython
```
response <- client$search_posts(q=“dogs | cats & pets”)
```
```
response = client.search_posts(q=“dogs | cats & pets”)
```
General rules
-------------

The following general rules apply to forming queries:

* The following operators are supported: AND, OR, NOT.
* Use an ampersand character (&) or a blank space to indicate AND.
* Use a pipe character ( | ) to indicate OR.
* Use a hyphen character (-) to indicate NOT. The en-dash and em-dash characters are *not* interpreted as substitutes for hyphen and are treated instead as keywords.
* For queries with multiple operators, NOT clauses are processed first, followed by AND, followed by OR. Imagine the terms grouped as if with parentheses.
* For clauses of equal precedence, there is a default left-to-right processing order.
* Grouping using parentheses is supported. Grouping can be used to modify the default processing order.
* You can use single-word keywords only (not phrases).
* Wild cards are not supported.
* Extra spaces around operators are ignored, so you can have them or not.

Because they have special meaning in the context of query syntax, the following characters cannot be used as keywords or embedded in keywords:

* & ampersand
* | pipe
* ‐ hyphen
* space
* ( open parenthesis
* ) close parenthesis

Using operators
---------------

The examples included here demonstrate the basic use of the AND, OR, and NOT operators.

 Search objective | How to write it | Examples || Find matches that include all of the provided search terms. | Use the AND operator expressed as an ampersand character (&) or a blank space. | cat&dog&allergy
cat dog allergy
cat&dog allergy
cat dog&allergy
Each match contains all three terms: “cat”, “dog”, and “allergy”. |
| Find matches that include at least one of the provided search terms. | Use the OR operator expressed as a pipe character (|). | cat | dog
cat|dog
cat |dog
cat| dog
Each match contains “cat” or “dog”, and could contain both. |
| Find matches that include the provided search term, excluding a second term. | Use the NOT operator expressed as a hyphen character (-). | dog -puppy
dog-puppy
dog- puppy
dog - puppy
Each match contains “dog” but not “puppy”. Results containing both “dog” and “puppy” are excluded. |
Multiple operators
------------------

When multiple operators are included in a single query string, the operators are processed (parsed) in a specific order: NOT first, followed by AND, followed by OR. This is important to understand because it means the order in which you place the operators in your query might be different from the order in which they are parsed, which might or might not affect the results.

The examples in this section demonstrate the use of multiple operators in a single query.

 Search objective | How to write it | Examples || Find matches that include both of two search terms (AND clause), as well as matches that include a third term (OR clause). | Use both an AND clause and an OR clause. The AND clause is parsed first. | lemon lime | grapefruit
grapefruit | lemon lime
Results include matches containing both “lemon” and “lime”, plus those containing “grapefruit”. |
| Find:1. Matches that contain one search term, excluding those containing a second term, and
2. Matches that contain a third term
**Note**: Some matches might meet both criteria 1 and 2, but to be included in the query results, the only requirement is to match at least one. | Use both a NOT clause and an OR clause. The NOT clause is parsed first. | fuyu | persimmon - astringent
persimmon - astringent | fuyu
Results include:1. Matches containing “persimmon” but not “astringent” (imagine persimmon - astringent grouped as if in parentheses), and
2. Matches containing “fuyu”
Some matches might contain “persimmon” but not “astringent” and also contain “fuyu” (matching both 1 and 2 above), but this is not a requirement to be included in the query results.
**Note**: If you actually want to exclude “astringent” from “fuyu” as well, you could achieve that using grouping, a technique for customizing the order of precedence. See the next section on Grouping. |
Grouping
--------

You can use grouping with parentheses to influence the order in which clauses are parsed. Clauses enclosed in parentheses are parsed first, followed by operators outside of parentheses.

The examples shown here demonstrate how this works.

 Search objective | How to write it | Examples || Find matches that contain at least one of two search terms, excluding those that also contain a third term. | Use an OR clause enclosed in parentheses to ensure it is parsed first, followed by a NOT clause. Without the parentheses, the NOT clause would be parsed first. | (fuyu | persimmon) - astringent
Results include matches containing either “fuyu” or “persimmon” (or both), but exclude those that also contain “astringent”. |
| Find matches that contain both of two search terms or at least one of two other search terms. Exclude from that list all results that also contain a fifth search term. | Use an AND clause in parentheses, and an OR clause in parentheses. Separate the two parenthetical clauses by an OR operator. Group those two groupings together. Finally, add the NOT clause.
The extra grouping ensures that "outlaw" is not excluded only from the (newman | redford) results, but also from the (action movie) results. | ((action movie) | (newman | redford)) - outlaw
Results:* Include matches containing both “action” and “movie”
* Include matches containing either “newman” or “redford” (can contain both)
* Exclude matches that also contain “outlaw”
 |
Right-to-left languages
-----------------------

A few notes about queries when applied to languages that are read right to left:

* Query logic for right-to-left languages is parsed right to left
* The parsing order (NOT followed by AND followed by OR) is maintained
* Grouping is not supported for right-to-left languages