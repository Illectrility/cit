# Gender identity
gender_points = {"Cis male": 0, "Cis female": 0, "Gender fluid": 0, "Non-binary": 0, "Transfem": 0, "Transmasc": 0, "Intersex": 0, "Agender": 0}

# Questions
gender_questions = [
        {
            "id": "sex",
            "text": "What is your sex?",
            "answers": {
                "Male": None,
                "Female": None,
                "Intersex": None,
                }
        },

        {
            "id": "identity_matches_sex",
            "text": "The sex I was assigned at birth truly and wholly matches and reflects how I perceive my gender identity.",
            "answers": {
                "Yes": {
                    "Male": "Cis male",
                    "Female": "Cis female",
                    "Intersex": "Intersex",
                },
                "No": {
                    "Male": ["Gender fluid", "Non-binary", "Transfem", "Agender"],
                    "Female": ["Gender fluid", "Non-binary", "Transmasc", "Agender"],
                    "Intersex": ["Gender fluid", "Non-binary", "Transfem", "Transmasc", "Agender"],
                },
            }
        },

        {
            "text": "I want to express myself in ways that highlight the gender stereotypes of the following gender:",
            "answers": {
                "Male": {
                    "Male": "Cis male",
                    "Female": "Transmasc",
                    "Intersex": "Transmasc",
                },
                "Female": {
                    "Male": "Transfem",
                    "Female": "Cis female",
                    "Intersex": "Transfem",
                },
                "Intersex": "Intersex",
                "It varies from time to time": "Gender fluid",
                "Neither male nor female": "Non-binary",
                "I don't feel like I am actively living as a particular gender": "Agender",
                "None": "Agender",
            }
        },

        {
            "text": "Even when I was younger, I felt my gender identity did not match the sex I was assigned at birth.",
            "condition": {
                "question_id": "identity_matches_sex",
                "value": "No"
            },
            "answers": {
                "True": {
                    "Male": ["Gender fluid", "Non-binary", "Transfem", "Agender"],
                    "Female": ["Gender fluid", "Non-binary", "Transmasc", "Agender"],
                    "Intersex": ["Gender fluid", "Non-binary", "Transfem", "Transmasc", "Agender"],
                },
                "False": {
                    "Male": "Cis male",
                    "Female": "Cis female",
                    "Intersex": "Intersex",
                },
                "I don't remember": None,
            }
        },

        {
            "text": "My internal sense of gender changes.",
            "answers": {
                "True": "Gender fluid",
                "False": None,
            }
        },

        {
            "id": "expresses_sex",
            "text": "My preferred style/behavior/mannerisms fully match the gender I was assigned at birth.",
            "answers": {
                "True": {
                    "Male": "Cis male",
                    "Female": "Cis female",
                    "Intersex": "Intersex",
                },
                "False": {
                    "Male": ["Non-binary", "Transfem"],
                    "Female": ["Non-binary", "Transmasc"],
                    "Intersex": ["Non-binary", "Transfem", "Transmasc"],
                },
                "It varies from time to time": "Gender fluid",
                "I don't feel like my gender identity influences my style/behavior/mannerisms": "Agender",
            }
        },

        {
            "text": "I consistently use or want to use my style, behavior, and mannerisms to live as the following gender, and doing so feels right for me:",
            "condition": {
                "question_id": "expresses_sex",
                "value": ["False", "It varies from time to time", "I don't feel like my gender identity influences my style/behavior/mannerisms"]
            },
            "answers": {
                "Male": {
                    "Male": "Cis male",
                    "Female": "Transmasc",
                    "Intersex": "Transmasc",
                },
                "Female": {
                    "Male": "Transfem",
                    "Female": "Cis female",
                    "Intersex": "Transfem",
                },
                "Intersex": "Intersex",
                "It varies from time to time": "Gender fluid",
                "Neither male nor female": "Non-binary",
                "I don't feel like I am actively living as a particular gender": "Agender",
                "None": "Agender",
            }
        },

        {
            "text": "It often seems to me as if people are oddly insistent on gendering everything whereas I don't see the world as gendered the way they do.",
            "answers": {
                "True": "Agender",
                "False": None,
            }
        },

        {
            "text": "Throughout my life, I have always felt most connected to this gender identity:",
            "condition": {
                "question_id": "identity_matches_sex",
                "value": ["False", "It varies from time to time", "I don't feel like my gender identity influences my style/behavior/mannerisms"]
            },
            "answers": {
                "Male": {
                    "Male": "Cis male",
                    "Female": "Transmasc",
                    "Intersex": "Transmasc",
                },
                "Female": {
                    "Male": "Transfem",
                    "Female": "Cis female",
                    "Intersex": "Transfem",
                },
                "Intersex": "Intersex",
                "It varies from time to time": "Gender fluid",
                "Neither male nor female": "Non-binary",
                "I don't feel like I have felt connected to any particular gender": "Agender",
                "None": "Agender",
            }
        },

        {
            "text": "I have not felt the need to give a lot of thought to my gender identity.",
            "answers": {
                "True": {
                    "Male": ["Cis male", "Agender"],
                    "Female": ["Cis female", "Agender"],
                    "Intersex": ["Intersex", "Agender"],
                },
                "False": {
                    "Male": ["Gender fluid", "Non-binary", "Transfem"],
                    "Female": ["Gender fluid", "Non-binary", "Transmasc"],
                    "Intersex": ["Gender fluid", "Non-binary", "Transfem", "Transmasc"],
                },
            }
        },

        {
            "text": "My gender identity changes over time.",
            "answers": {
                "True": "Gender fluid",
                "False": None,
            }
        },

        {
            "text": "If I could choose, I would like to have a physical body that looks typically:",
            "answers": {
                "Masculine": {
                    "Male": "Cis male",
                    "Female": "Transmasc",
                    "Intersex": "Transmasc",
                },
                "Feminine": {
                    "Male": "Transfem",
                    "Female": "Cis female",
                    "Intersex": "Transfem",
                },
                "Intersex": "Intersex",
                "Neither male nor female": "Non-binary",
                "Genderless": "Agender",
                "I don't care what gender my body looks like": ["Non-binary", "Agender"],
                "I don't feel like my body would match my gender identity, regardless": ["Non-binary", "Agender"],
                "It varies from time to time": "Gender fluid",
            }
        },

        {
            "text": "My preferred pronouns would be",
            "answers": {
                "He/Him": {
                    "Male": "Cis male",
                    "Female": "Transmasc",
                    "Intersex": "Transmasc",
                },
                "She/Her": {
                    "Male": "Transfem",
                    "Female": "Cis female",
                    "Intersex": "Transfem",
                },
                "They/Them": ["Intersex", "Non-binary", "Agender", "Gender fluid"],
                "I don't care what pronouns people use": "Agender",
                "It varies from time to time": "Gender fluid",
            }
        },

        {
            "text": "I often feel like I have no gender at all.",
            "condition": {
                "question_id": "identity_matches_sex",
                "value": ["False", "It varies from time to time", "I don't feel like my gender identity influences my style/behavior/mannerisms"]
            },
            "answers": {
                "True": "Agender",
                "False": None,
            }
        }
    ]

# Processing questions

user_sex = None
answers_given = {}

for q in gender_questions:
    # Check condition (handle multiple acceptable values)
    if "condition" in q:
        cond = q["condition"]
        prev_answer = answers_given.get(cond["question_id"])
        valid_values = cond["value"]

        # Check if the previous answer is in the valid values list
        if isinstance(valid_values, list):
            if prev_answer not in valid_values:
                continue
        else:
            if prev_answer != valid_values:
                continue

    # Show question and numbered options
    print("\n" + q["text"])
    options = list(q["answers"].keys())
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Input: choose by number
    answer_index = input("Choose a number: ").strip()
    while not answer_index.isdigit() or not (1 <= int(answer_index) <= len(options)):
        print("Invalid number. Try again.")
        answer_index = input("Choose a number: ").strip()
    
    answer = options[int(answer_index) - 1]

    # Store sex and answer
    if q.get("id") == "sex":
        user_sex = answer
    if "id" in q:
        answers_given[q["id"]] = answer

    # Get target outcome(s)
    target = q["answers"][answer]

    if isinstance(target, dict):
        resolved = target[user_sex]
    else:
        resolved = target

    if isinstance(resolved, list):
        for out in resolved:
            gender_points[out] += 1
    elif isinstance(resolved, str):
        gender_points[resolved] += 1

# Sort outcomes by points in descending order
sorted_outcomes = sorted(gender_points.items(), key=lambda x: x[1], reverse=True)

# Show top 3 outcomes
print("\n--- Top 3 Results ---")
top_three = sorted_outcomes[:3]
for i, (outcome, points) in enumerate(top_three, 1):
    print(f"{i}. {outcome}: {points}")

# Handle tie for the number 1 spot
if top_three[0][1] == top_three[1][1]:
    print("\nThere's a tie.")
    print("Please choose which of these identities best suits you:")
    for i, (outcome, points) in enumerate(top_three[:2], 1):
        print(f"{i}. {outcome}: {points}")
    
    choice = input("Enter 1 or 2: ").strip()
    while choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
        choice = input("Enter 1 or 2: ").strip()
    
    chosen_outcome = top_three[int(choice) - 1][0]
    print(f"\nYou chose: {chosen_outcome} as your gender identity.")
    gender_identity = chosen_outcome
else:
    gender_identity = top_three[0][0]
    print(f"\nYour gender identity result is: {gender_identity}")

input("Press enter to continue with the sexual orientation test.")

# Sexual orientation
sex_orientation_points = {"Asexual": 0, "Androphile": 0, "Gynophile": 0, "Bisexual": 0, "Pansexual": 0}

# Questions
sex_orientation_questions = [
        {
            "id": "no_arousal",
            "text": "I don't feel sexual desire or arousal, even in situations where I feel I \"should\".",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I rarely (or never) experience sexual urges or drives.",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I find it difficult to relate to media and culture that portrays sex as a universal aspect of human life.",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "id": "no_sexual_attraction",
            "text": "I generally don't feel sexually attracted to (i.e. want to actually have intercourse with) other people, regardless of their gender or appearance.",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "Even if I am fascinated with a person on account of their looks or personality, I do not wish to actually have sex with them.",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I wouldn't mind if I never had sex (again).",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I don't really know what it is like to feel sexual attraction.",
            "answers": {
                "True": "Asexual",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I want to touch intimately and/or be naked in the company of:",
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },

        {
            "text": "I have fantasized about sexual intercourse with:",
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },

        {
            "text": "I have found sexually attractive:",
            "condition": {
                "question_id": "no_sexual_attraction",
                "value": "False"
            },
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },

        {
            "text": "I have been sexually aroused by:",
            "condition": {
                "question_id": "no_arousal",
                "value": "False"
            },
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },

        {
            "text": "I have fantasized about non-sexual petting and/or bodily closeness with:",
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },

        {
            "text": "I have found myself wanting to have real-life sexual intercourse with:",
            "answers": {
                "A male-presenting person": "Androphile",
                "A female-presenting person": "Gynophile",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Bisexual",
                "No one": "Asexual",
                "People, regardless of their gender identity": "Pansexual",
            }
        },
    ]

# Processing questions
answers_given = {}

for q in sex_orientation_questions:
    # Check condition (handle multiple acceptable values)
    if "condition" in q:
        cond = q["condition"]
        prev_answer = answers_given.get(cond["question_id"])
        valid_values = cond["value"]

        # Check if the previous answer is in the valid values list
        if isinstance(valid_values, list):
            if prev_answer not in valid_values:
                continue
        else:
            if prev_answer != valid_values:
                continue

    # Show question and numbered options
    print("\n" + q["text"])
    options = list(q["answers"].keys())
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Input: choose by number
    answer_index = input("Choose a number: ").strip()
    while not answer_index.isdigit() or not (1 <= int(answer_index) <= len(options)):
        print("Invalid number. Try again.")
        answer_index = input("Choose a number: ").strip()
    
    answer = options[int(answer_index) - 1]

    # Get target outcome(s)
    target = q["answers"][answer]

    if isinstance(target, dict):
        resolved = target[gender_identity]
    else:
        resolved = target

    if isinstance(resolved, list):
        for out in resolved:
            sex_orientation_points[out] += 1
    elif isinstance(resolved, str):
        sex_orientation_points[resolved] += 1

# Sort outcomes by points in descending order
sorted_outcomes = sorted(sex_orientation_points.items(), key=lambda x: x[1], reverse=True)

# Ask about demi
demi_sex = False
print("\nI only feel sexually attracted to someone after I have built an emotional bond with them.\n1. True\n2. False")
while True:
    answer_index = input("Choose a number: ").strip()
    if int(answer_index) == 1:
        demi_sex = True
        break
    elif int(answer_index) == 2:
        demi_sex = False
        break
    else:
        print("Invalid number. Try again.")

# Show top 3 outcomes
print("\n--- Top 3 Results ---")
top_three = sorted_outcomes[:3]
for i, (outcome, points) in enumerate(top_three, 1):
    if demi_sex:
        print(f"{i}. Demi-{outcome}: {points}")
    else:
        print(f"{i}. {outcome}: {points}")

# Handle tie for the number 1 spot
if top_three[0][1] == top_three[1][1]:
    print("\nThere's a tie.")
    print("Please choose which of these orientations best suits you:")
    for i, (outcome, points) in enumerate(top_three[:2], 1):
        if demi_sex:
             print(f"{i}. Demi-{outcome}: {points}")
        else:
            print(f"{i}. {outcome}: {points}")
    
    choice = input("Enter 1 or 2: ").strip()
    while choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
        choice = input("Enter 1 or 2: ").strip()
    
    chosen_outcome = top_three[int(choice) - 1][0]
    if demi_sex:
        print(f"\nYou chose Demi-{chosen_outcome} as your sexual orientation.")
    else:
        print(f"\nYou chose {chosen_outcome} as your sexual orientation.")
    sexual_orientation = chosen_outcome
else:
    sexual_orientation = top_three[0][0]
    if demi_sex:
        print(f"\nYour sexual orientation result is: Demi-{sexual_orientation}")
    else:
        print(f"\nYour sexual orientation result is: {sexual_orientation}")

input("Press enter to continue with the romantic orientation test.")

# Romantic orientation
rom_orientation_points = {"Aromantic": 0, "Androromantic": 0, "Gynoromantic": 0, "Biromantic": 0, "Panromantic": 0, "Lithromantic": 0}

# Questions
rom_orientation_questions = [
        {
            "text": "I have difficulty understanding people’s obsession with romantic love and relationships.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I prefer to spend my time with friends or pursuing my own interests rather than seeking out a romantic partner.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I find it difficult to relate to media and culture that portrays romance as a universal aspect of human life.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I don't feel romantically attracted to (i.e. want to be in a romantic relationship with) other people, regardless of their gender or appearance.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "Even if I am fascinated with a person on account of their looks or personality, I do not wish to be in a romantic relationship with them.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I wouldn't mind if I would never be in a romantic relationship (again).",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I find it difficult to relate to the intense romantic feelings that others often express.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },
        
        {
            "text": "I don't really know what it's like to feel romantic attraction.",
            "answers": {
                "True": "Aromantic",
                "False": None,
                "I don't know": None,
            }
        },
        
        {
            "text": "I feel romantic attraction, but do not want it to be reciprocated.",
            "answers": {
                "True": "Lithromantic",
                "False": None,
                "I don't know": None,
            }
        },

        {
            "text": "I have felt \"butterflies\" in the presence of:",
            "answers": {
                "A male-presenting person": "Androromantic",
                "A female-presenting person": "Gynoromantic",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity": "Panromantic",
            }
        },

        {
            "text": "I have fantasized about a romantic relationship with:",
            "answers": {
                "A male-presenting person": "Androromantic",
                "A female-presenting person": "Gynoromantic",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity": "Panromantic",
            }
        },

        {
            "text": "I have felt a very strong urge/need to spend time with:",
            "answers": {
                "A male-presenting person before": "Androromantic",
                "A female-presenting person before": "Gynoromantic",
                "Both female and male-presenting people before": "Bisexual",
                "People of more than one gender identity before": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity before": "Panromantic",
            }
        },

        {
            "text": "I have had mild insomnia because of:",
            "answers": {
                "A male-presenting person before": "Androromantic",
                "A female-presenting person before": "Gynoromantic",
                "Both female and male-presenting people before": "Bisexual",
                "People of more than one gender identity before": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity": "Panromantic before",
            }
        },

        {
            "text": "I have had to compulsively think about:",
            "answers": {
                "A male-presenting person before": "Androromantic",
                "A female-presenting person before": "Gynoromantic",
                "Both female and male-presenting people before": "Bisexual",
                "People of more than one gender identity before": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity before": "Panromantic",
            }
        },

        {
            "text": "I have found myself wanting to be in a real-life romantic relationship with:",
            "answers": {
                "A male-presenting person": "Androromantic",
                "A female-presenting person": "Gynoromantic",
                "Both female and male-presenting people": "Bisexual",
                "People of more than one gender identity": "Biromantic",
                "No one": "Aromantic",
                "People, regardless of their gender identity": "Panromantic",
            }
        },
    ]

# Processing questions
answers_given = {}

for q in rom_orientation_questions:
    # Check condition (handle multiple acceptable values)
    if "condition" in q:
        cond = q["condition"]
        prev_answer = answers_given.get(cond["question_id"])
        valid_values = cond["value"]

        # Check if the previous answer is in the valid values list
        if isinstance(valid_values, list):
            if prev_answer not in valid_values:
                continue
        else:
            if prev_answer != valid_values:
                continue

    # Show question and numbered options
    print("\n" + q["text"])
    options = list(q["answers"].keys())
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Input: choose by number
    answer_index = input("Choose a number: ").strip()
    while not answer_index.isdigit() or not (1 <= int(answer_index) <= len(options)):
        print("Invalid number. Try again.")
        answer_index = input("Choose a number: ").strip()
    
    answer = options[int(answer_index) - 1]

    # Get target outcome(s)
    target = q["answers"][answer]

    if isinstance(target, dict):
        resolved = target[gender_identity]
    else:
        resolved = target

    if isinstance(resolved, list):
        for out in resolved:
            rom_orientation_points[out] += 1
    elif isinstance(resolved, str):
        rom_orientation_points[resolved] += 1

# Sort outcomes by points in descending order
sorted_outcomes = sorted(rom_orientation_points.items(), key=lambda x: x[1], reverse=True)

# Ask about demi
demi_rom = False
print("\nI only feel romantically attracted to someone after I have built an emotional bond with them.\n1. True\n2. False")
while True:
    answer_index = input("Choose a number: ").strip()
    if int(answer_index) == 1:
        demi_rom = True
        break
    elif int(answer_index) == 2:
        demi_rom = False
        break
    else:
        print("Invalid number. Try again.")

# Show top 3 outcomes
print("\n--- Top 3 Results ---")
top_three = sorted_outcomes[:3]
for i, (outcome, points) in enumerate(top_three, 1):
    if demi_rom:
        print(f"{i}. Demi-{outcome}: {points}")
    else:
        print(f"{i}. {outcome}: {points}")

# Handle tie for the number 1 spot
if top_three[0][1] == top_three[1][1]:
    print("\nThere's a tie.")
    print("Please choose which of these orientations best suits you:")
    for i, (outcome, points) in enumerate(top_three[:2], 1):
        if demi_rom:
             print(f"{i}. Demi-{outcome}: {points}")
        else:
            print(f"{i}. {outcome}: {points}")
    
    choice = input("Enter 1 or 2: ").strip()
    while choice not in ["1", "2"]:
        print("Invalid choice. Try again.")
        choice = input("Enter 1 or 2: ").strip()
    
    chosen_outcome = top_three[int(choice) - 1][0]
    if demi_rom:
        print(f"\nYou chose Demi-{chosen_outcome} as your romantic orientation.")
    else:
        print(f"\nYou chose {chosen_outcome} as your romantic orientation.")
    romantic_orientation = chosen_outcome
else:
    romantic_orientation = top_three[0][0]
    if demi_rom:
        print(f"\nYour romantic orientation result is: Demi-{romantic_orientation}")
    else:
        print(f"\nYour romantic orientation result is: {romantic_orientation}")

# Interpreting results based on gender identity
if sexual_orientation == "Androphile":
    if gender_identity in ("Cis male", "Transmasc"):
        sexual_orientation = "Homosexual"
    elif gender_identity in ("Cis female", "Transfem"):
        sexual_orientation = "Heterosexual"
elif sexual_orientation == "Gynophile":
    if gender_identity in ("Cis male", "Transmasc"):
        sexual_orientation = "Heterosexual"
    elif gender_identity in ("Cis female", "Transfem"):
        sexual_orientation = "Homosexual"

if romantic_orientation == "Androromantic":
    if gender_identity in ("Cis male", "Transmasc"):
        romantic_orientation = "Homoromantic"
    elif gender_identity in ("Cis female", "Transfem"):
        romantic_orientation = "Heteroromantic"
elif romantic_orientation == "Gynoromantic":
    if gender_identity in ("Cis male", "Transmasc"):
        romantic_orientation = "Heteroromantic"
    elif gender_identity in ("Cis female", "Transfem"):
        romantic_orientation = "Homoromantic"

if demi_sex:
    sexual_orientation = "Demi-" + sexual_orientation
if demi_rom:
    romantic_orientation = "Demi-" + romantic_orientation

print("\n=-=-=-=-=-=-=")
print(f"Your result is: {gender_identity} {romantic_orientation} {sexual_orientation}")
