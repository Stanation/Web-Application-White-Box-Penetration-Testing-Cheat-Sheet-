# Web Application White Box Penetration Testing Cheat Sheet

This repository, which is under contruction, will provide useful documentation on tools to use for conducting web application white box penetration testing.
Python code templates will also be provided to help the community to quickly write python 3 exploits when security issues are identify.

# Methodology

## Top Down Approach (TDA)
Start from the source code, identify the code architecture, endpoints, functionality. Look for issues then go into the web application and try to reach them.
 
## Bottom Up Approach (BUA)
Start from the web application, identify functionality, use web proxy to analyse requests and response. Then go into the source code and identify specific sections of the source code, functions/methods and files used by the functionality. Try to identify issues by starting from these sections of the source code.

# Tools
## Source code recovery
### From JAR file to Java file 
### From .NET DLL to C#

## Debugging
### PHP web application
### Java web application
### Javascript web application


# Common Issues
## Cross Site Scripting (XSS)
## Insecure Deserialization
## File upload restriction bypass
## Time based randomisation
## Type juggling
## Server Side Template injection (SSTI)
## SQL injection