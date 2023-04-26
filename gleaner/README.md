# NSDF

## Notes

There are 65 sourcs in the current config file generated from the 
sources listed at: https://nationalsciencedatafabric.org/catalog3d.html

Of these, 32 don't have obvious sitemaps in the default path.  This doesn't
mean they don't exist, some additional searching may find more in other 
locations.

This leaves 33 with resolvable ./sitemap.xml urls.

Note, I ignored AWS at this phase as it was too big for this simple
test.  It could be done later as the more scalable approach with 
a workflow system is available.  

Of those 33, 30 seems to have resources that can be indexed.  
Across those there are 176937 rsources, a first pass of indexing

Across those 30 I was able locate 163K resources expressed using JSON-LD

