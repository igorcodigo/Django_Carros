from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

client = OpenAI(
  api_key= os.getenv('openai_api_key'),
)
def gerar_car_ai_bio(model,brand,year):
    prompt = f" Me mostre uma descrição de venda para o carro {model} {brand} {year} em apenas 250 caracteres. Fale coisas. Comece com um artigo definido da língua portuguesa"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Este é um modelo exemplo, ajuste conforme sua necessidade
        max_tokens= 1000, # Limita a resposta para ate essa quantidade de tokens
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
