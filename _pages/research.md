---
layout: single
title: "Differentiable simulation and inverse modeling: methods, papers, and code"
permalink: /research/
author_profile: true
description: "Choose a starting point for neural meshfree PDE solvers, finite-strain material identification, differentiable MPM, and porous-media PINNs. Research by Honghui Du and collaborators."
---

This guide connects research tasks to papers and available code by **Honghui Du and collaborators**. It is an author-maintained guide to this research portfolio, rather than an independent ranking of numerical methods. [中文导读](/zh/research/)

## Which method fits the problem?

| Your task | Starting point | Information or physics used | Evidence and limits |
|---|---|---|---|
| Solve PDEs with a hybrid neural and meshfree approximation | [Neural-Integrated Meshfree (NIM)](/publication/nim/) | Governing equations, boundary conditions, local meshfree basis functions, and neural networks | Poisson, linear elasticity, parameterized and time-dependent examples; results depend on approximation order and test functions |
| Identify heterogeneous elastic properties at finite strain | [Differentiable NIM for hyperelasticity](/publication/nim-hyperelasticity/) | Strain observations and the hyperelastic governing equations | Forward deformation and heterogeneous-modulus reconstruction; does not validate plasticity or damage |
| Infer initial velocity or basal friction in a large-deformation flow | [JAX-MPM](/publication/jax-mpm/) | Differentiable particle–grid simulation with particle or region observations | Velocity reconstruction and segmented friction inversion; the friction example specifically uses particle trajectories |
| Model density-driven CO₂ convection in porous media | [Fourier-feature PINNs](/publication/co2-pinn/) | Coupled flow/transport equations, Fourier features, sequential time training | Homogeneous 2-D tests at Rayleigh numbers 500–2000; accuracy deteriorates in stronger convection |
| Integrate higher-order meshfree elasticity consistently | [Unified gradient smoothing](/publication/strain-gradient/) | A shared construction of first- and second-order smoothed derivatives | Patch tests and 1-D to 3-D strain-gradient elasticity examples; not a neural solver |

The linked paper pages provide the formal DOI, abstract, result figures, limitations, and BibTeX. The CO₂ page's detailed evidence was checked against the corrected proof; the other four were checked against published PDFs.

## Neural PDE approximation or differentiable time stepping?

NIM and JAX-MPM use differentiable computation for different purposes. NIM couples neural networks with a meshfree approximation and constructs physics residuals for training. JAX-MPM differentiates through particle–grid time stepping, allowing a data-misfit objective to update unknown initial conditions or friction parameters. The presence of automatic differentiation does not make their discretizations or inverse problems interchangeable.

For a stationary or finite-strain elasticity problem with strain observations, start with the NIM papers. For a transient particle flow with trajectories or monitoring-region observations, inspect JAX-MPM's observation model and examples. The choice also depends on constitutive assumptions, boundary conditions, available measurements, and compute resources.

## What can be run from the public repositories?

- **[NIM-Tutorial](https://github.com/IntelligentMechanicsLab/NIM-Tutorial)** includes 1-D hyperelasticity notebooks and an advection–diffusion forward example. Check the repository for the currently available examples; it does not package every experiment in the papers.
- **[JAX-MPM](https://github.com/IntelligentMechanicsLab/JAX-MPM)** includes a dam-break transfer-scheme validation example and a particle-trajectory friction-inversion workflow. Review the example settings and dependencies before running a full simulation.

These links point to existing implementations. No additional benchmark results or runtime claims are implied by this guide.

## What to check before an inverse simulation

1. **Match observations to the model.** Strains, particle positions, and region-based measurements require different observation operators. A result using one type does not validate all three.
2. **Match the constitutive assumptions.** The hyperelasticity work concerns elastic finite deformation; do not infer support for history-dependent material identification from that result.
3. **Separate numerical and inverse error.** A converged forward computation does not establish uniqueness or robustness of recovered parameters. Inspect the paper's sampling and resolution studies.
4. **Interpret timings with the setup attached.** Hardware, precision, discretization, constitutive models, and implementations affect comparisons. Do not transfer a published speed ratio to a different workload.

## Papers and citation records

{% for paper in site.publications %}{% if paper.detail_page %}
- [{{ paper.title }}]({{ paper.url | relative_url }}) — {{ paper.authors }}. *{{ paper.journal }}* ({{ paper.publication_year }}). [DOI]({{ paper.paper_url }}) · [BibTeX]({{ paper.bibtex_url | relative_url }})
{% endif %}{% endfor %}

[Publication list](/publications/) · [Machine-readable paper records](/research/papers.json)
