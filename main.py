import pandas as pd
import numpy as np 


def main():

	df = pd.read_csv("Data/symptoms.csv")
	print(df["question"])

	questions = df["question"].to_list()

	answers = []
	i = 0
	while (i < len(questions)):
		print(str(i +1) + '. '+ questions[i])
		a = input().lower()

		if(a == "sim" or a == "s" or a == "1"):
			answers.append(1)
			i += 1
			
		elif(a == "não" or a == "nao" or a == "n" or a == "0"):
			answers.append(0)
			i += 1

		else:
			print("\nResposta Inválida\nResponda novamente\n")
				

	probabilities = df["probability"].to_list()
	risk_sum = 0
	for answer, probability in zip(answers, probabilities):

		if(probability > 0.5 and answer == 1):
			risk_sum = -1	#high risk client
			break

		elif(probability < 0.5 and answer == 1):
			risk_sum += 1 	#medium risk client

	#case risk sum of not common symptoms are greater than the half ammount of symptoms 
	if(risk_sum > len(questions)/2):
		risk_sum = -1	#high riks client

	#check what final message will be delivered	
	if(risk_sum < 0):
		print("Chances altas de ter covid. Volte para casa e busque atendimento médico")
	elif(risk_sum > 0):
		print("Você possui alguns dos sintomas menos comuns da Covid-19.\nTalvez seja a hora de buscar atendimento médico.\nVocê poderá utilizar os serviços deste estabelecimento se seguir corretamente os protocolos de segurança:\n-Lavar Mãos\n-Usar Máscara")
	else:
		print("Seja Bem-Vindo ao estabelecimento. Durante sua estadia use máscara e lembre-se de lavar as mãos com alcool em gel")

if __name__ == '__main__':
	main()