import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    """Bresenham's Line Algorithm to generate points of a line."""
    points = []
    dx = x1 - x0
    dy = y1 - y0
    sx = 1 if dx > 0 else -1
    sy = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            points.append((x0, y0))
            err -= dy
            if err < 0:
                y0 += sy
                err += dx
            x0 += sx
    else:
        err = dy / 2.0
        while y0 != y1:
            points.append((x0, y0))
            err -= dx
            if err < 0:
                x0 += sx
                err += dy
            y0 += sy
    points.append((x1, y1))  # Include the last point
    return points

def draw_line_image(points):
    """Draw the line points on a matplotlib image."""
    x_vals, y_vals = zip(*points)  # Unzip points into x and y coordinates

    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, marker='o', color='black')  # Draw line
    plt.title("Bresenham's Line Drawing")
    plt.xlim(min(x_vals)-10, max(x_vals)+10)
    plt.ylim(min(y_vals)-10, max(y_vals)+10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    
    # Save the image
    plt.savefig("line_bresenham.png")
    plt.show()

if __name__ == "__main__":
    # Define line endpoints
    start_point = (20, 30)
    end_point = (180, 150)

    # Get the points of the line
    line_points = bresenham_line(start_point[0], start_point[1], end_point[0], end_point[1])

    # Print the points
    print("Line points:")
    for point in line_points:
        print(point)

    # Draw the line and save the image
    draw_line_image(line_points)
