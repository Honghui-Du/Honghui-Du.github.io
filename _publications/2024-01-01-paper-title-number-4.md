---
title: 'Neural-Integrated Meshfree (NIM) Method: A differentiable programming-based hybrid solver for computational mechanics'
collection: publications
category: manuscripts
layout: publication
permalink: /publication/nim/
detail_page: true
date: '2024-05-03'
publication_year: 2024
journal: Computer Methods in Applied Mechanics and Engineering
volume: '427'
pages: '117024'
doi: 10.1016/j.cma.2024.117024
paper_url: https://doi.org/10.1016/j.cma.2024.117024
authors: Honghui Du, QiZhi He
author_list:
- Honghui Du
- QiZhi He
excerpt: A hybrid neural–meshfree approximation and local variational solver for computational mechanics, combining partition-of-unity basis functions with neural networks.
description: A hybrid neural–meshfree approximation and local variational solver for computational mechanics, combining partition-of-unity basis functions with neural networks.
image: /images/cmame.png
image_size: 350px
keywords:
- Neural-Integrated Meshfree method
- NeuroPU
- Physics-informed machine learning
- Local variational formulation
- Computational mechanics
abstract: 'While deep learning and data-driven modeling approaches based on deep neural networks (DNNs) have recently attracted increasing attention for solving partial differential equations, their practical applications to real-world scientific and engineering problems remain limited due to the relatively low accuracy and high computational costs. In this study, we present a differentiable programming-based hybrid meshfree approach within the field of computational mechanics. This approach seamlessly integrates neural network-based deep learning architectures with physics-based meshfree discretization techniques, thus referred to as the neural-integrated meshfree (NIM) method. To effectively approximate the solution, NIM employs a hybrid scheme called NeuroPU approximation, which combines continuous DNN representations with partition of unity (PU) basis functions associated with the underlying spatial discretization. This neural-numerical hybridization not only enhances the solution representation
  through functional space decomposition but also reduces both the size of DNN model and the need of automatic differentiation for spatial gradient computations, leading to a significant improvement in training efficiency. Under the NIM framework, we propose two truly meshfree solvers: the strong form-based NIM (S-NIM) and the local variational form-based NIM (V-NIM). In the S-NIM solver, the strong-form governing equation is directly considered in the loss function, while the V-NIM solver employs a local Petrov–Galerkin approach that allows the construction of variational residuals based on arbitrary overlapping subdomains. This ensures both the satisfaction of underlying physics and the preservation of the meshfree property. We perform extensive numerical experiments on both stationary and transient benchmark problems to assess the effectiveness of the proposed NIM methods in terms of accuracy, scalability, generalizability, and convergence properties. Moreover, comparative analysis with
  other physics-informed machine learning methods demonstrates that NIM, especially V-NIM, significantly enhances both accuracy and efficiency in end-to-end predictive capabilities.'
comments: false
share: false
bibtex_url: /files/citations/nim.bib
code: https://github.com/IntelligentMechanicsLab/NIM-Tutorial
preprint: https://arxiv.org/abs/2311.12915
preprint_pdf: https://arxiv.org/pdf/2311.12915
links:
- name: Paper
  url: https://doi.org/10.1016/j.cma.2024.117024
- name: Code
  url: https://github.com/IntelligentMechanicsLab/NIM-Tutorial
---

{% include publication-header.html %}

## Overview

How can physics-informed learning use the approximation structure of numerical methods? NIM combines neural networks with local meshfree basis functions through the NeuroPU approximation. The resulting representation is used in strong-form and local variational solvers, with applications to boundary-value problems, parameterized solution surrogates, and time-dependent PDEs.

## Abstract

{{ page.abstract }}

## Method and contributions

NeuroPU combines neural network outputs with partition-of-unity basis functions. Spatial differentiation can therefore use derivatives of the meshfree basis functions. S-NIM minimizes strong-form residuals; V-NIM instead minimizes local Petrov–Galerkin residuals over overlapping subdomains. The paper studies Heaviside and cubic B-spline test functions for V-NIM.

- The NeuroPU representation couples neural networks with a meshfree approximation whose polynomial reproduction and smoothness can be specified through its basis functions.

- A local variational formulation supplies physics-based training residuals without a conforming integration mesh. The strong-form and variational alternatives are evaluated within the same hybrid approximation framework.

## Results

- Poisson and linear-elasticity benchmarks assess solution accuracy, derivative accuracy, and refinement behavior against analytical or finite-element references.

- The Poisson convergence study varies the polynomial order and meshfree resolution. Both solution and gradient errors decrease with refinement; the behavior also depends on the test function.

- Parameterized and time-dependent examples test the use of neural representations beyond a single stationary solution. Comparisons with PINN and variational PINN models use the configurations reported in the paper.

<figure class="publication-result">
  <a href="{{ '/images/publications/nim-result.png' | relative_url }}"><img src="{{ '/images/publications/nim-result.png' | relative_url }}" alt="Poisson benchmark: convergence of V-NIM/h (left) and V-NIM/c (right) as the meshfree resolution is refined. The curves compare solution and gradient errors for different NeuroPU polynomial orders. The observed rates support the approximation study; they are not runtime measurements. Source: Fig. 6 of the published paper." loading="lazy"></a>
  <figcaption>Poisson benchmark: convergence of V-NIM/h (left) and V-NIM/c (right) as the meshfree resolution is refined. The curves compare solution and gradient errors for different NeuroPU polynomial orders. The observed rates support the approximation study; they are not runtime measurements. Source: Fig. 6 of the published paper.</figcaption>
</figure>

## Scope and limitations

The reported accuracy and training-time comparisons concern the benchmark problems and architectures in this study. They do not establish a universal speed advantage over FEM or other PINN implementations. Linear-basis V-NIM with a Heaviside test function was excluded from the convergence study because of instability; approximation order and test-function regularity matter.

## Resources and reproduction

The NIM-Tutorial repository provides selected examples, including an advection–diffusion forward problem. It is a tutorial resource, rather than a complete archive of every experiment in this paper. For finite-strain forward and inverse material modeling, see the [hyperelasticity extension](/publication/nim-hyperelasticity/).

## Citation

Honghui Du; QiZhi He (2024). Neural-Integrated Meshfree (NIM) Method: A differentiable programming-based hybrid solver for computational mechanics. *Computer Methods in Applied Mechanics and Engineering*, 427, 117024. [DOI: 10.1016/j.cma.2024.117024](https://doi.org/10.1016/j.cma.2024.117024).

[Download BibTeX]({{ page.bibtex_url | relative_url }})

{% raw %}
```bibtex
@article{du2024nim,
  title = {{Neural-Integrated Meshfree (NIM) Method: A differentiable programming-based hybrid solver for computational mechanics}},
  author = {Du, Honghui and He, QiZhi},
  journal = {Computer Methods in Applied Mechanics and Engineering},
  volume = {427},
  pages = {117024},
  year = {2024},
  doi = {10.1016/j.cma.2024.117024},
  url = {https://doi.org/10.1016/j.cma.2024.117024}
}
```
{% endraw %}

[Back to all publications]({{ '/publications/' | relative_url }})
