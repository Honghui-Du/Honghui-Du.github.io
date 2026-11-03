---
title: A unified reproducing kernel gradient smoothing Galerkin meshfree approach to strain gradient elasticity
collection: publications
category: manuscripts
layout: publication
permalink: /publication/strain-gradient/
detail_page: true
date: '2022-04-30'
publication_year: 2022
journal: Computational Mechanics
volume: '70'
pages: 73–100
doi: 10.1007/s00466-022-02156-z
paper_url: https://doi.org/10.1007/s00466-022-02156-z
authors: Honghui Du, Junchao Wu, Dongdong Wang, Jian Chen
author_list:
- Honghui Du
- Junchao Wu
- Dongdong Wang
- Jian Chen
excerpt: A unified gradient-smoothing formulation that enforces integration consistency for Galerkin meshfree strain-gradient elasticity with cubic and quartic bases.
description: A unified gradient-smoothing formulation that enforces integration consistency for Galerkin meshfree strain-gradient elasticity with cubic and quartic bases.
image: /images/unified_new.png
image_size: 350px
keywords:
- Strain gradient elasticity
- Reproducing kernel gradient smoothing
- Galerkin meshfree method
- Integration consistency
- High-order approximation
abstract: A unified reproducing kernel gradient smoothing formulation is presented for efficient Galerkin meshfree analysis of strain gradient elasticity problems with particular reference to high order basis functions, such as cubic and quartic basis functions. The integration constraint is elaborated for the Galerkin meshfree formulation of strain gradient elasticity, where the possible inconsistency issue associated with the separate first and second order gradient smoothing formalism is completely resolved. In this approach, the first order smoothed gradients of meshfree shape functions are expressed as a reproduced kernel form and the second order smoothed gradients are deduced from their first order counterparts through direct differentiation. Thereafter, the unknown coefficients in the first and second order smoothed gradients are simultaneously solved from the integration constraint. The resulting smoothed gradients automatically meet the integration consistency by construction.
  Subsequently, it is proven that the reproducing kernel gradient smoothing quadrature rules for the conventional elasticity problems are well suitable for the strain gradient elasticity problems. Numerical results clearly demonstrate the superior performance of the proposed approach regarding convergence, accuracy, as well as efficiency, in comparison with the Gauss integration-based meshfree formulation for strain gradient elasticity problems.
comments: false
share: false
bibtex_url: /files/citations/strain-gradient.bib
links:
- name: Paper
  url: https://doi.org/10.1007/s00466-022-02156-z
---

{% include publication-header.html %}

## Overview

Strain-gradient elasticity introduces an internal length scale and requires higher-order spatial derivatives. This paper addresses a numerical difficulty in its meshfree discretization: constructing first- and second-order smoothed gradients separately can violate the integration constraint. A unified construction links both gradient orders through shared coefficients.

## Abstract

{{ page.abstract }}

## Method and contributions

The first-order smoothed gradients are represented in a reproducing-kernel form. Differentiating that representation gives the second-order gradients, so both orders share the unknown coefficients. Enforcing the coupled integration constraint determines these coefficients. The paper develops efficient quadrature rules for high-order meshfree approximations, including quartic bases.

- A unified integration-consistency condition and shared-coefficient gradient construction resolve the inconsistency that can arise from separate smoothing of first- and second-order derivatives.

- Efficient reproducing-kernel gradient-smoothing quadrature supports multidimensional strain-gradient elasticity with cubic and quartic basis functions.

## Results

- Patch tests expose the consistency issue in separate smoothing and assess the proposed unified formulation.

- One-, two-, and three-dimensional numerical examples compare accuracy and convergence with Gauss-integration-based meshfree formulations.

- The hollow-cylinder benchmark examines solution and derivative errors under refinement. The quartic formulation achieves the expected high-order convergence behavior in the reported study.

<figure class="publication-result">
  <a href="{{ '/images/publications/strain-gradient-result.png' | relative_url }}"><img src="{{ '/images/publications/strain-gradient-result.png' | relative_url }}" alt="Two-dimensional hollow-cylinder benchmark with a quartic meshfree basis. The panels compare L², H¹, and H² errors under refinement for reproducing-kernel gradient smoothing integration and Gauss integration. The comparison evaluates solution and derivative convergence. Source: Fig. 21 of the published paper." loading="lazy"></a>
  <figcaption>Two-dimensional hollow-cylinder benchmark with a quartic meshfree basis. The panels compare L², H¹, and H² errors under refinement for reproducing-kernel gradient smoothing integration and Gauss integration. The comparison evaluates solution and derivative convergence. Source: Fig. 21 of the published paper.</figcaption>
</figure>

## Scope and limitations

The formulation and validation concern strain-gradient elasticity and the basis and quadrature constructions developed in the paper. They do not establish performance for nonlinear plasticity, fracture, or arbitrary higher-order continuum models.

## Resources and reproduction

The journal article contains the formulation, quadrature construction, and numerical settings. A public code repository or open-access full-text copy has not been verified for this study; use the DOI link for the publisher access options.

## Research questions

### Why unify the smoothing of first and second derivatives?

Constructing first- and second-order smoothed gradients separately can violate the integration-consistency requirement for strain-gradient elasticity. The proposed construction links both derivative orders through shared coefficients and a unified consistency condition. See the formulation and patch tests in the journal article.

### How is accuracy assessed for the higher-order formulation?

The paper uses patch tests and one-, two-, and three-dimensional examples to compare the meshfree formulation with Gauss-integration-based alternatives. The hollow-cylinder example reports solution and derivative errors under refinement, including L², H¹, and H² errors for a quartic basis. See Fig. 21; these are accuracy and convergence results, not runtime measurements.

## Citation

Honghui Du; Junchao Wu; Dongdong Wang; Jian Chen (2022). A unified reproducing kernel gradient smoothing Galerkin meshfree approach to strain gradient elasticity. *Computational Mechanics*, 70, 73–100. [DOI: 10.1007/s00466-022-02156-z](https://doi.org/10.1007/s00466-022-02156-z).

[Download BibTeX]({{ page.bibtex_url | relative_url }})

{% raw %}
```bibtex
@article{du2022straingradient,
  title = {{A unified reproducing kernel gradient smoothing Galerkin meshfree approach to strain gradient elasticity}},
  author = {Du, Honghui and Wu, Junchao and Wang, Dongdong and Chen, Jian},
  journal = {Computational Mechanics},
  volume = {70},
  pages = {73--100},
  year = {2022},
  doi = {10.1007/s00466-022-02156-z},
  url = {https://doi.org/10.1007/s00466-022-02156-z}
}
```
{% endraw %}

[Back to all publications]({{ '/publications/' | relative_url }})
