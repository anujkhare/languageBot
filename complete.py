import readline


class MyCompleter(object):  # Custom completer
    def __init__(self, options):
        self.options = sorted(options)
        self.matches = self.options

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                if s and text in s]
            else:  # no text entered, all matches possible
                pass
                # self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None

if __name__ == "__main__":
    keywords = ["hello", "hi", "how", "how is everyone?", "how are you", "goodbye", "great"]
    completer = MyCompleter(keywords)
    readline.set_completer(completer.complete)
    # set tab key to be the completer
    readline.parse_and_bind('tab: complete')
    readline.set_completer_delims('\n')
    # add the words to the history
    for kw in keywords:
        readline.add_history(kw)

    i = raw_input("Input: ")
    print "You entered", i
