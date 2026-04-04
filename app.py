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

st.title("🧬 Social AI: Архитектура Доминирования")

# 1. Тот самый сценарий с четвергом (Главный хук)
with st.expander("🚩 РАЗБОР СЛИВА: Как ты теряешь ценность за одно сообщение"):
    st.markdown("""
    <div style='background: #161b22; padding: 20px; border-left: 4px solid #f85149; border-radius: 5px;'>
    <b>Ситуация:</b> Вы договорились на встречу в четверг. В среду она пишет:<br>
    <i>— "Ой, извини, завтра не получится, появились срочные дела..."</i><br><br>
    <b>❌ Ответ Оленя:</b> "Ничего страшного, я понимаю. Напиши тогда, как освободишься, подстроимся. Где тебе будет удобно встретиться?"<br>
    <span style='color: #f85149;'><b>ИТОГ:</b> Ты показал, что твое время ничего не стоит. Ты "удобный". Влечение умерло.</span><br><br>
    <b>✅ Ответ А2 (Premium):</b> "Принято. Раз у тебя форс-мажор, я тогда займу вечер другими планами. На связи."<br>
    <span style='color: #238636;'><b>ИТОГ:</b> Ты сохранил статус. Ты занятой человек с альтернативами. Теперь ОНА будет думать, как вернуть твое внимание.</span>
    </div>
    """, unsafe_allow_html=True)

# 2. РЕКЛАМНЫЙ СЛОТ (Будущий профит)
st.write("")
st.markdown("""
    <div style='background: rgba(255, 75, 75, 0.05); border: 1px dashed #444; padding: 15px; border-radius: 10px; text-align: center;'>
        <span style='color: #666; font-size: 14px;'>📢 МЕСТО ПОД ТВОЮ РЕКЛАМУ / ПАРТНЕРКУ</span><br>
        <span style='color: #444; font-size: 12px;'>(Например: Ссылка на твой ТГ-канал или закрытый клуб)</span>
    </div>
    """, unsafe_allow_html=True)
st.write("")

# 3. Бесплатные инструменты (Анализ без решений)
st.subheader("🕵️ Аналитическая Лаборатория")
col_a, col_b = st.columns(2)

with col_a:
    st.info("Анализ твоего сообщения")
    u_msg = st.text_input("Вставь фразу, которую ХОЧЕШЬ отправить:", placeholder="Например: Может увидимся завтра?")
    if st.button("Проверить харизму"):
        # ИИ критикует, но не правит (за правкой в Премиум)
        st.session_state.last_res = generate_response(f"Проанализируй это сообщение на мужественность и статус. Укажи на ошибки, но НЕ ДАВАЙ ИСПРАВЛЕННЫЙ ВАРИАНТ: {u_msg}")

with col_b:
    st.info("Анализ её манипуляций")
    h_msg = st.text_input("Что она тебе написала?", placeholder="Например: Я не знаю, я подумаю...")
    if st.button("Вскрыть подтекст"):
        st.session_state.last_res = generate_response(f"Проанализируй это сообщение от девушки. Какую проверку она проводит и что на самом деле имеет в виду? НЕ ДАВАЙ ВАРИАНТ ОТВЕТА: {h_msg}")

if st.session_state.last_res:
    st.markdown(f"<div class='result-box'>{st.session_state.last_res}</div>", unsafe_allow_html=True)
    if not st.session_state.pro_status:
        st.warning("⚠️ Идеальные формулировки для ответа доступны только в [PREMIUM РЕЖИМЕ]")

# ==========================================
# БЛОК 5: ОСНОВНОЙ ИНСТРУМЕНТАРИЙ (PREMIUM)
# За что отвечает: Проектировщик зацепок и Фильтр статуса.
# ==========================================

if st.session_state.pro_status:
    st.markdown("<h2 style='color: #ff4b4b;'>⭐ PREMIUM РЕЖИМ АКТИВЕН</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🚀 Идеальный Вход", "🎯 Контр-удар", "🧠 Индивидуальная Доводка"])
    
    with tab1:
        st.subheader("Генератор первого сообщения")
        st.write("Дай мне зацепки (профиль, фото, музыка), и я сделаю идеальный вход.")
        p_facts = st.text_area("Факты о ней:", 
                              placeholder="Любит корги, фото с винилом, в био фраза про Бродского...", key="p_facts")
        if st.button("Спроектировать идеальный вход"):
            st.session_state.last_res = generate_response(f"На основе фактов '{p_facts}' создай 3 уникальных, цепляющих первых сообщения в стиле А2.")

    with tab2:
        st.subheader("Перехват инициативы (Контр-удар)")
        st.write("Вставь контекст переписки, чтобы я нашел её слабое место и выдал ответ.")
        p_context = st.text_area("Контекст переписки:", 
                                placeholder="Твои и её сообщения по порядку...", key="p_context")
        if st.button("Сгенерировать идеальный ответ"):
            st.session_state.last_res = generate_response(f"Проанализируй контекст: '{p_context}'. Выдай один хирургически точный и статусный ответ в стиле А2.")

    with tab3:
        st.subheader("Работа с напарником (Тюнинг)")
        st.write("Не нравится ответ? Давай переделаем его под твой характер.")
        p_adjust = st.text_input("Твои пожелания:", placeholder="Например: 'Я так не хочу, сделай более иронично'...")
        if st.button("Перестроить ответ"):
            st.session_state.last_res = generate_response(f"Возьми прошлый вариант: {st.session_state.last_res}. Измени его согласно просьбе: {p_adjust}. Объясни преимущество новой версии.")

    if st.session_state.last_res:
        st.divider()
        st.markdown("<div class='result-box' style='border-color: #ff4b4b;'>", unsafe_allow_html=True)
        st.write(st.session_state.last_res)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # Тот самый баннер, который продает Премиум
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1f1f1f, #3d0e0e); padding: 40px; border-radius: 20px; border: 1px solid #ff4b4b; text-align: center;'>
        <h2 style='color: white;'>ХВАТИТ ТЕРЯТЬ ВРЕМЯ</h2>
        <p style='font-size: 18px;'>Бесплатный анализ — это только диагностика. <b>Premium</b> — это решение.</p>
        <div style='text-align: left; margin: 20px auto; display: inline-block;'>
            <p>✅ <b>Идеальные первые сообщения</b> (под любой профиль)</p>
            <p>✅ <b>Контр-удары</b> на любые женские проверки</p>
            <p>✅ <b>Индивидуальная доводка</b> с нейросетью</p>
        </div>
        <p style='font-weight: bold; color: #ff4b4b;'>Активируй доступ в боковом меню и забери инициативу себе.</p>
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
