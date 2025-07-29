# My Parent Helpers

Run using Streamlit.

## Usage

Install dependencies and start the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run main.py
```

The application expects an OpenAI API key configured in
`.streamlit/secrets.toml` under the `openai_key` setting:

```toml
[secrets]
openai_key = "sk-..."
```

The **Saved Items** page now lets you browse stored profiles (saved in the `profiles` folder) and view recent chat history. Selecting a profile also loads it for use in the chat helper.

