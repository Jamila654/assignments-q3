#type:ignore
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import typer

@dataclass
class Shape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def plot(self, ax: plt.Axes) -> None:
        pass

@dataclass
class Circle(Shape):
    radius: float

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def plot(self, ax: plt.Axes) -> None:
        circle = patches.Circle((0, 0), self.radius, fill=True, color='blue')
        ax.add_patch(circle)
        ax.set_aspect('equal')
        ax.set_xlim(-self.radius - 1, self.radius + 1)
        ax.set_ylim(-self.radius - 1, self.radius + 1)
        ax.set_title(f"Circle (Area: {self.area():.2f})")
        
@dataclass
class Rectangle(Shape):
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

    def plot(self, ax: plt.Axes) -> None:
        rect = patches.Rectangle((-self.width/2, -self.height/2), self.width, self.height, fill=True, color='green')
        ax.add_patch(rect)
        ax.set_aspect('equal')
        ax.set_xlim(-self.width/2 - 1, self.width/2 + 1)
        ax.set_ylim(-self.height/2 - 1, self.height/2 + 1)
        ax.set_title(f"Rectangle (Area: {self.area():.2f})")


app = typer.Typer()

@app.command()
def compare():
    user_input = input("Enter the radius of the circle: ")
    radius = float(user_input)
    user_input = input("Enter the width and height of the rectangle (comma-separated): ")
    width, height = map(float, user_input.split(","))
    shapes = [Circle(radius=radius), Rectangle(width=width, height=height)]
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for shape, ax in zip(shapes, axes):
        shape.plot(ax)
        print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}")
    plt.tight_layout()
    plt.savefig("comparison.png")
    plt.show()
    print("Plot saved as comparison.png")
    
if __name__ == "__main__":
    app()


