import streamlit as st
from openai import OpenAI

# ==========================================
# МОДУЛЬ 1: СТИЛЬ И КОНФИГУРАЦИЯ (СКЕЛЕТ)
# ==========================================
st.set_page_config(page_title="Social Sniper AI", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    /* Темная тема и шрифты А2 */
    .stApp { background-color: #0e1117; color: #ffffff; }
    
    /* Рекламные блоки и плашки */
    .ad-banner { background: #1e1e1e; padding: 15px; border-radius: 10px; border-bottom: 3px solid #ff4b4b; text-align: center; margin-bottom: 20px; }
    
    /* Контейнеры для разборов */
    .analysis-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin: 15px 0; }
    .failed-case { background-color: #2d1b1b; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    
    /* Текстовые акценты */
    .logic-hint { color: #8b949e; font-size: 0.9rem; border-top: 1px solid #30363d; padding-top: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Инициализация ИИ (Оставляем один раз)
try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except:
    st.error("Настрой API-ключ в Secrets!")

# ==========================================
# МОДУЛЬ 2: САЙДБАР (МОНЕТИЗАЦИЯ И РЕКЛАМА)
# ==========================================
with st.sidebar:
    st.title("🎯 Sniper Menu")
    status = st.radio("Твой статус:", ["Free (Антрополог)", "Premium ⭐ (Снайпер)"])
    st.divider()
    
    # Место для твоей рекламы
    st.write("📢 **Рекламный блок**")
    st.info("Твой ТГ-канал: [Подписаться](https://t.me/твой_канал)")
    
    if status == "Free (Антрополог)":
        st.markdown("---")
        st.write("💰 **Premium: 200₽**")
        st.caption("Докрутка сообщений + Снайперские ответы")

# ==========================================
# МОДУЛЬ 3: ВЕРХНИЙ ХУК (ОБЯЗАТЕЛЬНЫЕ ПРИМЕРЫ)
# ==========================================
st.markdown("<div class='ad-banner'>🚀 <b>КЕЙС ДНЯ:</b> Как не слить встречу за 30 минут до начала</div>", unsafe_allow_html=True)

st.header("📉 Анатомия слива (Разбор)")
st.markdown("""
<div class='failed-case'>
<b>Ситуация:</b> Она меняет место встречи в последний момент.<br>
<b>Слив:</b> "Ну ладно, давай там, мне без разницы".<br>
<b>Почему это плохо:</b> Ты показал, что твой комфорт и твои планы вторичны. Ты стал ведомым.<br>
<b>Как надо:</b> "Мне там неудобно. Жду тебя на месте".
</div>
""", unsafe_allow_ HTML=True)

st.divider()

# ==========================================
# МОДУЛЬ 4: ОСНОВНОЙ АНАЛИЗАТОР (ПОДТЕКСТ)
# ==========================================
st.header("1. Разбор подтекста и логика ответа")
chat_data = st.text_area("Вставь диалог:", height=150, key="main_chat")

if st.button("🚀 Вскрыть подтекст"):
    if chat_data:
        with st.spinner("Снайпер делает замер..."):
            prompt = f"Проанализируй подтекст сообщения: '{chat_data}'. Объясни скрытый мотив, дай краткий ответ и ГЛАВНУЮ МЫСЛЬ: почему отвечаем именно так. Стиль А2."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            
            st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
            st.write(response.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Поле пусто.")

st.divider()

# ==========================================
# МОДУЛЬ 5: ТАКТИЧЕСКИЙ ЧАТ (НАВИГАЦИЯ)
# ==========================================
st.header("2. Тактический Чат: Навигация цели")
col_a, col_b = st.columns(2)
with col_a:
    target = st.text_input("Твоя цель:", placeholder="Например: Кафе -> Дом")
with col_b:
    context = st.text_input("Контекст сейчас:", placeholder="Например: Мы в боулинге")

tactical_msg = st.text_area("Что она говорит или делает сейчас?")

if st.button("🏹 Построить маршрут"):
    if tactical_msg:
        with st.spinner("Просчитываю траекторию..."):
            prompt = f"Цель: {target}. Контекст: {context}. Текущая ситуация: {tactical_msg}. Дай тактический совет по сближению и перемещению. Стиль А2."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            st.success(response.choices[0].message.content)
            st.markdown("<div class='logic-hint'>Подсказка: Твоя задача — вести. Любое перемещение — это твое решение.</div>", unsafe_allow_html=True)

st.divider()

# ==========================================
# МОДУЛЬ 6: БАЗА ПАСХАЛОК (ПАМЯТКИ)
# ==========================================
st.header("📚 База знаний")
p1, p2 = st.columns(2)
with p1:
    with st.expander("📍 О границах"):
        st.write("Твои границы нерушимы. Если она их шатает — это тест. Не пройдешь — потеряешь влечение.")
with p2:
    with st.expander("🔥 О контексте"):
        st.write("Выбирай места, где можно двигаться и трогать, а не сидеть друг против друга.")

st.markdown("---")
st.caption("Social Sniper AI v4.8 Stable. Итоговый вариант текста — «А2».")
