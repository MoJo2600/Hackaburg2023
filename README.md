# Hackaburg 2023 Challenge WORK SMARTER & SUSTAINABLE demo data

## Overview

This repository contains some data you can use for your ideas and some sample code to generate your own data.

```
Hackaburg2023/
├─ data/
│  ├─ ratisbona-companies.csv   # A list of around 2000 companies located in ratisbona
|  ├─ people-with-addresses.csv # A list of 10000 fake people with real addresses
│  ├─ people.csv                # A list of 10000 fake people
│  ├─ ratisbona-addresses.csv   # A list of all addresses within 93000 > postal_code < 93300
├─ DemoData.ipynb               # A jupyter notebook to generate your own test data
```

With this data you have 10000 people distributed around Ratisbona and around 2000 companies that are located in Ratisbona. Everything else is up to your imagination. Feel free to add more data, new data, real data.

### Some ideas

* Imagine a desk booking system where you are able to retrieve data from and see who is when in the office. Could this data be used to make work travel more sustainable?
* Maybe there is an API for traffic data that we can use? Weather information?
* A company might have a parking lot with usage statistics

## How to generate your own data

You can use the provided Jupyter notebook to see how the data was generated and generate your own data.

### Quickstart

If you use VSCode, you can open the folder and use the [remote container](https://code.visualstudio.com/docs/devcontainers/containers) feature to start this folder within the provided development container.

After the container has startet you should be able to run the scripts inside the Jupyter Notebook.
