import matplotlib.pyplot as plt

def bresenham_circle(x_center, y_center, radius):
    """Bresenham's Circle Drawing Algorithm to generate points of a circle."""
    points = []
    x = radius
    y = 0
    p = 1 - radius  # Decision parameter

    while x > y:
        # Add the points in each octant
        points.append((x_center + x, y_center + y))
        points.append((x_center - x, y_center + y))
        points.append((x_center + x, y_center - y))
        points.append((x_center - x, y_center - y))
        points.append((x_center + y, y_center + x))
        points.append((x_center - y, y_center + x))
        points.append((x_center + y, y_center - x))
        points.append((x_center - y, y_center - x))
        
        y += 1

        if p <= 0:  # Midpoint is inside the circle
            p += 2 * y + 1
        else:  # Midpoint is outside the circle
            x -= 1
            p += 2 * y - 2 * x + 1

    return points

def draw_circle_image(points):
    """Draw the circle points on a matplotlib image."""
    x_vals, y_vals = zip(*points)  # Unzip points into x and y coordinates

    plt.figure(figsize=(6, 6))
    plt.scatter(x_vals, y_vals, color='black')  # Draw circle points
    plt.title("Bresenham's Circle Drawing")
    plt.xlim(min(x_vals) - 10, max(x_vals) + 10)
    plt.ylim(min(y_vals) - 10, max(y_vals) + 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)

    # Save the image
    plt.savefig("circle_bresenham.png")
    plt.show()

if __name__ == "__main__":
    # Define circle center and radius
    center_point = (100, 100)
    radius = 50

    # Get the points of the circle
    circle_points = bresenham_circle(center_point[0], center_point[1], radius)

    # Print the points
    print("Circle points:")
    for point in circle_points:
        print(point)

    # Draw the circle and save the image
    draw_circle_image(circle_points)
