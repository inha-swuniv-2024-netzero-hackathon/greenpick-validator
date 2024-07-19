import re

def parse_response(response: str) -> int:
    score_match = re.search(r'점수:\s*(\d+)', response)
    if not score_match:
        raise ValueError("응답 파싱 실패")
    return int(score_match.group(1))