# send_emails_with_python

# Language used:
   
   - Python 3.11.2
   - python-decouple
  
# About the program:
  
   This Python code aims to enable the asynchronous sending of emails using the smtplib library and the threading functionality from the threading library. It is designed to send an email after a certain period of time, specified as an argument. The content of the email is generated from an HTML template read from a file.

   The decouple library is used to read the sender's email credentials (email address and password) from an external configuration file. This helps to keep the credentials out of the source code, enhancing security.

The interesting part of this code is its ability to perform easy and free email marketing, fully functional on any mail server.

# Example of forwarded email marketing:
![image](https://user-images.githubusercontent.com/95552879/255031482-b60713bf-12bf-4597-a3f5-0fda47545493.png)

Check out this repository for more information on creating your email template:

https://github.com/gabflag/make_your_own_email_marketing

# Dev Comments:
   
   I had an issue that was occurring because the .format() method was being applied to the content of the HTML template, which caused conflicts with the replacement of the {} curly braces that are part of the CSS code. Since CSS also uses curly braces {} to define style blocks, the .format() method was interpreting these braces as placeholders for string formatting, which resulted in an error.

   By removing the usage of the .format() method and directly setting the email body as the content of the HTML template, I managed to avoid this conflict and allowed the HTML to be sent without unwanted changes or execution errors.

   An important point was convert html into string specifying UTF-8

# Read here if you have questions on how to download and use the code:

https://github.com/gabflag/readme#readme
