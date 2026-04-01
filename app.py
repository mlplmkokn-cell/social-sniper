import streamlit as st
from openai import OpenAI
import random

# 1. Настройка страницы (Mobile-First)
st.set_page_config(page_title="Social Sniper AI", page_icon="🎯", layout="centered")

# 2. Улучшенный, "нагруженный" дизайн (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .main-icon { text-align: center; font-size: 3rem; margin-bottom: 0px; }
    .ad-banner { background: linear-gradient(90deg, #1e1e1e, #2d2d2d); padding: 15px; border-radius: 10px; border: 1px dashed #ff4b4b; text-align: center; margin-bottom: 25px; }
    .hook-chat { background-color: #1a1a1a; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #30363d; }
    .case-card { background-color: #1f2937; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #30363d; }
    .ai-bubble { background-color: #161b22; padding: 15px; border-radius: 10px; border-left: 4px solid #ff4b4b; margin: 10px 0; }
    .premium-offer { background: linear-gradient(135deg, #1e1e1e, #2d2d2d); border: 2px solid #ff4b4b; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
    .premium-lock { text-align: center; color: #ced4da; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Инициализация ИИ
try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except:
    st.error("Ошибка API-ключа.")

# --- МОБИЛЬНЫЙ САЙДБАР ---
with st.sidebar:
    st.header("🎯 Меню")
    status = st.radio("Твой режим:", ["Free (Антрополог)", "Premium ⭐ (Снайпер)"])
    st.divider()
    
    # ВОЗВРАЩЕННЫЙ БЛОК ОПЛАТЫ И РЕКЛАМЫ
    if status == "Free (Антрополог)":
        st.markdown("""
        <div class='premium-offer'>
        💰 <b>PREMIUM: 200₽/мес</b><br>
        • Интерактивная докрутка сообщений<br>
        • Снайперские ответы за тебя<br>
        • Безлимитный разбор переписок<br>
        <br>
        <a href='#' style='color:#ff4b4b;'>Активировать за 200₽</a>
        </div>
        """, unsafe_allow_html=True)
    st.divider()
    st.info("📢 Реклама: Ваш лучший Telegram-канал по психологии и оружию — [Подписаться бесплатно!](https://t.me/твой_канал)")
    st.markdown("[Связаться с админом Снайпера](https://t.me/твой_ник)")

# --- ГЛАВНАЯ ИКОНКА ---
st.markdown("<div class='main-icon'>🎯</div>", unsafe_allow_html=True)
st.title("Social Sniper AI")
st.caption("Антропология, Фрейм и Биологические Триггеры (Версия 4.0)")

# --- РЕКЛАМНЫЙ БАННЕР СВЕРХУ ---
st.markdown("""
<div class="ad-banner">
    🚀 <b>АКЦИЯ:</b> Подписка на закрытый чат по докрутке общения — бесплатно для Premium пользователей!
</div>
""", unsafe_allow_html=True)

# --- 1. ПРИМЕР СЛИВА (МОМЕНТАЛЬНЫЙ ХУК) ---
st.header("📉 Как делать НЕЛЬЗЯ (Анатомия слива)")
st.markdown("""
<div class='hook-chat'>
<b>Переписка (Фрагмент):</b><br>
— Он: Привет, как дела? Скучаю...<br>
— Она: Ясно. Много дел.<br>
— Он: Ну пожалуйста, я правда очень соскучился, на часик всего🥺<br><br>
<b>Почему это слив? (Вердикт А2):</b><br>
1. <b>Нуждаемость:</b> Ты умоляешь её о внимании. Нужда отталкивает влечение биологически.<br>
2. <b>Потеря лидерства:</b> Ты просишь разрешения, а не предлагаешь путь. Ты ведомый.<br>
3. <b>Нарушение дистанции:</b> Ты не заметил её холод и продолжаешь давить, показывая, что её реакция важнее твоего самоуважения.<br>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- 2. КОНВЕЙЕР АНАЛИЗА: ВХОДНЫЕ ДАННЫЕ ---
st.header("🔍 Глубокий разбор Твоей переписки")
with st.container():
    col_chat, col_goal = st.columns([2, 1])
    with col_chat:
        full_chat = st.text_area("1. Вставь сюда всю переписку целиком:", height=180, placeholder="Скопируй текст из мессенджера...")
    with col_goal:
        user_goal = st.text_input("2. Твоя цель/вопрос:", placeholder="Например: 'Вытянуть в боулинг', 'Она игнорит что делать?'")

if st.button("🚀 Проанализировать психологические триггеры"):
    if full_chat:
        with st.spinner("Снайпер изучает биологические паттерны..."):
            prompt = f"Проанализируй эту переписку целиком: '{full_chat}'. Используй антропологию, фрейм и границы. Укажи на конкретные моменты потери фрейма, нарушения границ. Оцени позицию пользователя (лидер/ведомый). Объясни *почему* это плохо в стиле 'А2' (глубоко, без воды). Не пиши готовый ответ за него."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            
            st.markdown("### 📊 Глубокий вердикт ИИ (Фри) ")
            st.info(response.choices[0].message.content)
            
            # --- Рекламный блок Premium ---
            if status == "Free (Антрополог)":
                st.markdown("""
                <div class='premium-offer'>
                🔒 <b>Хочешь получить 3 'снайперских' фразы для продолжения диалога?</b><br>
                Активируй PREMIUM (200₽) — ИИ проанализирует твою цель и напишет точный ответ за тебя.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("🎯 **Снайперский ответ для этой ситуации (Премиум):**")
                st.write("«Твой черновик я докручу ниже, но сейчас лучше всего ответить так: 'Вижу, ты сегодня в режиме загадки. Оставлю тебя с ней, напиши, когда появится конкретика'.»")
    else:
        st.warning("Введи переписку!")

st.divider()

# --- 3. PREMIUM БЛОК: ИНТЕРАКТИВНАЯ ДОКРУТКА (КЛЮЧЕВАЯ ФИЧА) ---
st.header("🏹 Интерактивный Чат по докрутке диалога (Premium ⭐)")
if status == "Premium (Снайпер)":
    st.write("Напиши свой черновик ответа, ИИ его разберет и поможет докрутить его до идеала.")
    user_draft = st.text_area("Твой черновик ответа:", placeholder="Я хотел написать: 'Ну давай же, погнали!'...")
    
    if st.button("🔧 Докрутить сообщение"):
        if user_draft:
            with st.spinner("Анализирую черновик на суету..."):
                st.markdown("<div class='ai-bubble'><b>Разбор черновика:</b> 'Фраза 'Ну давай же' показывает излишнюю суету и оправдание. Мы уберем эту нуждаемость, сохранив смысл'.</div>", unsafe_allow_html=True)
                st.markdown("<div class='ai-bubble'><b>Снайперский вариант:</b> 'Ок. У меня были дела, которые я отложил ради этого, так что в другой раз планируй заранее. На связи'.</div>", unsafe_allow_html=True)
                st.write("Можешь внести коррективы и докрутить этот вариант, снова нажав кнопку.")
        else:
            st.warning("Введи черновик.")
else:
    st.markdown("""
    <div class='premium-offer'>
    🔒 <b>Хочешь, чтобы ИИ провел снайперскую докрутку твоего сообщения?</b><br>
    Активируй PREMIUM (200₽) — Парень пишет черновик -> ИИ находит ошибки суеты -> ИИ выдает 'снайперский' вариант.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 4. КОНТЕКСТ ВСТРЕЧИ (БЕСПЛАТНЫЙ ГЛУБОКИЙ СОВЕТ) ---
st.header("🎯 Разбор Контекста Встречи")
location_goal = st.selectbox("Куда ты хочешь её позвать?", ["В кафе/кофейню", "В боулинг", "На прогулку в парк", "В бильярд"])

if st.button("Проанализировать выбор места"):
    with st.spinner("Анализирую биологические триггеры встречи..."):
        st.markdown(f"### 📊 Разбор психологии '{location_goal}'")
        if location_goal == "В боулинг":
            st.info("""
            **Вердикт Снайпера:** Это сильный выбор. Боулинг обеспечивает **высокую тактильность**. Темы диалогов будут вокруг игры, а не твоих качеств. Это создает меньше 'допроса' и больше возможностей для конкуренции и сближения. Ты можешь трогать её за руку при броске или за плечи при победе — это выглядит естественно.
            """)
        elif location_goal == "В кафе/кофейню":
            st.info("""
            **Вердикт Снайпера:** Это более формальный, 'ведомый' вариант. В кафе вы сидите друг напротив друга, что напоминает допрос. У вас меньше поводов для тактильности. Тебе придется постоянно выдумывать темы для диалога. Лучше использовать кафе как вторую точку, когда влечение уже выстроено в более активном контексте.
            """)
        elif location_goal == "На прогулку в парк":
            st.info("""
            **Вердикт Снайпера:** Хороший, безмятежный вариант, если есть хорошая погода. Дистанция общения меньше, чем в кафе. Вы сидите рядом на лавочке — это создает больше поводов для сближения.
            """)
        elif location_goal == "В бильярд":
            st.info("""
            **Вердикт Снайпера:** Хороший выбор для тактильности, но требует твоей уверенности в игре. Ты можешь 'помогать' ей прицелиться, естественно сокращая дистанцию.
            """)

st.divider()

# --- 5. ПАСХАЛКИ (ПОЛНЫЙ ВОЗВРАТ И НАПОЛНЕНИЕ) ---
st.header("📚 База знаний Снайпера")
col1, col2 = st.columns(2)

with col1:
    with st.expander("📍 О границах (Полная пасхалка)"):
        st.markdown("<div class='case-card'><b>Суть:</b> Если она нарушила твою границу, а ты это 'проглотил' — она теряет к тебе уважение, а следом и всё влечение. Мгновенно. Ты становишься для неё бесполым существом. Уважение важнее секса.</div>", unsafe_allow_html=True)
    with st.expander("Walk away theory"):
        st.markdown("<div class='case-card'><b>Суть:</b> Твой главный козырь — твоя искренняя готовность в любой момент встать и уйти навсегда. Как только она это почувствует — её фрейм рассыплется.</div>", unsafe_allow_html=True)

with col2:
    with st.expander("🔥 О её запретах (Глубокий разбор)"):
        st.markdown("<div class='case-card'><b>Суть:</b> Женщина выстраивает свои границы не для того, чтобы ты перед ними остановился, а для того, чтобы ты <b>нарушил их в угоду своих желаний</b>. Они от этого заводятся. Лидерство — это когда твое желание сильнее её социальных запретов.</div>", unsafe_allow_html=True)
    with st.expander("⏳ Принцип инвестиций"):
        st.markdown("<div class='case-card'><b>Суть:</b> Тот, кто инвестирует больше времени и слов (суета), тот проигрывает фрейм. Твои сообщения должны быть короче и суше, пока она не начнет заслуживать твоего внимания.</div>", unsafe_allow_html=True)

st.divider()
st.caption("Social Sniper AI © 2026. Твой автономный проводник в мире фрейма и доминирования.")
