import re
import math

'''
---------------------------input
John likes to watch movies. Mary likes movies too.
John also likes to watch football games.
0.1

---------------------------input
-21.78476859340514
'''


def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)

    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print(calculate_doc_prob(training_model, testing_model, alpha))

def calculate_doc_prob(training_model, testing_model, alpha):
    # Implement likelihood function here...
    laplace_smoothing = {}
    bow_dict_training, bow_training = training_model
    bow_dict_testing, bow_testing = testing_model
    for k, v in bow_dict_training.items():
        laplace_smoothing[k] = (bow_training[v] + alpha)/ (sum(bow_training) + len(bow_dict_training) * alpha)
    prob = 1
    for k, v in bow_dict_testing.items():
        if k in laplace_smoothing:
            prob *= laplace_smoothing[k] ** bow_testing[v]
        else:
            prob *= alpha/ (sum(bow_training) + len(bow_dict_training) * alpha)
    
    logprob = math.log(prob)
    

    return logprob

def create_BOW(sentence):
    bow_dict = {}
    bow = []

    sentence = sentence.lower()
    sentence = replace_non_alphabetic_chars_to_space(sentence)
    words = sentence.split(' ')
    for token in words:
        if len(token) < 1: continue
        if token not in bow_dict:
            new_idx = len(bow)
            bow.append(0)
            bow_dict[token] = new_idx
        bow[bow_dict[token]] += 1

    return bow_dict, bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()
