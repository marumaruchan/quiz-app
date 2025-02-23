import streamlit as st
import random

def main():
    st.title("データサイエンス学習クイズ")

    stage = st.sidebar.selectbox("ステージを選択", [
        "ステージ1: Python基礎", 
        "ステージ2: データ操作", 
        "ステージ3: 可視化", 
        "ステージ4: 統計分析", 
        "ステージ5: 機械学習基礎", 
        "ステージ6: 応用問題チャレンジ！", 
        "ステージ7: 統計解析"
    ])
    
    questions = {
        # Add your questions for stages 6 and 7 here
    }
    
    # Display questions for the selected stage
    if stage in questions:
        stage_questions = questions[stage]
        score = 0

        for question in stage_questions:
            st.write(question['question'])
            user_answer = st.radio("選択肢を選んでください", question['options'])
            if st.button("回答"):
                if user_answer == question['answer']:
                    st.success("正解です！")
                    score += 1
                else:
                    st.error(f"不正解です。正しい答えは: {question['answer']}")
                st.write(question['explanation'])
        
        st.write(f"あなたのスコア: {score}/{len(stage_questions)}")

if __name__ == "__main__":
    main()
