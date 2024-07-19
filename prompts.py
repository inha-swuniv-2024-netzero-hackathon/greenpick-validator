from models import Product

def create_prompt(product: Product) -> str:
    return f"""제품 이름: {product.name}

위 정보를 바탕으로 이 제품이 친환경적이고 탄소중립에 도움이 되는 정도를 0점부터 100점까지 평가해주세요.
다음 기준을 고려하여 평가해 주십시오:
1. 재료의 친환경성
2. 제조 과정의 환경 영향
3. 제품 사용 시 환경 영향
4. 제품 수명 및 재사용 가능성
5. 포장재의 친환경성

응답 형식:
점수: [0-100 사이의 숫자]
"""