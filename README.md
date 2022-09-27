# uriencode

Tiny python tool that will uri encode a string one or more times

## Usage

### Single pass

    $ python3 uriencode.py
    Enter string to encode: <this is my string>
    Encode how many times (default: 1)? 
    ** ** ** ** **
    ** encoding **
    ** ** ** ** **
    Encoded string: 
    %3Cthis%20is%20my%20string%3E

### Multiple passes

    $ python3 uriencode.py
    Enter string to encode: <this is my string>
    Encode how many times (default: 1)? 3
    ** ** ** ** **
    ** encoding **
    ** ** ** ** **
    Encoded string: 
    %25253Cthis%252520is%252520my%252520string%25253E
