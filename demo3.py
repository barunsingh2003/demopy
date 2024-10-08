import matplotlib.pyplot as plt

def translate_triangle(vertices, tx, ty):
    """Translate a triangle by (tx, ty)."""
    translated_vertices = [(x + tx, y + ty) for x, y in vertices]
    return translated_vertices

def plot_triangle(vertices, title):
    """Plot the triangle."""
    x_vals, y_vals = zip(*vertices)  # Unzip points into x and y coordinates
    x_vals += (x_vals[0],)  # Close the triangle
    y_vals += (y_vals[0],)  # Close the triangle
    plt.plot(x_vals, y_vals, marker='o')
    plt.fill(x_vals, y_vals, alpha=0.3)
    plt.title(title)
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.axhline(0, color='grey', lw=1)
    plt.axvline(0, color='grey', lw=1)
    plt.grid(True)

if __name__ == "__main__":
    # Define the original triangle vertices
    triangle_vertices = [(1, 1), (4, 1), (2.5, 4)]
    
    # Translation values
    tx = 2
    ty = 2

    # Translate the triangle
    translated_vertices = translate_triangle(triangle_vertices, tx, ty)

    # Print the original and translated coordinates
    print("Original Triangle Coordinates:")
    for vertex in triangle_vertices:
        print(vertex)

    print("\nTranslated Triangle Coordinates:")
    for vertex in translated_vertices:
        print(vertex)

    # Plot the original triangle
    plt.figure(figsize=(8, 8))
    plot_triangle(triangle_vertices, "Original Triangle")
    
    # Plot the translated triangle
    plot_triangle(translated_vertices, "Translated Triangle (tx=2, ty=2)")

    # Show both triangles in one figure
    plt.legend(['Original Triangle', 'Translated Triangle'])
    plt.show()
