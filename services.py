from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_PROJECT_ID
from models import Product, ProductScore
from prompts import create_prompt
from utils import parse_response

#client = OpenAI(project=OPENAI_PROJECT_ID)
#client.api_key = OPENAI_API_KEY


async def evaluate_product_service(product: Product) -> ProductScore:
    prompt = create_prompt(product)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 제품의 친환경성과 탄소중립 기여도를 평가하는 전문가입니다. 점수만 제공해주세요."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        n=1,
        temperature=0.3,
    )

    result = response.choices[0].message.content
    score = parse_response(result)
    score = max(0, min(score, 100))

    return ProductScore(score=score)
