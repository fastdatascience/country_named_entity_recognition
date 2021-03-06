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

Example 1

```
from country_named_entity_recognition import find_countries

find_countries("We are expanding in the UK")
```

outputs a list of tuples.

```
[(Country(alpha_2='GB', alpha_3='GBR', flag='🇬🇧', name='United Kingdom', numeric='826', official_name='United Kingdom of Great Britain and Northern Ireland'),
  <re.Match object; span=(1, 15), match='united kingdom'>)]
s
```


# Who to contact

Thomas Wood at https://fastdatascience.com
