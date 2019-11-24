from intent import *
import re
from answer_dictionary import DEFAULT


input_intents=['keyword','source','domain']
sort_intents=['similar','popular']


def match_date(message):
    connections=['\.','/','-']
    l=['([0-9]{4})','([0-9]{1,2})','([0-9]{1,2})']
    pattern_string=['('+conn.join(l)+')' for conn in connections]
    pattern_string='|'.join(pattern_string)
    print(pattern_string)
    date_pattern=re.compile(pattern_string)
    return date_pattern.search(message)


def interpret(message,last_state):
    words=message.split()
    if 'news' in words:
        return 'read_news'
    date=match_date(message)
    if date:
        if last_state==INPUT:
            return 'date',date.group()
        elif last_state==GIVEN:
            return 'date_sort',date.group()
        else:
            return 'none',None
    for input_intent in input_intents:
        if input_intent in words:
            index=words.index(input_intent)
            addition=words[index+1]
            return input_intent,addtion
    for sort_intent in sort_intents:
        if sort_intent in words:
            return sort_intent,None
    return 'none',None


def respond(message,state,search_sequence,policy=policy_rules):
    intent,addition=interpret(message)
    if intent,state in policy:
        new_state,answer=policy[(intent,state)]
        if state in GIVEN_STATES:
            assert hasattr(answer,'__call__')
            answer=answer(intent,addition)
            search_sequence=intent,addition
        if state in SORTED_STATES:
            assert hasattr(answer,'__call__')
            search_intent,search_addition=search_sequence
            answer=answer(search_intent,search_addition,intent,addition)
        if new_state,None in policy:
            new_state,_=policy[new_state,None]
        return new_state,answer
    else:
        return state,DEFAULT[0]


if __name__=='__main__':
    print(match_date('my birthday is 2003/07/12'))