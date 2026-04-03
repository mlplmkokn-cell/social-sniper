import streamlit as st
from openai import OpenAI
# Инициализация памяти (чтобы чат не стирался при каждом нажатии кнопки)
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pro_status' not in st.session_state:
    st.session_state.pro_status = False
if 'last_generation' not in st.session_state:
    st.session_state.last_generation = None
    import streamlit as st
import google.generativeai as genai
from openai import OpenAI
import datetime

# ==========================================
# SLOT 1: КОНФИГУРАЦИЯ И ТРОЙНАЯ ЗАЩИТА АРХИТЕКТУРЫ
# ==========================================
import streamlit as st
# ... остальные импорты ...

# Берем ключи из безопасного хранилища Streamlit
GROK_KEY = st.secrets["GROK_KEY"]
GEMINI_KEY_1 = st.secrets["GEMINI_KEY_1"]
GEMINI_KEY_2 = st.secrets["GEMINI_KEY_2"]
MY_TG = "@Manipulator393"

# Системный промпт (Фундамент)
A2_PHILOSOPHY = """
Ты — эксперт по социальной архитектуре. Твой стиль — 'А2'.
ПРАВИЛА: 
1. Никакой нужды (низкая нуждаемость). 
2. Высокий статус и ценность. 
3. Текст глубокий, понятный, без лишнего упрощения, доступный, без специфических терминов.
4. Исключить банальщину и оправдания. 
5. Всегда пиши полный текст.
"""

def generate_response(prompt):
    """Каскадная система: Grok -> Gemini 1 -> Gemini 2"""
    full_prompt = f"{A2_PHILOSOPHY}\n\nЗАДАЧА: {prompt}"
    
    # Попытка 1: Grok
    try:
        grok_client = OpenAI(api_key=GROK_KEY, base_url="https://api.x.ai/v1")
        res = grok_client.chat.completions.create(model="grok-beta", messages=[{"role": "user", "content": full_prompt}])
        return res.choices[0].message.content
    except Exception:
        # Попытка 2: Gemini (Ключ 1)
        try:
            genai.configure(api_key=GEMINI_KEY_1)
            model = genai.GenerativeModel('gemini-1.5-flash')
            return model.generate_content(full_prompt).text
        except Exception:
            # Попытка 3: Gemini (Ключ 2)
            try:
                genai.configure(api_key=GEMINI_KEY_2)
                model2 = genai.GenerativeModel('gemini-1.5-flash')
                return model2.generate_content(full_prompt).text
            except Exception:
                return "⚠️ Все нейросети ушли в защиту. Нужно пролистать до бага и обновить систему."

st.set_page_config(page_title="Social AI", page_icon="🧬")

# База уникальных кодов
VALID_CODES = {
    "A2_TEST_MONTH": "2026-05-15",
    "A2_YEAR_PRO": "2027-04-01",
    "A2_FOREVER": "forever"
}

if 'pro_status' not in st.session_state: st.session_state.pro_status = False
if 'last_res' not in st.session_state: st.session_state.last_res = ""

# ==========================================
# SLOT 2: САЙДБАР И АВТОРИЗАЦИЯ
# ==========================================
with st.sidebar:
    st.title("🧬 Social AI")
    user_key = st.text_input("Код доступа:", type="password")
    
    if user_key in VALID_CODES:
        expiry = VALID_CODES[user_key]
        if expiry == "forever" or datetime.datetime.strptime(expiry, "%Y-%m-%d") > datetime.datetime.now():
            st.session_state.pro_status = True
            st.success("✅ Premium активирован")
        else:
            st.error("❌ Код истек")
            st.session_state.pro_status = False
    
    st.divider()
    if not st.session_state.pro_status:
        st.markdown("### 💎 Тарифы")
        st.markdown("""
        1. **Месяц:** 299₽
        2. **Год:** 1599₽
        3. **Навсегда:** 5000₽
        """)
        st.write("📸 **Оплата по QR (СБП):**")
        # Вставь реальную ссылку на свой QR-код вместо заглушки
        st.markdown("[🔗 Открыть QR-код для оплаты](#)")
        st.caption(f"После оплаты отправь чек в Telegram {MY_TG}, чтобы получить свой код.")
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
# SLOT 6: PREMIUM — ИНСТРУМЕНТАРИЙ
# ==========================================
if st.session_state.pro_status:
    st.header("🛠 Инструменты Архитектора")
    
    tab_strike, tab_tune = st.tabs(["🚀 Проектировщик Входа", "💎 Фильтр Статуса"])
    
    with tab_strike:
        st.subheader("Шаг 1: Сканирование триггеров")
        st.info("Впиши сюда факты: что она постит, что пишет о себе, какие у неё хобби. Чем больше деталей, тем точнее 'крючок'.")
        
        triggers = st.text_area("Факты о ней из Instagram/Bio:", 
                               placeholder="Например: она часто ходит на выставки, в профиле много фото с черным котом, любит техно 90-х...", 
                               key="trig_area")
        
        if st.button("🔍 Сгенерировать варианты входа"):
            if triggers:
                with st.spinner("Анализирую социальный профиль..."):
                    prompt = f"На основе фактов '{triggers}' создай 3 варианта первого сообщения. Стиль А2. Без подстройки и дешевых комплиментов."
                    res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
                    st.session_state.last_generation = res.choices[0].message.content
            else:
                st.warning("Сначала введи хотя бы один факт о ней.")

    with tab_tune:
        st.subheader("Очистка сообщения от 'суеты'")
        st.info("Вставь свой вариант ответа, и я сделаю его статусным, убрав всё лишнее.")
        user_draft = st.text_area("Твой черновик сообщения:", placeholder="Напиши сюда то, что ты хотел ей отправить...", key="draft_area")
        
        if st.button("💎 Повысить ценность"):
            if user_draft:
                with st.spinner("Удаляю признаки слабости..."):
                    tuning_prompt = f"Перепиши сообщение в стиле А2, убрав нуждаемость и оправдания: '{user_draft}'. Сделай его лаконичным."
                    res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": tuning_prompt}])
                    st.session_state.last_generation = res.choices[0].message.content
            else:
                st.warning("Вставь текст для анализа.")

    # ==========================================
    # ИНТУИТИВНЫЙ ШАГ 2: ВЫВОД И ДОКРУТКА
    # ==========================================
    if st.session_state.last_generation:
        st.divider()
        st.subheader("Шаг 2: Результат и финальная доводка")
        
        st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
        st.write(st.session_state.last_generation)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Отдельное окно для правок — теперь интуитивно понятно
        st.write("🗣 **AI-Напарник:** Если варианты кажутся слишком дерзкими или, наоборот, мягкими — напиши об этом ниже.")
        feedback = st.text_input("Что именно изменить в этих вариантах?", 
                                placeholder="Пример: 'сделай чуть короче', 'добавь больше юмора', 'убери провокацию'...")
        
        if st.button("🔄 Обновить варианты под меня"):
            with st.spinner("Пересчитываю контекст..."):
                refine_prompt = f"Твой прошлый вариант: {st.session_state.last_generation}. Измени его с учетом этого пожелания: {feedback}. Сохрани глубину А2."
                res = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": refine_prompt}])
                st.session_state.last_generation = res.choices[0].message.content
                st.rerun()

else:
    # Тизер для Free
    st.markdown("""
    <div style='background: #1a1a1a; padding: 30px; border-radius: 15px; border: 1px dashed #4a4a4a; text-align: center;'>
        <h4>🧬 Доступ к инструментам проектирования закрыт</h4>
        <p style='color: #8b949e;'>Функции 'Проектировщик' и 'Фильтр Статуса' доступны только в Premium-режиме.</p>
    </div>
    """, unsafe_allow_html=True)
    # ==========================================
# SLOT 7: FAQ & ИНСТРУКЦИЯ (БАЗА ЗНАНИЙ)
# ==========================================
st.divider()
st.header("📖 Инструкция и FAQ")

with st.expander("❓ Как пользоваться 'Проектировщиком входа'?"):
    st.write("""
    1. Зайди в профиль девушки (Instagram/VK/Tinder).
    2. Найди 2-3 детали: необычное хобби, локация на фото, порода собаки, музыка в сторис.
    3. Впиши их в поле 'Факты о ней'. 
    4. Получи 3 варианта. Если они кажутся слишком наглыми — используй поле 'AI-Напарник' и напиши: *'сделай более дружелюбно'*.
    """)

with st.expander("❓ Что такое 'Фильтр Статуса'?"):
    st.write("""
    Эта функция для тех, кто уже придумал ответ, но боится показаться 'удобным'. 
    Вставь свой текст, и ИИ удалит из него:
    * Лишние смайлики (признак суеты).
    * Оправдания (почему ты долго не отвечал или почему предлагаешь это место).
    * Вопросы-просьбы.
    На выходе ты получишь лаконичный, мужской текст.
    """)

with st.expander("❓ Я оплатил, что дальше?"):
    st.write("""
    После оплаты по QR-коду обязательно сделай скриншот чека. 
    Отправь его в поддержку (ссылка в боковом меню). 
    В ответ ты получишь секретный код доступа, который нужно ввести один раз в поле 'Режим доступа'.
    """)

with st.expander("❓ Почему ваши сообщения работают?"):
    st.write("""
    Мы используем алгоритм **А2 (Антропологический анализ)**. 
    В отличие от обычных советов, мы не учим 'пикап-фразам'. 
    Мы учим выстраивать коммуникацию так, чтобы твоя ценность в глазах женщины росла с каждым сообщением.
    """)
