import streamlit as st
import json
from io import StringIO
from converter import convert_examples

st.set_page_config(page_title="🛠️ Dataset Converter", layout="centered")
st.title("🛠️ Convert Transition Dataset Format")

uploaded_file = st.file_uploader("📄 Upload original JSON file", type=["json"])

if uploaded_file:
    raw_json = uploaded_file.read().decode("utf-8")
    try:
        data = json.loads(raw_json)
        converted = convert_examples(data)
        st.success(f"✅ Successfully converted {len(converted)} examples.")

        st.json(converted[:2])  # Preview first two

        # Prepare downloadable JSON
        converted_str = json.dumps(converted, ensure_ascii=False, indent=2)
        st.download_button(
            label="⬇️ Download converted JSON",
            data=converted_str,
            file_name="converted_transitions.json",
            mime="application/json"
        )

    except Exception as e:
        st.error(f"❌ Error parsing JSON: {e}")
