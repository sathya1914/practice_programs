#s-algorithm code
data = [
    ['ponds', 'moist', 'dry', 'mrng', 'No'],
    ['dot_key', 'sunscreen', 'oily', 'mrng', 'No'],
    ['foxtail', 'serum', 'dry', 'mrng', 'Yes'],
    ['plum', 'serum', 'oil', 'night', 'No'],
    ['wishcare', 'lipbalm', 'break', 'mrng', 'Yes'],
    ['himalaya', 'facewash', 'combination', 'night', 'Yes']
]

h = ['Ø', 'Ø', 'Ø', 'Ø']
for row in data:
    if row[-1] == 'Yes':        
        if h[0] == 'Ø':         
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
print("Final Hypothesis:", h)
