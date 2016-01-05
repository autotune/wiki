### FILE VERIFICATION

This command can be used to detect which files have changed from their original package.
For example, if someone puts in "disallow *" in /etc/postfix/transport, this can detect
it. If you don't know every concept behind a specific package it'll at least possible to identify possible user configuration errors by knowing which files have changed from their defaults. 


    [autotune@ansibledev security]$ sudo grep disallow /etc/postfix/transport
    #        The trivial-rewrite(8) server disallows regular expression
    disallow *

    [autotune@ansibledev security]$ sudo rpm -V postfix
    S.5....T.  c /etc/postfix/transport
 
