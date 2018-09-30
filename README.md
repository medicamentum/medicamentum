# Medicine Leaflets

The objective of this project is to collect, organize and mine information from medicine leaflets regulated by health regulatory agencies around the world . This is an open science project. This means everybody is welcome (and encouraged) to contribute however they can, using whichever skills they have. Your contributions to the project will be recorded as comments in the issue tracker and pull requests to our repo. We will use those to automatically build a list of participants to give credit to everyone that helped.

## How to participate?

You can choose to help with whatever you're comfortable with:
* if you do not possess specialized scientific or engineering skills, you can help us find more material to add, or with many other tasks we may have (ask us!)
* if you are a health sciences professional, send questions you'd like us to answer, help us to curate the data and analyze the results
* if you are a data scientist, help us acquire + clean + mine the data
* if you are a software engineer or developer, help us to create or improve the code to support all of the above tasks
* if you are a designer, help us to do all of this with more efficacy and beauty!

## Minimum Viable Product (MVP)

Many of us can only work on this project in spare time, so we will take baby steps. The first MVP we are targetting is the collection and annotation of all medicine leaflets available distributed by health regulatory agencies. First we will automatically extract entities and concepts mentioned in those leaflets. Subsequently, we will curate the extracted data to remove unrelated content and include missing entities/concepts.

## Developer Quickstart

If you want to run/develop with us at this stage of the project, we assume you are running Docker

## Design Decisions

We describe below a few design decisions to help you understand how we got where we got, but we're also open to constructive criticism and suggestions on how we can improve our project.

* Reproducibility
  * as much as possible, I'd like for the code to work such that whoever downloads it can build all of the data files from scratch;
  * each step of the workflow is recorded in a file, so that we can easily inspect the output of each step;
  * errors are logged in a master errors.log so we can know when a given file didn't get correctly generated.

* Github issue tracker to coordinate development, issues, bugs, etc.

* Pull requests with diff patches to provide reproducible fixes to the data
