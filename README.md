# Simple rule-based chatbot story-teller.

This is aimed at being a very simple story telling chatbot. The replies are all
hard-coded and used statically!

## TODO
- *Explore available options!*
- input info like name and store it!

## Nice to haves
- Nested converstaions
- remember information!
- voice recognition
- meaning of words
- Correction of words (Hi -> Hola): send only nearest match

## DONE
- autocomplete
- only allow from options


## Design
The idea is to have something like Duolingo chatbots. An important aspect of it
is that they are not actually open domain chatbots, but more like
Question-Answer chatbots. The idea is for the bot to prompt replies from the
user, and allow only a set of predefined replies. The trick is to make the set
of replies large enough to give a sense of freedom, and to have
autocomplete-to-select rather than a menu. Both of these give the illusion of
freedom of choice, while keeping the chatbot relatively simple.

After writing this basic program, having all the scalability issues in mind, I
started exploring the online available APIs and Open source software.

Some notes:
### Intent
This is exactly what I had in mind, to be able to generalize to other
similar sentences of the same intent given a few examples.
It would be interesting to explore ways to populate a given intent with phrases
/ sentences.
*Used in wit.ai, api.ai and others.*

### Context
The nature of our chatbot is such that we do not really require to parse user
input. Context would implicitly exist in each individual conversation bot that
we program.
