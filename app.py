import streamlit as st
from openai import OpenAI
# Инициализация памяти (чтобы чат не стирался при каждом нажатии кнопки)
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pro_status' not in st.session_state:
    st.session_state.pro_status = False
if 'last_generation' not in st.session_state:
    st.session_state.last_generation = None
# ==========================================
# МОДУЛЬ 1: СТИЛЬ И КОНФИГУРАЦИЯ
# ==========================================

st.set_page_config(page_title="Social AI", page_icon="🧬", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .premium-top { background: linear-gradient(90deg, #1e1e1e, #2d2d2d); padding: 20px; border-radius: 15px; border: 1px solid #4a4a4a; text-align: center; margin-bottom: 30px; }
    .feature-tag { background: #2d2d2d; color: #00ff88; padding: 4px 10px; border-radius: 5px; font-size: 0.8rem; margin-right: 10px; border: 1px solid #00ff88; }
    .analysis-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #00ff88; margin: 15px 0; }
    .failed-case { background-color: #1a1a1a; padding: 20px; border-radius: 10px; border: 1px dotted #4a4a4a; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# МОДУЛЬ 2: САЙДБАР
# ==========================================
with st.sidebar:
    st.title("🧬 Навигация")
    
    # Поле для ввода кода (твой "ключ" к Pro)
    access_code = st.text_input("Введи код доступа (Pro):", type="password")
    if access_code == "A2_PRO_2026": # Придумай свой секретный код
        st.session_state.pro_status = True
        st.success("✅ Доступ открыт")
    else:
        st.session_state.pro_status = False

    st.divider()
    if not st.session_state.pro_status:
        st.error("💎 Доступ ограничен")
        st.write("**Как получить Pro:**")
        st.write("1. Переведи 200₽ на [ТВОЙ НОМЕР/КАРТА]")
        st.write("2. Скинь скрин в ТГ: [@ТВОЙ_НИК]")
        st.write("3. Получи вечный код доступа.")
    else:
        st.info("⭐ Режим эксперта активен")

# ==========================================
# МОДУЛЬ 3: ВЕРХНИЙ ХУК (СЛИВЫ)
# ==========================================
st.title("🧬 Social AI")
st.caption("Антропологический анализ коммуникации и проектирование фрейма")

# ВЫНОСИМ ПРЕМИУМ ВЫШЕ (Тизер для всех)
if 'status' not in st.session_state: st.session_state.status = "Free"

st.markdown("""
<div class='premium-top'>
    <h3 style='margin-bottom:10px;'>💎 PREMIUM ДОСТУП</h3>
    <div style='display: flex; justify-content: center; flex-wrap: wrap; gap: 10px;'>
        <span class='feature-tag'>✅ Идеальное первое сообщение</span>
        <span class='feature-tag'>✅ Интерактивная докрутка</span>
        <span class='feature-tag'>✅ Анализ Instagram-триггеров</span>
    </div>
    <p style='margin-top:15px; font-size: 0.9rem; color: #8b949e;'>
        Активируй доступ за 200₽, чтобы использовать алгоритмы с конверсией ответа 85%+.
    </p>
</div>
""", unsafe_allow_html=True)

st.header("🔍 Разбор скрытой потери статуса")
st.markdown("""
<div class='failed-case'>
<b>СИТУАЦИЯ:</b> Ты предлагаешь встречу в четверг. Она пишет: <i>"Ой, в четверг я точно не могу, очень много работы, прямо завал..."</i><br><br>
<b>КАК ОТВЕЧАЕТ ОБЫЧНЫЙ ПАРЕНЬ:</b> <i>"Понятно, работа — это важно! А в субботу освободишься?"</i><br><br>
<b>ПОЧЕМУ ЭТО ОШИБКА:</b> Вроде бы вежливо, но ты только что сообщил ей: "Моё время не имеет значения, я буду ждать твоего окна в графике". Ты моментально потерял ценность. Она не "завал" разгребает, она тестирует твою готовность ждать.<br>
<b>ПРАВИЛЬНЫЙ ВЕКТОР:</b> <i>"Ок, тогда работай. Как освободишься — маякни, если буду свободен, что-нибудь придумаем."</i> (Ты закрыл диалог на своих условиях, сохранив статус).
</div>
""", unsafe_allow_html=True)

# ==========================================
# МОДУЛЬ 4: АНАЛИЗАТОР ПОДТЕКСТА
# ==========================================
st.header("1. Разбор подтекста и логика ответа")
chat_data = st.text_area("Вставь диалог:", height=150, key="main_chat_input")

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
# МОДУЛЬ 5: ТАКТИЧЕСКИЙ ЧАТ
# ==========================================
st.header("2. Тактический Чат: Навигация цели")
col_a, col_b = st.columns(2)
with col_a:
    target = st.text_input("Твоя цель:", placeholder="Например: Кафе -> Дом", key="target_input")
with col_b:
    context = st.text_input("Контекст сейчас:", placeholder="Например: Мы в боулинге", key="context_input")

tactical_msg = st.text_area("Что она говорит или делает сейчас?", key="tactical_msg_input")

if st.button("🏹 Построить маршрут"):
    if tactical_msg:
        with st.spinner("Просчитываю траекторию..."):
            prompt = f"Цель: {target}. Контекст: {context}. Текущая ситуация: {tactical_msg}. Дай тактический совет по сближению и перемещению. Стиль А2."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            st.success(response.choices[0].message.content)
            st.markdown("<div class='logic-hint'>Подсказка: Твоя задача — вести. Любое перемещение — это твое решение.</div>", unsafe_allow_html=True)

st.divider()

# ==========================================
# МОДУЛЬ 6: БАЗА ПАСХАЛОК
# ==========================================
# ==========================================
# SLOT 6: PREMIUM — ИНТЕРФЕЙС ДОКРУТКИ
# ==========================================
if st.session_state.pro_status:
    st.header("🏹 Проектирование входа & Тюнинг")
    
    # Вкладки для удобства
    tab1, tab2 = st.tabs(["Первое сообщение", "Докрутка твоего варианта"])
    
    with tab1:
        triggers = st.text_area("Анализ профиля (Instagram триггеры):", 
                               placeholder="Напиши факты: что на фото, что в описании, какие хобби...")
        if st.button("✨ Сгенерировать базу"):
            prompt = f"На основе триггеров '{triggers}' создай 3 глубоких зацепки в стиле А2. Без суеты."
            response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
            st.session_state.last_generation = response.choices[0].message.content

        if st.session_state.last_generation:
            st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
            st.write(st.session_state.last_generation)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # ИНТЕРАКТИВ
            feedback = st.text_input("Что изменить? (например: 'сделай жестче' или 'добавь больше иронии'):")
            if st.button("🔄 Докрутить"):
                refine_prompt = f"Контекст: {st.session_state.last_generation}. Твоя задача изменить это под запрос: {feedback}. Сохрани глубину А2."
                res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": refine_prompt}])
                st.session_state.last_generation = res.choices[0].message.content
                st.rerun()

    with tab2:
        st.subheader("🔧 Интерактивный тюнинг (Дорогой ответ)")
        user_draft = st.text_area("Вставь свой вариант ответа:", placeholder="Напиши, как бы ты ответил сам...")
        if st.button("💎 Сделать дороже"):
            tuning_prompt = f"Исправь ошибки суеты и низкой ценности в этом сообщении: '{user_draft}'. Сделай его статусным, кратким и в стиле А2."
            res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": tuning_prompt}])
            st.success(res.choices[0].message.content)
            st.info("Подсказка: Мы убрали лишние оправдания и добавили фокус на твои границы.")

else:
    st.markdown("""
    <div style='background: #1a1a1a; padding: 30px; border-radius: 15px; border: 1px dashed #4a4a4a; text-align: center;'>
        <h4>🧬 Модуль проектирования закрыт</h4>
        <p>Для доступа к интерактивной докрутке сообщений и анализу Instagram-триггеров введи код в боковом меню.</p>
    </div>
    """, unsafe_allow_html=True)
