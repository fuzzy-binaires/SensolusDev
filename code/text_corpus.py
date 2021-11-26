

# taken from https://www.sensolus.com/terms-conditions/
import random


def get_noun():
    return random.choice(['cat', 'dog', 'fish', 'lion'])


def get_verb():
    return random.choice(['eats', 'sleeps', 'plays', 'smiles'])


text_corpus = [
    # from section 1
    f"""
    Agreement: the collective term for all {get_noun()} related to the Solution, applicable between the Customer
    and SENSOLUS. The Agreement {get_verb()} of both (i) the {get_noun()} (signed or otherwise accepted by the Customer), 
    and (ii) these Terms;
    """,
    f"""
    Subscription: The personal, limited, non-exclusive, non-assignable and non-transferable {get_verb()} and use right to the
    different {get_noun()} of the Platform offered by SENSOLUS to the Customer, in accordance with the type of {get_noun()} 
    chosen in the Agreement (i.e. Essential, Professional, Analytics);
    """,
    # from section 3
    f"""
    The Customer shall be responsible for the {get_noun()} of any submitted order. 
    The Customer shall also be responsible to give SENSOLUS any and all necessary {get_noun()} 
    relating to the Hardware, {get_noun()} and/or {get_noun()} within a sufficient time.
    """,
    # from section 5
    f"""
    Unless when otherwise agreed upon, 
    all {get_noun()} of SENSOLUS regarding the Solution are to be considered {get_noun()}. 
    Hence, SENSOLUS shall always provide the Solution with {get_noun()}, 
    with appropriate care and in good faith, and shall deliver the Solution to the best of its {get_noun()}, 
    skill, insight and ability, as reasonably expected of a professional experienced in services of comparable scope, complexity and size. However, SENSOLUS does not guarantee a certain result.
    """,

    # from section 7
    f"""
    SENSOLUS grants the Customer a {get_noun()} in accordance with 
    the {get_noun()} type described in the Agreement ,subject to (i) correct and timely 
    payment of the {get_noun()}, (ii) use in correspondence with the {get_noun()}, and (iii) {get_noun()} 
    in compliance with the Agreement and Terms.
    """,
    f"""
    The Subscription can include the use of {get_noun()},
    if specified in the Agreement. 
    The Customer is obligated to {get_verb()}, prior to concluding an Agreement, 
    whether the {get_noun()} is available in the countries where it intends to use the Solution. 
    A regularly {get_noun()} is available on the Platform and/or the Website. 
    As the {get_noun()} is not under the control of SENSOLUS, it can never be responsible 
    for any {get_noun()} or {get_noun()} in this regard. 
    Nonetheless, SENSOLUS {get_verb()} to inform the Customer on the aforementioned characteristics 
    of the {get_noun()} before the Agreement is concluded.
    """,

    # from section 9
    f"""
    SENSOLUS provides different additional {get_noun()} to the Customer upon request, 
    such as but not limited to {get_noun()}, {get_noun()}, {get_noun()}, etc. 
    The specific scope, content, deadlines, etc. related to these Services will 
    be agreed upon by the parties in the Order Form.
    """,

    # from section 11
    f"""
    {get_noun()} are as stated in the Order Form. 
    {get_noun()} confirmed by SENSOLUS for one order are not binding for subsequent 
    orders, unless it concerns orders within a larger {get_noun()} agreement.
    """
]

print(random.choice(text_corpus))