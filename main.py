import pandas as pd
from mqtt_protocol import Publisher
import form_lib

def main():
	print("Olá, eu sou o Robios e vou te fazer algumas perguntas B)\nEssas perguntas são importantes para a segurança de todos\nVamos lá!")

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
			print("\nResposta Inválida\nResponda novamente usando sim/não ou s/n ou 1/0\n")
				

	probabilities = df["probability"].to_list()
	risk = form_lib.form_analyzer(answers, probabilities)

	#check what final message will be delivered	
	if(risk < 0):
		risk = 'high'
		print("Você tem chances altas de ter covid. É melhor ficar em casa e buscar atendimento médico")

	elif(risk > 0):
		risk = 'medium'
		print("Você possui alguns dos sintomas menos comuns da Covid-19.\nTalvez seja a hora de buscar atendimento médico.\nVocê poderá utilizar os serviços deste estabelecimento se seguir corretamente os protocolos de segurança:\n-Lavar Mãos\n-Usar Máscara")
	
	else:
		risk = 'low'
		print("Seja Bem-Vindo ao estabelecimento.\nDurante sua visita use máscara e lembre-se de lavar as mãos com alcool em gel")

	result = "Risco: " + risk + '; Respostas: ' + str(answers)
	
	#send a message with the result
	publisher = Publisher()
	publisher.publish(broker_adress="localhost", topic="dw/demo", message=result)

if __name__ == '__main__':
	main()