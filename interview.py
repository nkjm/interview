#!/usr/bin/python

# This software can be freely modified, embedded and redistributed under LGPL.
# http://www.gnu.org/copyleft/lesser.html
# Copyright Kazuki Nakajima <nkjm.kzk@gmail.com>

import string
import sys

class Interview:
    def interview(self, question, default, choice_list): 
        if (choice_list is None):
            if not default is None and default != '':
                print "Please enter %s (just Enter to accept default '%s'): " % (question, default),
            else:
                print "Please enter %s: " % question,

            for line in iter(sys.stdin.readline, ""):
                answer = line.replace("\n","")
                if not (default is None) and (answer == ""):
                    print ""
                    return default
                elif (default is None) and (answer == ""):
                    print ""
                    print "Please enter %s: " % question,
                    continue
                break
            print ""
            return answer
        else:
            print "Please select %s from following list. (Enter the number)" % question
            if not default is None and default != '':
                print "(just Enter to accept default '%s')" % default
            offset = 0
            for choice in choice_list:
                print "\t[%s] %s" % (offset, choice)
                offset = offset + 1
            print "Answer: ",
            for line in iter(sys.stdin.readline, ""):
                answer = line.replace("\n","")
                if not (default is None) and (answer == ""):
                    print ""
                    return default
                else:
                    try:
                        answer = int(answer)
                    except:
                        print "Invalide answer. Please enter the NUMBER [0-%s]." % (offset - 1)
                        print "Answer: ",
                        continue

                if (int(answer) >= 0) and (int(answer) < offset):
                    print ""
                    return (choice_list[int(answer)])
                else:
                    print "Invalide answer. Please enter the NUMBER [0-%s]." % (offset - 1)
                    print "Answer: ",

    def ask_yes_or_no(self):
        for line in iter(sys.stdin.readline, ""):
            if (line == "y\n"):
                return "yes"
            elif (line == "n\n"):
                return "no"
            else:
                print "Enter just 'y' or 'n'. [y/n]: ",

    def ask_new_name(self, question, input, default, choice_list=None):
        if input is None:
            try:
                name = self.interview(question=question, choice_list=None, default=default)
            except:
                sys.exit()
        else:
            name = input

        while True:
            if choice_list is None:
                break
            elif isinstance(choice_list, list) or isinstance(choice_list, tuple) and name not in choice_list:
                break
            elif isinstance(choice_list, list) or isinstance(choice_list, tuple) and name in choice_list:
                print "Specified NEW %s already exist. Please try another name." % question
            elif not isinstance(choice_list, list) and not isinstance(choice_list, tuple):
                print "choice_list is not neither list nor tuple."
                sys.exit()
            else:
                print "Unexpected situation."
                sys.exit()
            try:
                name = self.interview(question=question, choice_list=None, default=default)
            except:
                sys.exit()
        return name

    def ask_name_from_list(self, question, input, default, choice_list):
        if input is None:
            try:
                name = self.interview(question=question, choice_list=choice_list, default=default)
            except:
                sys.exit()
        else:
            name = input
            if not isinstance(choice_list, list) and not isinstance(choice_list, tuple):
                print "choice_list is not neither list nor tuple."
                sys.exit()
            while not name in choice_list:
                print "%s is not valid." % question
                try:
                    name = self.interview(question=question, choice_list=choice_list, default=default)
                except:
                    sys.exit()
        return name

    def ask_number(self, question, input, default):
        if input is None:
            try:
                number = self.interview(question=question, choice_list=None, default=default)
            except:
                sys.exit()
        else:
            number = input

        while True:
            if isinstance(number, int) and number > 0:
                break
            elif number.isdigit() and int(number) > 0:
                break
            else:
                print "%s is not valid." % question
            try:
                number = self.interview(question=question, choice_list=None, default=default)
            except:
                sys.exit()
        return int(number)

    def ask_list_from_list(self, question, input, default, choice_list):
        if not isinstance(choice_list, list) and not isinstance(choice_list, tuple):
            print "choice_list is not neither list nor tuple."
            sys.exit()
        dynamic_list = list(choice_list)
        name_list = []
        while True:
            if not len(name_list) == 0:
                dynamic_list.append("That's it.")
            name = self.select_from_list(question=question, choice_list=dynamic_list, input=input, default=default)
            dynamic_list.remove(name)
            if name == "That's it.":
                break
            if not name in name_list:
                name_list.append(name)
            print "Selected %s:" % question
            for i in name_list:
                print "\t" + i
            print ""
            try:
                dynamic_list.remove("That's it.")
            except:
                pass
            if len(dynamic_list) < 1:
                break
        return name_list

