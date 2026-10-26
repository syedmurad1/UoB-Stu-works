marks = {
    "Alice": 85, "Ben": 72, "Chloe": 91, "David": 66,
    "Ella": 78, "George": 55, "Hannah": 88, "Isaac": 93,
    "Julia": 70, "Kevin": 61, "Lily": 82, "Mason": 74,
    "Nora": 95, "Oliver": 58, "Paula": 80,
}

marks["Frank"] = 60                      
for name, mark in marks.items():        
    print(f"{name}: {mark}")