#CLIENT TO SYSTEM MAIL
#!/usr/bin/python

import smtplib
import re
import os
import time

sender = 'sn.subir1997@gmail.com'
receivers = ['coolsubir1997@gmail.com']

message = """From: SN <coolsubir1997.com>
To: To Person <sn.subir1997.com>
Subject: Regarding leave due to emergency.

Respected Sir, this is to inform you that I'll be on leave from 29-01-2018 to 06-02-2018 due to certain emergencies.
Please grant me the necessary leave.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")

except SMTPException:
   print ("Error: unable to send email")
#Extract from email
time.sleep(2)

print('x')
data=""
files = [file for file in os.listdir(".") if (file.lower().endswith('.eml'))]
files.sort(key=os.path.getmtime)
for file in sorted(files, key=os.path.getmtime):
    with open(file) as myfile:
        data = myfile.readlines()
        print('data',data)






#FUTURE
"""Record of phased-in incompatible language changes.

Each line is of the form:

    FeatureName = "_Feature(" OptionalRelease "," MandatoryRelease ","
                              CompilerFlag ")"

where, normally, OptionalRelease < MandatoryRelease, and both are 5-tuples
of the same form as sys.version_info:

    (PY_MAJOR_VERSION, # the 2 in 2.1.0a3; an int
     PY_MINOR_VERSION, # the 1; an int
     PY_MICRO_VERSION, # the 0; an int
     PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" or "final"; string
     PY_RELEASE_SERIAL # the 3; an int
    )

OptionalRelease records the first release in which

    from __future__ import FeatureName

was accepted.

In the case of MandatoryReleases that have not yet occurred,
MandatoryRelease predicts the release in which the feature will become part
of the language.

Else MandatoryRelease records when the feature became part of the language;
in releases at or after that, modules no longer need

    from __future__ import FeatureName

to use the feature in question, but may continue to use such imports.

MandatoryRelease may also be None, meaning that a planned feature got
dropped.

Instances of class _Feature have two corresponding methods,
.getOptionalRelease() and .getMandatoryRelease().

CompilerFlag is the (bitfield) flag that should be passed in the fourth
argument to the builtin function compile() to enable the feature in
dynamically compiled code.  This flag is stored in the .compiler_flag
attribute on _Future instances.  These values must match the appropriate
#defines of CO_xxx flags in Include/compile.h.

No feature line is ever to be deleted from this file.
"""

all_feature_names = [
    "nested_scopes",
    "generators",
    "division",
    "absolute_import",
    "with_statement",
    "print_function",
    "unicode_literals",
    "barry_as_FLUFL",
    "generator_stop",
]

__all__ = ["all_feature_names"] + all_feature_names

# The CO_xxx symbols are defined here under the same names used by
# compile.h, so that an editor search will find them here.  However,
# they're not exported in __all__, because they don't really belong to
# this module.
CO_NESTED            = 0x0010   # nested_scopes
CO_GENERATOR_ALLOWED = 0        # generators (obsolete, was 0x1000)
CO_FUTURE_DIVISION   = 0x2000   # division
CO_FUTURE_ABSOLUTE_IMPORT = 0x4000 # perform absolute imports by default
CO_FUTURE_WITH_STATEMENT  = 0x8000   # with statement
CO_FUTURE_PRINT_FUNCTION  = 0x10000   # print function
CO_FUTURE_UNICODE_LITERALS = 0x20000 # unicode string literals
CO_FUTURE_BARRY_AS_BDFL = 0x40000
CO_FUTURE_GENERATOR_STOP  = 0x80000 # StopIteration becomes RuntimeError in generators

class _Feature:
    def __init__(self, optionalRelease, mandatoryRelease, compiler_flag):
        self.optional = optionalRelease
        self.mandatory = mandatoryRelease
        self.compiler_flag = compiler_flag

    def getOptionalRelease(self):
        """Return first release in which this feature was recognized.

        This is a 5-tuple, of the same form as sys.version_info.
        """

        return self.optional

    def getMandatoryRelease(self):
        """Return release in which this feature will become mandatory.

        This is a 5-tuple, of the same form as sys.version_info, or, if
        the feature was dropped, is None.
        """

        return self.mandatory

    def __repr__(self):
        return "_Feature" + repr((self.optional,
                                  self.mandatory,
                                  self.compiler_flag))

nested_scopes = _Feature((2, 1, 0, "beta",  1),
                         (2, 2, 0, "alpha", 0),
                         CO_NESTED)

generators = _Feature((2, 2, 0, "alpha", 1),
                      (2, 3, 0, "final", 0),
                      CO_GENERATOR_ALLOWED)

division = _Feature((2, 2, 0, "alpha", 2),
                    (3, 0, 0, "alpha", 0),
                    CO_FUTURE_DIVISION)

absolute_import = _Feature((2, 5, 0, "alpha", 1),
                           (3, 0, 0, "alpha", 0),
                           CO_FUTURE_ABSOLUTE_IMPORT)

with_statement = _Feature((2, 5, 0, "alpha", 1),
                          (2, 6, 0, "alpha", 0),
                          CO_FUTURE_WITH_STATEMENT)

print_function = _Feature((2, 6, 0, "alpha", 2),
                          (3, 0, 0, "alpha", 0),
                          CO_FUTURE_PRINT_FUNCTION)

unicode_literals = _Feature((2, 6, 0, "alpha", 2),
                            (3, 0, 0, "alpha", 0),
                            CO_FUTURE_UNICODE_LITERALS)

barry_as_FLUFL = _Feature((3, 1, 0, "alpha", 2),
                         (3, 9, 0, "alpha", 0),
                         CO_FUTURE_BARRY_AS_BDFL)

generator_stop = _Feature((3, 5, 0, "beta", 1),
                         (3, 7, 0, "alpha", 0),
                         CO_FUTURE_GENERATOR_STOP)


#UTIL UTILITIES
# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2017 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.

import re
import random

from six.moves import input


reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len,
                reverse=True)
        return  re.compile(r"\b({0})\b".format("|".join(map(re.escape,
            sorted_refl))), re.IGNORECASE)

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(lambda mo:
                self._reflections[mo.string[mo.start():mo.end()]],
                    str.lower())

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos+1:pos+2])
            response = response[:pos] + \
                self._substitute(match.group(num)) + \
                response[pos+2:]
            pos = response.find('%')
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)    # pick a random response
                resp = self._wildcards(resp, match) # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try: user_input = input(">")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.": user_input = user_input[:-1]
                print(self.respond(user_input))


#ELIZA
# Natural Language Toolkit: Eliza
#
# Copyright (C) 2001-2017 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
#          Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <mailto:jez@jezuk.co.uk>.

# a translation table used to convert things you say into things the
# computer says back, e.g. "I am" --> "you are"

#from __future__ import print_function
#from nltk.chat.util import Chat, reflections

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

pairs = (
    (r'I need (.*)',
     ("Why do you need %1?",
      "Would it really help you to get %1?",
      "Are you sure you need %1?")),

    (r'Why don\'t you (.*)',
     ("Do you really think I don't %1?",
      "Perhaps eventually I will %1.",
      "Do you really want me to %1?")),

    (r'Why can\'t I (.*)',
     ("Do you think you should be able to %1?",
      "If you could %1, what would you do?",
      "I don't know -- why can't you %1?",
      "Have you really tried?")),

    (r'I can\'t (.*)',
     ("How do you know you can't %1?",
      "Perhaps you could %1 if you tried.",
      "What would it take for you to %1?")),

    (r'I am (.*)',
     ("Did you come to me because you are %1?",
      "How long have you been %1?",
      "How do you feel about being %1?")),

    (r'I\'m (.*)',
     ("How does being %1 make you feel?",
      "Do you enjoy being %1?",
      "Why do you tell me you're %1?",
      "Why do you think you're %1?")),

    (r'Are you (.*)',
     ("Why does it matter whether I am %1?",
      "Would you prefer it if I were not %1?",
      "Perhaps you believe I am %1.",
      "I may be %1 -- what do you think?")),

    (r'What (.*)',
     ("Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?")),

    (r'How (.*)',
     ("How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?")),

    (r'Because (.*)',
     ("Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If %1, what else must be true?")),

    (r'(.*) sorry (.*)',
     ("There are many times when no apology is needed.",
      "What feelings do you have when you apologize?")),

    (r'Hello(.*)',
     ("Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?")),

    (r'I think (.*)',
     ("Do you doubt %1?",
      "Do you really think so?",
      "But you're not sure %1?")),

    (r'(.*) friend (.*)',
     ("Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?")),

    (r'Yes',
     ("You seem quite sure.",
      "OK, but can you elaborate a bit?")),

    (r'(.*) computer(.*)',
     ("Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?")),

    (r'Is it (.*)',
     ("Do you think it is %1?",
      "Perhaps it's %1 -- what do you think?",
      "If it were %1, what would you do?",
      "It could well be that %1.")),

    (r'It is (.*)',
     ("You seem very certain.",
      "If I told you that it probably isn't %1, what would you feel?")),

    (r'Can you (.*)',
     ("What makes you think I can't %1?",
      "If I could %1, then what?",
      "Why do you ask if I can %1?")),

    (r'Can I (.*)',
     ("Perhaps you don't want to %1.",
      "Do you want to be able to %1?",
      "If you could %1, would you?")),

    (r'You are (.*)',
     ("Why do you think I am %1?",
      "Does it please you to think that I'm %1?",
      "Perhaps you would like me to be %1.",
      "Perhaps you're really talking about yourself?")),

    (r'You\'re (.*)',
     ("Why do you say I am %1?",
      "Why do you think I am %1?",
      "Are we talking about you, or me?")),

    (r'I don\'t (.*)',
     ("Don't you really %1?",
      "Why don't you %1?",
      "Do you want to %1?")),

    (r'I feel (.*)',
     ("Good, tell me more about these feelings.",
      "Do you often feel %1?",
      "When do you usually feel %1?",
      "When you feel %1, what do you do?")),

    (r'I have (.*)',
     ("Why do you tell me that you've %1?",
      "Have you really %1?",
      "Now that you have %1, what will you do next?")),

    (r'I would (.*)',
     ("Could you explain why you would %1?",
      "Why would you %1?",
      "Who else knows that you would %1?")),

    (r'Is there (.*)',
     ("Do you think there is %1?",
      "It's likely that there is %1.",
      "Would you like there to be %1?")),

    (r'My (.*)',
     ("I see, your %1.",
      "Why do you say that your %1?",
      "When your %1, how do you feel?")),

    (r'You (.*)',
     ("We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I %1?")),

    (r'Why (.*)',
     ("Why don't you tell me the reason why %1?",
      "Why do you think %1?")),

    (r'I want (.*)',
     ("What would it mean to you if you got %1?",
      "Why do you want %1?",
      "What would you do if you got %1?",
      "If you got %1, then what would you do?")),

    (r'(.*) mother(.*)',
     ("Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important.")),

    (r'(.*) father(.*)',
     ("Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?")),

    (r'(.*) child(.*)',
     ("Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?")),

    (r'(.*)\?',
     ("Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?")),

    (r'quit',
     ("Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!")),

    (r'(.*)',
     ("Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that %1?",
      "I see.",
      "Very interesting.",
      "%1.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"))
)

eliza_chatbot = Chat(pairs, reflections)


def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('=' * 72)
    print("Hello.  How are you feeling today?")

    eliza_chatbot.converse()


def demo():
    eliza_chat()


if __name__ == "__main__":
    demo()

#SYSTEM TO CLIENT
#!/usr/bin/python

sender = 'sn.subir1997@gmail.com'
receivers = ['coolsubir1997@gmail.com']

message = """From: SN <coolsubir1997.com>
To: To Person <sn.subir1997.com>
Subject: Regarding leave due to emergency.

Respected Sir, this is to inform you that I'll be on leave from 29-01-2018 to 06-02-2018 due to certain emergencies.
Please grant me the necessary leave.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")

except SMTPException:
   print ("Error: unable to send email")