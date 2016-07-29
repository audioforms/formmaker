Audioform formmaker and Internals
===============

# Audioform internals


## Why yaml?
yaml is used for readibility, flexibility, and simplicity

## Form Templates

Form templates look like:
``` yaml
    --- !example1survey
    title    : Example Form Response
    owner    : admin
    behavior :
        intro-message : Let's test audioform
        confirm-each  : Yes
        read-summary  : Yes
        outro-message : Thank you for testing audioform
    questions :
        - title      : What do you want to do with audioform?
          type       : Long Text
          validation : No
        - title      : Out of five, how do you rate audioform?
          type       : Number
          validation : int range(1-5)
          default    : 5
```
## Form Responses

Filled out forms look like the below.
All template information is preserved; this allows for users to use responses as templates ::
``` yaml
    --- !example1out
    title    : Example Form Response
    owner    : admin
    replier  : Bob Bobbs
    timefiled: 10-18-2016 16:23
    behavior :
        intro-message : Let's test audioform
        confirm-each  : Yes
        read-summary  : Yes
        outro-message : Thank you for testing audioform
    questions :
        - title      : What do you want to do with audioform?
          type       : Long Text
          validation : No
          response   : I want to be able to note things while cooking
        - title      : Out of five, how do you rate audioform?
          type       : Number
          validation : int range(1-5)
          default    : 5
          response   : 5
```
