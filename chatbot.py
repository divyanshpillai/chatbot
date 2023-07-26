import re
import longresponse as long
import random

def message_probability(
    user_input, recognised_words, single_response=False, required_words=[]
):
    message_certainity = 0
    has_required_words = True

    for word in user_input:
        if word in recognised_words:
            message_certainity += 1

    percentage = float(message_certainity) / float(len(recognised_words))

    for word in required_words:
        if word not in user_input:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def unknown():
    response = [
        "Sorry, I could not get it",
        "Will you please re-phrase your question?",
        "Sorry, I didn't understand",
        "What does that mean?",
    ][random.randrange(4)]

    return response


def checkAllMessages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_word=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(
            message, list_of_words, single_response, required_word
        )

    # response---------------------------------------------
    response("Hello!", ["hello", "hii", "hey", "hlw"], single_response=True)
    response(
        "I'm fine! What about you?",
        ["how", "are", "you", "doing"],
        required_word=["how"],
    )
    response(
        "Divyansh build me using python",
        ["who", "build", "you"],
        required_word=["build"],
    )
    response(
        "We're sorry about last night but divyansh have to build me by yesterday only bcoz he set himself a goal",
        ["what", "happens", "yesterday"],
        required_word=["yesterday"],
    )
    response(
        "My pleasure",
        ["thank", "you", "bot", "for", "your", "service"],
        required_word=["thank", "service"],
    )
    # response(long.yesterday, ['what', 'happens', 'yesterday'], required_word=['yesterday'])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def get_response(user_input):
    split_response = re.split(
        r"\s+|[,;?!.-]\s*", user_input.lower()
    )  #'\s+|[,;?!.-]\s*'
    response = checkAllMessages(split_response)
    return response


while True:
    print("Bot: " + get_response(input("You: ")))

# while answer_key:
#     if :
#         print("Bot: " + get_response(input("You: ")))
#         answer_key == True
#     else:
#         answer_key = False