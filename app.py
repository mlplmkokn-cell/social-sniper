import streamlit as st
from openai import OpenAI

# 1. Настройка и Стили (Mobile-Ready)
st.set_page_config(page_title="Social Sniper AI", page_icon="🎯", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .ad-banner { background: #1e1e1e; padding: 15px; border-radius: 10px; border-bottom: 3px solid #ff4b4b; text-align: center; margin-bottom: 20px; }
    .analysis-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin: 15px 0; }
    .logic-box { background-color: #21262d; padding: 15px; border-radius: 8px; border: 1px solid #30363d; color: #8b949e; font-size: 0.9rem; }
    .premium-badge { color: #ff4b4b; font-weight: bold; border: 1px solid #ff4b4b; padding: 2px 5px; border-radius: 4px; font-size: 0.7rem; }
    </style>
    """, unsafe_allow_html=True)

# Инициализация ИИ (OpenRouter)
try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except:
    st.error("Ошибка подключения. Проверь API-ключ в настройках.")

# --- ВЕРХНИЙ БЛОК (РЕКЛАМА И ХУК) ---
st.markdown("<div class='ad-banner'>🚀 <b>TG-КАНАЛ:</b> База антропологии и психологии — <a href='#' style='color:#ff4b4b;'>Вступить бесплатно</a></div>", unsafe_allow_html=True)

st.title("🎯 Social Sniper AI")
st.caption("Версия 4.5: Интеллектуальный разбор и тактика выравнивания фрейма")

# --- 1. ПРИМЕР: РАЗБОР ПОДТЕКСТА (ПРОЛИСТАТЬ ДО БАГА) ---
with st.expander("🔍 Как работает анализ подтекста (Пример)"):
    st.markdown("""
    **Ситуация:** Вы договорились на 19:00 у метро. В 18:30 она пишет: *"Ой, я тут рядом с ТЦ, давай лучше здесь встретимся?"*<br>
    **Подтекст:** Она проверяет, готов ли ты менять свои планы ради её минутного удобства. Это тест на 'удобного парня'.<br>
    **Твой ответ:** *"Мне неудобно там. Жду тебя на месте, как договаривались".*<br>
    **Главная мысль:** Ты не 'нападаешь', ты просто сохраняешь свои границы нерушимыми. Если ты поедешь к ТЦ — ты уже проиграл встречу до её начала.
    """)

st.divider()

# --- 2. ГЛАВНЫЙ АНАЛИЗАТОР (ПОДТЕКСТ И СУТЬ) ---
st.header("1. Разбор переписки и Подтекста")
chat_input = st.text_area("Вставь сообщение или диалог:", height=150, placeholder="Её фраза или ваш чат...")

if st.button("🚀 Вскрыть подтекст"):
    if chat_input:
        with st.spinner("Снайпер анализирует мотивы..."):
            prompt = f"""
            Проанализируй подтекст этого сообщения: '{chat_input}'.
            1. Что она на самом деле проверяет или хочет?
            2. Краткий, жесткий ответ для сохранения фрейма.
            3. Главная мысль: почему нужно ответить именно так и какую границу мы защищаем.
            Стиль: А2, глубоко, без воды, антропологический подход.
            """
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            
            st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
            st.markdown(f"### 📊 Разбор:")
            st.write(response.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Введи текст.")

st.divider()

# --- 3. ТАКТИЧЕСКИЙ ЧАТ (ПОМОЩЬ В ДОСТИЖЕНИИ ЦЕЛИ) ---
st.header("2. Тактический Чат: Навигация встречи")
st.write("Используй этот чат, чтобы понять, как переместить её из точки А в точку Б.")

goal_context = st.text_input("Твоя цель (например: 'вытянуть домой из кафе' или 'перейти к тактильности'):")
current_state = st.text_area("Что происходит сейчас? (её реакция, контекст):")

if st.button("🏹 Получить тактический план"):
    if goal_context and current_state:
        with st.spinner("Просчитываю маршрут..."):
            prompt = f"Цель: {goal_context}. Текущая ситуация: {current_state}. Напиши, что именно нужно делать сейчас, как использовать контекст места (например, кафе или боулинг) для сближения и какой фразой предложить перемещение. Стиль А2."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            
            st.markdown("### 🗺️ Тактический план:")
            st.success(response.choices[0].message.content)
            st.markdown("<div class='logic-box'>Помни: перемещение должно выглядеть как твоя инициатива, а не просьба. Ты просто приглашаешь её в своё пространство.</div>", unsafe_allow_html=True)
    else:
        st.warning("Заполни цель и текущую ситуацию.")

st.divider()

# --- 4. БАЗА ПАСХАЛОК (Памятки) ---
st.header("📚 Памятки Снайпера")
col1, col2 = st.columns(2)
with col1:
    with st.expander("📍 О нерушимых границах"):
        st.write("Твоё 'нет' имеет большую ценность, чем твое 'да'. Если она видит, что твои правила не меняются под её давлением — её биология считывает в тебе надежного и сильного лидера.")
with col2:
    with st.expander("🔥 О контексте места"):
        st.write("В кафе вы сидите друг против друга — это допрос. В боулинге вы двигаетесь — это жизнь. Используй активность, чтобы естественным образом сокращать дистанцию.")

st.sidebar.markdown("### 💎 Статус: Free")
st.sidebar.write("Доступ к базовому анализу открыт.")
st.sidebar.markdown("---")
st.sidebar.caption("Social Sniper AI © 2026. Итоговый вариант текста — «А2».")
