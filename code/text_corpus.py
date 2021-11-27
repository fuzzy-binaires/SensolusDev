

# taken from https://www.sensolus.com/terms-conditions/
import random


def get_noun():
    return random.choice(['cat', 'dog', 'fish', 'lion'])


def get_verb():
    return random.choice(['eats', 'sleeps', 'plays', 'smiles'])


def modify_text(text):
    return text.replace('<NOUN>', get_noun()).replace('<VERB>', get_verb())


contract_text = [
    # from section 1
    """
    Agreement: the collective term for all <NOUN> related to the Solution, applicable between the Customer
    and SENSOLUS. The Agreement <VERB> of both (i) the <NOUN> (signed or otherwise accepted by the Customer), 
    and (ii) these Terms;
    """,
    """
    Subscription: The personal, limited, non-exclusive, non-assignable and non-transferable <VERB> and use right to the
    different <NOUN> of the Platform offered by SENSOLUS to the Customer, in accordance with the type of <NOUN> 
    chosen in the Agreement (i.e. Essential, Professional, Analytics);
    """,
    # from section 3
    """
    The Customer shall be responsible for the <NOUN> of any submitted order. 
    The Customer shall also be responsible to give SENSOLUS any and all necessary <NOUN> 
    relating to the Hardware, <NOUN> and/or <NOUN> within a sufficient time.
    """,
    # from section 5
    """
    Unless when otherwise agreed upon, 
    all <NOUN> of SENSOLUS regarding the Solution are to be considered <NOUN>. 
    Hence, SENSOLUS shall always provide the Solution with <NOUN>, 
    with appropriate care and in good faith, and shall deliver the Solution to the best of its <NOUN>, 
    skill, insight and ability, as reasonably expected of a professional experienced in services of comparable scope, complexity and size. However, SENSOLUS does not guarantee a certain result.
    """,

    # from section 7
    """
    SENSOLUS grants the Customer a <NOUN> in accordance with 
    the <NOUN> type described in the Agreement ,subject to (i) correct and timely 
    payment of the <NOUN>, (ii) use in correspondence with the <NOUN>, and (iii) <NOUN> 
    in compliance with the Agreement and Terms.
    """,
    """
    The Subscription can include the use of <NOUN>,
    if specified in the Agreement. 
    The Customer is obligated to <VERB>, prior to concluding an Agreement, 
    whether the <NOUN> is available in the countries where it intends to use the Solution. 
    A regularly <NOUN> is available on the Platform and/or the Website. 
    As the <NOUN> is not under the control of SENSOLUS, it can never be responsible 
    for any <NOUN> or <NOUN> in this regard. 
    Nonetheless, SENSOLUS <VERB> to inform the Customer on the aforementioned characteristics 
    of the <NOUN> before the Agreement is concluded.
    """,

    # from section 9
    """
    SENSOLUS provides different additional <NOUN> to the Customer upon request, 
    such as but not limited to <NOUN>, <NOUN>, <NOUN>, etc. 
    The specific scope, content, deadlines, etc. related to these Services will 
    be agreed upon by the parties in the Order Form.
    """,

    # from section 11
    """
    <NOUN> are as stated in the Order Form. 
    <NOUN> confirmed by SENSOLUS for one order are not binding for subsequent 
    orders, unless it concerns orders within a larger <NOUN> agreement.
    """
]
