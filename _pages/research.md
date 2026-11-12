---
layout: single
title: "Research"
permalink: /research/
author_profile: true
description: "Honghui Du's research in computational mechanics: neural meshfree methods, differentiable simulation, inverse modeling, and numerical discretization."
---

My research focuses on numerical methods for computational mechanics, combining meshfree discretization, scientific machine learning, and differentiable programming. I develop methods for solving governing equations and inferring material properties and system conditions from observations. Together with my collaborators, I study these ideas in solid mechanics, large-deformation flows, and transport in porous media.

## Neural–numerical methods for computational mechanics

The Neural-Integrated Meshfree (NIM) method combines the approximation structure of meshfree methods with trainable neural representations. Its NeuroPU approximation couples neural networks with local partition-of-unity basis functions, bringing polynomial reproduction and spatial regularity into the solution representation. We developed both strong-form and local variational formulations and studied their accuracy and convergence for stationary and time-dependent partial differential equations.

We subsequently extended NIM to finite-strain hyperelasticity. A consistent local variational formulation incorporates nonlinear material behavior, while NeuroPU represents both displacement and spatially varying material properties. This provides a common formulation for forward deformation analysis and the identification of heterogeneous elastic modulus fields from strain observations.

[NIM (2024)](/publication/nim/) · [Finite-strain hyperelasticity (2025)](/publication/nim-hyperelasticity/) · [Code and tutorials](https://github.com/IntelligentMechanicsLab/NIM-Tutorial)

## Differentiable simulation and inverse modeling

Large-deformation flows involve evolving geometry, contact, and material behavior. JAX-MPM implements the material point method in JAX, combining GPU computation with differentiation through the simulation's time-stepping operations. The framework supports forward simulation of fluid and granular flows and gradient-based estimation of unknown initial conditions and friction parameters.

A differentiable observation layer connects simulated states to particle measurements and measurements over fixed spatial regions. Our inverse studies reconstruct initial velocity fields and recover spatially varying basal friction from sparse observations. These developments connect particle-based mechanics with data assimilation and neural representations of unknown fields.

[JAX-MPM (2026)](/publication/jax-mpm/) · [Code](https://github.com/IntelligentMechanicsLab/JAX-MPM)

## Physics-informed learning for porous-media flow

Density-driven convection governs the mixing of dissolved CO₂ and brine in geological carbon storage. We investigated physics-informed neural networks for the coupled flow and transport equations in a two-dimensional homogeneous porous medium. Fourier-feature embeddings represent spatial variation, and sequential training over time intervals follows the evolution of convective fingers. Comparisons with stabilized finite element solutions examine how the neural approximation captures concentration fields and flow statistics across different convection regimes.

[Density-driven flow and CO₂ sequestration (2023)](/publication/co2-pinn/)

## Consistent meshfree discretization

My work on meshfree numerical methods also addresses integration consistency for higher-order continuum models. In strain-gradient elasticity, the discretization requires both first- and second-order spatial derivatives. We developed a unified reproducing-kernel gradient-smoothing formulation that derives these derivatives through a shared set of coefficients determined by the integration constraint. The construction supports high-order meshfree approximations, with accuracy and convergence assessed through patch tests and one-, two-, and three-dimensional elasticity problems.

[Gradient smoothing for strain-gradient elasticity (2022)](/publication/strain-gradient/)

[Full publication list](/publications/)
