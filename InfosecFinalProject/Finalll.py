import pickle
import streamlit as st

# Load model and scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('DModel.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Diamond Price Predictor", page_icon="https://cdn-icons-png.flaticon.com/128/18717/18717513.png",
    layout="wide")

# Custom styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Serif&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Serif&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');


    html, body, [class*="css"] {
        font-family: 'Roboto Serif', serif;
        background-color: #d0eaff;  /* light blue fallback */
    }

    .stApp {
        background-image: linear-gradient(to bottom right, #d0eaff, #e6f3ff);
        background-attachment: fixed;
        background-size: cover;
    }

    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border-radius: 10px !important;
        padding: 8px !important;
        border: 1px solid #bcdfff !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #333 !important;
        font-weight: 500;
    }

    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        color: #333 !important;
    }

    div[data-baseweb="option"] {
        background-color: #ffffff !important;
        color: #222 !important;
    }

    div[data-baseweb="option"]:hover {
        background-color: #bcdfff !important;
    }
    </style>
""", unsafe_allow_html=True)


# Logo + Title
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("https://i.postimg.cc/PqN2QS2m/Radiant-Riches.png")
with col_title:
    st.markdown("""
    <h1 style='color: #002147; font-family: "Roboto Serif", serif;'>
        💎 Diamond Price Predictor 💎
    </h1>
    <h4 style='color: #333; font-family: "Great Vibes", serif; font-weight: 500;'>
        Know the price of your diamond easily
    </h4>
""", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)

st.image("https://i.postimg.cc/2562xCCc/dmns-removebg-preview.png", use_container_width=True)



# Two-column layout: inputs (left), result + gif (right)
input_col, output_col = st.columns([2, 2])

with input_col:
    st.markdown("### 💎 Diamond Specifications")

    # Dropdowns
    cut_list = ["Good", "Very Good", "Premium", "Ideal"]
    cut_idx = [0, 1, 4, 3, 2]
    color_list = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    color_idx = [6, 5, 4, 3, 2, 1, 0]
    clarity_list = ["I1", "SI2", "SII", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    clarity_idx = [0, 3, 2, 5, 4, 7, 6, 1]

    cut = st.selectbox(' Cut Quality', cut_list)
    color = st.selectbox(' Diamond Color', color_list)
    clarity = st.selectbox(' Clarity Grade', clarity_list)

    # Sliders
    st.markdown("### 💎 Physical Dimensions")
    carat = st.slider(' Weight of the Diamond (carats)', 0.20, 5.00, 0.20, 0.01)
    x = st.slider(' Length (mm)', 0.01, 10.74, 0.01, 0.01)
    y = st.slider(' Width (mm)', 0.01, 58.90, 0.01, 0.01)
    z = st.slider(' Depth (mm)', 0.01, 31.80, 0.01, 0.01)

    # Prediction button
    predict = st.button(' Predict Price')

with output_col:
    st.markdown("### 💎 Prediction Result")

    if predict:
        # Prepare and scale input
        X = [
            float(carat),
            float(x),
            float(y),
            float(z),
            int(cut_idx[cut_list.index(cut)]),
            int(color_idx[color_list.index(color)]),
            int(clarity_idx[clarity_list.index(clarity)])
        ]
        X_scaled = scaler.transform([X])
        price = model.predict(X_scaled)

        # Show result
        st.markdown(f"""
            <div style='text-align:center; background-color:#ffffff; padding:20px; border-radius:10px;'>
                <h2 style='color:#002147;'> Estimated Price</h2>
                <h1 style='color:#111;'>${int(price[0]):,}</h1>
            </div>
        """, unsafe_allow_html=True)

        # GIF
        st.image(
            "https://gifdb.com/images/high/diamond-stones-old-man-cool-swag-f0db4ku6fwb1vzxd.gif",
            caption="Your diamond sparkles bright!",
            use_container_width=True
        )
