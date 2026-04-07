# ==========================================
# БЛОК 1: ДВИГАТЕЛЬ И БЕЗОПАСНОСТЬ (V4-MONOLITH)
# ==========================================
import streamlit as st
import requests

st.title("А2: Диагностика систем")

# Проверка ключей
key = st.secrets.get("GEMINI_KEY_1", "КЛЮЧ НЕ НАЙДЕН")
st.write(f"Ваш ключ (первые 5 знаков): {key[:5]}...")

if st.button("Сделать тестовый выстрел"):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    data = {"contents": [{"parts": [{"text": "Привет, ты работаешь?"}]}]}
    
    try:
        res = requests.post(url, json=data)
        st.write(f"Ответ сервера (Код): {res.status_code}")
        if res.status_code == 200:
            st.success("ПОБЕДА! Связь есть. Значит, проблема была в старых библиотеках.")
            st.write(res.json()['candidates'][0]['content']['parts'][0]['text'])
        else:
            st.error(f"Ошибка: {res.text}")
    except Exception as e:
        st.error(f"Связь вообще не установлена: {e}")
# ==========================================
# БЛОК 2: ВИЗУАЛЬНАЯ УПАКОВКА (CSS)
# За что отвечает: Создает темную, дорогую атмосферу сайта.
# ==========================================
st.set_page_config(page_title="Social AI", page_icon="🧬")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #e6edf3; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #161b22; border-radius: 5px; padding: 10px 20px; color: white; }
    .result-box { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# БЛОК 3: САЙДБАР, ОПЛАТА И КОДЫ ДОСТУПА
# За что отвечает: Авторизация пользователей и продажа подписок.
# ==========================================

# 1. ТВОЯ БАЗА КОДОВ (Редактируй только здесь)
# Просто добавляй новый код в кавычках через запятую в нужный список
CODS_MONTH = ["M_ALPHA_1", "M_BETA_2"]    # Коды на 1 месяц
CODS_YEAR = ["Y_ELITE_2026", "Y_PRO_777"] # Коды на 1 год
CODS_FOREVER = ["A2_BOSS", "MASTER_KEY"]  # Коды навсегда

# Инициализация состояний, если они еще не созданы
if 'pro_status' not in st.session_state: 
    st.session_state.pro_status = False
if 'status_text' not in st.session_state:
    st.session_state.status_text = "Free Version"

with st.sidebar:
    st.title("🧬 SOCIAL AI")
    st.caption("Твой архитектор социальных связей")
    
    st.divider()
    
    # СЕКЦИЯ АКТИВАЦИИ
    st.subheader("🔑 Доступ к Premium")
    
    # Одно поле ввода
    user_key = st.text_input("Введите ваш секретный код:", type="password", help="Вставь код, полученный после оплаты")
    
    # Кнопка активации (то, чего не хватало)
    if st.button("Активировать доступ", use_container_width=True):
        if user_key in CODS_MONTH:
            st.session_state.pro_status = True
            st.session_state.status_text = "Premium: Месяц активен"
            st.success("✅ Код на месяц принят!")
        elif user_key in CODS_YEAR:
            st.session_state.pro_status = True
            st.session_state.status_text = "Premium: Год активен"
            st.success("✅ Код на год принят!")
        elif user_key in CODS_FOREVER:
            st.session_state.pro_status = True
            st.session_state.status_text = "Premium: Навсегда"
            st.success("👑 Доступ навсегда открыт!")
        else:
            st.error("❌ Код не найден или истек")
    
    # Отображение текущего статуса
    if st.session_state.pro_status:
        st.info(f"Статус: {st.session_state.status_text}")
    
    st.divider()

    # СЕКЦИЯ ОПЛАТЫ (показывается только тем, у кого нет Pro)
    if not st.session_state.pro_status:
        st.markdown("### 💎 Купить Premium")
        st.write("Выбери тариф и стань архитектором своих переписок:")
        
        # Тарифы в виде таблицы или списка
        st.markdown("""
        * **1 Месяц:** 299₽
        * **1 Год:** 1599₽
        * **Навсегда:** 5000₽
        """)
        
        st.write("📸 **Оплата по QR (СБП):**")
        # Место под твой QR-код
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", width=180)
        
        st.info(f"После оплаты отправь чек в Telegram: {MY_TG}")
        st.markdown(f"[🚀 Написать в поддержку](https://t.me/{MY_TG.replace('@', '')})")
    
    # Кнопка сброса (для тестов, можешь потом убрать)
    if st.session_state.pro_status:
        if st.button("Выйти из системы (Reset)"):
            st.session_state.pro_status = False
            st.rerun()

# ==========================================
# БЛОК 4: БЕСПЛАТНЫЙ РАЗБОР (МАРКЕТИНГ)
# За что отвечает: Объясняет ценность продукта новичку.
# ==========================================

st.title("🧬 Social AI: Архитектура Доминирования")

# 1. Тот самый сценарий с четвергом
with st.expander("🚩 РАЗБОР СЛИВА: Как ты теряешь ценность за одно сообщение"):
    st.markdown("""
    <div style='background: #161b22; padding: 20px; border-left: 4px solid #f85149; border-radius: 5px;'>
    <b>Ситуация:</b> Вы договорились на встречу в четверг. В среду она пишет, что не может.<br>
    <b>❌ Ответ Оленя:</b> "Ничего страшного, напиши как освободишься..." (Слив статуса)<br>
    <b>✅ Ответ А2:</b> "Принято. Раз у тебя форс-мажор, я займу вечер другими планами. На связи." (Сохранение позиции)
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 2. РЕКЛАМНЫЙ СЛОТ
st.markdown("<div style='text-align: center; color: #444; border: 1px dashed #444; padding: 10px;'>📢 МЕСТО ПОД ТВОЮ РЕКЛАМУ</div>", unsafe_allow_html=True)
st.write("")

# 3. Бесплатный Анализатор с ЦЕЛЬЮ
st.subheader("🕵️ Аналитическая Лаборатория")
target = st.text_input("🎯 Твоя цель общения:", placeholder="Например: вытянуть на свидание, заинтриговать, перевести в горизонтальное положение...")

col_a, col_b = st.columns(2)

with col_a:
    st.info("Анализ твоего сообщения")
    u_msg = st.text_input("Вставь фразу для отправки:", placeholder="Например: Привет, как дела?")
    if st.button("Проверить харизму"):
        # ИИ анализирует соответствие цели, но НЕ дает ответ
        prompt = f"Цель пользователя: {target}. Его сообщение: {u_msg}. Проанализируй, подходит ли это под контекст общения, захочет ли она этого и дойдет ли он до своей цели? Укажи на ошибки. НЕ ДАВАЙ ГОТОВЫЙ ВАРИАНТ ОТВЕТА."
        st.session_state.last_res = generate_response(prompt)

with col_b:
    st.info("Анализ её манипуляций")
    h_msg = st.text_input("Что она написала?", placeholder="Например: У меня есть парень...")
    if st.button("Вскрыть подтекст"):
        st.session_state.last_res = generate_response(f"Проанализируй сообщение от девушки: {h_msg}. Что она имеет в виду на самом деле и как это мешает цели '{target}'? НЕ ДАВАЙ ТЕКСТ ОТВЕТА.")

if st.session_state.last_res:
    st.markdown(f"<div class='result-box'>{st.session_state.last_res}</div>", unsafe_allow_html=True)
    if not st.session_state.pro_status:
        st.warning("⚠️ Анализ готов. Идеальные формулировки для достижения цели доступны только в [PREMIUM РЕЖИМЕ].")
# ==========================================
# БЛОК 5: ОСНОВНОЙ ИНСТРУМЕНТАРИЙ (PREMIUM)
# За что отвечает: Проектировщик зацепок и Фильтр статуса.
# ==========================================

if st.session_state.pro_status:
    st.markdown("<h2 style='color: #ff4b4b;'>⭐ PREMIUM РЕЖИМ АКТИВЕН</h2>", unsafe_allow_html=True)
    
    # Поле ввода цели переносим и сюда для удобства
    p_target = st.text_input("🎯 Установи главную цель (для ИИ):", value=target if target else "", placeholder="Например: Свидание в эту субботу")

    tab1, tab2, tab3 = st.tabs(["🚀 Идеальный Вход", "🎯 Контр-удар", "🧠 Стратегия А2"])
    
    with tab1:
        st.subheader("Генератор входа под цель")
        p_facts = st.text_area("Факты о ней (профиль, фото):", placeholder="Любит винил, фото из Парижа...")
        if st.button("Спроектировать вход"):
            # ИИ генерирует вход, который ведет к цели
            st.session_state.last_res = generate_response(f"Цель: {p_target}. На основе фактов '{p_facts}' создай 3 сообщения в своем стиле , которые максимально быстро ведут к этой цели.")

    with tab2:
        st.subheader("Контр-удар (Перехват инициативы)")
        p_context = st.text_area("Контекст переписки:", placeholder="Твои и её сообщения...")
        if st.button("Сгенерировать ответ"):
            st.session_state.last_res = generate_response(f"Цель: {p_target}. Контекст: '{p_context}'. Выдай один идеальный ответ по А2. Учти её подтекст и направь общение к цели.")

    with tab3:
        st.subheader("🧠 Анализ подцелей и поведение")
        if st.button("Разработать план доминирования"):
            # ИИ разбивает цель на подцели
            prompt = f"Цель: {p_target}. Разбей эту цель на 3 тактические подцели. Как себя вести? Какие триггеры использовать? Дай подробную инструкцию по поведению в стиле А2."
            st.session_state.last_res = generate_response(prompt)

    if st.session_state.last_res:
        st.divider()
        st.markdown("<div class='result-box' style='border-color: #ff4b4b;'>", unsafe_allow_html=True)
        st.write(st.session_state.last_res)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # Баннер продажи
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1f1f1f, #3d0e0e); padding: 40px; border-radius: 20px; border: 1px solid #ff4b4b; text-align: center;'>
        <h2 style='color: white;'>ХВАТИТ ГАДАТЬ НА КОФЕЙНОЙ ГУЩЕ</h2>
        <p style='font-size: 18px;'>Ты знаешь цель, но не знаешь дорогу. <b>Premium</b> проложит маршрут.</p>
        <ul style='text-align: left; display: inline-block; color: white;'>
            <li>✅ <b>Разбивка цели на этапы</b> (от интриги до встречи)</li>
            <li>✅ <b>Готовые формулировки</b>, которые ведут к результату</li>
            <li>✅ <b>Инструкции по поведению</b> (когда молчать, когда давить)</li>
        </ul>
        <p style='font-weight: bold; color: #ff4b4b;'>Активируй доступ в боковом меню.</p>
    </div>
    """, unsafe_allow_html=True)
# ==========================================
# БЛОК 6: БАЗА ЗНАНИЙ И ЧАСТЫЕ ВОПРОСЫ (FAQ)
# За что отвечает: Обучение пользователя и снятие страхов.
# ==========================================
st.divider()
st.header("📖 Инструкция и FAQ")

col1, col2 = st.columns(2)

with col1:
    with st.expander("❓ Как это работает?"):
        st.write("""
        Мы используем каскад нейросетей Grok и Gemini. Когда ты вводишь данные, система анализирует 
        их через призму антропологии. ИИ отсекает всё лишнее и выдает текст, который 
        соответствует высокому социальному статусу.
        """)
    
    with st.expander("❓ Что если она не ответит?"):
        st.write("""
        Стиль А2 минимизирует риски. Даже если она не ответила, твое лицо сохранено, так как в твоем 
        сообщении не было нужды. Ты просто 'маякнул' и пошел дальше. Это и есть победная стратегия.
        """)

with col2:
    with st.expander("❓ Как вводить факты?"):
        st.write("""
        Ищи детали, а не общее. Вместо 'Она красивая' напиши 'У неё на фоне гитара' или 'Она была в горах'. 
        Чем точнее факт, тем мощнее будет 'Крючок' от ИИ.
        """)
    
    with st.expander("❓ Как общатся в своем фрейме?"):
        st.write("""
        Это наше внутреннее понятие. Оно означает, что ты используешь уникальную модель поведения, 
        которой нет у 99% парней. Твой 'фрейм' — это спокойствие и статус.
        """)

# ==========================================
# БЛОК 7: ПОДВАЛ (FOOTER)
# За что отвечает: Финальная подпись и техподдержка.
# ==========================================
st.divider()
st.caption(f"Social AI © 2026 | Итоговый вариант текста — А2 | Поддержка: {MY_TG}")
