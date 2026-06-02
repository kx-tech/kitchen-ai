import streamlit as st
import requests

DEEPSEEK_API_KEY = "sk-1963667372f949f2a3e756f2780cf0eb"

def deepseek_chat(prompt):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    res = requests.post("https://api.deepseek.com/v1/chat/completions", json=data, headers=headers)
    return res.json()["choices"][0]["message"]["content"]

st.title("厨研AI·多功能模块化厨具智能设计系统")
tab1, tab2, tab3 = st.tabs(["图一主机设计", "图二模块套装", "图四收纳配件"])

with tab1:
    st.subheader("【图一：动力主机底座】方案&商业化分析")
    user_input = st.text_input("输入产品需求（例：小户型多功能料理主机）")
    if st.button("AI生成方案+商业价值"):
        res = deepseek_chat(f"撰写多功能厨具主机产品设计方案+详细商业化价值，{user_input}")
        st.write(res)

with tab2:
    st.subheader("【图二：可拆卸功能模块组】方案&商业化分析")
    user_input2 = st.text_input("输入模块需求（例：切片/研磨/搅拌三合一模块）")
    if st.button("生成模块内容"):
        res2 = deepseek_chat(f"厨具功能模块设计+商业化盈利分析：{user_input2}")
        st.write(res2)

with tab3:
    st.subheader("【图四：收纳便携配件】方案&商业化分析")
    user_input3 = st.text_input("输入配件需求（例：磁吸收纳盒+露营便携盒）")
    if st.button("生成配件内容"):
        res3 = deepseek_chat(f"厨具收纳配件设计+商业化价值：{user_input3}")
        st.write(res3)
