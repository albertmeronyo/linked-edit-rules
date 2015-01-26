# QBsistent: an *obvious consistency* checker for RDF Data Cubes using Linked Edit Rules

**QBsistent** is a tool built on top of the [Stardog](http://www.stardog.com/) graph database that:

1. ingests Linked Edit Rules published on the Web as Linked Data,
2. updates its reasoning engine with such rules, and
3. generates reasoning-based consistency reports on user generated queries over arbitrary RDF Data Cubes.

The generated reports flag any incosistent data points with respect to the rules using the [Open Annotation Data Model](http://www.openannotation.org/spec/core/) and [PROV](http://www.w3.org/TR/prov-primer/) W3C standards.

## Installation

QBsistent requires a separate install of Stardog, with a valid license. Community and developer licenses can be obtained for free at http://www.stardog.com

QBsistent also requires the Java/R Interface (JRI) to execute Linked Macro-Edits. If you plan to use Linked-Macro Edits, please follow the instructions to install JRI at http://rforge.net/JRI/ (quick howto: execute `install.packages("rJava")` in your R environment).

1. Unzip Stardog anywhere (`$STARDOG_HOME`) and copy the license file to `$STARDOG_HOME/bin/`
2. Make sure the Stardog server works: `./$STARDOG_HOME/bin/stardog-admin server start; ./$STARDOG_HOME/bin/stardog-admin server stop`
3. If you plan to use Linked Macro-Edits, and hence the [Stardog-R integration extension](https://github.com/albertmeronyo/stardog-r), you need to add the following lines to the script `$STARDOG_HOME/bin/stardog-admin`:
   3.1. Make Stardog aware of where your R install lives: `export R_HOME="/usr/lib/R"` (Linux), or `export R_HOME="/Library/Frameworks/R.framework/Resources"` (MacOS X)
   3.2. Make Stardog aware of where your JRI shared libraries live. This can be achieved in [many ways](http://www.chilkatsoft.com/java-loadLibrary-MacOSX.asp). Recommended: in Linux, modify the LD_LIBRARY_PATH environment variable (add `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/R/site-library/rJava/jri` using your valid JRI path to `$STARDOG_HOME/bin/stardog-admin`; in MacOS X, it's easier to symlink the library `libjri.so` in your Java library path (you can get your Java library path by `System.out.println(System.getProperty("java.library.path"));`).
4. Install Python's SPARQLWrapper module: `pip install SPARQLWrapper`

## Configuration

A file `../config.ini` (note the parent directory) contains all parameters that will be used by QBsistent at execution time:

- Section *general*
  - **qb_sparql_endopint**: URI of the SPARQL endpoint with the RDF Data Cube to be checked
  - **ler_sparql_endpoint**: URI of the SPARQL endpoint with the Linked Edit Rules to be used
  - **qb_query**: SPARQL query with matching RDF Data Cube data to be checked (e.g. all QB observations, observations meeting certain criteria, etc.)
  - **ler_query**: SPARQL query with matching Linked Edit Rules to be used (e.g. rules only concerning particular dimensions, like age or sex; all rules available in the endpoint; etc.)
  - **sl_query**: SPARQL query to be used in SL reasoning mode. This query is used to generate PROV and OA metadata. Modify its value at your own risk.
  - **report_query**: SPARQL query to be used to return the consistency output to the user. The default value will CONSTRUCT a PROV/OA graph with all inconsistencies found, but less verbose alternatives (e.g. SPARQL select just the URIs of inconsistent observations) are also possible
- Section *io*
  - **data_path**: Path to store retrieved QB/LER data temporarily
  - **rule_file**: File to store retrieved LER data temporariliy
  - **qb_file**: File to store retrieved QB data temporarily
- Section *debug*
  - **verbose**: Be verbose
- Section *Stardog*
  - **home_stardog**: Path where your Stardog installation lives
  - **db_name**: Database name to be used in Stardog

## Usage

`./QBsistent.py`

All parameters will be read from your `../config.ini`

## Requirements

- R >= 3.0.2
- JRI >= 0.5-5
- Python >= 2.7.6, with modules
  - SPARQLWrapper >= 1.5.2

