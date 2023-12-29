from translate import translate_pptx

# Usage
input_pptx = "example.pptx"

source_lang = "chinese"
target_lang = "english"

# backend = "google"
backend = "deepl"

output_pptx = f"output_{backend}.pptx"

translate_pptx(input_pptx, output_pptx, source_lang, target_lang, backend)
