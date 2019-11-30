import re
if __package__:
    from scripts.intent import *
    from scripts.answer_dictionary import DEFAULT,INIT_GREETINGS,SHOW_LIST 
else:
    from intent import *
    from answer_dictionary import DEFAULT,INIT_GREETINGS,SHOW_LIST


input_intents=['keyword','source','domain']
sort_intents=['similar','popular']


def match_date(message):
    connections=['\.','/','-']
    l=['([0-9]{4})','([0-9]{1,2})','([0-9]{1,2})']
    pattern_string=['('+conn.join(l)+')' for conn in connections]
    pattern_string='|'.join(pattern_string)
    date_pattern=re.compile(pattern_string)
    return date_pattern.search(message)


def interpret(message,last_state):
    words=message.split()
    if 'news' in words:
        return 'read_news',None
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
            return input_intent,addition
    for sort_intent in sort_intents:
        if sort_intent in words:
            return sort_intent,None
    return 'none',None


def respond(message,state,search_sequence,policy=policy_rules):
    intent,addition=interpret(message,state)
    print('get intent:'+intent+' state is:'+str(state))
    if (state,intent) in policy:
        new_state,answer=policy[(state,intent)]
        if new_state in GIVEN_STATES:
            assert hasattr(answer,'__call__')
            answer=answer(intent,addition)
            assert type(answer)==list
            #print(answer)
            answer=format_list(answer)
            #print(answer)
            search_sequence=intent,addition
        if new_state in SORTED_STATES:
            assert hasattr(answer,'__call__')
            (search_intent,search_addition)=search_sequence
            answer=answer(search_intent,search_addition,intent,addition)
            assert type(answer)==list
            answer=format_list(answer)
        if (new_state,None) in policy:
            new_state,_=policy[new_state,None]
        return answer,new_state,search_sequence
    else:
        return DEFAULT[0],state,search_sequence


def format_list(title_list):
    return SHOW_LIST[0].format('<br>'.join(['"'+title+'"' for title in title_list]))


def start():
    state=0
    answer=INIT_GREETINGS[0]
    search_sequence=('','')
    return answer,state,search_sequence


def bot_template(answer):
    if type(answer)==str:
        print('bot:{0}'.format(answer))
    else:
        print('bot:{0}'.format(''))


if __name__=='__main__':
    from generate import read,sort
    TEST_TYPE=1
    user_template='user:{0}'
    bot_template='bot:{0}'
    answer,state,search_sequence=start()
    if TEST_TYPE==0:
        message=''
        while(message!='\n'):
            print(bot_template.format(answer))
            message=input('user:')
            answer,state,search_sequence=respond(message,state,search_sequence)
    if TEST_TYPE==1:
        messages=['hi, I want to read some news','keyword France']
        print(bot_template.format(answer))
        for message in messages:
            print(user_template.format(message))
            answer,state,search_sequence=respond(message,state,search_sequence)
            print(bot_template.format(answer))