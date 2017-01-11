Intro
=====

**secret-santa** can help you manage a list of secret santa participants by
randomly assigning pairings and sending emails. It can avoid pairing 
couples to their significant other, and allows custom email messages to be 
specified.

Dependencies
------------

pytz
pyyaml

Usage
-----

Copy config.yml.template to config.yml and enter in the connection details 
for your outgoing mail server. Modify the participants and couples lists and 
the email message if you wish.

    cd secret-santa/
    cp config.yml.template config.yml

Once configured, call secret-santa:

    ./secret_santa.py

Calling secret-santa without arguments will output a test pairing of 
participants.

To send the emails, call using the `--send` argument

    ./secret_santa.py --send

Todos for next year
-------------------

Make sure the santas form a chain, e.g. a -> b -> c -> d -> a instead of
a -> b -> a, c -> d -> d. It's always more fun that way!
