import numpy as np
import matplotlib.pyplot as plt

def rotate_point(point, angle, origin):
    """Rotate a point around a given origin by a specific angle."""
    angle_rad = np.radians(angle)
    ox, oy = origin
    px, py = point

    # Translate point back to origin
    px -= ox
    py -= oy

    # Rotate point
    qx = ox + (px * np.cos(angle_rad) - py * np.sin(angle_rad))
    qy = oy + (px * np.sin(angle_rad) + py * np.cos(angle_rad))
    
    return (qx, qy)

def rotate_triangle(vertices, angle, origin):
    """Rotate a triangle around a specified point."""
    return [rotate_point(vertex, angle, origin) for vertex in vertices]

def plot_triangle(vertices, title):
    """Plot the triangle."""
    x_vals, y_vals = zip(*vertices)  # Unzip points into x and y coordinates
    x_vals += (x_vals[0],)  # Close the triangle
    y_vals += (y_vals[0],)  # Close the triangle
    plt.plot(x_vals, y_vals, marker='o')
    plt.fill(x_vals, y_vals, alpha=0.3)
    plt.title(title)
    plt.xlim(-5, 10)
    plt.ylim(-5, 10)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    plt.grid(True)

if __name__ == "__main__":
    # Define the original triangle vertices
    triangle_vertices = [(1, 1), (4, 1), (2.5, 4)]
    
    # Define the rotation angle and the origin point
    rotation_angle = 60  # degrees
    origin_point = (1, 1)  # Rotate around the first vertex

    # Rotate the triangle
    rotated_vertices = rotate_triangle(triangle_vertices, rotation_angle, origin_point)

    # Plot the original triangle
    plt.figure(figsize=(8, 8))
    plot_triangle(triangle_vertices, "Original Triangle")
    
    # Plot the rotated triangle
    plot_triangle(rotated_vertices, "Rotated Triangle (60° Clockwise)")

    # Show both triangles in one figure
    plt.legend(['Original Triangle', 'Rotated Triangle'])
    plt.show()
import numpy as np
import matplotlib.pyplot as plt

def rotate_point(point, angle, origin):
    """Rotate a point around a given origin by a specific angle (in degrees)."""
    angle_rad = np.radians(angle)
    ox, oy = origin
    px, py = point

    # Translate point back to origin
    px -= ox
    py -= oy

    # Rotate point
    qx = ox + (px * np.cos(angle_rad) - py * np.sin(angle_rad))
    qy = oy + (px * np.sin(angle_rad) + py * np.cos(angle_rad))
    
    return (qx, qy)

def rotate_triangle(vertices, angle, origin):
    """Rotate a triangle around a specified point."""
    return [rotate_point(vertex, angle, origin) for vertex in vertices]

def plot_triangle(vertices, title):
    """Plot the triangle."""
    x_vals, y_vals = zip(*vertices)  # Unzip points into x and y coordinates
    x_vals += (x_vals[0],)  # Close the triangle
    y_vals += (y_vals[0],)  # Close the triangle
    plt.plot(x_vals, y_vals, marker='o')
    plt.title(title)
    plt.xlim(-5, 10)
    plt.ylim(-5, 10)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    plt.grid(True)

if __name__ == "__main__":
    # Define the original triangle vertices
    triangle_vertices = [(1, 1), (4, 1), (2.5, 4)]
    
    # Define the rotation angle and the origin point
    rotation_angle = 60  # degrees
    origin_point = (1, 1)  # Point P for rotation

    # Rotate the triangle
    rotated_vertices = rotate_triangle(triangle_vertices, rotation_angle, origin_point)

    # Print the original and rotated coordinates
    print("Original Triangle Coordinates:")
    for vertex in triangle_vertices:
        print(vertex)

    print("\nRotated Triangle Coordinates:")
    for vertex in rotated_vertices:
        print(vertex)

    # Plot the original triangle
    plt.figure(figsize=(8, 8))
    plot_triangle(triangle_vertices, "Original Triangle")
    
    # Plot the rotated triangle
    plot_triangle(rotated_vertices, "Rotated Triangle (60° Clockwise)")

    # Show both triangles in one figure
    plt.legend(['Original Triangle', 'Rotated Triangle'])
    plt.show()
