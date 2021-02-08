import pandas as pd
from numpy import sum


def main():
	#Dado alguns sintomas qual a probabilidade da pessoa estar com covid?
	questions = {
		1: 'Você está com febre?',
		2: 'Você tem tido tosse seca?',
		3: 'Você notou a perda do paladar ou olfato nos últimos dias?',
		4: 'Você teve falta de ar?',
		5: 'Você teve diarreia?',
	}

	probabilities = {
		"cough": 85.2,
		"fever": 79.6,
		"dyspnoea": 76.6,
		"respiratory_discomfort ": 63.0,
		"sore_troat ": 24.0,
		"diarrhoea ": 12.5,
		"vomiting ": 06.0
		"inter_travel" : 34.4
		"positiv_contact": 61.1
	}

	answers = []
	keys = list(questions.keys())
	i = 0 
	while(i < len(keys)):
		print(questions[keys[i]])
			
		a = input().lower()

		if(a == "sim" or a == "s" or a == "1"):
			answers.append(1)
			i+=1

		elif(a == "não" or a == "nao" or a == "0"):
			answers.append(0)
			i+= 1

		else:
			print("\nResposta Inválida\nResponda novamente\n")
			i = i


	total_score = sum(answers)
	if(total_score > len(keys)/2):
		print("Chances altas de ter covid X.X")

	else:
		print("Chances baixas de ter covid :)")


if __name__ == '__main__':
	main()