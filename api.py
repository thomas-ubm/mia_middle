from one import *


app = FastAPI()

# Exemples de prompts de l'utilisateur qui arriveent ici
# prompt1 = "Je désirerais réserver la salle K101 mardi prochain"
# prompt2 = "Je voudrais des informations sur les horaires d'ouverture"
# prompt3 = "Je recherche des informations financières sur le budger de la Direction Générale"


# Requêtte vers l'API /
@app.get("/")
def index(prompt):
    response = client.agents.complete(
        #model='mistral-large-latest',
        agent_id="ag:9be9de82:20241217:analyse-sentiments:ce6e978e",
        messages = [
            {"role": "user", "content":prompt},
         ]
    )
    #return response.choices[0].message.content
    return {"message": response}

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





