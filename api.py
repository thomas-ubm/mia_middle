from one import *


app = FastAPI()

# Exemples de prompts de l'utilisateur qui arriveent ici
# prompt1 = "Je désirerais réserver la salle K101 mardi prochain."
# prompt2 = "Je voudrais des informations sur les horaires d'ouverture."
# prompt3 = "Je recherche des informations financières sur le budget de la Direction Générale."
# prompt4 = "Je désirerais réserver la salle K101 mardi prochain, et je voudrais des informations sur les horaires d'ouverture."
# Avec :
# client_key = Mistral(api_key="trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2")
# agent_id = agent_id="ag:56f583a3:20241220:untitled-agent:631f6eb5"

# Requêtte vers l'API /
@app.get("/")
def index(prompt):
    client = Mistral(api_key=api_key)
    response = client.agents.complete(
        agent_id = agent_id,
        messages = [
            {"role": "user", "content":prompt},
         ]
    )
    # return response.choices[0].message.content
    # return {"message": response}
    response_agent = response.choices[0].message.content.replace("\n","")

    dict_response = eval(str(response_agent))
    response_salles = ""
    response_infos = ""
    response_finances = ""

    if len(dict_response["RESERVATION_SALLE"]) != 0:
        print ("Thème RESERVATION_SALLE trouvé")
        data_salles = {"prompt":prompt}
        response_salles = requests.get('https://c827-82-126-180-240.ngrok-free.app/salles', params = data_salles).text
        print(response_salles)

    if len(dict_response["INFO_GENERALE"]) != 0:
        print ("Thème INFO_GENERALE trouvé")
        data_infos = {"prompt":prompt}
        response_infos = requests.get('https://c827-82-126-180-240.ngrok-free.app/infos', params = data_infos).text
        print(response_infos)

    if len(dict_response["FINANCE"]) != 0:
        print ("Thème FINANCE trouvé")
        data_finances = {"prompt":prompt}
        response_finances = requests.get('https://c827-82-126-180-240.ngrok-free.app/finances', params = data_finances).text
        print(response_finances)
    
    """
    response_test = requests.get('https://c827-82-126-180-240.ngrok-free.app/')
    response_test.text
    return response_test.text
    """
    response_full = response_salles + response_infos + response_finances
    return response_full
    





"""
# Requêtte vers l'API /rag
@app.get("/rag")
def index(prompt):
    messages = [
        {"role": "user", "content":prompt},
    ]
    #response = pipe(messages, max_new_tokens=5)[0]['generated_text'][1]['content']
    response = prompt
    print(response)
    return {"message": response}

    # 1. Transf. prompt en embedding (obtenir un vecteur)
    # 2. Analyse. du COS entre le prompt et les embedding des différents agents localisés sur l'autre serveur d'API
    # 3. Une fois trouver le bon agent (COSmax)
    # 4. On appelle l'API correspondant à l'agent(COSmax) pour envoyer le prompt utilisateur
"""





