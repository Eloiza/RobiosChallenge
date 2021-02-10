import pandas as pd
from mqtt_protocol import Publisher
import form_lib

def main():
	df = pd.read_csv("Data/symptoms.csv")
	questions = df["question"].to_list()

	answers = []
	i = 0
	while (i < len(questions)):
		print(str(i +1) + '. '+ questions[i])

		a = form_lib.answer_standardize(input().lower())

		if(a != -1):
			answers.append(a)
			i += 1
	
		else:
			print("\nResposta Inválida\nResponda novamente\n")
				

	probabilities = df["probability"].to_list()
	risk = form_lib.form_analyzer(answers, probabilities)

	#check what final message will be delivered	
	if(risk < 0):
		risk = 'high'
		print("Chances altas de ter covid. Volte para casa e busque atendimento médico")

	elif(risk > 0):
		risk = 'medium'
		print("Você possui alguns dos sintomas menos comuns da Covid-19.\nTalvez seja a hora de buscar atendimento médico.\nVocê poderá utilizar os serviços deste estabelecimento se seguir corretamente os protocolos de segurança:\n-Lavar Mãos\n-Usar Máscara")
	
	else:
		risk = 'low'
		print("Seja Bem-Vindo ao estabelecimento. Durante sua estadia use máscara e lembre-se de lavar as mãos com alcool em gel")

	#send a message with the result
	publisher = Publisher()
	publisher.publish(broker_adress="localhost", topic="dw/demo", message=risk)

if __name__ == '__main__':
	main()