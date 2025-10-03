![Fast Data Science logo](https://raw.githubusercontent.com/fastdatascience/brand/main/primary_logo.svg)

<a href="https://fastdatascience.com"><span align="left">🌐 fastdatascience.com</span></a>
<a href="https://www.linkedin.com/company/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/linkedin.svg" alt="Fast Data Science | LinkedIn" width="21px"/></a>
<a href="https://twitter.com/fastdatascienc1"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/x.svg" alt="Fast Data Science | X" width="21px"/></a>
<a href="https://www.instagram.com/fastdatascience/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/instagram.svg" alt="Fast Data Science | Instagram" width="21px"/></a>
<a href="https://www.facebook.com/fastdatascienceltd"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/fb.svg" alt="Fast Data Science | Facebook" width="21px"/></a>
<a href="https://www.youtube.com/channel/UCLPrDH7SoRT55F6i50xMg5g"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/yt.svg" alt="Fast Data Science | YouTube" width="21px"/></a>
<a href="https://g.page/fast-data-science"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/google.svg" alt="Fast Data Science | Google" width="21px"/></a>
<a href="https://medium.com/fast-data-science"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/medium.svg" alt="Fast Data Science | Medium" width="21px"/></a>
<a href="https://mastodon.social/@fastdatascience"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/mastodon.svg" alt="Fast Data Science | Mastodon" width="21px"/></a>

# Country named entity recognition


<!-- badges: start -->
![my badge](https://badgen.net/badge/Status/In%20Development/orange)
[![PyPI package](https://img.shields.io/badge/pip%20install-country_named_entity_recognition-brightgreen)](https://pypi.org/project/country-named-entity-recognition/) [![version number](https://img.shields.io/pypi/v/country-named-entity-recognition?color=green&label=version)](https://github.com/fastdatascience/country_named_entity_recognition/releases) [![License](https://img.shields.io/github/license/fastdatascience/country_named_entity_recognition)](https://github.com/fastdatascience/country_named_entity_recognition/blob/main/LICENSE)
[![pypi Version](https://img.shields.io/pypi/v/country_named_entity_recognition.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/country_named_entity_recognition/)
 [![version number](https://img.shields.io/pypi/v/country_named_entity_recognition?color=green&label=version)](https://github.com/fastdatascience/country_named_entity_recognition/releases) [![PyPi downloads](https://static.pepy.tech/personalized-badge/country_named_entity_recognition?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/country_named_entity_recognition/)
[![forks](https://img.shields.io/github/forks/fastdatascience/country_named_entity_recognition)](https://github.com/fastdatascience/country_named_entity_recognition/forks)

<!-- badges: end -->

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/country_named_entity_recognition

PyPI package: https://pypi.org/project/country-named-entity-recognition/

Python library for finding country names in a string.

Please note this library finds only high confidence countries. A text such as "America" is ambiguous.

It also only finds the English names of these countries. Names in the local language are not supported.

**New! In 2025 we have added support for [spaCy](#using-the-library-with-spacy)**

# Requirements

Python 3.9 and above

pycountry 22.1.10 and above

# Installation

```
pip install country-named-entity-recognition
```

# Usage examples

## Example 1

```
from country_named_entity_recognition import find_countries
find_countries("We are expanding in the UK")
```

outputs a list of tuples.

```
[(Country(alpha_2='GB', alpha_3='GBR', flag='🇬🇧', name='United Kingdom', numeric='826', official_name='United Kingdom of Great Britain and Northern Ireland'),
  <re.Match object; span=(1, 15), match='united kingdom'>)]
```

## Example 2

The tool's default behaviour assumes countries are correctly capitalised and punctuated:

```
from country_named_entity_recognition import find_countries
find_countries("I want to visit france.")
```

will not return anything.

However, if your text comes from social media or another non-moderated source, you might want to allow case-insensitive matching:

```
from country_named_entity_recognition import find_countries
find_countries("I want to visit france.", is_ignore_case=True)
```

## Example 3

This illustrates how you can bring context into the tool.  If we encounter the string "Georgia", by default it refers to the US state.

```
from country_named_entity_recognition import find_countries
find_countries("Gladys Knight and the Pips wrote the Midnight Train to Georgia")
```

will return an empty list.

But what happens if we include a clear contextual clue?

```
from country_named_entity_recognition import find_countries
find_countries("Salome Zourabichvili is the current president of Georgia.")
```

returns

```
[(Country(alpha_2='GE', alpha_3='GEO', flag='🇬🇪', name='Georgia', numeric='268'), <re.Match object; span=(34, 41), match='Georgia'>)]
```

You can force the latter behaviour:

```
from country_named_entity_recognition import find_countries
find_countries("I want to visit Georgia.", is_georgia_probably_the_country=True)
```


# Adding custom variants

If you find that a variant country name is missing, you can add it using the *add_custom_variants* method.

Let's imagine we want to add Neverneverland as a synonym for the UAE:

```
from country_named_entity_recognition import find_countries, add_custom_variants
add_custom_variants(["Neverneverland"], "AE")
find_countries("I want to visit Neverneverland")
```

# Using the library with spaCy

If you are already using [spaCy](https://spacy.io) in your project, you'll be pleased to see that you can pass a spaCy Doc object into the tool:

```
import spacy
from country_named_entity_recognition.country_finder_spacy import find_countries_in_spacy_doc
nlp = spacy.blank("en")
doc = nlp("I went to the USA")
country_matches = find_countries_in_spacy_doc(nlp, doc)
print (country_matches)
```

# Raising issues

If you find a problem, you are welcome either to raise an issue at https://github.com/fastdatascience/country_named_entity_recognition/issues or to make a pull request and I will merge it into the project.

# Who to contact

Thomas Wood at https://fastdatascience.com

# How to cite Country Named Entity Recognition?

We would be grateful for your taking the consideration to cite us. We would suggest something like the following (depending on your style):

Wood, T.A. Country Named Entity Recognition. Zenodo, 5 Sept. 2025, https://doi.org/10.5281/zenodo.17062716.

A BibTeX entry for LaTeX users is

```
@unpublished{countrynamedentityrecognition,
    AUTHOR = {Wood, T.A.},
    TITLE  = {Country Named Entity Recognition (Computer software), Version 1.0.2},
    YEAR   = {2025},
    doi    = {10.5281/zenodo.17062716},
    url = {https://fastdatascience.com/natural-language-processing/country-named-entity-recognition/}
}
```

## Case studies of the Country Named Entity Recognition Library

People and organisations around the world have been using the library and have cited us.

### The sixth wave of mass species extinction...

Alisa Redding at the University of Helsinki used the tool for her Masters thesis on mass species extinction and biodiversity.

* Redding, Alisa. [Animals of the Digital Age: Assessing digital media for public interest and engagement in species threatened by wildlife trade.](https://helda.helsinki.fi/items/77960829-145a-4efb-b364-3dbe6ac6bfb4/full) University of Helsinki, Faculty of Science, 2023.

### The UN's Sustainable Development Goals (SDGs)

Christoph Funk and his colleagues at Justus-Liebig-Universität Gießen (Justus Liebig University Giessen) in Germany used country-named-entity-recognition for their meta-analysis of articles related to Sustainable Development Goals in 2023:

* Funk, Christoph and Tönjes, Elena and Teuber, Ramona and Breuer, Lutz, Reading Between the Lines: The Intersection of Research Attention and Sustainable Development Goals (May 31, 2023). Available at SSRN: [https://ssrn.com/abstract=4465055](https://ssrn.com/abstract=4465055) or [http://dx.doi.org/10.2139/ssrn.4465055](http://dx.doi.org/10.2139/ssrn.4465055)

### The European Commission: detecting terrorism and extremism

Francesco Bosso and his team at the European Commission wrote a report investigating NLP for location detection with a focus on the JRC Terrorism and Extremism Database.

* Bosso, Francesco, et al. [Use of Large Language Models for location detection on the example of the terrorism and extremism event database.](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC134961/JRC134961_01.pdf), JRC Technical Report, European Commission (2023).


### Labelling radical content online

Ugochukwu Etudo and Victoria Y. Yoon at Virginia Commonwealth University used the tool in their analysis of radical content online:

* Ugochukwu Etudo, Victoria Y. Yoon (2023) [Ontology-Based Information Extraction for Labeling Radical Online Content Using Distant Supervision](https://pubsonline.informs.org/doi/abs/10.1287/isre.2023.1223). Information Systems Research 0(0). [https://doi.org/10.1287/isre.2023.1223](https://doi.org/10.1287/isre.2023.1223)

### Analysing text to assess indicators in Sustainable Development Goals

Elena Tönjes used the library to assess sustainability indicators in her PhD thesis:

* Tönjes, Elena. [A Text-based Approach to Sustainability Indicators](https://jlupub.ub.uni-giessen.de/server/api/core/bitstreams/7fd77fae-28df-4769-ae94-905977892f00/content). Diss. Justus-Liebig-University Giessen, 2024.

### De-risking clinical trials: the Clinical Trial Risk Tool

Fast Data Science are using the Country Named Entity Recognition library in the Clinical Trial Risk Tool, where it's important to identify the countries where a trial takes place, avoiding false positives from spurious mentions. More information at: https://clinicaltrialrisk.org/

## Other named entity recognition tools

* [Medical and clinical named entity recognition Python library](https://fastdatascience.com/ai-in-pharma/medical-named-entity-recognition-python-library/)
