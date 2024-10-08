import numpy as np
import matplotlib.pyplot as plt

def scale_point(point, scale_factor, origin):
    """Scale a point relative to a given origin by a specific factor."""
    ox, oy = origin
    px, py = point

    # Scale the point
    qx = ox + scale_factor * (px - ox)
    qy = oy + scale_factor * (py - oy)
    
    return (qx, qy)

def scale_triangle(vertices, scale_factor, origin):
    """Scale a triangle around a specified point."""
    return [scale_point(vertex, scale_factor, origin) for vertex in vertices]

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
    
    # Define the scaling factor and the origin point
    scaling_factor = 2  # Magnify to twice the size
    origin_point = (2.5, 2)  # Fixed point (could be the centroid or another point)

    # Scale the triangle
    scaled_vertices = scale_triangle(triangle_vertices, scaling_factor, origin_point)

    # Print the original and scaled coordinates
    print("Original Triangle Coordinates:")
    for vertex in triangle_vertices:
        print(vertex)

    print("\nScaled Triangle Coordinates:")
    for vertex in scaled_vertices:
        print(vertex)

    # Plot the original triangle
    plt.figure(figsize=(8, 8))
    plot_triangle(triangle_vertices, "Original Triangle")
    
    # Plot the scaled triangle
    plot_triangle(scaled_vertices, "Scaled Triangle (2x Size)")

    # Show both triangles in one figure
    plt.legend(['Original Triangle', 'Scaled Triangle'])
    plt.show()
