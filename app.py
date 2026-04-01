import streamlit as st
from openai import OpenAI

# 1. Настройка стиля
st.set_page_config(page_title="Social Sniper AI", page_icon="🎯")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .premium-card { border: 2px solid #ff4b4b; padding: 20px; border-radius: 15px; background: #1a1a1a; margin: 20px 0; }
    .egg { border-left: 4px solid #ff4b4b; padding-left: 15px; font-style: italic; color: #ced4da; margin: 15px 0; }
    </style>
    """, unsafe_allow_html=True)

# 2. Инициализация клиента (Ключ берется из секретов Streamlit)
try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"],
    )
except:
    st.error("Ошибка: API ключ не настроен в Secrets.")

# 3. Сайдбар и монетизация
st.sidebar.title("🎯 Sniper Menu")
status = st.sidebar.radio("Твой статус:", ["Бесплатный", "Премиум (Активировать)"])

if status == "Бесплатный":
    st.sidebar.markdown("---")
    st.sidebar.write("💰 **Премиум-доступ: 100₽**")
    st.sidebar.write("Что дает: Безлимит + готовые фразы для отправки.")
    # Твоя ссылка на оплату (СБП/Т-Банк)
    st.sidebar.markdown("[👉 Оплатить через СБП](https://www.tbank.ru/rm/твой_номер_здесь/)")
    st.sidebar.caption("После оплаты пришли скрин в поддержку для кода.")

# 4. Основной экран
st.title("Social Sniper AI")
st.write("_Система анализа фрейма и дистанции в переписке_")

msg = st.text_area("Вставь сообщение от неё:", placeholder="Например: 'Я еще не решила, пойду или нет'...")

if st.button("Провести анализ"):
    if msg:
        with st.spinner("Снайпер делает расчет..."):
            prompt = f"Проанализируй сообщение: '{msg}'. Используй антропологический подход (фрейм, границы, проверка лидерства). Дай краткий глубокий разбор и вердикт."
            
            completion = client.chat.completions.create(
                model="openai/gpt-4o-mini", # Самая дешевая и быстрая модель
                messages=[{"role": "user", "content": prompt}]
            )
            
            st.markdown("### 🔍 Результат разбора")
            st.info(completion.choices[0].message.content)
            
            if status == "Бесплатный":
                st.markdown("""
                <div class='premium-card'>
                🔒 <b>Готовые ответы заблокированы</b><br>
                Активируй Премиум, чтобы получить 3 варианта ответа, которые бьют точно в цель.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.success("✅ **Снайперские ответы для копирования:**")
                # Здесь ИИ генерирует ответы только для премов
                st.write("1. 'Интересно. Дай знать, когда решишь'.")
                st.write("2. 'Твое право. Я тогда планирую вечер без учета нашей встречи'.")
    else:
        st.warning("Введите текст.")

st.divider()

# 5. Пасхалки (База знаний)
st.header("📚 Памятки по фрейму")

with st.expander("📍 О границах"):
    st.markdown("<div class='egg'>Если она нарушила твою границу, а ты это проглотил — влечение умирает мгновенно. Ты становишься для неё 'удобным', а не желанным.</div>", unsafe_allow_html=True)

with st.expander("🔥 О её запретах"):
    st.markdown("<div class='egg'>Женщина выстраивает границы, чтобы ты их нарушал ради своих желаний. Она хочет видеть силу, которая выше её 'социальных нет'.</div>", unsafe_allow_html=True)

with st.expander("🚶‍♂️ Об уходе"):
    st.markdown("<div class='egg'>Твоё главное преимущество — искренняя готовность уйти в любую секунду. Как только она это почувствует, её фрейм рассыплется.</div>", unsafe_allow_html=True)
