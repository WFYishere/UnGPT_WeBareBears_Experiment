# UnGPT Challenge - We Bare Bears

## Introduction

This repository contains two Python scripts demonstrating how Principal Component Analysis (PCA) can be used to visualize complex data and identify key contributors to a country's happiness, based on the [World Happiness Report 2021 dataset](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021/data). The scripts provide a side-by-side comparison of visualizations with and without PCA.

## Contents

- `without_pca.py`: Visualizes the relationship between happiness score and other factors using direct scatter plots.
- `with_pca.py`: Applies PCA to reduce dimensionality and visualizes the first two principal components, along with the happiness score.
- `happiness_2021.csv`: Dataset obtained from kaggle

## Requirements

- Python 3.x
- Required libraries: `pandas`, `matplotlib`, `sklearn`
