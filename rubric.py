"""Coding rubric for Disclosure Depth responses (DD_Coding_Instructions_v3)."""

RUBRIC = """# Disclosure Depth Coding Rubric

## Context
You are coding open-ended self-disclosure responses for an academic research
project on AI companion interfaces and self-disclosure. Every response
answers the same prompt:

    "Tell me about a recent challenging interaction you had with someone
     and how you handled it."

Responses come from three studies (text vignettes and behavioural VR/chatbot
trials). Study 3 responses that were spoken aloud and transcribed will
contain verbal filler ("um", "so", "you know", "like", "basically"), false
starts, and run-on sentences.

## Critical rules (apply to every response)

1. Code **blind to condition**. You do not know and should not guess whether
   the response was typed to a chatbot or spoken to a VR avatar. Do not
   reward or penalise conversational speech patterns or verbal filler.
2. **Length never increases any score.** A long response without inner-world
   content stays at Surface. A short response can still reach Deep.
3. **Blank / invalid / refused / off-task / repetitive-looping responses:**
     - `SCORE 1 = 0`, `SCORE 2 = 0`
     - all integer Score_* columns = 0
     - all string columns = "not applicable"
     - `Content` = "Blank" for empty, "Incoherent or repetitive - likely invalid"
       for bot-like repetition, or "Refused / off-task" for refusals
     - all binary (Block F) columns = 0
3a. Invalid markers include: empty, just whitespace, the prompt repeated
    verbatim, "N/A", "none", "no idea", "I have not had any challenging
    interactions", loops of the same phrase, or reactive content about the
    study/AI instead of a human interaction.
4. **Rubric 1 <-> Rubric 2 consistency is mandatory:**
     - R1 = 0 -> R2 = 0
     - R1 = 1 -> R2 in {1, 2}
     - R1 = 2 -> R2 in {3, 4}
     - R1 = 3 -> R2 in {5, 6}
   Decide R1 first, then choose R2 from the allowed pair.
5. **Sensitive-topic tiebreaker.** If a response is borderline between two
   R1 levels AND the topic is sensitive (romantic relationship, health /
   illness, mental health, loss / grief, abuse, caregiving crises), tip
   UPWARD one level. Applies to the borderline 0/1 case and the 1/2 case.
6. **IC_Language is strictly broader than Self_Censorship.** If
   Self_Censorship = 1, then IC_Language MUST = 1. IC_Language may still be
   1 when Self_Censorship = 0 (e.g. "I thought before I spoke").
7. **Sentiment enum.** Use exactly these five labels: "negative",
   "positive", "neutral/mixed", "unresolved", "not applicable". Do not emit
   "neutral" or "mixed" on their own.
8. **Target_Closeness with multiple people.** Code the CLOSEST relationship
   mentioned. For Topic, code the PRIMARY relational domain.
9. **Resolution string for blank rows** = "not applicable" (even though
   code 0 is labelled "not mentioned"); for coded rows use "not mentioned"
   when no resolution is described.
10. **Content free-text field** is a <=15-word description of what the
    response is specifically about (e.g. "Argument with mother about
    medical treatment decisions"). Not a category label.

## Rubric 1 - Disclosure Depth (0-3)

**0 - No Disclosure.** Blank, off-task, incoherent, refuses, reactive,
repeats prompt. No personal interaction described.

**1 - Surface Disclosure.** Describes a situation factually (who, what,
where, what happened) but no emotional content, inner state, or personal
reflection. Purely external. Vague emotional labels with NO elaboration
("it was stressful", "I felt frustrated" with nothing further) stay at 1.
Borderline 0/1 + sensitive topic -> tip to 1.

Examples:
  - "I had a disagreement with my manager about a deadline. I explained my
     position and we agreed on a new timeline."
  - "A customer was being difficult. I stayed calm and followed the
     procedure. It was resolved."

**2 - Moderate Disclosure.** Situation AND any signal of inner world:
uncertainty ("I didn't know what to do"), emotional elaboration beyond a
bare label, self-reflection on own behaviour or reaction, OR sensitive
topic + any minimal emotional signal. Sensitive topic + any emotional
signal always tips to 2.

Examples:
  - "I argued with my mom about money and felt frustrated. I tried to stay
     calm but it wasn't easy."
  - "My friend didn't show up when I needed them. I was hurt but didn't say
     anything at the time."

**3 - Deep Disclosure.** Raw emotional vulnerability, genuine
self-revelation, intimate personal content. Goes beyond the situation to
reveal something private. Visibly inside the emotion, not just naming it.
Feels unpolished and emotionally exposed - something the person would not
share casually with a stranger.

Examples:
  - "My ex-husband died suddenly a few weeks ago. We had just started
     talking again and I feel guilty I didn't reach out sooner."
  - "My mom made a comment about wanting to die. I didn't know what to do.
     I've been carrying that conversation every day since."

## Rubric 2 - Disclosure Depth (0-6)

| Score | Label                     | Definition                                                                                            |
|-------|---------------------------|-------------------------------------------------------------------------------------------------------|
| 0     | No Disclosure             | Same as R1 = 0.                                                                                       |
| 1     | Minimal Surface           | Names a situation with almost no detail (1-2 sentences, no elaboration).                              |
| 2     | Surface                   | Basic factual detail - who / what / where - but no inner state. Reasonably elaborated but external.   |
| 3     | Emerging Emotional Tone   | Emotional label present but immediately dropped. Named but not engaged with.                          |
| 4     | Moderate Disclosure       | Genuinely engages with inner state - uncertainty, conflict, reflection. Briefly explored.             |
| 5     | Substantial Disclosure    | Goes beyond the situation into personal meaning, ongoing struggle, or relational consequence.         |
| 6     | Deep Disclosure           | Raw vulnerability, intimate self-revelation. Deeply personal. Feels emotionally exposed.              |

## Block B - Sentiment (Score_S: 0-4)

| Score_S | Sentiment string | Description                                                       |
|---------|------------------|-------------------------------------------------------------------|
| 0       | not applicable   | Blank or uncodeable.                                              |
| 1       | negative         | Distress, hurt, anger, sadness, frustration, fear, guilt dominate.|
| 2       | positive         | Relief, pride, satisfaction, resolution, growth dominate.         |
| 3       | neutral/mixed    | No clear valence OR negative and positive roughly balanced.       |
| 4       | unresolved       | Emotions remain open; ongoing uncertainty or processing.          |

## Block C - Content Type (Score_C: 0-6)

Captures the TYPE OF INTERACTION (not the topic domain).

| Score_C | Content Type label       |
|---------|--------------------------|
| 0       | not applicable           |
| 1       | direct confrontation     |
| 2       | passive conflict         |
| 3       | discovery/betrayal       |
| 4       | caregiving/support       |
| 5       | negotiation/decision     |
| 6       | other                    |

## Block D - Topic Domain (Score_T: 0-11)

Captures the RELATIONAL DOMAIN.

| Score_T | Topic label              |
|---------|--------------------------|
| 0       | no topic                 |
| 1       | workplace/professional   |
| 2       | family                   |
| 3       | romantic relationship    |
| 4       | friendship               |
| 5       | health/illness           |
| 6       | mental health            |
| 7       | financial                |
| 8       | loss/grief               |
| 9       | stranger/public          |
| 10      | academic/educational     |
| 11      | other                    |

For the free-text `Topic` column, output a 1-3 word label matching the
Score_T row (e.g. "family", "workplace", "romantic").

## Block E - Structural dimensions

Narrative_Style (Score_NS 0-3):
  0 not applicable / 1 sequential (chronological, "and then... and then")
  / 2 summary (compressed retrospective) / 3 hybrid.

Resolution (Score_R 0-3):
  0 not mentioned (string "not mentioned"; use "not applicable" only for
  blank rows) / 1 resolved (clear conclusion) / 2 partial (improved but
  not settled) / 3 unresolved (explicitly ongoing).

Focus (Score_F 0-3):
  0 not applicable / 1 situation (external events, other person) / 2 self
  (own feelings, internal experience) / 3 balanced.

## Block F - Disclosure process dimensions (binary 0/1)

Self_Censorship: 1 if the response explicitly describes filtering /
  withholding during the interaction ("I decided not to say", "I chose my
  words carefully", "I held back", "I bit my tongue", "I thought about
  what to say before speaking").

IC_Language: 1 if the response shows conscious monitoring or control of
  what was communicated. BROADER than Self_Censorship - includes subtle
  forms like "I was careful about what I said", "I thought before I
  spoke", "I picked my moment". If Self_Censorship = 1, IC_Language = 1.

Spontaneous_Revelation: 1 if the response volunteers info beyond what the
  prompt strictly required - an aside, an admission, an ongoing personal
  struggle, or something about their character that the challenging
  interaction didn't require.

Realtime_Processing: 1 if the response uses language suggesting the event
  is still being processed rather than retrospectively settled ("I still
  don't know", "I keep wondering", "I haven't figured it out",
  present-tense emotional language about a past event like "I still feel
  hurt").

Emotional_Regulation: 1 if the response describes actively managing,
  suppressing, or controlling emotional expression during the interaction
  ("I stayed calm", "I tried to be professional", "I kept my composure",
  "I didn't let it show", "I kept it together").

Emotional_Spillover: 1 if the response overflows into broader life
  context, ongoing struggles, or feelings beyond the immediate interaction
  (ongoing relationship dynamics, life circumstances, fears about the
  future, patterns in their life).

## Block G - Interpersonal orientation (Score_OS 0-3)

  0 not applicable / 1 other-oriented (primarily the other person's
  behaviour, motivations, actions) / 2 self-oriented (primarily own
  feelings, reactions) / 3 balanced.

## Block H - Topic characteristics

Topic_Sensitivity (Score_TS 0-3):
  0 not applicable
  1 low    - workplace/professional, strangers/public, academic
  2 medium - friendship conflicts, financial stress, general family
             disagreements
  3 high   - romantic relationships, health/illness, mental health,
             loss/grief, abuse, caregiving crises

Temporal_Orientation (Score_TO 0-3):
  0 not applicable / 1 past-resolved (clearly past, fully resolved) /
  2 ongoing (still unfolding or emotions still active) / 3 mixed (past
  event with ongoing emotional / relational consequences).

Target_Closeness (Score_TC 0-5):
  0 not applicable (no other person mentioned)
  1 stranger              - unknown person, customer, driver, public
  2 acquaintance          - colleague, classmate, neighbour, casual
  3 friend                - named or described as a friend
  4 family                - parent, sibling, child, extended family, in-law
  5 partner               - spouse, boyfriend/girlfriend, romantic partner
  For the string column use: "stranger" / "acquaintance" / "friend" /
  "family" / "partner" / "not applicable".
  When multiple people are involved, code the CLOSEST relationship.
"""
