def dfs(image, start, sr, sc, color, n, m):
    image[sr][sc] = color
    for row, col in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        new_r = sr + row
        new_c = sc + col
        if 0 <= new_r < n and 0 <= new_c < m and image[new_r][new_c] == start:
            dfs(image, start, new_r, new_c, color, n, m)

def flood_fill(image, sr, sc, color):
    n = len(image)
    m = len(image[0])
    start = image[sr][sc]

    if start == color:
        return image
    
    dfs(image, start, sr, sc, color, n, m)
    return image


def main():
    print("Enter the image (2D matrix):")
    rows = int(input("Number of rows: "))
    image = []

    for i in range(rows):
        row = list(map(int, input(f"Row {i+1} (space separated): ").split()))
        image.append(row)

    sr = int(input("Enter starting row (sr): "))
    sc = int(input("Enter starting column (sc): "))
    color = int(input("Enter new color: "))

    result = flood_fill(image, sr, sc, color)

    print("\nResultant Image:")
    for row in result:
        print(row)

main()


"""
1. Start from the given position.
2. Store the given position color in some variable, say, start.
3. Recursion:
    * color the pos with given "color"
    * check in any direction
4. Return the image
"""