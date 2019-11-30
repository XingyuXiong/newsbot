if __package__:
    from scripts.answer_dictionary import *
    from scripts.generate import read,sort
else:
    from answer_dictionary import *
    from generate import read,sort


INIT=0
INPUT=1
DEFAULT_RANDOM_HEADLINES=2
RETURN_WITH_KEYWORD=3
RETURN_WITH_DATE=4
RETURN_WITH_SOURCE=5
RETURN_WITH_DOMAIN=6
GIVEN_STATES=[DEFAULT_RANDOM_HEADLINES,RETURN_WITH_KEYWORD,RETURN_WITH_DATE,RETURN_WITH_SOURCE,RETURN_WITH_DOMAIN]
GIVEN=10

SORT_WITH_DATE=7
SORT_WITH_SIMILARITY=8
SORT_WITH_POPULARITY=9
SORTED_STATES=[SORT_WITH_DATE,SORT_WITH_SIMILARITY,SORT_WITH_POPULARITY]


policy_rules={
    (INIT,'read_news'):(INPUT,NEWS_INQUIRY[0]),
    (INIT,'none'):(INIT,NEWS_INQUIRY[1]),
    #(INPUT,'none'):(DEFAULT_RANDOM_HEADLINES,'Alright, here is headlines for today\'s news'),
    (INPUT,'none'):(INIT,NEWS_INQUIRY[1]),
    (INPUT,'keyword'):(RETURN_WITH_KEYWORD,read),
    (INPUT,'date'):(RETURN_WITH_DATE,read),
    (INPUT,'source'):(RETURN_WITH_SOURCE,read),
    (INPUT,'domain'):(RETURN_WITH_DOMAIN,read),
    (GIVEN,'date_sort'):(SORT_WITH_DATE,sort),
    (GIVEN,'sim_sort'):(SORT_WITH_SIMILARITY,sort),
    (GIVEN,'pop_sort'):(SORT_WITH_POPULARITY,sort),
}
for GIVEN_STATE in GIVEN_STATES:
    policy_rules[(GIVEN_STATE,None)]=(GIVEN,None)