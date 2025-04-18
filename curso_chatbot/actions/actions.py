# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionValidarEspecialidade(Action):
    def name(self) -> Text:
        return "action_validade_especialidade"
    
    def run(self, dispacther: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        especialidade = tracker.get_slot("especialidade_medico")
        data = tracker.get_slot("data_hora_consulta")
        periodo = tracker.get_slot("periodo_consulta_agenda")

        especialidades_validas = ["endocrino", "nutricionista", "cardiologista"]

        print("CHAMOU O SCRIPT")

        if especialidade.lower() in especialidades_validas:
            dispacther.utter_message(text=f"Especialidade confirmada para atendimento. Certo, iremos encaminhar esses dados para a nossa central: \n-{especialidade}\n- {data}\n- {periodo}.\nLogo mais eles entrarão em contato! Posso ajudar com mais alguma coisa?")
            return[]
        else:
            dispacther.utter_message(text="Desculpe, essa especialidade não está disponível. As especialidades válidas são: Endocrino, Nutricionista e Cardiologista.\n Favor, digitar: 'Quero agendar uma consulta para reiniciar o dialogo se desejar'")
            return[SlotSet("especialidade_medico", None)]
# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
