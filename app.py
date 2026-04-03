# ==========================================
# БЛОК 1: ДВИГАТЕЛЬ И БЕЗОПАСНОСТЬ (FAILOVER)
# За что отвечает: Подключение ключей, логика переключения 
# между Grok и Gemini, если одна из сетей упадет.
# ==========================================
import streamlit as st
import google.generativeai as genai
from openai import OpenAI
import datetime

# Ключи тянем из Settings -> Secrets в Streamlit Cloud (GROK_KEY, GEMINI_KEY_1, GEMINI_KEY_2)
try:
    GROK_KEY = st.secrets["GROK_KEY"]
    GEMINI_KEY_1 = st.secrets["GEMINI_KEY_1"]
    GEMINI_KEY_2 = st.secrets["GEMINI_KEY_2"]
except Exception:
    st.error("Ошибка: Ключи не найдены в Secrets! Сайт не сможет отвечать.")
    st.stop()

MY_TG = "@Manipulator393"

# Системная установка А2: глубокий стиль, высокий статус, без нужды.
A2_PHILOSOPHY = """
Ты — эксперт по социальной архитектуре и антропологии общения. Твой стиль — 'А2'.
ПРАВИЛА: 
1. Никакой нужды (низкая нуждаемость). 
2. Высокий статус и ценность (Frame Control). 
3. Текст глубокий, понятный, без лишнего упрощения, доступный, без специфических терминов.
4. Исключить банальный пикап, дешевые комплименты и оправдания. 
5. Юмор — тонкая ирония, а не клоунада.
6. Всегда выдавай полный, готовый к отправке текст.
"""

def generate_response(prompt):
    """Каскадная система защиты: если один ключ падает, включается следующий."""
    full_prompt = f"{A2_PHILOSOPHY}\n\nЗАДАЧА: {prompt}"
    
    # 1. Попытка через Grok
    try:
        client = OpenAI(api_key=GROK_KEY, base_url="https://api.x.ai/v1")
        res = client.chat.completions.create(model="grok-beta", messages=[{"role": "user", "content": full_prompt}])
        return res.choices[0].message.content
    except Exception:
        # 2. Попытка через Gemini (Ключ 1)
        try:
            genai.configure(api_key=GEMINI_KEY_1)
            model = genai.GenerativeModel('gemini-1.5-flash')
            return model.generate_content(full_prompt).text
        except Exception:
            # 3. Попытка через Gemini (Ключ 2)
            try:
                genai.configure(api_key=GEMINI_KEY_2)
                model2 = genai.GenerativeModel('gemini-1.5-flash')
                return model2.generate_content(full_prompt).text
            except Exception:
                return "⚠️ Все нейросети временно недоступны. Попробуй пролистать до бага и обновить страницу."

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
# База кодов. Формат: "код": "дата (гггг-мм-дд)" или "forever"
VALID_CODES = {
    "A2_TEST_MONTH": "2026-05-15",
    "A2_YEAR_PRO": "2027-04-01",
    "A2_FOREVER": "forever"
}

if 'pro_status' not in st.session_state: st.session_state.pro_status = False
if 'last_res' not in st.session_state: st.session_state.last_res = ""

with st.sidebar:
    st.title("🧬 Social AI")
    st.caption("Твой личный архитектор социальных связей")
    
    user_key = st.text_input("Введите ваш секретный код:", type="password")
    
    if user_key in VALID_CODES:
        expiry = VALID_CODES[user_key]
        if expiry == "forever" or datetime.datetime.strptime(expiry, "%Y-%m-%d") > datetime.datetime.now():
            st.session_state.pro_status = True
            st.success(f"Доступ одобрен: {expiry}")
        else:
            st.error("Срок действия кода истек.")
            st.session_state.pro_status = False

    st.divider()
    if not st.session_state.pro_status:
        st.markdown("### 💎 Активировать Premium")
        st.write("Получите доступ к алгоритмам А2 и увеличьте свою ценность в переписке.")
        st.markdown("""
        * **1 Месяц:** 299₽
        * **1 Год:** 1599₽ (Выгодно)
        * **Навсегда:** 5000₽
        """)
        st.write("📸 **Оплата по QR (СБП):**")
        # Место под твой QR-код
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", width=180)
        st.info(f"После оплаты отправь скриншот чека в Telegram: {MY_TG}")
        st.markdown(f"[🚀 Написать в поддержку](https://t.me/{MY_TG.replace('@', '')})")

# ==========================================
# БЛОК 4: БЕСПЛАТНЫЙ РАЗБОР (МАРКЕТИНГ)
# За что отвечает: Объясняет ценность продукта новичку.
# ==========================================
st.title("🧬 Архитектура Социального Входа")

with st.expander("🔍 Почему твои сообщения не работают? (Анализ ошибки)"):
    st.write("""
    Большинство парней заваливают переписку в первые 5 минут. Причина — высокая нуждаемость (Tryhard). 
    Вы пытаетесь понравиться, задаете много вопросов и быстро отвечаете. Это убивает интерес.
    Алгоритм **А2** пересобирает твой текст так, чтобы ты выглядел самодостаточным и статусным мужчиной, 
    который выбирает, а не навязывается.
    """)

# ==========================================
# БЛОК 5: ОСНОВНОЙ ИНСТРУМЕНТАРИЙ (PREMIUM)
# За что отвечает: Проектировщик зацепок и Фильтр статуса.
# ==========================================
if st.session_state.pro_status:
    tab1, tab2 = st.tabs(["🚀 Проектировщик Входа", "💎 Фильтр Статуса"])
    
    with tab1:
        st.subheader("Генерация 'Крючка' на основе контекста")
        st.write("Впиши детали её профиля, которые ты заметил.")
        facts = st.text_area("Факты о ней (хобби, фото, музыка):", 
                             placeholder="Например: Любит корги, фото с выставки винила, в био фраза про интровертов...",
                             key="facts_input")
        if st.button("Спроектировать варианты"):
            st.session_state.last_res = generate_response(f"На основе фактов '{facts}' создай 3 варианта первого сообщения. Стиль А2.")

    with tab2:
        st.subheader("Фильтр 'Нулевой суеты'")
        st.write("Преврати свой черновик в сообщение, которое транслирует ценность.")
        draft = st.text_area("Твой текст:", 
                             placeholder="Вставь то, что ты хотел ей написать...",
                             key="draft_input")
        if st.button("Повысить статус"):
            st.session_state.last_res = generate_response(f"Перепиши это сообщение, удалив нужду, суету и лишние знаки препинания. Стиль А2: '{draft}'")

    # Вывод результата
    if st.session_state.last_res:
        st.divider()
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.write(st.session_state.last_res)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Докрутка результата (AI Напарник)
        st.write("---")
        feedback = st.text_input("🗣 AI-Напарник (Правка):", placeholder="Например: 'сделай это чуть более дерзким'...")
        if st.button("Обновить варианты"):
            st.session_state.last_res = generate_response(f"Измени прошлый результат: {st.session_state.last_res}. Учти правку: {feedback}")
            st.rerun()
else:
    st.warning("🔒 Доступ закрыт. Чтобы использовать функции Проектировщика и Фильтра, активируйте Premium в боковом меню.")

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
    
    with st.expander("❓ Где взять скин на рынке?"):
        st.write("""
        Это наше внутреннее понятие. Оно означает, что ты используешь уникальную модель поведения, 
        которой нет у 99% парней. Твой 'скин' — это спокойствие и статус.
        """)

# ==========================================
# БЛОК 7: ПОДВАЛ (FOOTER)
# За что отвечает: Финальная подпись и техподдержка.
# ==========================================
st.divider()
st.caption(f"Social AI © 2026 | Итоговый вариант текста — А2 | Поддержка: {MY_TG}")
