import streamlit as st
import pandas as pd
import os

# Set page config
st.set_page_config(page_title="MediSynth", layout="wide")

# Translation dictionary
translations = {
    "English": {
        "login": "Login",
        "about": "About",
        "services": "Services",
        "language": "Language",
        "synthetic_data": "Synthetic Data",
        "country": "Choose Country",
        "data_preview": "Synthetic Medical Data",
        "age_distribution": "Age Distribution",
        "download": "Download Data",
        "download_button": "Download CSV",
        "intro": "A secure and scalable synthetic data generation platform that produces realistic, anonymized medical datasets. These datasets preserve the statistical patterns of real data without compromising patient privacy empowering innovation in healthcare AI, diagnostics, and research.\nTurkey and the MENA (Middle East and North Africa) region"
    },
    "Arabic": {
        "login": "تسجيل الدخول",
        "about": "حول",
        "services": "الخدمات",
        "language": "اللغة",
        "synthetic_data": "البيانات الاصطناعية",
        "country": "اختر الدولة",
        "data_preview": "بيانات طبية اصطناعية",
        "age_distribution": "توزيع الأعمار",
        "download": "تحميل البيانات",
        "download_button": "تحميل CSV",
        "intro": "منصة آمنة وقابلة للتوسع لتوليد البيانات الاصطناعية التي تنتج مجموعات بيانات طبية واقعية ومجهولة المصدر. تحافظ هذه البيانات على الأنماط الإحصائية للبيانات الحقيقية دون المساس بخصوصية المرضى، مما يعزز الابتكار في الذكاء الاصطناعي في الرعاية الصحية والتشخيص والبحث.\nتركيا ومنطقة الشرق الأوسط وشمال إفريقيا"
    },
    "Turkish": {
        "login": "Giriş Yap",
        "about": "Hakkında",
        "services": "Hizmetler",
        "language": "Dil",
        "synthetic_data": "Sentetik Veri",
        "country": "Ülke Seçin",
        "data_preview": "Sentetik Tıbbi Veriler",
        "age_distribution": "Yaş Dağılımı",
        "download": "Veriyi İndir",
        "download_button": "CSV İndir",
        "intro": "Gerçekçi, anonimleştirilmiş tıbbi veri kümeleri üreten güvenli ve ölçeklenebilir bir sentetik veri üretim platformu. Bu veri kümeleri, hasta gizliliğini ihlal etmeden gerçek verilerin istatistiksel desenlerini koruyarak sağlıkta yapay zeka, tanı ve araştırmalarda yeniliği mümkün kılar.\nTürkiye ve MENA (Orta Doğu ve Kuzey Afrika) bölgesi"
    },
    "French": {
        "login": "Connexion",
        "about": "À propos",
        "services": "Services",
        "language": "Langue",
        "synthetic_data": "Données Synthétiques",
        "country": "Choisir le pays",
        "data_preview": "Données médicales synthétiques",
        "age_distribution": "Répartition par âge",
        "download": "Télécharger les données",
        "download_button": "Télécharger le CSV",
        "intro": "Une plateforme sécurisée et évolutive de génération de données synthétiques produisant des ensembles de données médicales réalistes et anonymisées. Ces ensembles conservent les modèles statistiques des données réelles sans compromettre la confidentialité des patients, favorisant l'innovation dans l'IA médicale, les diagnostics et la recherche.\nTurquie et région MENA (Moyen-Orient et Afrique du Nord)"
    }
}

# File map (Excel files)
file_map = {
    "English": "diabetes_translated_english.xlsx",
    "Arabic": "diabetes_translated_arabic.xlsx",
    "Turkish": "diabetes_translated_turkish.xlsx",
    "French": "diabetes_translated_french.xlsx"
}

# Set default language
if 'language' not in st.session_state:
    st.session_state.language = "English"

# Sidebar language selection
selected_lang = st.sidebar.selectbox("Language / اللغة / Dil / Langue", list(translations.keys()))
st.session_state.language = selected_lang
T = translations[selected_lang]  # Active translation dict

# Navigation menu
menu = st.sidebar.radio("Navigation", [T['about'], T['services'], T['login']])

# Branding at the top
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #025C7A;'>MediSynth</h1>
        <p style='font-size:18px;'>{}</p>
    </div>
    <hr>
""".format(T['intro']), unsafe_allow_html=True)

# Function to load data
@st.cache_data
def load_data(file_name):
    return pd.read_excel(file_name)

# Page Routing
if menu == T['about']:
    st.subheader(T['about'])
    st.write(T['intro'])

elif menu == T['services']:
    service_option = st.selectbox(T['services'], [T['synthetic_data']])
    if service_option == T['synthetic_data']:

        country = st.selectbox(T['country'], ["Turkey", "Egypt", "Lebanon", "Jordan"])

        try:
            df = load_data(file_map[selected_lang])

            st.subheader(T['data_preview'])
            st.dataframe(df)

            st.subheader(T['age_distribution'])
            if "Age" in df.columns:
                st.bar_chart(df["Age"])

            st.subheader(T['download'])
            st.download_button(
                label=T['download_button'],
                data=df.to_csv(index=False).encode('utf-8-sig'),
                file_name=f"synthetic_data_{country.lower()}.csv",
                mime='text/csv'
            )
        except Exception as e:
            st.error("Error loading data: {}".format(str(e)))

elif menu == T['login']:
    st.subheader(T['login'])
    st.info("This is a prototype. Authentication is not implemented yet.")
