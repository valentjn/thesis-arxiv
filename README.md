Source Code of Julian Valentin's PhD Thesis (arXiv version)
===========================================================

[![CI](https://github.com/valentjn/thesis-arxiv/workflows/CI/badge.svg?branch=develop)](https://github.com/valentjn/thesis-arxiv/actions?query=workflow%3ACI+branch%3Adevelop)
[![PDF download](https://img.shields.io/badge/PDF%20download-arXiv-darkred)][arxiv]
[![CC BY-SA 4.0 license](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue)][license]

This is the source code of the [arXiv version][arxiv] of the PhD thesis of Julian Valentin.

The thesis is titled **B-Splines for Sparse Grids: Algorithms and Application to Higher-Dimensional Optimization**. It was submitted to the University of Stuttgart, Germany, and it was successfully defended on April 2, 2019.

The code is provided here as is, without any further support or warranty. The thesis is Copyright © 2019 Julian Valentin. It is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)][license].

Download
--------

The resulting PDF can be downloaded at [arXiv][arxiv] or on the [GitHub Releases page](https://github.com/valentjn/thesis-arxiv/releases).

How to Cite
-----------

This section applies if you want to cite the thesis in a scientific paper, in a blog, or in any other kind of publication.

Cite the thesis as follows:

> Julian Valentin: B-Splines for Sparse Grids: Algorithms and Application to Higher-Dimensional Optimization. PhD thesis, University of Stuttgart, Germany, 2019. Available at `arXiv:1910.05379 [math.NA]`. DOI: `10.18419/opus-10504`.

```biblatex
@phdthesis{Valentin2019,
  author      = {Valentin, Julian},
  title       = {B-Splines for Sparse Grids: Algorithms and Application to Higher-Dimensional Optimization},
  institution = {University of Stuttgart, Germany},
  year        = {2019},
  eprint      = {1910.05379},
  eprinttype  = {arxiv},
  eprintclass = {math.NA},
  doi         = {10.18419/opus-10504}
}
```

How to Attribute
----------------

This section applies if you want to share the thesis, even in modified form (“Adapted Material” in terms of the license). Examples include:

* Distribution of the source code or compiled PDFs.
* Distribution of an excerpt, e.g., a figure.
* Distribution of printouts, e.g., as books.
* Translation into other languages.
* Compilation of the source code to different formats, e.g., to PDF via pdfL<sup>A</sup>T<sub>E</sub>X.

This applies to source code and compiled documents (e.g., PDF), as a whole and to parts thereof such as text, figures, tables, other components, or source code snippets.

Per the [license][license], you must at least do the following:

* Attribute the author and reproduce the copyright notice: Copyright © 2019 Julian Valentin
* Link to the license: [licensed under CC BY-SA 4.0][license]
* Link to the thesis: [https://arxiv.org/abs/1910.05379][arxiv]
* List modifications, if any

Modified versions must be licensed under the CC BY-SA 4.0 license as well (share alike), or a compatible license.

Versions and Changes
--------------------

The arXiv version `arxiv-v1` slightly differs from the originally submitted version `published-v1`:

* Some typos have been fixed.
* The LuaL<sup>A</sup>T<sub>E</sub>X code has been converted to pdfL<sup>A</sup>T<sub>E</sub>X, as LuaL<sup>A</sup>T<sub>E</sub>X is not supported by arXiv. As a result, some word breaks and the indentation of some paragraphs differ.
* No changes regarding the actual content have been made.

Check the back of the title page if you want to identify the version of your specific PDF. The originally submitted version can be obtained from the library of the University of Stuttgart (DOI: `10.18419/opus-10504`).

[arxiv]: https://arxiv.org/abs/1910.05379
[license]: https://creativecommons.org/licenses/by-sa/4.0/
