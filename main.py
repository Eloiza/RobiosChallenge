import pandas as pd
import paho.mqtt.client as mqtt

def publish_result(broker_adress, topic, result):
	client = mqtt.Client()	
	client.connect(broker_adress)
	client.publish(topic, result)
	client.disconnect()


def risk_analyzer(answers, probabilities):
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

def main():
	df = pd.read_csv("Data/symptoms.csv")
	questions = df["question"].to_list()

	answers = []
	i = 0
	while (i < len(questions)):
		print(str(i +1) + '. '+ questions[i])

		a = answer_standardize(input().lower())

		if(a != -1):
			answers.append(a)
			i += 1
	
		else:
			print("\nResposta Inválida\nResponda novamente\n")
				

	probabilities = df["probability"].to_list()
	risk = risk_analyzer(answers, probabilities)

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
	publish_result(broker_adress="localhost", topic= "dw/demo", result=result)

if __name__ == '__main__':
	main()