DOMAINS = {

"Gross Motor":[
"Walks independently",
"Runs without frequent falling",
"Jumps with both feet",
"Climbs stairs alternating feet",
"Balances on one foot"
],

"Fine Motor":[
"Scribbles spontaneously",
"Turns pages one at a time",
"Holds crayon with fingers",
"Copies circle",
"Draws simple human figure"
],

"Speech":[
"Uses 20–50 words",
"Combines 2 words meaningfully",
"Speaks 3–4 word sentences",
"Speech understood by adults",
"Can narrate simple events"
],

"Receptive":[
"Responds to name",
"Follows 1-step instruction",
"Follows 2-step instruction",
"Understands concepts",
"Answers what/where questions"
],

"Social":[
"Makes eye contact",
"Shows objects to share interest",
"Engages in pretend play",
"Plays cooperatively",
"Has preferred peer"
],

"Cognitive":[
"Matches objects",
"Identifies objects",
"Recognizes colors",
"Counts 1–10",
"Maintains attention"
],

"Adaptive":[
"Feeds self with spoon",
"Indicates toilet need",
"Toilet trained",
"Wears simple clothing",
"Washes hands"
],

"Sensory":[
"Overreacts to sound",
"Avoids textures",
"Seeks spinning/jumping",
"Repetitive movements",
"Distressed by routine change"
],

"Attention":[
"Sits for structured activity",
"Completes simple task",
"Extremely restless",
"Frequently shifts activity",
"Waits turn"
]

}


# milestone ages in months

MILESTONE_AGE = {

"Walks independently":24,
"Runs without frequent falling":30,
"Jumps with both feet":36,
"Climbs stairs alternating feet":48,
"Balances on one foot":60,

"Scribbles spontaneously":24,
"Turns pages one at a time":30,
"Holds crayon with fingers":36,
"Copies circle":48,
"Draws simple human figure":60,

"Uses 20–50 words":24,
"Combines 2 words meaningfully":30,
"Speaks 3–4 word sentences":36,
"Speech understood by adults":48,
"Can narrate simple events":60
}


def validate_question(age,question):

    if question in MILESTONE_AGE:

        required_age = MILESTONE_AGE[question]

        if age < required_age:

            return False

    return True



def compute_scores(scores):

    domain_scores = {}

    max_score = 0

    total = 0

    for domain,items in scores.items():

        domain_total = 0

        valid_items = 0

        for item in items:

            if item is not None:

                domain_total += item

                valid_items += 1

        domain_scores[domain] = domain_total

        max_score += valid_items * 2

        total += domain_total


    if max_score == 0:
        percent = 0
    else:
        percent = (total / max_score) * 100


    if percent > 50:
        risk = "High Red Flag"

    elif percent > 30:
        risk = "Moderate Concern"

    elif percent > 15:
        risk = "Monitor"

    else:
        risk = "Low Risk"


    return domain_scores,total,percent,risk