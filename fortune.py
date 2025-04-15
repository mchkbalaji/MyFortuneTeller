print("🔮 Welcome to Balaji Mirthipati's Fortune Teller (22JE0573) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Joy radiates from within you, spreading light wherever you go. Bask in it, Balaji, and keep shining bright! ✨")
elif mood == "sad":
    print("🌧️ Your fortune: Even the stormiest skies clear with time. Hold on tight, Balaji-the rainbow is closer than you think. 🌈")
elif mood == "neutral":
    print("😐 Your fortune: Life flows steadily, Balaji. Embrace the calm—it’s the perfect moment to plant seeds for future triumphs. 🌿")
else:
    print("🤔 Sorry, I don't have a fortune for that mood.")
