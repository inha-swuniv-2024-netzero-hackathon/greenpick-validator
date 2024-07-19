import pandas as pd

from models import Product
from services import evaluate_product_service

unscored_df = pd.read_csv('./test.csv')
unscored_df['green_score'] = None
for idx, row in unscored_df.iterrows():
    green_score = evaluate_product_service(Product(name=row['name'])).score
    unscored_df.loc[idx, 'green_score'] = green_score
    print(green_score)

    # 결과를 CSV로 저장 (선택 사항)
unscored_df.to_csv('./scored_test2.csv', index=False)
