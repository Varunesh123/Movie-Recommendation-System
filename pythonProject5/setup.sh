mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableleCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml