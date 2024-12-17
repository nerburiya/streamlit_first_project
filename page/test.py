import streamlit as st
import random

# 랜덤 숫자 생성 함수
def generate_number():
    return random.sample(range(10), 3)

# 스트라이크와 볼 계산 함수
def check_numbers(secret, guess):
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == secret[i]:  # 같은 위치, 같은 숫자
            strike += 1
        elif guess[i] in secret:   # 다른 위치, 같은 숫자
            ball += 1
    return strike, ball

# Streamlit 초기 설정
st.title("🎮 숫자 야구 게임")
st.write("**서로 다른 3개의 숫자를 맞춰보세요!**")
st.write("각 자리 숫자는 **서로 달라야** 합니다.")

# 게임 상태 관리
if "secret" not in st.session_state:
    st.session_state.secret = generate_number()  # 비밀 숫자 생성
    st.session_state.attempts = 0  # 시도 횟수 초기화
    st.session_state.game_over = False  # 게임 종료 여부

# 사용자 입력
user_input = st.text_input("3자리 숫자를 입력하세요:", key="user_input")

# 입력 검증 및 처리
if st.button("확인") and not st.session_state.game_over:
    if len(user_input) != 3 or not user_input.isdigit() or len(set(user_input)) != 3:
        st.error("⚠️ 잘못된 입력입니다. 서로 다른 **3자리 숫자**를 입력해주세요.")
    else:
        # 입력 처리
        st.session_state.attempts += 1
        guess = [int(n) for n in user_input]
        strike, ball = check_numbers(st.session_state.secret, guess)
        
        # 결과 출력
        st.info(f"🎯 결과: **{strike} 스트라이크, {ball} 볼**")
        
        # 승리 조건 확인
        if strike == 3:
            st.success(f"🎉 축하합니다! {st.session_state.attempts}번 만에 맞추셨습니다!")
            st.session_state.game_over = True
        else:
            st.write(f"🔄 시도 횟수: {st.session_state.attempts}")

# 게임 재시작
if st.session_state.game_over:
    if st.button("다시 시작하기"):
        st.session_state.secret = generate_number()
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()
