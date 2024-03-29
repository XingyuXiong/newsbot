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
SORTED=11

GIVEN_CHOOSE=20


policy_rules={
    (INIT,'read_news'):(INPUT,NEWS_INQUIRY[0]),
    (INIT,'none'):(INIT,NEWS_INQUIRY[1]),
    #(INPUT,'none'):(DEFAULT_RANDOM_HEADLINES,'Alright, here is headlines for today\'s news'),
    (INPUT,'keyword'):(RETURN_WITH_KEYWORD,read),
    (INPUT,'date'):(RETURN_WITH_DATE,read),
    (INPUT,'source'):(RETURN_WITH_SOURCE,read),
    (INPUT,'domain'):(RETURN_WITH_DOMAIN,read),
    (INPUT,'none'):(INIT,NEWS_INQUIRY[1]),
    (GIVEN,'date_sort'):(SORT_WITH_DATE,sort),
    (GIVEN,'relevant'):(SORT_WITH_SIMILARITY,sort),
    (GIVEN,'popular'):(SORT_WITH_POPULARITY,sort),
    (GIVEN,'choose'):(GIVEN_CHOOSE,read),
    (GIVEN,'none'):(INIT,NEWS_INQUIRY[1]),
    (SORTED,'none'):(INIT,NEWS_INQUIRY[1]),
}
for GIVEN_STATE in GIVEN_STATES:
    policy_rules[(GIVEN_STATE,None)]=(GIVEN,None)
for SORTED_STATE in SORTED_STATES:
    policy_rules[(SORTED_STATE,None)]=(SORTED,None)