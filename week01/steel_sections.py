steel_sections = [
    {
        "name": "Section A",
        "type": "H-beam",
        "area": 45,
        "Ix": 7200.0
    },
    {
        "name": "Section B",
        "type": "I-beam",
        "area": 30,
        "Ix": 5400.0
    },
    {
        "name": "Section C",
        "type": "Channel",
        "area": 25,
        "Ix": 3600.0
    },
    {
        "name": "Section D",
        "type": "H-beam",
        "area": 25,
        "Ix": 3600.0
    },
    {
        "name": "Section E",
        "type": "Angle",
        "area": 25,
        "Ix": 850
    },
]
sorted_sections = sorted(
    steel_sections,
    key=lambda x: x['area'], 
    reverse=True
)
for section in sorted_sections:
    if section["Ix"] > 4000:
      print(
        section['name'],
        section['type'],
        section['area'],
        section['Ix']
    )