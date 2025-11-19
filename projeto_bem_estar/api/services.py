import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def calcular_indice_bem_estar(humor: int, foco: int, pausas: int) -> float:
    """Calcula o Índice de Bem-Estar com base nas entradas do usuário."""
    if humor is None or foco is None or pausas is None:
        return 0.0
    return round((humor + foco + pausas) / 3, 2)

def calcular_risco_burnout(horas_trabalhadas: int, pausas: int) -> float:
    """Calcula o Risco de Burnout com base nas entradas do usuário."""
    if horas_trabalhadas is None or pausas is None:
        return 0.0
    return round((horas_trabalhadas * 0.2) - (pausas * 0.3), 2)

def gerar_feedback_ia(indice_bem_estar: float, risco_burnout: float, humor: int) -> str:
    """
    Gera uma mensagem de feedback personalizada usando a IA Generativa (GPT).
    """
    try:
        prompt = f"""
        Aja como um coach de bem-estar corporativo.
        Gere uma mensagem de feedback curta (2-3 frases), motivacional e empática para um colaborador.
        O feedback deve ser baseado nos seguintes dados:
        - Índice de Bem-Estar (0-5): {indice_bem_estar}
        - Risco de Burnout (quanto maior, pior): {risco_burnout}
        - Nota de Humor do dia (1-5): {humor}

        Se o risco de burnout for alto (acima de 1.5) ou o humor baixo (1 ou 2),
        a mensagem deve ser mais acolhedora e sugerir uma micro-pausa (ex: "faça um alongamento", "beba um copo d'água").
        Caso contrário, pode ser mais positiva e encorajadora.
        Seja humano e evite jargões.
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente de bem-estar empático e motivacional."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Erro ao chamar a API da OpenAI: {e}")
        return "Lembre-se de cuidar do seu bem-estar hoje. Pequenas pausas podem fazer uma grande diferença!"

