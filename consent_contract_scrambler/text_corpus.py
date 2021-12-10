# -*- coding: utf-8 -*-

# taken from https://www.sensolus.com/terms-conditions/
import random
from os.path import isfile
from .utils import concat_pwd

verb_list = []
noun_list = []


def initialize():
    global verb_list
    global noun_list
    verb_file_name = concat_pwd('verb_list.txt')
    noun_file_name = concat_pwd('noun_list.txt')
    if not isfile(verb_file_name):
        raise Exception(' file not found {}'.format(verb_file_name))

    if not isfile(noun_file_name):
        raise Exception(' file not found {}'.format(noun_file_name))

    with open(verb_file_name) as file:
        verb_list = [word.rstrip() for word in file.readlines()]

    with open(noun_file_name) as file:
        noun_list = [word.rstrip() for word in file.readlines()]


def modify_text(text):
    while text.find('<NOUN>') != -1:
        text = text.replace('<NOUN>', random.choice(noun_list), 1)

    while text.find('<VERB>') != -1:
        text = text.replace('<VERB>', random.choice(verb_list), 1)

    return text


contract_text = [
    # from section 1
    """Agreement: the collective term for all <NOUN> related to the Solution, applicable between the Customer and SENSOLUS. The Agreement <VERB> of both (i) the <NOUN> (signed or otherwise accepted by the Customer), and (ii) these Terms.""",
    """ Subscription: The personal, limited, non-exclusive, non-assignable and non-transferable <VERB> and use right to the different <NOUN> of the Platform offered by SENSOLUS to the Customer, in accordance with the type of <NOUN> chosen in the Agreement (i.e. <NOUN>, <NOUN>, <NOUN>).""",
    # from section 2: Applicability of the Terms
    """Unless explicitly otherwise in writing, the offering, sale and delivery of all <NOUN>, Subscriptions and/or Services by SENSOLUS shall be governed by the present Terms.""",
    """By relying on <NOUN>, the Customer agrees to be bound by these Terms. The Terms shall always <VERB> over any terms and conditions of the Customer, which shall not be enforceable against SENSOLUS, even if the Customer (later) declares them to be the only valid <NOUN>. In the event that explicit preference is given in writing to the <NOUN> of the Customer, the following Terms shall remain valid in a supplementary way.""",
    # from section 3
    """The Customer shall be responsible for the <NOUN> of any submitted order.""",
    """The Customer shall also be responsible to give SENSOLUS any and all necessary <NOUN> relating to the Hardware, <NOUN> and/or <NOUN> within a sufficient time.""",
    # from section 4: Cancellation
    """In the event of the cancellation of the Agreement by the Customer (without this being due to a shortcoming of SENSOLUS), SENSOLUS <VERB> the right to charge the <NOUN>, Subscriptions and Services already provided (incl. <NOUN>). The aforementioned <NOUN> are increased with lump sum damages amounting to 10 percent of the total value of fees (excl. VAT) of the cancelled Agreement, with a minimum of €250, and such without prejudice to SENSOLUS’ right to compensation for higher proven damage. The same applies when SENSOLUS <VERB> the Agreement because of shortcomings of the Customer (without prejudice to other <NOUN>).""",
    # from section 5
    """Unless when otherwise agreed upon, all <NOUN> of SENSOLUS regarding the Solution are to be considered <NOUN>.""",
    """Hence, SENSOLUS shall always provide the Solution with <NOUN>, with appropriate care and in good faith, and shall deliver the Solution to the best of its <NOUN>, skill, insight and ability, as reasonably expected of a professional experienced in services of comparable scope, complexity and size.""",
    """However, SENSOLUS does not guarantee a certain <NOUN>.""",
    # from section 6: Delivery
    """SENSOLUS delivers <NOUN> to the Customer as described in the Agreement.""",
    """SENSOLUS retains the entire ownership of all <NOUN> delivered to the Customer for as long as the Customer has not fully paid the price, costs, interests and all other accessories related to purchase thereof.""",
    """The Customer must <VERB> (i) the conformity of the Hardware with <NOUN>, and (ii) the proper functioning of the Hardware, upon delivery.""",
    """If the Hardware presents <NOUN>, the Customer must immediately (and no later than seven (7) Business Days after the delivery) <VERB> the non-conformity and/or visible defect – at the risk of <NOUN> – by email, to the address: support@sensolus.com.""",
    """The Customer must inform SENSOLUS of any hidden <NOUN> by email to the address <VERB>@sensolus.com no later than fourteen (14) Business Days after it has/should have been detected, and in any case within twelve (12) months upon delivery, at the risk of forfeiture.""",
    """SENSOLUS shall <VERB> and examine the <NOUN> and investigate the complaint within ten (10) Business Days. The cost of such examinations shall be payable by SENSOLUS only to the extent the claim of the defect is found to be <NOUN>.""",
    """SENSOLUS cannot be held liable for, nor does it warrant defects caused by: <NOUN>, <VERB> <NOUN> or <NOUN>.""",
    """SENSOLUS cannot be held liable for, nor does it warrant defects caused by: An act of the Customer or a third party, regardless of whether these were caused by a <NOUN> or <NOUN>.""",
    # from section 7
    """SENSOLUS grants the Customer a <NOUN> in accordance with the <NOUN> type described in the Agreement ,subject to (i) correct and timely payment of the <NOUN>, (ii) use in correspondence with the <NOUN>, and (iii) <NOUN> in compliance with the Agreement and Terms.""",
    """The Subscription can include the use of <NOUN>, if specified in the Agreement.""",
    """The Customer is obligated to <VERB>, prior to concluding an Agreement, whether the <NOUN> is available in the countries where it intends to use the Solution.""",
    """A regularly <NOUN> is available on the Platform and/or the Website.""",
    """As the <NOUN> is not under the control of SENSOLUS, it can never be responsible for any <NOUN> or <NOUN> in this regard.""",
    """Nonetheless, SENSOLUS <VERB> to inform the Customer on the aforementioned characteristics of the <NOUN> before the Agreement is concluded.""",
    # from section 8: The Platform
    """The Customer is entitled to <VERB> and use the Platform in accordance with the applicable <NOUN> type (cfr. Article 7.1), the Acceptable Use Policy and/or Data Processing Terms.""",
    """The Platform of SENSOLUS is provided to the Customer “AS-IS”. In the event of problems with the <NOUN> of the Platform, SENSOLUS undertakes its best effort to <VERB> such issue as soon as reasonably possible without giving any guarantee.""",
    """SENSOLUS performs maintenance activities and <VERB> <NOUN> of the Platform on a regular basis. SENSOLUS strives to minimize the impact on the availability of the Platform.""",
    # from section 9
    """SENSOLUS provides different additional <NOUN> to the Customer upon request, such as but not limited to <NOUN>, <NOUN>, <NOUN>, etc. The specific scope, content, deadlines, etc. related to these Services will be agreed upon by the parties in the Order Form.""",
    # from section 10: Complaint
    """Any complaints concerning SENSOLUS’ Solution shall only <VERB> if submitted to SENSOLUS in writing within a period of five (5) Business Days following the discovery of the <NOUN> by the Customer. Complaints shall always be submitted to SENSOLUS by e-mail to the address support@sensolus.com, containing a detailed justification of the complaint.""",
    # from section 11
    """<NOUN> are as stated in the Order Form. <NOUN> confirmed by SENSOLUS for one order are not binding for subsequent orders, unless it concerns orders within a larger <NOUN> agreement.""",
    #  12. Payment
    """SENSOLUS’ invoices are <VERB> to SENSOLUS’ designated <NOUN> account at the latest on the due date indicated on the Order Form or in the relevant <NOUN>.""",
    """Invoices that are not <VERB> by registered letter and/or via email to support@sensolus.com within eight (8) days after their <VERB> will be considered to have been fully accepted.""",
    """If the Customer fails to <VERB> in full any <NOUN> by the due date, then (without previous notice of default): - the Customer shall <VERB> interest on the overdue amount at the rate of 1% per month, to be <VERB> at the start of each month; and – the Customer shall <VERB> SENSOLUS 5 percent of the outstanding balance, with a <NOUN> amount of 250,00 EUR for <NOUN> associated with a.o. the <VERB> of the amounts due and with the adverse consequence on SENSOLUS’ <NOUN> flow, as <NOUN> damages.""",
    """Late, incomplete or non-payment of one expired <NOUN> will cause all other <NOUN>, for which a particular instalment term has been agreed on, to <VERB> immediately <VERB>, without previous notice of default.""",
    """If the Customer has not complied with a <NOUN> condition or other obligation, SENSOLUS is entitled to suspend or postpone its obligations in connection to any active Agreement between the parties.""",
    """By <VERB> the Hardware, the Subscriptions and/or Services, the Customer <VERB> to electronic invoicing by SENSOLUS.""",
    """SENSOLUS shall not <VERB> the Customer nor award the Customer with any compensation and/or credits when the access and/or use of the Subscription is lowered or halted by the Customer during the Term.""",
    # 13. Term
    """The Subscription is <VERB> (and the Term starts) on the date the Hardware is invoiced, unless <NOUN> agreed upon.""",
    """The Term shall <VERB> be renewed for one year, unless either party gives notice of <NOUN> to the other party at the latest one month before the end of the Term.""",
    # 14. Termination
    """Either party may <VERB> the Agreement per registered mail for material <NOUN>, <VERB> and without definitive <NOUN> decision if the other party has committed a material breach and fails to remedy such breach within fifteen (15) days of written <NOUN> of default by the claiming party.""",
    """The Agreement may be <VERB> if an <NOUN> event occurs, i.e. a party ceases to pay its debts or ceases its activities, files for <NOUN>, liquidation of the legal entity or enters proceedings in receivership or judicial composition proceedings.""",
    """SENSOLUS shall never be <VERB> to refund the Customer any <NOUN> if the Customer terminates the Agreement during the Term.""",
    """Articles 15, 17 and 18 shall survive the <VERB> of the Agreement and continue in full force and effect.""",
    # 15. Liability
    """SENSOLUS’ <NOUN> <VERB> always be <VERB> in the light of the best efforts obligation to which SENSOLUS has <VERB>.""",
    """SENSOLUS’ <NOUN> is limited to the mandatory <NOUN> <VERB> by law, and to: – For the Hardware: the invoice <NOUN> of the Hardware. SENSOLUS shall <VERB> (at its sole discretion) to either (i) <VERB> or repair the Hardware, or (ii) credit a pro rata part of the invoice <NOUN> of the Hardware. – For the Subscriptions: the invoice value of the Subscriptions <VERB> by SENSOLUS to the Customer as <NOUN> of the Agreement during the twelve (12) <NOUN> period <VERB> the date on which the applicable <NOUN> claim <VERB>. – For the Services: the applicable <NOUN> <VERB> in the <NOUN> Form.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Damage to, <NOUN> or theft of the Assets to which <NOUN> is attached.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Damage <VERB> from the <NOUN> in devices or infrastructure <VERB> to the Customer.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: <NOUN> or performance of the <NOUN>. Network quality and availability are <VERB> by <NOUN> out of SENSOLUS’ control, such as atmospheric conditions, physical <NOUN>, <NOUN> interference, etc.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Defects that are <VERB> directly or indirectly by an act of the <NOUN> or a third party, regardless of whether they were <VERB> by a fault, negligence or carelessness (e.g. improper installation);""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Damage <VERB> by incorrect, unreliable, incomplete or late <NOUN> from the <NOUN> with regard to the data, objectives, specifications, features, applications, etc.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Damage caused by the further <NOUN> or application by the <NOUN> after a problem has been <VERB>.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Damage caused by force majeure or <NOUN> in accordance with the provisions of <NOUN> 16.""",
    """SENSOLUS cannot <VERB> any <NOUN> from the Customer for indemnification for: Incidental, special, consequential, exemplary or punitive damages, such as but not limited to loss of <NOUN>, <NOUN>, <NOUN>, <NOUN> or <VERB> savings or loss of goodwill.""",
    """<NOUN> alone <VERB> the responsibility for the use made of the Solution by its <NOUN>, <VERB> but not limited to the proper and legal use of Hardware and the Platform, the use of information <VERB> by the <NOUN> and the analysis generated by the Solution in general.""",
    """<NOUN> <VERB> hold SENSOLUS harmless against all claims from third parties arising from the incorrect or unlawful use of the Solution.""", 
    # 16. Force majeure & Hardship
    """The <VERB> are conventionally considered as cases of <NOUN> or hardship: all circumstances which <VERB> reasonably unforeseeable at the time the <NOUN> was concluded, are unavoidable, and create (i) the inability on the part of SENSOLUS to carry out the <NOUN>, or (ii) <VERB> the implementation of the Agreement harder or more difficult than normally anticipated.""",
    """Cases of force majeure or <NOUN> give SENSOLUS the <NOUN> to temporarily <VERB> the performance of its obligations.""",
    """The Customer <VERB> always be required to pay all <NOUN> for the Hardware, the <NOUN> and the Services that have already <VERB> performed resp. <VERB> on the date of suspension/termination.""",
    # 17. Confidentiality
    """All <NOUN> (<VERB>  but not limited to all <NOUN> of financial, commercial, legal, fiscal, social, technical and organizational nature, business and trade secrets, business partner, customer and supplier data, employee data, personal data, programs, source codes, computer programs, computer code, modules, scripts, algorithms, features and modes of operation, inventions (whether or not patentable), processes, schematics, testing procedures, software design and architecture, design and function specifications) disclosed by one party to the other party prior to <VERB> into an <NOUN> as well as during the <NOUN> shall be considered confidential and be <VERB> with the utmost secrecy.""",
    """This confidentiality <NOUN> applies during the course of the cooperation and <VERB> continue to <VERB> for a period of two (2) years <VERB> from the termination of the cooperation for any reason whatsoever.""",
    """Both <NOUN> <VERB> remain at any moment the sole owner of their confidential information.""",
    """Except as expressly set forth herein, <NOUN> in these Terms or the relationship between parties <VERB> grant to the other party any rights to or interest in the confidential information, and no <VERB> licenses are granted.""",
    """This confidentiality obligation <VERB>, however, in no <NOUN> imply that SENSOLUS shall not be entitled to <NOUN> and/or <VERB> any ideas, input, feedback received from the Customer, which may serve to improve and/or <VERB> the Solution.""",
    # 18. Intellectual property rights
    """The <NOUN> shall not alter, remove or tamper with the brands, trademarks, or other means of identification on the Solution.""",
    """In case of <VERB> of the obligations, SENSOLUS is <VERB> to claim full compensation for all damage caused by the <NOUN>.""",
    """By uploading, providing or otherwise using data on, through or in connection with the Solution, the Customer grants SENSOLUS a non-exclusive, royalty-free, worldwide, sub-licensable, transferable, license to use, copy, store, modify, transmit and display the <NOUN> to the extent necessary to <VERB> the <NOUN>.""",
    # 19. Privacy
    """The <VERB> by SENSOLUS of personal data of the (potential) <NOUN> and/or its personnel/staff shall take place in accordance with the provisions of SENSOLUS’ privacy declaration, to be found on the <NOUN>.""",
    """In such event, SENSOLUS acts as <VERB>.""",
    """By <VERB> on the Solution and entering into an Agreement with SENSOLUS, the Customer acknowledges to have read and <VERB> the privacy declaration.""",
    """The <NOUN> acknowledges that – with regard to the <VERB> of all data collected via and/or processed through the Solution by the Customer and/or the End-User– it shall act as controller and SENSOLUS as <VERB>.""",
    """All <VERB> made between parties in this respect shall be solely governed by the Data Processing Terms (available on the Website and/or Platform).""",
    """The <NOUN> acknowledges explicitly that by relying on the Solution and entering into an Agreement with SENSOLUS to have read and <VERB> the Data Processing <NOUN> in its entirety.""",
    # 20. Changes to the Terms or the Solution
    """SENSOLUS reserves the right to <VERB> these <NOUN>, the offer, the fees and composition of its Solution at any time.""",
    """New or <VERB> Terms shall apply from the thirtieth (30th) day after they were made known to the <NOUN> (e.g. through a notification on the Website and/or the Platform).""",
    """Subject to <VERB> of at least thirty (30) days, SENSOLUS shall be <VERB>, except in a case of <NOUN>, <NOUN> or <NOUN>, to discontinue the sale of <NOUN> or to make changes to the type, design or model thereof.""",
    """In such cases, SENSOLUS shall not be under <VERB> to make such <VERB> to <NOUN> already held or ordered by the Customer.""",
    """The <NOUN> cannot hold SENSOLUS liable for any <VERB> within the meaning of this article and shall not have any <VERB> against SENSOLUS for its discontinuation of the supply of Hardware previously sold by SENSOLUS.""",
    """In the event the <NOUN> cannot agree with a change in the offer of the Terms or the Solution and the change entails a significant disadvantage for the Customer during the Term or the tacitly renewed Term, it is allowed to <VERB> the <VERB> within 30 calendar days after being notified thereof by SENSOLUS.""",
    """Under no circumstances, this entitles the <NOUN> to claim any sort of damages or compensation from <NOUN>.""",
    # 21. Netting
    """In <VERB> with the stipulations of the Law on Financial Collateral dated 15 December 2004, SENSOLUS and the Customer will <VERB> and legally compensate and offset each other for all current and future debts.""",
    # 22. Miscellaneous
    """If there has been an express written <VERB> of a right following a specific failure by SENSOLUS, this waiver cannot be <VERB> by the Customer in favor of a new failure, similar to the prior one, or in favor of any other kind of failure.""",
    """If any part or any <NOUN> of these Terms is for whatever reason held to be illegal, invalid or unenforceable, such provisions shall be deleted and the remaining parts or clauses shall not be affected and shall remain <VERB> and <VERB> as if the invalid or unenforceable parts or clauses were not part of the Terms.""",
    """Any such part or clause shall be <VERB> by a provision that, insofar as legally possible, comes closest to the intention of parties in the affected part or clause.""",
    """Parties shall in good faith <VERB> and agree a mutually acceptable provision that shall <VERB> the deleted provision.""",
    """This <NOUN> and the rights and obligations ensuing from it for the <NOUN> may not be transferred either directly or indirectly without the written consent of <NOUN>.""",
    # 23. Jurisdiction and applicable law
    """The Parties hereby undertake to <VERB> the <NOUN> Mediation Rules to all disputes arising out of or in connection with this <NOUN>.""",
    """Should the mediation fail, any <VERB> arising out of or in relation with this Agreement shall be finally settled under the <NOUN> Rules of Arbitration by one or more arbitrators appointed in accordance with those <NOUN>."""
]
