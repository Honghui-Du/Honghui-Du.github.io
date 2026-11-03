---
title: Differentiable neural-integrated meshfree method for forward and inverse modeling of finite strain hyperelasticity
collection: publications
category: manuscripts
layout: publication
permalink: /publication/nim-hyperelasticity/
detail_page: true
date: '2024-12-24'
publication_year: 2025
journal: Engineering with Computers
volume: '41'
pages: 1597–1617
doi: 10.1007/s00366-024-02090-z
paper_url: https://doi.org/10.1007/s00366-024-02090-z
authors: Honghui Du, Binyao Guo, QiZhi He
author_list:
- Honghui Du
- Binyao Guo
- QiZhi He
excerpt: A differentiable meshfree formulation for finite-strain hyperelasticity and identification of heterogeneous elastic modulus fields from strain observations.
description: A differentiable meshfree formulation for finite-strain hyperelasticity and identification of heterogeneous elastic modulus fields from strain observations.
image: /images/ewc.png
image_size: 350px
keywords:
- Finite-strain hyperelasticity
- Inverse material identification
- Differentiable meshfree simulation
- NeuroPU
- JAX
abstract: The present study aims to extend the novel physics-informed machine learning approach, specifically the neural-integrated meshfree (NIM) method, to model finite-strain problems characterized by nonlinear elasticity and large deformations. To this end, the hyperelastic material models are integrated into the loss function of the NIM method by employing a consistent local variational formulation. Thanks to the inherent differentiable programming capabilities, NIM can circumvent the need for derivation of Newton–Raphson linearization of the variational form and the resulting tangent stiffness matrix, which are typically required in traditional numerical methods. Additionally, NIM utilizes a hybrid neural-numerical approximation encoded with partition-of-unity basis functions, coined NeuroPU, to effectively represent the displacement solution and streamline the model training process. NeuroPU can also be used for approximating the unknown material fields, enabling NIM a unified framework
  for both forward and inverse modeling. For the imposition of displacement boundary conditions, this study introduces a new approach based on singular kernel functions into the NeuroPU approximation, leveraging its unique feature that allows for customized basis functions. Numerical experiments demonstrate the NIM method’s capability in forward hyperelasticity modeling, achieving desirable accuracy, with errors among 10⁻³ to 10⁻⁵ in the relative L² norm, comparable to the well-established finite element solvers. Furthermore, NIM is applied to address the complex task of identifying heterogeneous mechanical properties of hyperelastic materials from strain data, validating its effectiveness in the inverse modeling of nonlinear materials. To leverage GPU acceleration, NIM is fully implemented on the JAX deep learning framework in this study, utilizing the accelerator-oriented array computation capabilities offered by JAX.
comments: false
share: false
bibtex_url: /files/citations/nim-hyperelasticity.bib
code: https://github.com/IntelligentMechanicsLab/NIM-Tutorial
preprint: https://arxiv.org/abs/2407.11183
preprint_pdf: https://arxiv.org/pdf/2407.11183
links:
- name: Paper
  url: https://doi.org/10.1007/s00366-024-02090-z
- name: Code
  url: https://github.com/IntelligentMechanicsLab/NIM-Tutorial
---

{% include publication-header.html %}

## Overview

This study asks how one differentiable framework can predict large elastic deformations and identify spatially varying material properties from strain data. It extends NIM to finite-strain hyperelasticity and uses NeuroPU to represent both the displacement solution and unknown material fields.

## Abstract

{{ page.abstract }}

## Method and contributions

Hyperelastic constitutive relations enter a consistent local variational residual. Optimization of this residual avoids the explicit derivation of a Newton–Raphson tangent stiffness matrix for the NIM solve. A boundary singular-kernel construction enforces prescribed displacements within the NeuroPU approximation. The implementation uses JAX for automatic differentiation and accelerator-oriented computation.

- A finite-strain extension of the local variational NIM formulation supports nonlinear hyperelastic forward analysis within a differentiable computation graph.

- The same NeuroPU representation is used for unknown material fields, allowing joint displacement and material identification from strain observations. Boundary singular kernels provide a compatible displacement-constraint treatment.

## Results

- Uniaxial tension, a two-dimensional plate, and a large-deflection cantilever test forward predictions against reference solutions.

- Inverse examples recover heterogeneous elastic modulus fields, including a Gaussian-random-field case, using strain observations and the governing equations.

- Figures 21 and 22 compare estimated modulus fields with ground truth and show that a finer approximation space improves recovery of the more complex field.

<figure class="publication-result">
  <a href="{{ '/images/publications/nim-hyperelasticity-result.png' | relative_url }}"><img src="{{ '/images/publications/nim-hyperelasticity-result.png' | relative_url }}" alt="Inverse material identification for a Gaussian-random-field elastic modulus: (a) the NIM estimate, (b) the ground truth, and (c) the pointwise absolute error. The modulus is inferred through the inverse formulation using strain observations. Source: Fig. 21 of the published paper; the finer-resolution comparison appears in Fig. 22." loading="lazy"></a>
  <figcaption>Inverse material identification for a Gaussian-random-field elastic modulus: (a) the NIM estimate, (b) the ground truth, and (c) the pointwise absolute error. The modulus is inferred through the inverse formulation using strain observations. Source: Fig. 21 of the published paper; the finer-resolution comparison appears in Fig. 22.</figcaption>
</figure>

## Scope and limitations

The demonstrated material models are hyperelastic. The results do not by themselves validate plasticity, damage, or other history-dependent constitutive behavior. Forward errors and inverse reconstruction quality depend on the benchmark, discretization, and observations; more complex material fields require sufficient approximation resolution.

## Resources and reproduction

The public repository includes one-dimensional hyperelasticity tutorials for the NIM/c and NIM/h variants. These illustrate the formulation, but do not constitute a complete reproduction package for all two-dimensional inverse examples. The [original NIM paper](/publication/nim/) introduces the hybrid approximation and solver framework.

## Citation

Honghui Du; Binyao Guo; QiZhi He (2025). Differentiable neural-integrated meshfree method for forward and inverse modeling of finite strain hyperelasticity. *Engineering with Computers*, 41, 1597–1617. [DOI: 10.1007/s00366-024-02090-z](https://doi.org/10.1007/s00366-024-02090-z).

[Download BibTeX]({{ page.bibtex_url | relative_url }})

{% raw %}
```bibtex
@article{du2025nimhyperelasticity,
  title = {{Differentiable neural-integrated meshfree method for forward and inverse modeling of finite strain hyperelasticity}},
  author = {Du, Honghui and Guo, Binyao and He, QiZhi},
  journal = {Engineering with Computers},
  volume = {41},
  pages = {1597--1617},
  year = {2025},
  doi = {10.1007/s00366-024-02090-z},
  url = {https://doi.org/10.1007/s00366-024-02090-z}
}
```
{% endraw %}

[Back to all publications]({{ '/publications/' | relative_url }})
