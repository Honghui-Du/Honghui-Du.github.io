---
title: Modeling density-driven flow in porous media by physics-informed neural networks for CO2 sequestration
collection: publications
category: manuscripts
layout: publication
permalink: /publication/co2-pinn/
detail_page: true
date: '2023-07-01'
publication_year: 2023
journal: Computers and Geotechnics
volume: '159'
pages: '105433'
doi: 10.1016/j.compgeo.2023.105433
paper_url: https://doi.org/10.1016/j.compgeo.2023.105433
authors: Honghui Du, Ze Zhao, Haojia Cheng, Jinhui Yan, QiZhi He
author_list:
- Honghui Du
- Ze Zhao
- Haojia Cheng
- Jinhui Yan
- QiZhi He
excerpt: Fourier-feature physics-informed neural networks and sequential time-domain training for density-driven CO2 dissolution and convection in porous media.
description: Fourier-feature physics-informed neural networks and sequential time-domain training for density-driven CO2 dissolution and convection in porous media.
image: /images/co2.gif
image_size: 350px
keywords:
- CO2 sequestration
- Density-driven convection
- Physics-informed neural networks
- Fourier feature embedding
- Time domain decomposition
abstract: Accurate prediction of density-driven convection of CO₂ overlaying brine in porous media is crucial to the applications of geological carbon sequestration. In this paper, we introduce the physics-informed neural network (PINN) method to investigate the mass transfer of CO₂ injected into a homogeneous subsurface porous formation, where the concentration and the streamfunction are approximated by neural network representations. To mitigate the computational burden and training difficulties arising from learning the longterm diffusion and convection processes, we implement a time domain decomposition-based scheme so that the PINN solution can represent short-interval dynamics in a sequential manner. Furthermore, Fourier-type basis functions are encoded in the PINN architecture to map the spatial coordinates onto an embedding feature space characterized by various frequencies. The numerical results show that the use of Fourier feature embedding improves the training performance by
  handling the notorious spectral bias in deep neural networks and enhances the stability for long-term prediction of flow and transport. The proposed PINN method is applied to a benchmark problem to understand the effect of natural convection on the simulation performance. Compared to the high-fidelity stabilized FEM solution, the PINN approach presents agreeable statistical characteristics of CO₂-rich brine fingers, demonstrating the effectiveness of PINNs in modeling density-driven flow.
comments: false
share: false
bibtex_url: /files/citations/co2-pinn.bib
preprint: https://www.researchgate.net/publication/369482698_Modeling_density-driven_flow_in_porous_media_by_physics-informed_neural_networks_for_CO_2_sequestration
equal_contribution: Honghui Du and Ze Zhao contributed equally to this work.
links:
- name: Paper
  url: https://doi.org/10.1016/j.compgeo.2023.105433
---

{% include publication-header.html %}

## Overview

Dissolved CO₂ increases brine density and can trigger descending convective fingers in a porous formation. This paper investigates whether physics-informed neural networks can represent the resulting flow and transport. Fourier features improve the representation of spatial variation, while sequential time-domain training addresses longer simulations.

## Abstract

{{ page.abstract }}

## Method and contributions

Two neural networks approximate concentration and streamfunction in a two-dimensional homogeneous porous medium. The streamfunction representation satisfies incompressibility, and the loss combines governing-equation, initial-condition, and boundary-condition residuals. Fourier features enrich the spatial inputs. Time-domain decomposition trains the solution over successive intervals, passing the preceding prediction to the next interval.

- Fourier-feature embedding is applied to PINN modeling of density-driven CO₂ flow, with a study of how feature order affects prediction and flow-pattern representation.

- Sequential time-domain training is combined with the enriched representation to study longer-time convection, using stabilized FEM as a reference for concentration fields and flow statistics.

## Results

- An initial benchmark examines approximation error and stability before the density-driven convection experiments.

- The convection study varies Rayleigh number over 500–2000 and examines Fourier order, residual sampling, and time-interval decomposition.

- Concentration fields and statistical descriptors of convective fingers are compared with stabilized FEM. Shorter training intervals and increased residual sampling improve agreement in the reported cases.

<figure class="publication-result">
  <a href="{{ '/images/publications/co2-pinn-result.png' | relative_url }}"><img src="{{ '/images/publications/co2-pinn-result.png' | relative_url }}" alt="Concentration at dimensionless time t = 1.0 and Rayleigh number 1000. Panels (a)–(c) use Fourier-feature PINNs with different residual-point counts and training-interval lengths; panel (d) is the stabilized FEM reference. The Fourier order is 4. The comparison illustrates sensitivity to sampling and time decomposition. Source: Fig. 13 of the corrected proof." loading="lazy"></a>
  <figcaption>Concentration at dimensionless time t = 1.0 and Rayleigh number 1000. Panels (a)–(c) use Fourier-feature PINNs with different residual-point counts and training-interval lengths; panel (d) is the stabilized FEM reference. The Fourier order is 4. The comparison illustrates sensitivity to sampling and time decomposition. Source: Fig. 13 of the corrected proof.</figcaption>
</figure>

## Scope and limitations

The experiments concern a two-dimensional homogeneous porous medium. Agreement with FEM deteriorates as convection becomes stronger, particularly at Rayleigh number 2000. The paper leaves a systematic PINN-versus-FEM computational-cost comparison and heterogeneous-media extension for further investigation; a lower residual-point count is not a measured runtime speedup.

## Resources and reproduction

The paper states that data are available on request. A public code repository for this study has not been verified. The author-uploaded preprint is linked above; access to its download may depend on ResearchGate availability.

## Research questions

### Why combine Fourier features with sequential time-domain training?

Fourier-feature embedding enriches the spatial representation for convective patterns, while sequential training divides the time domain into shorter intervals. The paper investigates Fourier order, residual sampling, and interval length against a stabilized FEM reference. See Sections 3–4 and Fig. 13; the source reviewed here is the corrected proof.

### What limits were observed for stronger convection?

The experiments cover a two-dimensional homogeneous porous medium with Rayleigh numbers from 500 to 2000. Agreement with the FEM reference deteriorates as convection strengthens, particularly at Rayleigh number 2000. The paper does not establish a systematic runtime advantage over FEM or validate heterogeneous porous formations. See the numerical results and conclusions.

## Citation

Honghui Du; Ze Zhao; Haojia Cheng; Jinhui Yan; QiZhi He (2023). Modeling density-driven flow in porous media by physics-informed neural networks for CO2 sequestration. *Computers and Geotechnics*, 159, 105433. [DOI: 10.1016/j.compgeo.2023.105433](https://doi.org/10.1016/j.compgeo.2023.105433).

[Download BibTeX]({{ page.bibtex_url | relative_url }})

{% raw %}
```bibtex
@article{du2023co2pinn,
  title = {{Modeling density-driven flow in porous media by physics-informed neural networks for CO2 sequestration}},
  author = {Du, Honghui and Zhao, Ze and Cheng, Haojia and Yan, Jinhui and He, QiZhi},
  journal = {Computers and Geotechnics},
  volume = {159},
  pages = {105433},
  year = {2023},
  doi = {10.1016/j.compgeo.2023.105433},
  url = {https://doi.org/10.1016/j.compgeo.2023.105433}
}
```
{% endraw %}

[Back to all publications]({{ '/publications/' | relative_url }})
