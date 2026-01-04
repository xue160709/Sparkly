import json
import os

def extract_cards():
    input_file = 'sparkly.json'
    output_file = 'sparkly_cn.json'

    # Get the absolute path if needed, or assume current working directory
    # verify file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found in {os.getcwd()}")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        extracted_cards = []
        if 'cards' in data:
            for card in data['cards']:
                new_card = {
                    'title': card.get('title', {}).get('cn', ''),
                    'subtitle': card.get('subtitle', {}).get('cn', ''),
                    'id': card.get('id', '')
                }
                extracted_cards.append(new_card)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(extracted_cards, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully extracted {len(extracted_cards)} cards to {output_file}")
        
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {input_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_cards()
