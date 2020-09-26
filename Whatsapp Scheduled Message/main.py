""" Send scheduled whatsapp message using python
library - 
$ pip install pywhatkit

All we need is signing into whatsapp web on browser. That's it.
"""

import pywhatkit

# syntax (phone_number_in_text, message, hour_format_24hr, minute)
pywhatkit.sendwhatmsg('+97450024398', "Hello primitive human with crushable skull, how you doin'?", 2, 20)
