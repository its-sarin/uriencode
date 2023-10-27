# uriencode

Tiny python tool that will uri encode a string one or more times

## Usage

### Single pass

    $ python3 uriencode.py --string <this is my string>
    
    Encoded string: 
    %3Cthis%20is%20my%20string%3E

### Multiple passes

    $ python3 uriencode.py --string <this is my string> --count 3
    
    Encoded string: 
    %25253Cthis%252520is%252520my%252520string%25253E

### Encode ALL characters (including . and /)

    $ python3 uriencode.py --string ../this/is/my/string/.. --all

    Encoded string:
    %2E%2E%2Fthis%2Fis%2Fmy%2Fstring%2F%2E%2E