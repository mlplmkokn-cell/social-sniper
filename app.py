import streamlit as st
from openai import OpenAI

# ==========================================
# МОДУЛЬ 1: СТИЛЬ И КОНФИГУРАЦИЯ
# ==========================================
st.set_page_config(page_title="Social Sniper AI", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .ad-banner { background: #1e1e1e; padding: 15px; border-radius: 10px; border-bottom: 3px solid #ff4b4b; text-align: center; margin-bottom: 20px; }
    .analysis-box { background-color: #161b22; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; margin: 15px 0; }
    .failed-case { background-color: #2d1b1b; padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; margin-bottom: 25px; }
    .logic-hint { color: #8b949e; font-size: 0.9rem; border-top: 1px solid #30363d; padding-top: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

try:
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=st.secrets["OPENROUTER_API_KEY"])
except Exception:
    st.error("Настрой API-ключ в Secrets!")

# ==========================================
# МОДУЛЬ 2: САЙДБАР
# ==========================================
with st.sidebar:
    st.title("🧬 Навигация")
    status = st.radio("Твой статус:", ["Free (Антрополог)", "Premium ⭐ (Доступ открыт)"])
    st.divider()
    
    st.markdown("""
    **Что входит в Premium:**
    * **🎯 Идеальный ответ:** Получаешь готовую фразу, которая выравнивает твой статус в любой ситуации.
    * **🏹 Идеальное начало:** Генерация первой фразы на основе интересов (Instagram, хобби) с максимальным процентом отклика.
    * **🔧 Интерактивный тюнинг:** Чат, где ты пишешь свой вариант, а ИИ исправляет ошибки суеты и делает его "дороже".
    """)
    st.divider()
    st.info("📢 [Закрытый TG-канал](https://t.me/твой_канал)")

# ==========================================
# МОДУЛЬ 3: ВЕРХНИЙ ХУК (СЛИВЫ)
# ==========================================
st.markdown("<div class='ad-banner'>🚀 <b>КЕЙС ДНЯ:</b> Как не слить встречу за 30 минут до начала</div>", unsafe_allow_html=True)

st.header("📉 Анатомия слива (Разбор)")
st.markdown("""
<div class='failed-case'>
<b>Ситуация:</b> Она меняет место встречи в последний момент.<br>
<b>Слив:</b> "Ну ладно, давай там, мне без разницы".<br>
<b>Почему это плохо:</b> Ты показал, что твой комфорт вторичен. Ты стал ведомым.<br>
<b>Как надо:</b> "Мне там неудобно. Жду тебя на месте".
</div>
""", unsafe_allow_html=True)

st.divider()

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
# SLOT 6: FIRST STRIKE (Premium Модуль)
# ==========================================
if status == "Premium ⭐ (Доступ открыт)":
    st.header("🏹 First Strike: Проектирование входа")
    st.write("Проанализируй её профиль (Instagram, описание, фото) и впиши сюда ключевые зацепки.")
    
    triggers = st.text_area("Зацепки из профиля (например: фото с собакой, любит винил, часто бывает в горах):", 
                           placeholder="Что она любит? О чем ее контент?", key="tg_input")
    
    if st.button("✨ Сгенерировать идеальные зацепки"):
        if triggers:
            with st.spinner("Анализирую социальные триггеры..."):
                prompt = f"""
                На основе триггеров: '{triggers}' создай 3 варианта первого сообщения.
                ТРЕБОВАНИЯ:
                - Стиль А2 (глубоко, без банальностей).
                - Исключить комплименты внешности.
                - Использовать легкую провокацию или общие ценности.
                - Цель: Вызвать любопытство и желание ответить.
                - Никакой суеты и 'Привет, как дела'.
                """
                response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
                st.session_state.strike_results = response.choices[0].message.content
        else:
            st.warning("Введи хотя бы один триггер.")

    if 'strike_results' in st.session_state:
        st.markdown("<div class='analysis-box'>", unsafe_allow_html=True)
        st.write(st.session_state.strike_results)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Блок интерактивного изменения
        st.subheader("🔧 Докрутка под твой стиль")
        adjust = st.text_input("Как изменить? (например: 'сделай короче' или 'добавь больше дерзости'):")
        if st.button("🔄 Обновить варианты"):
            with st.spinner("Пересчитываю контекст..."):
                prompt = f"Переделай эти варианты: {st.session_state.strike_results}, учитывая пожелание: {adjust}. Сохрани стиль А2."
                response = client.chat.completions.create(model="openai/gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
                st.session_state.strike_results = response.choices[0].message.content
                st.rerun()

else:
    st.markdown("""
    <div style='border: 1px solid #4a4a4a; padding: 20px; border-radius: 10px; text-align: center;'>
        <p>🔒 <b>Генератор идеальных сообщений заблокирован.</b></p>
        <p style='font-size: 0.8rem; color: #8b949e;'>
           Хочешь перестать гадать, что написать? Premium дает доступ к алгоритму, 
           который находит слабые места в защите и генерирует зацепки по Instagram-профилю.
        </p>
    </div>
    """, unsafe_allow_html=True)
