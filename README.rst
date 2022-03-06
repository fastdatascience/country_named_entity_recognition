Country finder
==============

Developed by Fast Data Science, https://fastdatascience.com

Source code at https://github.com/fastdatascience/countryfinder

Python library for finding country names in a string.

Please note this library finds only high confidence countries. A text such as "America" is ambiguous.

It also only finds the English names of these countries. Names in the local language are not supported.

Requirements
============

Python 3.6 and above

pycountry 22.1.10

Installation
============

::

  pip install countryfinder

Usage examples
==============

Example 1

.. code:: python

  from countryfinder import find_countries
  find_countries("We are expanding in the UK")

outputs a list of tuples.


Who to contact
==============

Thomas Wood at https://fastdatascience.com

