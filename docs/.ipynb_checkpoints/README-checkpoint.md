# More Details


There are 65 sources in the current Glaner config file generated from the sources listed at: https://nationalsciencedatafabric.org/catalog3d.html

Of these, 32 don't have obvious sitemaps in the default path.  This doesn't mean they don't exist, some additional searching may find more in other locations.

This leaves 33 with resolvable ./sitemap.xml urls.

Note, I ignored AWS at this phase as it was too big for this simple test.  It could be done later as the more scalable approach with a workflow system is available.

Of those 33, 30 seems to have resources that can be indexed. Across those there are 176937 resources.

A first pass of indexing across those 30 I was able to locate 163K resources expressed using JSON-LD.




This is just a tiny fraction of the resources that make up the NSDF-Catalog. The goal of this work is look at how
to connect the catalog to the more detailed KG graphs.
