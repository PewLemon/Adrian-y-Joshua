# Character attributes
skin_tones = ['Light White', 'Dark White', 'Light Tan', 'Dark Tan', 'Light Black', 'Dark Black']
helmets = ['Wizard Knight', 'Leather', 'Crown', 'Cat Ears', 'Chainmail', 'Steel']
eye_colors = ['Blue', 'Green', 'Brown', 'Black']
hair_types = ['Spikey', 'Curly', 'Straight', 'Short', 'Long']
hair_colors = ['Red', 'Black', 'Blond', 'Brown']

# Indexes for current selections
skin_tone_idx = 0
helmet_idx = 0
eye_color_idx = 0
hair_type_idx = 0
hair_color_idx = 0

def draw_character_creator():
    print(f"Skin Tone: {skin_tones[skin_tone_idx]}")
    print(f"Helmet: {helmets[helmet_idx]}")
    print(f"Eye Color: {eye_colors[eye_color_idx]}")
    print(f"Hair Type: {hair_types[hair_type_idx]}")
    print(f"Hair Color: {hair_colors[hair_color_idx]}")

while True:
    draw_character_creator()
    
    key = input("Press a key (q, w, e, r, t) to cycle through options or 'exit' to quit: ")
    
    if key == 'exit':
        break
    elif key == 'q':
        skin_tone_idx = (skin_tone_idx + 1) % len(skin_tones)
    elif key == 'w':
        helmet_idx = (helmet_idx + 1) % len(helmets)
    elif key == 'e':
        eye_color_idx = (eye_color_idx + 1) % len(eye_colors)
    elif key == 'r':
        hair_type_idx = (hair_type_idx + 1) % len(hair_types)
    elif key == 't':
        hair_color_idx = (hair_color_idx + 1) % len(hair_colors)