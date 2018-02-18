#CLIENT TO SYSTEM MAIL TKINTER
#!/usr/bin/python

import smtplib
import re
import os
import time
import pandas as pd
from tkinter import*

import numpy as np




outside = ['Farmer','Farmer','Farmer','Farmer','employement','employement','employement','employement']
inside = [1,2,3,4,1,2,3,4]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df=pd.DataFrame([['Gramin Bhandaran Yojana','Under this Gramin provides supports to an individual, a company, a farmer , local government, NGOs and various associations'],['Livestock Insurance Scheme','Under the scheme, the crossbred and high yielding cattle and buffaloes are being insured at maximum of their current market price. '],['National Scheme on Welfare of Fishermen','The Centrally Sponsored ‘National Scheme of Welfare of Fishermen’ envisaging to provide financial assistance to fishers for construction of house, community hall for recreation and common working place and installation of tube-wells for drinking water and assistance during lean period through saving cum relief component was in operation till the terminal year of the 9th Plan. This welfare scheme has been continued during the 10th Plan. The Plan Outlay approved for the scheme for the entire period of the 10th Plan is Rs 120 crore.'],['Rashtriya Krishi Vikas Yojana','Components of the schemes:The scheme is operated as a Centrally Sponsored Scheme through States/UT’s/FISHCOPFED (Insurance component only) and has the following three broad components:- 1:Development of Model Fishermen Villages. 2: Group Accident Insurance for Active Fishermen and 3:Saving-cum-Relief.This programme is essentially a State Plan Scheme that seeks to provide the States and Territories of India with the autonomy to draw up plans for increased public investment in Agriculture by incorporating information on local requirements,geographical/climatic conditions, available natural resources/ technology and cropping patterns in their districts so as to significantly increase the productivity of Agriculture and its allied sectors and eventually maximize the returns of farmers in agriculture and its allied sectors.A State is eligible for funding under the RKVY if it maintains or increases the percentage of its expenditure on Agriculture and its Allied Sectors with respect to the total State Plan Expenditure, where the Base Line (which will move every year) for this expenditure is the average of the percentage of expenditure incurred by a State Government for the previous three years on Agriculture and its Allied Sectors minus any funds related to Agriculture and its allied sectors that it may already have received in that time under its State Plan.'],['Mahatma Gandhi National Rural Employment Guarantee Act','The MGNREGA was initiated with the objective of  enhancing livelihood security in rural areas by providing at least 100 days of guaranteed wage employment in a financial year, to every household whose adult members volunteer to do unskilled manual work .[7] Another aim of MGNREGA is to create durable assets (such as roads, canals, ponds, wells). Employment is to be provided within 5 km of an applicants residence, and minimum wages are to be paid. If work is not provided within 15 days of applying, applicants are entitled to an unemployment allowance. Thus, employment under MGNREGA is a legal entitlement.'],['Sampoorna Grameen Rozgar Yojana','Sampoorna Grameen Rojgar Yojana (SGRY) was a dual objective programme that aimed to break the cycle of unemployment and food insecurity by providing wage employment during the lean agricultural season, and by creating rural infrastructure. The self-targeting programme was open to all rural poor with a desire to supplement their primary income by doing unskilled manual work near their villages but laid special emphasis on women, Scheduled Caste (SC), Scheduled Tribes (ST) and parents of children withdrawn from hazardous occupations'],['Swarnajayanti Gram Swarozgar Yojana','The SGSY(Swarnajayanti Gram Swarojgar Yojana) aims at providing self-employment to villagers through the establishment of self-help groups. Activity clusters are established based on the aptitude and skill of the people which are nurtured to their maximum potential. Funds are provided by NGOs, banks and financial institutions.'],['National Career Service (India)(NCS)','A National ICT based portal is developed primarily to connect the opportunities with the aspirations of youth. This portal facilitates registration of job seekers, job providers, skill providers, career counsellors, etc.']],index=hier_index,columns=['Schemes','Description'])






root= Tk()
root.config(bg="#6C7A89", )
root.title("SKAR")


#user mail
user_email = Label(root, text="Enter your Mail address:  ")
user_email.pack()
user_email.config(bg="black", fg="white")

var1 = Entry(root, bd =2.75,bg="#ECECEC")
var1.pack(fill=X)

#receiver email
receiver_email = Label(root, text="Enter the recipient's email address: ")
receiver_email.pack( )
receiver_email.config(bg="black", fg="white")


var2 = Entry(root, bd =2.75,bg="#ECECEC")
var2.pack(fill=X)

#subject line
subj= Label(root, text="Enter your subject here: ")
subj.pack( )
subj.config(bg="black", fg="white")


var3 = Entry(root, bd =2.75,bg="#ECECEC")
var3.pack(fill=X)



#Body of the message
body = Text(root, font="Tahoma",  relief=SUNKEN , bd=8)
body.config(bg="#ECECEC", height=15)
body.pack(fill=BOTH, expand=True)

def get_var():

    global sender
    sender=var1.get()
    global receiver
    receiver=var2.get()
    global subject
    subject=var3.get()
    global mail
    mail=body.get("1.0","end-1c")
    root.quit()



#submit button
submit_mail = Button(root, bd =1.75, text="Click here to submit the mail", command=get_var)
submit_mail.pack(fill=X)

root.mainloop()




message = """From:"""+sender+"""
To: """+receiver+"""
Subject:"""+subject+"""\n"""+mail

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receiver, message)
   print ("Successfully sent email")

except SMTPException:
   print ("Error: unable to send email")
#Extract from email


data=""
files = [file for file in os.listdir(".") if (file.lower().endswith('.eml'))]
files.sort(key=os.path.getmtime)
for file in sorted(files, key=os.path.getmtime):
    with open(file) as myfile:
        data = myfile.readlines()

print(subject,mail)






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

    # Hold a conversation with a bot
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try: user_input = mail
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.": user_input = user_input[:-1]
                s=(self.respond(user_input))
                message = "Respected Sir/Madam\n"+ s

                master = Tk()
                master.config(bg="#6C7A89", )

                # user mail
                user_email = Label(master, text="From:  ")
                user_email.pack()
                user_email.config(bg="black", fg="white")

                var1 = Label(master, bd=2.75,text=receiver)
                var1.pack(fill=X)

                # receiver email
                receiver_email = Label(master, text="To:")
                receiver_email.pack()
                receiver_email.config(bg="black", fg="white")

                var2 = Label(master, bd=2.75,text=sender)
                var2.pack(fill=X)

                # subject line
                subj = Label(master, text="Subject")
                subj.pack()
                subj.config(bg="black", fg="white")

                var3 = Label(master, bd=2.75,text=subject)
                var3.pack(fill=X)

                # Body of the message
                frame=Frame(master)
                frame.pack()
                body = Frame(frame)
                text=Text(body)
                text.insert(INSERT,message)
                scroll=Scrollbar(body)
                text.configure(yscrollcommand=scroll.set)
                text.pack()
                scroll.pack(side=RIGHT,fill=Y)
                body.pack()
                #body.config(bg="red", height=15)





                # submit button


                master.mainloop()

                try:
                    smtpObj = smtplib.SMTP('localhost')
                    smtpObj.sendmail(sender, receiver, message)


                except SMTPException:
                    print("Error: unable to send email")

            user_input=quit


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


(r'(.*)GNREG(.*)',
     (df.loc['employement'].loc[1]['Description'],
      df.loc['employement'].loc[1]['Description'],)),

(r'(.*)pooran Gramin Rojgar Yoja(.*)',
 (df.loc['employement'].loc[2]['Description'],
  df.loc['employement'].loc[2]['Description'],)),

(r'(.*)arnj(.*)ti Gram Sw(.*)gar Yoj(.*)',
 (df.loc['employement'].loc[3]['Description'],
  df.loc['employement'].loc[3]['Description'],)),

(r'(.*)tional Career Servic(.*)',

 (df.loc['employement'].loc[4]['Description'],
  df.loc['employement'].loc[4]['Description'],)),

(r'(.*)amin Bh(.*)ar(.*)n Yoj(.*)',
 (df.loc['Farmer'].loc[1]['Description'],df.loc['Farmer'].loc[1]['Description'])),

(r'(.*)vestock Insurance Sche(.*)',
 (df.loc['Farmer'].loc[2]['Description'],
  df.loc['Farmer'].loc[2]['Description'])),

(r'(.*)at(.*)nal(.*)cheme(.*)on(.*)lfare of Fis(.*)rm(.*)',
 (df.loc['Farmer'].loc[3]['Description'],
  df.loc['Farmer'].loc[3]['Description'],)),

(r'(.*)shtriya Krishi Vikas Yoj(.*)',

 (df.loc['Farmer'].loc[4]['Description'],
  df.loc['Farmer'].loc[4]['Description'],)),

  (r'(.*)employ(.*)scheme(.*)',
  ( "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4])),

  (r'(.*)scheme(.*)employ(.*)',
  ( "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
  "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4])),


  (r'(.*)job(.*)opportunit(.*)',
  ( "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:"+df.loc['employement']['Schemes'].loc[1]+'\n'+df.loc['employement']['Schemes'].loc[2]+'\n'+df.loc['employement']['Schemes'].loc[3]+'\n'+df.loc['employement']['Schemes'].loc[4])),

  (r'(.*)opportunit(.*)job(.*)',
   ("According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4])),

  (r'(.*)scheme(.*)farm(.*)',
  ("According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'(.*)farm(.*)scheme(.*)',
  ( "According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'(.*)opportunit(.*)farm(.*)',
  ( "According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'(.*)farm(.*)opportunit(.*)',
  ( "According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'(.*)scheme(.*)',
  ( "Hello!\nWelcome to RTI Dept.\nFor which Department, Sir/Ma'am?",
    "Hello!\nWelcome to RTI Dept.\nWhich Department are you concerned with?",
    )),

  (r'(.*)opportunit(.*)',
  ( "Hello!\nWelcome to RTI Dept.\nFor which Department, Sir/Ma'am?",
    "Hello!\nWelcome to RTI Dept.\nWhich Department are you concerned with?",
    )),


  (r'farm(.*)',
   ("According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'(.*)farm(.*)',
  ( "According to your request of farming dept, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['Farmer']['Schemes'].loc[1] + '\n' + df.loc['Farmer']['Schemes'].loc[2] + '\n' +
    df.loc['Farmer']['Schemes'].loc[3] + '\n' + df.loc['Farmer']['Schemes'].loc[4])),

  (r'employ(.*)',
  ( "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4])),

  (r'(.*)employ(.*)',
  ( "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4])),

  (r'job(.*)',
  ( "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4])),

  (r'(.*)job(.*)',
  ( "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4],
    "According to your request of employment, we have following opportunities for you:" +
    df.loc['employement']['Schemes'].loc[1] + '\n' + df.loc['employement']['Schemes'].loc[2] + '\n' +
    df.loc['employement']['Schemes'].loc[3] + '\n' + df.loc['employement']['Schemes'].loc[4])),

  (r'I am(.*)',
  ( "Hello!\nWelcome to RTI Dept.\nWhat do you want to query about?",
    "Hello!\nWelcome to RTI Dept.\nHow can we help you?",
    )),
  (r'(.*)',
  ( "Hello!\nWelcome to RTI Dept.\nPlease be precise with your queries, Sir/Ma'am.",
    "Hello!\nWelcome to RTI Dept.\nPlease use accurate keywords, Sir/Ma'am."))

)

eliza_chatbot = Chat(pairs, reflections)


def eliza_chat():
    eliza_chatbot.converse()


def demo():
    eliza_chat()


if __name__ == "__main__":
    demo()

#SYSTEM TO CLIENT
#!/usr/bin/python


