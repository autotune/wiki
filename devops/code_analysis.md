### CODE ANALYSIS

### METHODOLOGY

1) View imported objects

Example: how is the TASK field displayed on the ansible* screen?

    grep import bin/ansible-playbook
    import pkg_resources
    import sys
    import os
    import stat
    import ansible.playbook
    import ansible.constants as C
    import ansible.utils.template
    from ansible import errors
    from ansible import callbacks
    from ansible import utils
    from ansible.color import ANSIBLE_COLOR, stringc
    from ansible.callbacks import display


     grep "TASK: " lib/ansible/callbacks.py
        msg = "TASK: [%s]" % name

        name = utils.unicode.to_bytes(name)

        msg = "TASK: [%s]" % name

### TOOLS

#### STRACE

1) View files being read and written

    strace -e open,write -o oecalls.txt mycommand
 
#### GREP 

2) Search content of files within directories for string except for dir.

   -r search recursively.

   -n include line number.

   -w match line with whole word only.

    grep -rnw -e 'sudo' ./* --exclude-dir=./v2


