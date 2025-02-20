def print_menu():
    chars = {
        'G': [
            "+++++",
            "+    ",
            "+ +++",
            "+   +",
            "+++++"
        ],
        'O': [
            "+++++",
            "+   +",
            "+   +",
            "+   +",
            "+++++"
        ],
        'L': [
            "+    ",
            "+    ",
            "+    ",
            "+    ",
            "+++++"
        ],
        'D': [
            "++++ ",
            "+   +",
            "+   +",
            "+   +",
            "++++ "
        ],
        '_': [
            "     ",
            "     ",
            "     ",
            "     ",
            "+++++"
        ],
        'P': [
            "+++++",
            "+   +",
            "+++++",
            "+    ",
            "+    "
        ],
        'U': [
            "+   +",
            "+   +",
            "+   +",
            "+   +",
            "+++++"
        ],
        'S': [
            "+++++",
            "+    ",
            "+++++",
            "    +",
            "+++++"
        ],
        'E': [
            "+++++",
            "+    ",
            "+++++",
            "+    ",
            "+++++"
        ]
    }

    word = "gold_pulse"
    
    print("\n")
    for row in range(5):
        line = ""
        for char in word.upper():
            if char == '_':
                line += chars['_'][row] + " "
            else:
                line += chars[char][row] + " "
        print("  " + line)
        
    print("\n")
