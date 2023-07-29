# More Details

## About

There are 65 sources in the current Gleaner config file generated 
from the sources listed at: https://nationalsciencedatafabric.org/catalog3d.html

Of these, 32 don't have obvious sitemaps in the default path.  
This doesn't mean they don't exist, some additional searching may 
find more in other locations.

This leaves 33 with resolvable ./sitemap.xml urls.

Note, I ignored AWS at this phase as it was too big for this simple test.  
It could be done later as the more scalable approach 
with a workflow system is available.

Of those 33, 30 seems to have resources that can be indexed. 
Across those there are 176937 resources.

A first pass of indexing across those 30 I was able to locate 163K resources 
expressed using JSON-LD.

This is just a tiny fraction of the resources that make up the NSDF-Catalog. 
The goal of this work is look at how to connect the catalog to 
the more detailed KG graphs.


## Connections

### About

Leveraging the parquet files and duckdb it will be interesting to see 
how we might have existing connections between the NSDF Catalog and
the graph files in [the graphs directory](../graphs/README.md).

The first goal will be to simply see if we can make connections between the
exposed schema.org metadata by the providers and the catalog.

## References
* [FDO Specifications](https://fairdo.org/specifications/)
* [RDA Kernel](https://zenodo.org/record/8009739)
* [A Photovoltaic System Model Integrating FAIR Digital Objects and Ontologies](https://www.mdpi.com/1996-1073/16/3/1444)
* https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=933889
* [Data Type Model and Registry - Data Type Registries (DTR) WG Recommendations](https://www.rd-alliance.org/group/data-type-registries-wg/outcomes/data-type-registries)
* [Implementation of Attributes, Types, Profiles and Registries](https://zenodo.org/record/7825573)
* [Typing FAIR Digital Objects](https://zenodo.org/record/7825599)

