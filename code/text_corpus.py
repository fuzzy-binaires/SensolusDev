

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
    and (ii) these Terms.
    """,
    """
    Subscription: The personal, limited, non-exclusive, non-assignable and non-transferable <VERB> and use right to the
    different <NOUN> of the Platform offered by SENSOLUS to the Customer, in accordance with the type of <NOUN> 
    chosen in the Agreement (i.e. <NOUN>, <NOUN>, <NOUN>).
    """,
    # from section 2: Applicability of the Terms
    """
   	Unless explicitly otherwise in writing, the offering, sale and delivery of all <NOUN>, Subscriptions and/or Services by SENSOLUS shall be governed by the present Terms.
    """,
    """
	By relying on <NOUN>, the Customer agrees to be bound by these Terms. The Terms shall always <VERB> over any terms and conditions of the Customer, which shall not be enforceable against SENSOLUS, even if the Customer (later) declares them to be the only valid <NOUN>. In the event that explicit preference is given in writing to the <NOUN> of the Customer, the following Terms shall remain valid in a supplementary way.
    """,
    # from section 3
    """
    The Customer shall be responsible for the <NOUN> of any submitted order.
    """,
    """
    The Customer shall also be responsible to give SENSOLUS any and all necessary <NOUN> 
    relating to the Hardware, <NOUN> and/or <NOUN> within a sufficient time.
    """,
    # from section 4: Cancellation
	"""
	In the event of the cancellation of the Agreement by the Customer (without this being due to a shortcoming of SENSOLUS), SENSOLUS <VERB> the right to charge the <NOUN>, Subscriptions and Services already provided (incl. <NOUN>). The aforementioned <NOUN> are increased with lump sum damages amounting to 10 percent of the total value of fees (excl. VAT) of the cancelled Agreement, with a minimum of €250, and such without prejudice to SENSOLUS’ right to compensation for higher proven damage. The same applies when SENSOLUS <VERB> the Agreement because of shortcomings of the Customer (without prejudice to other <NOUN>).
    """,
    # from section 5
    """
    Unless when otherwise agreed upon, 
    all <NOUN> of SENSOLUS regarding the Solution are to be considered <NOUN>.
    """,
    """
    Hence, SENSOLUS shall always provide the Solution with <NOUN>, 
    with appropriate care and in good faith, and shall deliver the Solution to the best of its <NOUN>, 
    skill, insight and ability, as reasonably expected of a professional experienced in services of comparable scope, complexity and size.
    """,
    """
    However, SENSOLUS does not guarantee a certain <NOUN>.
    """,
    # from section 6: Delivery
	"""
	SENSOLUS delivers <NOUN> to the Customer as described in the Agreement.
    """,
	"""
	SENSOLUS retains the entire ownership of all <NOUN> delivered to the Customer for as long as the Customer has not fully paid the price, costs, interests and all other accessories related to purchase thereof.
    """,
	"""
	The Customer must <VERB> (i) the conformity of the Hardware with <NOUN>, and (ii) the proper functioning of the Hardware, upon delivery.
    """,
	"""
	If the Hardware presents <NOUN>, the Customer must immediately (and no later than seven (7) Business Days after the delivery) <VERB> the non-conformity and/or visible defect – at the risk of <NOUN> – by email, to the address: support@sensolus.com.
    """,
	"""
	The Customer must inform SENSOLUS of any hidden <NOUN> by email to the address <VERB>@sensolus.com no later than fourteen (14) Business Days after it has/should have been detected, and in any case within twelve (12) months upon delivery, at the risk of forfeiture.
    """,
	"""
	SENSOLUS shall <VERB> and examine the <NOUN> and investigate the complaint within ten (10) Business Days. The cost of such examinations shall be payable by SENSOLUS only to the extent the claim of the defect is found to be <NOUN>.
    """,
	"""
	SENSOLUS cannot be held liable for, nor does it warrant defects caused by: <NOUN>, <VERB> <NOUN> or <NOUN>.
    """,
	"""
	SENSOLUS cannot be held liable for, nor does it warrant defects caused by: An act of the Customer or a third party, regardless of whether these were caused by a <NOUN> or <NOUN>.
	""",
    # from section 7
    """
    SENSOLUS grants the Customer a <NOUN> in accordance with 
    the <NOUN> type described in the Agreement ,subject to (i) correct and timely 
    payment of the <NOUN>, (ii) use in correspondence with the <NOUN>, and (iii) <NOUN> 
    in compliance with the Agreement and Terms.
    """,
    """
    The Subscription can include the use of <NOUN>, if specified in the Agreement.
    """,
    """
    The Customer is obligated to <VERB>, prior to concluding an Agreement, 
    whether the <NOUN> is available in the countries where it intends to use the Solution.
    """,
    """
    A regularly <NOUN> is available on the Platform and/or the Website.
    """,
    """    
    As the <NOUN> is not under the control of SENSOLUS, it can never be responsible 
    for any <NOUN> or <NOUN> in this regard.
    """,
    """
    Nonetheless, SENSOLUS <VERB> to inform the Customer on the aforementioned characteristics 
    of the <NOUN> before the Agreement is concluded.
    """,
    # from section 8: The Platform
    """
    The Customer is entitled to <VERB> and use the Platform in accordance with the applicable <NOUN> type (cfr. Article 7.1), the Acceptable Use Policy and/or Data Processing Terms.
    """,
    """
    The Platform of SENSOLUS is provided to the Customer “AS-IS”. In the event of problems with the <NOUN> of the Platform, SENSOLUS undertakes its best effort to <VERB> such issue as soon as reasonably possible without giving any guarantee.
    """,
    """
    SENSOLUS performs maintenance activities and <VERB> <NOUN> of the Platform on a regular basis. SENSOLUS strives to minimize the impact on the availability of the Platform.
    """,
    # from section 9
    """
    SENSOLUS provides different additional <NOUN> to the Customer upon request, 
    such as but not limited to <NOUN>, <NOUN>, <NOUN>, etc. 
    The specific scope, content, deadlines, etc. related to these Services will 
    be agreed upon by the parties in the Order Form.
    """,
    # from section 10: Complaint
	"""
	Any complaints concerning SENSOLUS’ Solution shall only <VERB> if submitted to SENSOLUS in writing within a period of five (5) Business Days following the discovery of the <NOUN> by the Customer. Complaints shall always be submitted to SENSOLUS by e-mail to the address support@sensolus.com, containing a detailed justification of the complaint.
	"""
    # from section 11
    """
    <NOUN> are as stated in the Order Form. 
    <NOUN> confirmed by SENSOLUS for one order are not binding for subsequent 
    orders, unless it concerns orders within a larger <NOUN> agreement.
    """
]
