from dataclasses import dataclass
from src.classes.tuple import *
from src.classes.canvas import *


@dataclass
class Projectile:
    position: Tuple
    velocity: Tuple


@dataclass
class Environment:
    gravity: Tuple
    wind: Tuple


def tick(environment: Environment, projectile: Projectile) -> Projectile:
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(position, velocity)


if __name__ == '__main__':
    c = Canvas(900, 550)

    start = point(1,250, 0)
    velocity = normalize(vector(20, 20, 0)) * 30
    p = Projectile(start, velocity)

    gravity = vector(0, -0.5, 0)
    wind = vector(-1, 0, 0)
    e = Environment(gravity, wind)


    while p.position.y > 0 and p.position.y <c.height() and p.position.x > 0 and p.position.x < c.width():
        c.write_pixel_float(p.position.x, c.height() - p.position.y, Color(0.5, 0.25, 0))
        p = tick(e, p)

    write_canvas_to_file(c,"projectile")