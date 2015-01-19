# QBsistent: an *obvious consistency* checker for RDF Data Cubes using Linked Edit Rules

**QBsistent** is a tool built on top of the [Stardog](http://www.stardog.com/) graph database that:

1. ingests Linked Edit Rules published on the Web as Linked Data,
2. updates its reasoning engine with such rules, and
3. generates reasoning-based consistency reports on user generated queries over arbitrary RDF Data Cubes.

The generated reports flag any incosistent data points with respect to the rules using the [Open Annotation Data Model](http://www.openannotation.org/spec/core/) and [PROV](http://www.w3.org/TR/prov-primer/) W3C standards.

## Installation

QBsistent requires a separate install of Stardog, with a valid license. Community and developer licenses can be obtained for free at http://www.stardog.com

1. Unzip Stardog anywhere (`$STARDOG_HOME`) and copy the license file to `$STARDOG_HOME/bin/`
2. Make sure the Stardog server works: `./$STARDOG_HOME/bin/stardog-admin server start; ./$STARDOG_HOME/bin/stardog-admin server stop`
3. 


## Configuration

## Usage

`./QBsistent.py`

## Requirements

- R >= 3.0.2
- Python >= 2.7.6, with modules
  - 

