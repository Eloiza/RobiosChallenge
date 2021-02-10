# -*- coding: utf-8 -*-
def form_analyzer(answers, probabilities):
	risk_sum = 0
	for answer, probability in zip(answers, probabilities):

		if(probability > 0.5 and answer == 1):
			risk_sum = -1	#high risk client
			break

		elif(probability < 0.5 and answer == 1):
			risk_sum += 1 	#medium risk client

	#case risk sum of not common symptoms are greater than the half ammount of symptoms 
	if(risk_sum > len(probabilities)/2):
		risk_sum = -1	#high riks client

	return risk_sum

def answer_standardize(a):
	if(a == "sim" or a == "s" or a == "1"): return 1

	elif(a == "não" or a == "nao" or a == "n" or a == "0"): return 0

	else: return -1
