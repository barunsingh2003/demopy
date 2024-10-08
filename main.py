import matplotlib.pyplot as plt

def dda_line(x0, y0, x1, y1):
    """DDA Line Drawing Algorithm to generate points of a line."""
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / float(steps)  # Increment in x
    y_inc = dy / float(steps)  # Increment in y

    x, y = x0, y0
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

def draw_line_image(points):
    """Draw the line points on a matplotlib image."""
    x_vals, y_vals = zip(*points)  # Unzip points into x and y coordinates

    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, marker='o', color='black')  # Draw line
    plt.title("DDA Line Drawing")
    plt.xlim(min(x_vals)-10, max(x_vals)+10)
    plt.ylim(min(y_vals)-10, max(y_vals)+10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)

    # Save the image
    plt.savefig("line_dda.png")
    plt.show()

if __name__ == "__main__":
    # Define line endpoints
    start_point = (20, 30)
    end_point = (180, 150)

    # Get the points of the line
    line_points = dda_line(start_point[0], start_point[1], end_point[0], end_point[1])

    # Print the points
    print("Line points:")
    for point in line_points:
        print(point)
    draw_line_image(line_points)
