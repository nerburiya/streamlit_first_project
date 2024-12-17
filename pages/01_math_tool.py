import streamlit as st

# 소수 판별 함수
def is_prime(n):
    # 2보다 작은 수는 소수가 아님
    if n < 2:
        return False

    # 2는 소수
    if n == 2:
        return True

    # 짝수는 2를 제외하고 소수가 아님
    if n % 2 == 0:
        return False

    # 3부터 n의 제곱근까지의 홀수로 나누어 떨어지는지 확인
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# 가장 가까운 소수를 찾는 함수
def find_closest_prime(n):
    if is_prime(n):
        return n

    # 위아래로 동시에 검사
    lower = n - 1
    upper = n + 1

    while True:
        # 더 작은 수에서 소수 확인
        if lower >= 2 and is_prime(lower):
            # 위쪽 수와의 거리 비교
            if is_prime(upper):
                # 둘 다 소수라면 더 가까운 것 반환
                if (upper - n) < (n - lower):
                    return upper
                return lower
            return lower

        # 더 큰 수에서 소수 확인
        if is_prime(upper):
            return upper

        lower -= 1
        upper += 1

# Streamlit UI 구성
st.title("가장 가까운 소수 찾기")
st.write("숫자를 입력하면 해당 숫자가 소수인지 확인하고 가장 가까운 소수를 찾아줍니다.")

# 사용자 입력
num = st.number_input("숫자를 입력하세요 (0 입력 시 프로그램 종료)", min_value=0, step=1, value=0)

# 입력값 처리 및 결과 표시
if num != 0:
    closest = find_closest_prime(num)
    if closest == num:
        st.success(f"🎉 {num}은(는) 이미 소수입니다!")
    else:
        st.info(f"🔍 {num}에서 가장 가까운 소수는 **{closest}**입니다.")
        st.write(f"📏 차이: {abs(num - closest)}")
else:
    st.write("프로그램을 종료하려면 숫자 0을 입력하세요.")
