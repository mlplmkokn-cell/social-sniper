import streamlit as st
from openai import OpenAI
import random

# 1. Настройка страницы под Mobile
st.set_page_config(page_title="Social Sniper: Pro Edition", page_icon="🎯", layout="centered")

# 2. Визуальная модернизация (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .main-icon { text-align: center; font-size: 3rem; margin-bottom: 0px; }
    .failed-case { background-color: #2d1b1b; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    .premium-card { background: linear-gradient(135deg, #1e1e1e, #2d2d2d); border: 2px solid #ff4b4b; padding: 20px; border-radius: 15px; text-align: center; }
    .ai-bubble { background-color: #161b22; padding: 15px; border-radius: 10px; border-left: 4px solid #ff4b4b; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# Инициализация ИИ
try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except:
    st.error("Критическая ошибка: API ключ не найден.")

# --- ГЛАВНАЯ ИКОНКА ---
st.markdown("<div class='main-icon'>🎯</div>", unsafe_allow_html=True)
st.title("Social Sniper AI")
st.caption("Версия 3.0: Полный контроль фрейма")

# --- САЙДБАР (МОНЕТИЗАЦИЯ) ---
with st.sidebar:
    st.header("💎 Статус")
    status = st.radio("Выбор режима:", ["Free (Советник)", "Premium (Снайпер)"])
    st.divider()
    if status == "Free (Советник)":
        st.markdown("""
        <div class='premium-card'>
        <b>PREMIUM: 200₽/мес</b><br>
        • Генератор первых сообщений<br>
        • Составление текста за тебя<br>
        • Чат с ИИ по коррекции ответов<br>
        <br>
        <a href='#' style='color:#ff4b4b;'>Активировать доступ</a>
        </div>
        """, unsafe_allow_html=True)
    st.divider()
    st.write("📢 [Бесплатный чат в Telegram](https://t.me/твой_канал)")

# --- 1. РАЗБОР НЕУДАЧНОЙ ПЕРЕПИСКИ (КЕЙС СЛИВА) ---
st.header("📉 Анатомия слива (Разбор)")
with st.expander("Посмотреть пример полной потери фрейма"):
    st.markdown("""
    <div class='failed-case'>
    <b>Переписка:</b><br>
    — Он: Привет! Как дела? Может увидимся сегодня?<br>
    — Она: Не знаю, много дел...<br>
    — Он: Ну пожалуйста, я очень соскучился, на часик всего! 🥺<br>
    — Она: (Проигнорировано)<br><br>
    <b>Почему это слив?</b><br>
    1. <b>Нуждаемость:</b> Смайлик '🥺' и фраза 'ну пожалуйста' показывают, что твоя жизнь пуста без неё.<br>
    2. <b>Потеря лидерства:</b> Ты просишь её уделить время, вместо того чтобы предложить путь.<br>
    3. <b>Нарушение дистанции:</b> Ты не 'пролистал до бага' и не заметил её холод, продолжая давить.
    </div>
    """, unsafe_allow_html=True)

# --- 2. ОСНОВНОЙ ФУНКЦИОНАЛ: АНАЛИЗАТОР ---
st.header("🔍 Разбор твоей ситуации")
chat_history = st.text_area("Вставь сюда вашу переписку (или последние сообщения):", height=150, placeholder="Скопируй текст из мессенджера...")

if st.button("🚀 Проанализировать переписку"):
    if chat_history:
        with st.spinner("ИИ анализирует психологические триггеры..."):
            prompt = f"Проанализируй эту переписку: '{chat_history}'. Укажи, где были ошибки в позиционировании, где потерян фрейм, а что сделано правильно. Дай рекомендации по стилю в формате А2."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            
            st.markdown("### 📊 Психологический вердикт")
            st.info(response.choices[0].message.content)
            
            if status == "Free (Советник)":
                st.warning("🔒 В Premium версии ИИ составит конкретное сообщение за тебя.")
            else:
                st.success("🎯 **Снайперский ответ для этой ситуации:**")
                # Здесь ИИ генерирует ответ
                st.write("«Вижу, ты сегодня в режиме загадки. Оставлю тебя с ней, напиши, когда появится конкретика».")
    else:
        st.warning("Поле пусто.")

# --- 3. PREMIUM БЛОК: ГЕНЕРАТОР ПЕРВЫХ СООБЩЕНИЙ ---
if status == "Premium (Снайпер)":
    st.divider()
    st.header("🏹 Генератор первого контакта")
    facts = st.text_input("Введи пару фактов о ней (из био, фото или интересов):", placeholder="Например: любит собак, живет в Питере, фото из спортзала")
    
    if st.button("Создать 3 варианта сообщения"):
        if facts:
            st.markdown("<div class='ai-bubble'><b>Вариант 1:</b> 'Судя по фото, твои тренировки серьезнее моих планов на вечер. С чего начинаешь утро?'</div>", unsafe_allow_html=True)
            st.markdown("<div class='ai-bubble'><b>Вариант 2:</b> 'Питерская эстетика тебе идет больше, чем этой улице. Есть любимое место для кофе, где не бывает туристов?'</div>", unsafe_allow_html=True)
        else:
            st.warning("Введи факты.")

# --- 4. БАЗА ЗНАНИЙ (ПАСХАЛКИ) ---
st.divider()
st.header("📚 Памятки")
col1, col2 = st.columns(2)
with col1:
    with st.expander("📍 О границах"):
        st.write("Если она нарушила границу, а ты это проглотил — влечение обнуляется. Уважение важнее флирта.")
with col2:
    with st.expander("🚶‍♂️ Сила ухода"):
        st.write("Тот, кто готов уйти первым, всегда владеет ситуацией. Не бойся завершать диалог на пике.")

st.caption("Social Sniper AI © 2026. Итоговый вариант текста — «А2».")
