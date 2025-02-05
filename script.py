import asyncio
from googletrans import Translator

async def translate_file(input_file, output_file):
    translator = Translator()
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            hindi_text = infile.read()

        #Splitting text into parts
        chunks = [hindi_text[i:i + 5000] for i in range(0, len(hindi_text), 5000)]

        translated_text = ""
        for chunk in chunks:
            translated_chunk = await translator.translate(chunk, src='hi', dest='en')
            translated_text += translated_chunk.text + "\n"

        # writing
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_text)

        print(f"Translation completed. Translated file saved as '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")


input_file = 'hindi_text.txt'
output_file = 'english_text.txt'


asyncio.run(translate_file(input_file, output_file))
