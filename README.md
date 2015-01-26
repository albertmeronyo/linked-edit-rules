<center><img src="http://lod.cedar-project.nl/linked-edit-rules/img/LER-logo-web.png" style="max-width:50%"></a></center>

Copyright © 2014, 2015 Albert Meroño Peñuela, DANS / VU University Amsterdam

Linked Edit Rules: a methodology to publish, link, combine and execute edit rules on the Web as Linked Data to verify consistency of statistical datasets.

See http://www.linkededitrules.org/

## Linked Edit What?

Statistical offices have many procedures to make sure that statistical datasets they release are in good shape. One of such procedures are **edit rules**. Edit rules check automatically the consistency of a dataset. For instance, some are written to detect records with forbidden values (e.g. *age* can never be negative), while others are written to detect odd data behaviour (e.g. *height* should follow a normal distribution). These rules are rarely released to the public, which makes re-executing them out of the statistical office difficult. But even if they are, it's complicated to retrieve them and adapt them to each specific statistical dataset.

With this effort we make edit rules available as Linked Data, and we call them **Linked Edit Rules** (LER). This means that any edit rule can be published in RDF on the Web as a LER, de-referenced and potentially used to check consistency of any data explicitly constrained by the edit rule. We showcase this with *QBsistent*, a demo that shows how these Linked Edit Rules can be used to customize a reasoning engine (Stardog) and check the consistency of arbitrary data in RDF Data Cube.

More details are avaialable at http://www.linkededitrules.org

On this repository:

## Data

Directory: `data`

Contains the following:

- [Examples of edit rules](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/edits.txt) as used by statistical offices
- A conversion of the [example edit rules as Linked Edit Rules](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/people-rules.ttl)
- [Examples of statistical data](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/people.csv) where these edit rules can be tested
- A conversion of these [examples to RDF Data Cube](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/people.ttl), the Linked Data vocabulary for statistical data
- [Macro-edits](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/people-macro.ttl) (i.e. rules that checks statistical properties over all dataset records) as Linked Edit Rules
- [Randomly generated synthetic data](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/test.ttl) with *QBrand* to be checked using LER
- [Census domain Linked Edit Rules](https://raw.githubusercontent.com/albertmeronyo/linked-edit-rules/master/data/cedar-rules.ttl), of constraints that general census data have to fulfill

## Source

Directory: `src`

Contains the implementation of:

- [**QBsistent**](https://github.com/albertmeronyo/linked-edit-rules/tree/master/src): an automatic consistency checker of statistical datasets using Linked Edit Rules, built on top of [Stardog](http://www.stardog.com)
- **QBrand**: an automatic generator of artificial RDF Data Cubes with intentional errors (to be found using LER)

## Vocabulary

Directory: `vocab`

Contains the RDF description of the vocabulary terms used by Linked Edit Rules.
