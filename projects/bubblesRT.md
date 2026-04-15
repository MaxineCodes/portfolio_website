---
title: Simple Recursive C++ CPU Raytracer
date: 2025-01-01
thumbnail: static/media/bubbles_rt_thumbnail.png
---

A simple CPU raytracer written in C++ I made in 2022, supporting only the simplest SDF primitive, a sphere. It supports basic lambertian diffusion scattering, as well as dielectrics with refraction and metallic scattering.
It runs on a single CPU core without offloading any work to the GPU. Performance is abysmal and rendering a non-noisy image at higher resolution can take minutes. However, this project really got my feet wet in using mathematics and programming to turn abstract 3D data into a super cool image! Graphics programming is a lot of fun and this is the first of many to come. 
