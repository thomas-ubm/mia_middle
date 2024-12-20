from mistralai import Mistral
from fastapi import FastAPI
import requests

# from function import * 


# Connexion au client via une api_key = "aytrA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2"
client = Mistral(api_key="trA3qWPCyCxnGFqXozRTOh1bSNMoZmQ2")
# api_keys = os.environ["MISTRAL_API"]    #avec variable d'environnement
#client = Mistral(api_key=api_keys)

# Agent Mistral : mia_general
agent_id="ag:56f583a3:20241220:untitled-agent:631f6eb5"
