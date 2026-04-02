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

st.markdown("""
    <style>
    /* Делаем фон приложения более темным и текстурированным */
    .stApp { 
        background-color: #0a0c10;
        background-image: radial-gradient(#1a1d24 1px, transparent 1px);
        background-size: 20px 20px;
        color: #ffffff; 
    }
    
    /* Стилизация заголовка с "огоньком" */
    .stHeader h1 {
        text-shadow: 0 0 10px #ff4b4b, 0 0 20px #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# МОДУЛЬ 2: САЙДБАР
# ==========================================
with st.sidebar:
    st.title("🧬 Social AI")
    
    # ПЕРЕКЛЮЧАТЕЛЬ ДЛЯ ТЕСТОВ (Оставляем тебе)
    status_mode = st.radio("Режим:", ["Базовый", "Premium ⭐"])
    st.session_state.pro_status = True if status_mode == "Premium ⭐" else False

    st.divider()
    
    if not st.session_state.pro_status:
        st.markdown("### 💎 Активировать Premium")
        
        # Визуальный ХУК (Безопасный арт)
        # Мы используем стилизованный нейросетевой арт. Это безопасно и стильно.
        # Можешь заменить эту ссылку на свою (созданную в Midjourney/Kandinsky)
        st.image("https://raw.githubusercontent.com/Anvil-Developer/public-assets/main/social-ai-hook.jpg", 
                 caption="Твой проводник в мире фрейма", use_container_width=True)
        
        st.markdown("""
        1. **🔥 Проектировщик Входа**
        2. **💎 Корректор Ценности**
        """)
        
        st.divider()
        st.write("📸 **Оплата по QR (СБП):**")
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", width=150)
        st.caption("Сканируй QR, плати 200₽ и присылай скрин.")
        st.markdown("[Скинуть скрин в ТГ](https://t.me/твой_ник)")
    else:
        st.success("⭐ Доступ Архитектора активен")
        # Здесь можно добавить другой арт, более сдержанный
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
