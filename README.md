# World Cup 2022 Panini Missing x Repeated cards Intersection
This project aims to provide a simple way to check the intersection of your missing and a third party repeated Panini 2022 World Cup Album cards.

This is a project made simply for fun and to help checking which friends repeated cards are within my missing cards.

# Requirements

`python 3.5+`

# Input

Create a json file with the following attributes:

```json
{
    "missing": "MANDATORY",
    "repeated": "MANDATORY",
    "separator": "OPTIONAL | DEFAULT VALUE: ', ' ",
}
```

EXAMPLE
```json
{
    "missing": "<CARD 1>, <CARD 2>, ..., <CARD N>",
    "repeated": "<CARD 1>, <CARD 2>, ..., <CARD N>"
}
```

# How to run
`python3 main.py <json_input_file>.json`

# How to run unit tests
`make unit_test`
