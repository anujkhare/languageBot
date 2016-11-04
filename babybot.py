import json
# from pprint import pprint
import readline

from complete import MyCompleter


def printOpts(cur_replies):
    for i, reply in enumerate(cur_replies):
        print i, ':', reply


# set tab key to be the completer
readline.parse_and_bind('tab: complete')
readline.set_completer_delims('\n')


with open('questions.json') as in_file:
    qa = json.load(in_file)

questions = qa["bot"]
replies = qa["replies"]

curQ = questions.get("_start_", None)
if not curQ:
    print('Questions file does not have a "_start_" question.')
    raise()

while(curQ.get("id", "_end_") != "_end_"):
    # Print the Bot's questions/statement
    print
    print "Anuj says:", curQ["str"]

    # get the list of possible replies
    cur_replies = []
    cur_reply_ids = []
    for reply_id in curQ["replies"]:
        if not replies.get(reply_id):
            print('Reply "' + reply_id + '" is not in replies!')
            raise()

        cur_reply_list = replies[reply_id]["list"]
        cur_replies.extend(cur_reply_list)
        cur_reply_ids.extend([reply_id] * len(cur_reply_list))

    # set the current replies for auto-complete
    completer = MyCompleter(cur_replies)
    readline.set_completer(completer.complete)
    # set tab key to be the completer
    readline.parse_and_bind('tab: complete')
    # add the words to the history
    for kw in cur_replies:
        readline.add_history(kw)

    # # try to input a valid reply using option list
    # while True:
    #     printOpts(cur_replies)
    #     opt = input("Enter your selection:")
    #     opt = int(opt)
    #     if opt < len(cur_replies) and 0 <= opt:  # a valid option
    #         break
    #     print("Invalid choice")

    # Try to get a valid input!
    print(' ; '.join(cur_replies))
    while True:
        reply = raw_input("Say something: ")
        # TODO: Ideally, have back links / dicts with replies mapping to nextQIds,
        # have a script to precompute such a mapping from the current JSON.
        try:
            opt = cur_replies.index(reply)
            break
        except ValueError:
            print("That is not a valid response!")

    # print "You selected:", cur_replies[opt], cur_reply_ids[opt]
    nextQIds = replies[cur_reply_ids[opt]]["nextQ"]
    # We can have some "non-reply" statements before the actual question.
    # later I might switch to a stack based model to have nested conversations.
    num_qs = len(nextQIds)
    for i in range(num_qs - 1):
        print(questions[nextQIds[i]]["str"])

    # the question to ask will be the last one in the list
    curQ = questions[nextQIds[num_qs - 1]]
    # print(curQ)
