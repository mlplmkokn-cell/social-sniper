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
    
    # ПЕРЕКЛЮЧАТЕЛЬ ДЛЯ ТЕСТОВ (оставляем для тебя)
    status_mode = st.radio("Режим доступа:", ["Базовый (Наблюдатель)", "Premium (Архитектор)"])
    st.session_state.pro_status = True if status_mode == "Premium (Архитектор)" else False

    st.divider()
    
    if not st.session_state.pro_status:
        st.markdown("### 💎 Активировать Premium")
        
        # Список "триггеров" для покупки
        st.markdown("""
        1. **🔥 Проектировщик Входа** — *Ищу зацепки в её Instagram и создаю первое сообщение, на которое невозможно не ответить.*
        2. **💎 Корректор Ценности** — *Присылаешь свой вариант, а я убираю из него 'нуждаемость' и слабость. Делаю текст статусным.*
        3. **🤖 AI-Напарник** — *Не просто фраза, а живой диалог. Докручиваем сообщение вместе, пока оно не станет идеальным.*
        """)
        
        st.markdown("---")
        st.write("💰 **Цена: 200₽ (Навсегда)**")
        st.write("📸 **Оплата по QR (СБП):**")
        
        # Инструкция и заглушка под QR
        st.info("Сканируй QR-код в приложении банка и присылай скрин в ТГ.")
        # Чтобы вывести реальный QR, просто замени ссылку ниже на ссылку на фото своего QR-кода
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", caption="Отсканируй для оплаты")
        
        st.markdown("[Написать в поддержку / Скинуть скрин](https://t.me/твой_ник)")
    else:
        st.success("⭐ Доступ Архитектора активен")

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

if st.session_state.pro_status:
    st.header("🛠 Инструментарий Premium")
    
    # Переключение между функциями через понятные вкладки
    tab_strike, tab_tune = st.tabs(["🚀 Проектировщик Входа", "💎 Корректор Ценности"])
    
    with tab_strike:
        st.subheader("Сканер Личности (Instagram / Bio)")
        st.write("Впиши любые факты о ней, и я найду 'крючок' для общения.")
        triggers = st.text_area("Факты о ней:", placeholder="Например: любит тату, фото из Парижа, в сторис всегда кофе...", key="trig_area")
        
        if st.button("🔍 Найти идеальную зацепку"):
            if triggers:
                with st.spinner("Анализирую социальный профиль..."):
                    prompt = f"На основе фактов '{triggers}' создай 3 варианта сообщения в стиле А2. Задача: зацепить внимание без подстройки и комплиментов."
                    res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
                    st.session_state.last_generation = res.choices[0].message.content
            else:
                st.warning("Сначала введи факты.")

    with tab_tune:
        st.subheader("Фильтр Статуса")
        st.write("Вставь сообщение, которое хочешь отправить. Я уберу из него всё, что выдает в тебе 'слабого' игрока.")
        user_draft = st.text_area("Твой черновик:", placeholder="Напиши, что ты хотел ей отправить...", key="draft_area")
        
        if st.button("💎 Сделать сообщение 'дороже'"):
            if user_draft:
                with st.spinner("Удаляю суету и оправдания..."):
                    tuning_prompt = f"Перепиши это сообщение в стиле А2, убрав нуждаемость и лишние слова: '{user_draft}'. Сделай его мужским и лаконичным."
                    res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": tuning_prompt}])
                    st.session_state.last_generation = res.choices[0].message.content
            else:
                st.warning("Вставь свой текст.")

    # ОБЩИЙ БЛОК ВЫВОДА И ИНТЕРАКТИВНОЙ ДОКРУТКИ
    if st.session_state.last_generation:
        st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
        st.markdown("**Рекомендация Social AI:**")
        st.write(st.session_state.last_generation)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ИНТЕРАКТИВНЫЙ ТЮНИНГ
        st.write("---")
        st.write("🗣 **AI-Напарник:** Не нравится результат? Давай подправим.")
        feedback = st.text_input("Что изменить? (например: 'сделай жестче', 'добавь юмора', 'слишком длинно')")
        
        if st.button("🔄 Переделать по моему запросу"):
            with st.spinner("Пересчитываю траекторию..."):
                refine_prompt = f"Твой прошлый вариант: {st.session_state.last_generation}. Измени его с учетом этого пожелания: {feedback}. Стиль А2."
                res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": refine_prompt}])
                st.session_state.last_generation = res.choices[0].message.content
                st.rerun()
else:
    # Блок-заглушка (Тизер)
    st.markdown("""
    <div style='background: #1a1a1a; padding: 30px; border-radius: 15px; border: 1px dashed #4a4a4a; text-align: center;'>
        <h4>🧬 Доступ к проектированию закрыт</h4>
        <p style='color: #8b949e;'>Функции 'Сканер Личности' и 'Фильтр Статуса' доступны только в Premium-режиме.</p>
    </div>
    """, unsafe_allow_html=True)
