# Country named entity recognition

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/country_named_entity_recognition

Python library for finding country names in a string.

Please note this library finds only high confidence countries. A text such as "America" is ambiguous.

It also only finds the English names of these countries. Names in the local language are not supported.

# Requirements

Python 3.9 and above

pycountry 22.1.10

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

# Raising issues

If you find a problem, you are welcome either to raise an issue at https://github.com/fastdatascience/country_named_entity_recognition/issues or to make a pull request and I will merge it into the project.

# Who to contact

Thomas Wood at https://fastdatascience.com

# How to cite Country Named Entity Recognition?

We would be grateful for your taking the consideration to cite us. We would suggest something like the following (depending on your style):

Wood, T.A., Country Named Entity Recognition [Computer software], Version 0.4, accessed at https://pypi.org/project/country-named-entity-recognition, Fast Data Science Ltd (2022)

A BibTeX entry for LaTeX users is

```
@unpublished{countrynamedentityrecognition,
    AUTHOR = {Wood, T.A.},
    TITLE  = {Country Named Entity Recognition (Computer software), Version 0.4},
    YEAR   = {2023},
    Note   = {To appear},
    url = {https://pypi.org/project/country-named-entity-recognition}
}
```
