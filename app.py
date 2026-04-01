import streamlit as st
from openai import OpenAI
import random

# 1. Настройка страницы
st.set_page_config(page_title="Social Sniper: Pro Edition", page_icon="🎯", layout="centered")

# 2. Улучшенный дизайн (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .ad-block { background: linear-gradient(90deg, #1e1e1e, #2d2d2d); padding: 15px; border-radius: 10px; border: 1px dashed #ff4b4b; text-align: center; margin-bottom: 20px; }
    .quote-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 4px solid #ff4b4b; font-style: italic; margin: 15px 0; }
    .case-card { background-color: #1f2937; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #30363d; }
    .premium-badge { background-color: #ff4b4b; color: white; padding: 2px 8px; border-radius: 5px; font-size: 0.8rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Инициализация ИИ
try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except:
    st.error("Ошибка API-ключа.")

# --- МОБИЛЬНЫЙ САЙДБАР ---
with st.sidebar:
    st.title("🎯 Меню")
    status = st.radio("Статус аккаунта:", ["Бесплатный", "PREMIUM ⭐"])
    st.divider()
    st.write("📢 **Рекламный блок**")
    st.info("Здесь может быть ваша реклама или ссылка на ТГ-канал")
    st.markdown("[Связаться с админом](https://t.me/твой_ник)")

# --- ОСНОВНОЙ КОНТЕНТ ---
st.title("Social Sniper AI 🎯")
st.caption("Версия 2.0: Антропология, Фрейм и Доминирование")

# 1. Рекламная плашка сверху (как в мобильных приложениях)
st.markdown("""
<div class="ad-block">
    🚀 <b>АКЦИЯ:</b> Подписка на закрытый чат по баллистике и психологии — 100₽/мес.
</div>
""", unsafe_allow_html=True)

# 2. Основной функционал
with st.container():
    msg = st.text_area("Вставь её сообщение:", placeholder="Например: 'Я еще не решила...'")
    if st.button("🚀 Провести снайперский анализ"):
        if msg:
            with st.spinner("Анализирую биологические триггеры..."):
                prompt = f"Проанализируй сообщение: '{msg}'. Используй антропологию, фрейм и границы. Дай ответ в стиле А2 (глубоко и четко)."
                completion = client.chat.completions.create(
                    model="openai/gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.markdown("### 🔍 Психологический вердикт")
                st.info(completion.choices[0].message.content)
                
                if status == "Бесплатный":
                    st.warning("🔒 Готовые 'снайперские' фразы доступны в PREMIUM версии.")
                else:
                    st.success("🎯 **Используй одну из этих фраз:**")
                    st.write("— 'Твое право. Если надумаешь — пиши, если нет — хорошего вечера'.")
                    st.write("— 'Мне нравится твоя неопределенность, но мой график её не любит. На связи'.")
        else:
            st.warning("Введи текст!")

st.divider()

# 3. НОВЫЙ БЛОК: Разбор реальных кейсов
st.header("📂 Разбор полетов (Кейсы)")
with st.expander("Кейс #1: Она отменила встречу за час"):
    st.markdown("""
    <div class="case-card">
    <b>Ситуация:</b> 'Прости, я не успеваю, давай в другой раз'.<br>
    <b>Ошибка:</b> 'Ну блин, жалко. Когда сможешь?' (Потеря фрейма).<br>
    <b>Верный ход:</b> 'Ок. У меня были дела, которые я отложил ради этого, так что в другой раз планируй заранее. На связи'.
    </div>
    """, unsafe_allow_html=True)

with st.expander("Кейс #2: Она проверяет твой доход/статус"):
    st.markdown("""
    <div class="case-card">
    <b>Ситуация:</b> 'А на какой машине ты приедешь?'<br>
    <b>Верный ход:</b> 'На той, которая довезет меня до цели. Тебе важен комфорт или компания?' (Перехват фрейма).
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. НОВЫЙ БЛОК: Мысли дня (Цитаты)
st.header("💡 Мудрость Снайпера")
quotes = [
    "«Если ты не ведешь — ведут тебя. В отношениях нет нейтральной полосы». — Август",
    "«Твоя сила не в том, что ты можешь получить, а в том, от чего ты готов отказаться».",
    "«Границы — это не забор, это фильтр, который отсеивает тех, кто тебя не ценит».",
    "«Влечение не выбирают головой, его чувствуют кожей через твою уверенность».",
    "«Никогда не объясняй свои правила. Либо их принимают, либо дверь там»."
]
st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)

# 5. ПАМЯТКИ (Теперь более наполненные)
st.header("📚 База знаний")
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.subheader("📍 О границах")
        st.write("Если ты прощаешь неуважение, ты даешь ей карт-бланш на его повторение. Либо ты пресекаешь это сразу, либо теряешь ценность.")

with col2:
    with st.container():
        st.subheader("🔥 О лидерстве")
        st.write("Женщина хочет чувствовать твою волю. Когда ты просишь разрешения, ты кажешься слабым. Когда ты предлагаешь путь — ты лидер.")

st.markdown("---")
st.caption("Social Sniper AI © 2026. Используй знания с умом.")
